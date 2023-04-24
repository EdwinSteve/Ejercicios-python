""""Ejercicios python Edwin Steve Suarez Rivera FET

Primer Ejericio:

cadena = input("Escribe la cadena que quieres contar: ")

while cadena.strip() == "":
    cadena = input("Por favor, escribe una cadena válida: ")

cadena = cadena.lower()

palabra_mas_larga =  max(cadena.split(' '), key=len)

print("la cadena de texto mas larga es:" + palabra_mas_larga)"""


#Ejercicio 2#

def bin_decimal(binario):

    suma = 0
    posicion = 0
    
    print("Tu binario: ", binario)
 
    while(binario > 0):
    
        digito = binario % 10;
        print(digito)
        binario = int(binario / 10);
        suma = suma + digito * pow(2,posicion);
        posicion = posicion + 1;
    
    print("Corresponde al decimal: ", suma, end='')   
    
    
def decimal_bin(decimal):
    
    binario = []
    
    print("Tu decimal ", decimal)
 
    while(decimal > 0):
    
        binario.append(decimal % 2);
        decimal = int(decimal / 2);

        digitos = binario[:: -1]
    
    print("Corresponde al binario: ", digitos, end='')
    
def deci_oct(n):
    
    octal = []
    
    print("Tu decimal: ", n)
    
    while(n != 0):
        
        octal.append(n % 8);
        n = int(n/8);
        
        num_octal = octal[:: -1]
        
    print("Corresponde a: ", num_octal, end= '')
    
def dec_hexadecimal(n):
    
    print("El decimal: ", n);
    
    hexadecimal = format(n, '0x');
    
    print("Equivale a: ", hexadecimal);
    
    
#Ejercicio 3

def random():
    
    import random
    # Genera una lista de 10 números aleatorios
    lista = [random.randint(0, 100) for i in range(10)];

    # Imprimir la lista original
    print("Lista original: ", lista, end= '');

    # Ordenar la lista de menor a mayor
    lista.sort()

    # Imprimir la lista ordenada
    print("Lista ordenada: ", lista, end= '');
    
#Ejercicio 4

def convert_cel(dato):

    # Convertir de Celsius a Fahrenheit usando la fórmula de conversión
    fahrenheit = (dato * 9/5) + 32

    # Imprimir el resultado de la conversión
    print("La temperatura en grados Fahrenheit es:", fahrenheit) 
    
#Ejercicio 5

def factorial(n):

    # Inicializar el resultado en 1
    factorial = 1

    # Calcular el factorial del número ingresado
    for i in range(1, n + 1):
        factorial *= i

    # Imprimir el resultado del factorial
    print("El factorial de", n, "es", factorial)
    
if __name__ == '__main__':
    factorial(5);   
    
#Ejercicio 6

def primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
if primo(n):
    print(f"{n} es un número primo")
else:
    print(f"{n} no es un número primo")
    
    primo(5);
    
# Ejercicio 7

def contar_palabras(cadena):
    # Eliminamos los espacios en blanco al principio y al final de la cadena
    cadena = cadena.strip()
    # Si la cadena está vacía, devuelve 0
    if not cadena:
        return 0
    # Contamos el número de espacios en blanco en la cadena y le sumamos 1
    num_palabras = cadena.count(' ') + 1
    return num_palabras

contar_palabras(jijijija sasas);
num_palabras = contar_palabras(cadena)
print(f"El texto tiene {num_palabras} palabras.")

#Ejercicio 8

def millas_a_kilometros(millas):
    # Una milla equivale a 1.60934 kilómetros
    kilometros = millas * 1.60934
    return kilometros

millas_a_kilometros(13);