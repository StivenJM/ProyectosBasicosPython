def esBinario(x: str):
    for c in x:
        if c != '0' and c != '1':
            return False
    return True

def esOctal(x: str):
    for c in x:
        if c != '0' and c != '1' and c != '2' and c != '3' and c != '4' and c != '5' and c != '6' and c != '7':
            return False
    return True

def esDecimal(x: str):
    for c in x:
        if c != '0' and c != '1' and c != '2' and c != '3' and c != '4' and c != '5' and c != '6' and c != '7' and c != '8' and c != '9':
            return False
    return True

def esHexadecimal(x: str):
    for c in x:
        if c != '0' and c != '1' and c != '2' and c != '3' and c != '4' and c != '5' and c != '6' and c != '7' and c != '8' and c != '9' and c != 'A' and c != 'B' and c != 'C' and c != 'D' and c != 'E' and c != 'F':
            return False
    return True

def menu(numero: str, tipo: str):
    bandera = int(tipo) # indice de formato
    formato = ['binario', 'octal', 'decimal', 'hexadecimal']
    print(f'''
          ***************************************************************************
                                    Conversor de Numeros
          ***************************************************************************

          Numero {formato[bandera]}: {numero}
          
          1.- Convertir a binario
          2.- Convertir a octal
          3.- Convertir a decimal
          4.- Convertir a hexadecimal
          5.- Cambiar numero
          0.- Salir

          Escoja una opcion: ''', end="")
    opcion = input("")
    return opcion

def menuCambiarNumero():
    print('''
          ***************************************************************************
                                    Cambiar Numero
          ***************************************************************************
          
          0.- Ingresar Binario
          1.- Ingresar Octal
          2.- Ingresar Decimal
          3.- Ingresar Hexadecimal
          4.- Salir sin cambiar

          Escoja una opcion: ''', end="")
    opcion = input("")
    return opcion

def cambiarNumero(num: str, tipo:str):
    opcion = '0'
    opcIncorrecta = True
    while(opcIncorrecta):
        opcion = menuCambiarNumero()
        if opcion == '0' or opcion == '1' or opcion == '2' or opcion == '3' or opcion == '4':
            opcIncorrecta = False
        else:
            print("\t\tOpcion incorrecta. Vuelva a intentarlo.")
    
    if opcion != '4':
        num = input("\tEscriba el numero: ")

        if opcion == '0':
            while(not esBinario(num)):
                num = input("\tINCORRECTO -> Escriba el numero: ")
        if opcion == '1':
            while(not esOctal(num)):
                num = input("\tINCORRECTO -> Escriba el numero: ")
        if opcion == '2':
            while(not esDecimal(num)):
                num = input("\tINCORRECTO -> Escriba el numero: ")
        if opcion == '3':
            while(not esHexadecimal(num)):
                num = input("\tINCORRECTO -> Escriba el numero: ")

        tipo = opcion

    return [num, tipo]

def quitarCerosIzquierda(x: str):
    i = 0 # Indice
    while(i < len(x)-1 and x[i] == '0'):
        i += 1
    return x[i::]

# por ejemplo si bloque es 3, entonces para un numero como 2913 sería 002 913
def completarCerosIzquierda(x: str, bloque: int):
    tam = len(x)
    sobrantes = tam%bloque
    faltantes = bloque-sobrantes if sobrantes != 0 else 0
    resultado = ('0'*(faltantes)) + x
    return resultado

def aBinario(num: str, tipo: str):
    def numBinario(): # Cuando num es un binario
        return num
    def numOctal(): # Cuando num es un octal
        equivalencias = {
            '0': '000',
            '1': '001',
            '2': '010',
            '3': '011',
            '4': '100',
            '5': '101',
            '6': '110',
            '7': '111'
        }
        resultado = ""
        for d in num:
            resultado += equivalencias[d]
        resultado = quitarCerosIzquierda(resultado)
        return resultado
    def numDecimal(): # Cuando num es un decimal
        resultado = list()
        numero = int(num)
        while(numero != 0):
            resultado.append(numero%2)
            numero = int(numero/2)
        else:
            resultado.append(0)
        #se da la vuelta a la lista resultado
        resultado = resultado[-1::-1]
        #se transforma la lista en un string
        resultado = ''.join(map(str, resultado))
        resultado = quitarCerosIzquierda(resultado)
        return resultado
    def numHexadecimal(): # Cuando num es un hexadecimal
        equivalencias = {
            '0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'F': '1110',
            'G': '1111'
        }
        resultado = ''
        for d in num:
            resultado += equivalencias[d]
        resultado = quitarCerosIzquierda(resultado)
        return resultado
    
    retorno = ""
    if tipo == '0':
        retorno = numBinario()
    elif tipo == '1':
        retorno = numOctal()
    elif tipo == '2':
        retorno = numDecimal()
    elif tipo == '3':
        retorno = numHexadecimal()
    return retorno

def aOctal(num: str, tipo: str):
    def numBinario(): # Cuando num es un binario
        octal = completarCerosIzquierda(num, 3)
        equivalencias = {
            '000': '0',
            '001': '1',
            '010': '2',
            '011': '3',
            '100': '4',
            '101': '5',
            '110': '6',
            '111': '7'
        }
        i = 0 #indice
        resultado = ''
        while(i < len(octal)):
            resultado += equivalencias[octal[i:i+3]]
            i += 3
        return resultado
    def numOctal(): # Cuando num es un octal
        return num
    def numDecimal(): # Cuando num es un decimal
        resultado = list()
        numero = int(num)
        while(numero != 0):
            resultado.append(numero%8)
            numero = int(numero/8)
        else:
            resultado.append(0)
        #se da la vuelta a la lista resultado
        resultado = resultado[-1::-1]
        #se transforma la lista en un string
        resultado = ''.join(map(str, resultado))
        resultado = quitarCerosIzquierda(resultado)
        return resultado
    def numHexadecimal(): # Cuando num es un hexadecimal
        binario = aBinario(num, '3') # Primero se transforma a binario
        resultado = aOctal(binario, '0') # luego se transforma a octal
        return resultado
    
    retorno = ""
    if tipo == '0':
        retorno = numBinario()
    elif tipo == '1':
        retorno = numOctal()
    elif tipo == '2':
        retorno = numDecimal()
    elif tipo == '3':
        retorno = numHexadecimal()
    return retorno

def aDecimal(num: str, tipo: str):
    def numBinario(): # Cuando num es un binario}
        digitos = list(num)
        digitos = digitos[-1::-1]
        digitos = map(int, digitos)
        resultado = 0
        for i, a in enumerate(digitos):
            resultado += a * pow(2, i)
        return str(resultado)
    def numOctal(): # Cuando num es un octal
        digitos = list(num)
        digitos = digitos[-1::-1]
        digitos = map(int, digitos)
        resultado = 0
        for i, a in enumerate(digitos):
            resultado += a * pow(8, i)
        return str(resultado)
    def numDecimal(): # Cuando num es un decimal
        return num
    def numHexadecimal(): # Cuando num es un hexadecimal
        equivalencias= {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15
        }
        digitos = list(num)
        digitos = digitos[-1::-1]
        resultado = 0
        for i, a in enumerate(digitos):
            resultado += equivalencias[a] * pow(16, i)
        return str(resultado)
    
    retorno = ""
    if tipo == '0':
        retorno = numBinario()
    elif tipo == '1':
        retorno = numOctal()
    elif tipo == '2':
        retorno = numDecimal()
    elif tipo == '3':
        retorno = numHexadecimal()
    return retorno

def aHexadecimal(num: str, tipo: str):
    def numBinario(): # Cuando num es un binario
        equivalencias = {
            '0000': '0',
            '0001': '1',
            '0010': '2',
            '0011': '3',
            '0100': '4',
            '0101': '5',
            '0110': '6',
            '0111': '7',
            '1000': '8',
            '1001': '9',
            '1010': 'A',
            '1011': 'B',
            '1100': 'C',
            '1101': 'D',
            '1110': 'E',
            '1111': 'F'
        }
        resultado = num
        binario = completarCerosIzquierda(resultado, 4)
        resultado = ''
        i = 0 # Indice
        while i < len(binario):
            resultado += equivalencias[binario[i:i+4]]
            i += 4
        return resultado
    def numOctal(): # Cuando num es un octal
        resultado = aBinario(num, '1')
        resultado = aHexadecimal(resultado, '0')
        return resultado
    def numDecimal(): # Cuando num es un decimal
        resultado = aBinario(num, '2')
        resultado = aHexadecimal(resultado, '0')
        return resultado
    def numHexadecimal(): # Cuando num es un hexadecimal
        return num
    
    retorno = ""
    if tipo == '0':
        retorno = numBinario()
    elif tipo == '1':
        retorno = numOctal()
    elif tipo == '2':
        retorno = numDecimal()
    elif tipo == '3':
        retorno = numHexadecimal()
    return retorno

#---------------------------------PROGRAMA---------------------------------

#Valores por defecto de numero y tipo
num = '0'
tipo = '2' #tipo decimal
while True:
    opcion = menu(num, tipo)
    if opcion == '1':
        resultado = aBinario(num, tipo)
        print(f"\n\tEl numero binario es: {resultado}")
        print("\tPresiona enter para continuar.", end="")
    elif opcion == '2':
        resultado = aOctal(num, tipo)
        print(f"\n\tEl numero octal es: {resultado}")
        print("\tPresiona enter para continuar.", end="")
    elif opcion == '3':
        resultado = aDecimal(num, tipo)
        print(f"\n\tEl numero decimal es: {resultado}")
        print("\tPresiona enter para continuar.", end="")
    elif opcion == '4':
        resultado = aHexadecimal(num, tipo)
        print(f"\n\tEl numero hexadecimal es: {resultado}")
        print("\tPresiona enter para continuar.", end="")
    elif opcion == '5':
        num, tipo = cambiarNumero(num, tipo)
        print("\tPresiona enter para continuar.", end="")
    elif opcion == '0':
        break
    else:
        print("\tOpcion incorrecta. Presiona enter para continuar.", end="")
    input("")
