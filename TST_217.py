import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
from functools import cmp_to_key

class ClientFilterWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.initUI()
        self.loadData()

    def initUI(self):
        self.window.title('Filtro de clientes')
        self.window.geometry('800x600')

        # Frame para los filtros
        filter_frame = tk.Frame(self.window)
        filter_frame.pack(pady=10)

        # Campos de búsqueda
        self.tipo_cuenta_var = tk.StringVar()
        self.saldo_var = tk.StringVar()
        self.edad_var = tk.StringVar()

        ttk.Label(filter_frame, text="Tipo de cuenta").grid(row=0, column=0, padx=5)
        ttk.Entry(filter_frame, textvariable=self.tipo_cuenta_var).grid(row=0, column=1, padx=5)

        ttk.Label(filter_frame, text="Saldo").grid(row=0, column=2, padx=5)
        ttk.Entry(filter_frame, textvariable=self.saldo_var).grid(row=0, column=3, padx=5)

        ttk.Label(filter_frame, text="Edad").grid(row=0, column=4, padx=5)
        ttk.Entry(filter_frame, textvariable=self.edad_var).grid(row=0, column=5, padx=5)

        # Botón "Mostrar todo"
        ttk.Button(filter_frame, text="Mostrar todo", command=self.showAll).grid(row=0, column=6, padx=5)

        # Tabla
        self.tree = ttk.Treeview(self.window, columns=('Nombre', 'Apellido', 'Edad', 'Tipo de cuenta', 'Rut', 'Saldo'), show='headings')
        for col in self.tree['columns']:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)
        self.tree.pack(expand=True, fill='both')

        # Vincular eventos de entrada
        self.tipo_cuenta_var.trace('w', self.filterData)
        self.saldo_var.trace('w', self.filterData)
        self.edad_var.trace('w', self.filterData)

    def loadData(self):
        try:
            with open('datos_clientes.json', 'r') as file:
                self.clientes = json.load(file)
            with open('datos_cuentas.json', 'r') as file:
                self.cuentas = json.load(file)[0]
        except FileNotFoundError:
            self.clientes = []
            self.cuentas = {}

        # Calcular edades y agregar saldos
        for cliente in self.clientes:
            if 'fecha_de_nacimiento' in cliente:
                birth_date = datetime.strptime(cliente['fecha_de_nacimiento'], '%d/%m/%Y')
                cliente['edad'] = str((datetime.now() - birth_date).days // 365)
            if 'cuentas' in cliente:
                cliente['saldo'] = sum(self.cuentas[cuenta.split('-')[1]]['saldo'] for cuenta in cliente['cuentas'] if cuenta.split('-')[1] in self.cuentas)

    def filterData(self, *args):
        self.tree.delete(*self.tree.get_children())
        for cliente in self.clientes:
            if 'rut' not in cliente:  # Excluir al gerente
                continue
            if self.matchesFilter(cliente):
                nombre, apellido = cliente['nombre'].split(' ', 1)
                self.tree.insert('', 'end', values=(
                    nombre,
                    apellido,
                    cliente.get('edad', ''),
                    ', '.join(cliente['cuentas']),
                    cliente['rut'],
                    f"{cliente.get('saldo', 0):,}"
                ))

    def matchesFilter(self, cliente):
        tipo_cuenta = self.tipo_cuenta_var.get().lower()
        saldo = self.saldo_var.get()
        edad = self.edad_var.get()

        if tipo_cuenta and not any(tipo_cuenta in cuenta.lower() for cuenta in cliente['cuentas']):
            return False
        if saldo and cliente.get('saldo', 0) < int(saldo):
            return False
        if edad and cliente.get('edad', '') != edad:
            return False
        return True

    def showAll(self):
        self.tipo_cuenta_var.set('')
        self.saldo_var.set('')
        self.edad_var.set('')
        self.filterData()

class ClientDataWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title('Datos de clientes')
        self.window.geometry('800x600')
        self.initUI()

    def initUI(self):
        # Crear los botones desplegables
        self.combos = {}
        self.sort_order = []
        combo_frame = tk.Frame(self.window)
        combo_frame.pack(pady=10)
        for field in ['Nombre', 'Edad', 'Fecha de nacimiento', 'Rut', 'Cuenta bancaria']:
            combo = ttk.Combobox(combo_frame, values=['Ascendente', 'Descendente'])
            combo.set('Ascendente')
            combo.bind('<<ComboboxSelected>>', lambda e, f=field: self.updateTable(f))
            combo.pack(side=tk.LEFT, padx=5)
            self.combos[field] = combo

        # Crear la tabla
        self.tree = ttk.Treeview(self.window, columns=('Nombre', 'Edad', 'Fecha de nacimiento', 'Rut', 'Cuenta bancaria'), show='headings')
        for col in self.tree['columns']:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(expand=True, fill='both')

        # Añadir el botón "Tabla de Clientes" al final
        btn_tabla = ttk.Button(self.window, text="Tabla de Clientes", command=self.abrir_tabla_clientes)
        btn_tabla.pack(pady=10)

        # Cargar datos del archivo JSON
        self.loadData()
        self.updateTable()

    def loadData(self):
        try:
            with open('datos_clientes.json', 'r') as file:
                self.data = json.load(file)
                self.data = [client for client in self.data if 'rut' in client]
                for client in self.data:
                    birth_date = datetime.strptime(client['fecha_de_nacimiento'], '%d/%m/%Y')
                    client['edad'] = (datetime.now() - birth_date).days // 365
        except FileNotFoundError:
            self.data = []

    def compare_clients(self, client1, client2):
        for field in self.sort_order:
            key = field.lower().replace(' ', '_')
            reverse = self.combos[field].get() == 'Descendente'
            
            if key == 'cuenta_bancaria':
                value1 = client1['cuentas'][0] if client1['cuentas'] else ''
                value2 = client2['cuentas'][0] if client2['cuentas'] else ''
            elif key == 'edad':
                value1 = int(client1[key])
                value2 = int(client2[key])
            elif key == 'fecha_de_nacimiento':
                value1 = datetime.strptime(client1[key], '%d/%m/%Y')
                value2 = datetime.strptime(client2[key], '%d/%m/%Y')
            else:
                value1 = client1[key]
                value2 = client2[key]
            
            if value1 != value2:
                return (value2 > value1) - (value1 > value2) if reverse else (value1 > value2) - (value2 > value1)
        return 0

    def updateTable(self, changed_field=None):
        if changed_field:
            if changed_field in self.sort_order:
                self.sort_order.remove(changed_field)
            self.sort_order.insert(0, changed_field)

        self.data.sort(key=cmp_to_key(self.compare_clients))
        
        for i in self.tree.get_children():
            self.tree.delete(i)

        for client in self.data:
            self.tree.insert('', 'end', values=(
                client['nombre'],
                client['edad'],
                client['fecha_de_nacimiento'],
                client['rut'],
                client['cuentas'][0] if client['cuentas'] else ''
            ))

    def abrir_tabla_clientes(self):
        ClientFilterWindow(self.window)

class Registro_Usuario:
    def __init__(self, parent):
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Registro de Usuario")

        style = ttk.Style()
        style.configure('Blue.TLabelframe.Label', foreground='blue')

        self.labelframe1 = ttk.LabelFrame(self.ventana, text="Registro Usuario", style='Blue.TLabelframe')     
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)        
        self.registro_usuario()
        self.labelframe2 = ttk.LabelFrame(self.ventana, text="Operaciones", style='Blue.TLabelframe')        
        self.labelframe2.grid(column=0, row=1, padx=5, pady=10)        
        self.form_operaciones()

    def registro_usuario(self):
        self.label1=ttk.Label(self.labelframe1, text="Nombres:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.entry1=ttk.Entry(self.labelframe1)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Apellidos:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.entry2=ttk.Entry(self.labelframe1)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe1, text="RUT:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.entry3=ttk.Entry(self.labelframe1)
        self.entry3.grid(column=1, row=2, padx=4, pady=4)
        self.label4=ttk.Label(self.labelframe1, text="Direccion:")
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.entry4=ttk.Entry(self.labelframe1)
        self.entry4.grid(column=1, row=3, padx=4, pady=4)
        self.label5=ttk.Label(self.labelframe1, text="Telefono:")
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.entry5=ttk.Entry(self.labelframe1)
        self.entry5.grid(column=1, row=4, padx=4, pady=4)
        self.label6=ttk.Label(self.labelframe1, text="Correo Electronico:")
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.entry6=ttk.Entry(self.labelframe1)
        self.entry6.grid(column=1, row=5, padx=4, pady=4)

    def form_operaciones(self):
        self.boton1=ttk.Button(self.labelframe2, text="Registrar")
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.boton2=ttk.Button(self.labelframe2, text="Cancelar", command=self.ventana.destroy)
        self.boton2.grid(column=1, row=0, padx=4, pady=4)
        self.boton3=ttk.Button(self.labelframe2, text="Continuar")
        self.boton3.grid(column=2, row=0, padx=4, pady=4)

class VentanaAdministrador:
    def __init__(self, parent):
        self.parent = parent
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Login Administrador")
        
        # Crear estilo personalizado
        style = ttk.Style()
        style.configure('Blue.TLabelframe.Label', foreground='blue')

        self.labelframe1 = ttk.LabelFrame(self.ventana, text="Administrador:", style='Blue.TLabelframe')      
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)        
        self.login()

    def login(self):
        self.label1 = ttk.Label(self.labelframe1, text="Ingrese Clave:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.entry1 = ttk.Entry(self.labelframe1, show="*")
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.boton1 = ttk.Button(self.labelframe1, text="Ingresar", command=self.validar_clave)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def validar_clave(self):
        try:
            with open('Clave_Administrador.json', 'r') as archivo:
                datos = json.load(archivo)
                clave_correcta = datos[0]['Clave_Administrador']
                
            clave_ingresada = self.entry1.get()
            
            if clave_ingresada == clave_correcta:
                messagebox.showinfo("Éxito", "Clave correcta")
                self.ventana.destroy()
                ClientDataWindow(self.parent)
            else:
                messagebox.showerror("Error", "Clave incorrecta")
                self.entry1.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer el archivo: {str(e)}")

class VentanaUsuario:
    def __init__(self, parent):
        self.parent = parent
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Login Usuario")
        
        style = ttk.Style()
        style.configure('Blue.TLabelframe.Label', foreground='blue')

        self.labelframe1 = ttk.LabelFrame(self.ventana, text="Usuario:", style='Blue.TLabelframe')      
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)        
        self.login()

    def login(self):
        self.label1 = ttk.Label(self.labelframe1, text="Nombre de usuario:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.entry1 = ttk.Entry(self.labelframe1)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2 = ttk.Label(self.labelframe1, text="Ingrese clave:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.entry2 = ttk.Entry(self.labelframe1, show="*")
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        
        self.btn_registrar = ttk.Button(self.labelframe1, text="Registrarse", command=self.abrir_registro)
        self.btn_registrar.grid(column=0, row=2, padx=4, pady=4)
        
        self.btn_ingresar = ttk.Button(self.labelframe1, text="Ingresar")
        self.btn_ingresar.grid(column=1, row=2, padx=4, pady=4)

    def abrir_registro(self):
        self.ventana.destroy()  # Cerrar ventana de login
        Registro_Usuario(self.parent)  # Abrir ventana de registro

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ventana Principal")
        
        # Crear estilo personalizado
        style = ttk.Style()
        style.configure('Blue.TLabelframe.Label', foreground='blue')
        
        self.labelframe1 = ttk.LabelFrame(self.ventana1, text="Administrador:", style='Blue.TLabelframe')        
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)        
        self.Administrador()
        
        self.labelframe2 = ttk.LabelFrame(self.ventana1, text="Usuario", style='Blue.TLabelframe')        
        self.labelframe2.grid(column=0, row=1, padx=10, pady=10)        
        self.Usuario()
        self.ventana1.mainloop()

    def Administrador(self):
        self.label1 = ttk.Button(self.labelframe1, text="Ingresar", command=self.abrir_ventana_admin)
        self.label1.grid(column=0, row=0, padx=50, pady=4)

    def Usuario(self):
        self.boton2 = ttk.Button(self.labelframe2, text="Ingresar", command=self.abrir_ventana_usuario)
        self.boton2.grid(column=0, row=0, padx=50, pady=4)

    def abrir_ventana_admin(self):
        VentanaAdministrador(self.ventana1)

    def abrir_ventana_usuario(self):
        VentanaUsuario(self.ventana1)

if __name__ == "__main__":
    aplicacion1 = Aplicacion()