import math

class Triangulo:
    def __init__(self, base, altura, angulo):
        self.base = base
        self.altura = altura
        self.angulo = angulo
    
    def calcular_area(self):
        return 0.5 * self.base * self.altura
    
    def calcular_perimetro(self):
        lado = math.sqrt(self.base**2 + self.altura**2)
        return self.base + self.altura + lado
    
    def es_equilatero(self):
        return self.base == self.altura and self.angulo == 60
    
    def calcular_altura(self):
        return self.altura
    
    def cambiar_tamano(self, factor):
        self.base *= factor
        self.altura *= factor

class Circulo:
    def __init__(self, radio, color, semi_circulo):
        self.radio = radio
        self.color = color
        self.semi_circulo = semi_circulo
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def diametro(self):
        return 2 * self.radio
    
    def duplicar_tamano(self):
        self.radio *= 2
    
    def es_punto(self):
        return self.radio == 0

class Rectangulo:
    def __init__(self, base, altura, color):
        self.base = base
        self.altura = altura
        self.color = color
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def obtener_diagonal(self):
        return math.sqrt(self.base**2 + self.altura**2)
    
    def es_cuadrado(self):
        return self.base == self.altura
    
    def cambiar_dimensiones(self, nueva_base, nueva_altura):
        self.base = nueva_base
        self.altura = nueva_altura

class Cuadrado:
    def __init__(self, lado, color, origen_plano):
        self.lado = lado
        self.color = color
        self.origen_plano = origen_plano
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return 4 * self.lado
    
    def diagonal(self):
        return self.lado * math.sqrt(2)
    
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
    
    def cambiar_tamano(self, factor):
        self.lado *= factor

class Pentagono:
    def __init__(self, lado, apotema, color):
        self.lado = lado
        self.apotema = apotema
        self.color = color
    
    def calcular_perimetro(self):
        return 5 * self.lado
    
    def calcular_area(self):
        return (5 * self.lado * self.apotema) / 2
    
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
    
    def escalar(self, factor):
        self.lado *= factor
        self.apotema *= factor
    
    def obtener_info(self):
        return f"Pentágono de lado {self.lado}, apotema {self.apotema}"

# Instanciación de objetos

# Triángulos
triangulo1 = Triangulo(3, 4, 90)
triangulo2 = Triangulo(5, 5, 60)
triangulo3 = Triangulo(6, 8, 120)

# Círculos
circulo1 = Circulo(5, "rojo", False)
circulo2 = Circulo(3, "azul", False)
circulo3 = Circulo(7, "verde", False)

# Rectángulos
rectangulo1 = Rectangulo(4, 6, "amarillo")
rectangulo2 = Rectangulo(5, 5, "naranja")
rectangulo3 = Rectangulo(8, 3, "morado")

# Cuadrados
cuadrado1 = Cuadrado(4, "blanco", True)
cuadrado2 = Cuadrado(6, "negro", False)
cuadrado3 = Cuadrado(5, "gris", True)

# Pentágonos
pentagono1 = Pentagono(5, 3.4, "rosado")
pentagono2 = Pentagono(7, 4.8, "celeste")
pentagono3 = Pentagono(6, 4.1, "verde")