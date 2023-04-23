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
    
    
if __name__ == '__main__':
    decimal_bin(13)
    