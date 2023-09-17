def imprimirMenu():
    print('''
**********************************
    MENU DE CALCULADORA BASICA
**********************************
1.- Sumar
2.- Restar
3.- Multiplicar
4.- Dividir
0.- Salir
''', end="")
    retorno = input("Escoja una opción: ")
    return retorno

def pedirNumeros():
    lista = list()
    while True:
        try:
            tam = int(input("¿Cuantos numeros desea ingresar? "))
            if tam > 0:
                break
            else:
                print("Valor incorrecto. Vuelva a escribir.")
        except ValueError:
            print("Valor incorrecto. Vuelva a escribir.")
    
    for i in range(1, tam+1):
        while True:
            try:
                num = int(input(f"Escriba el numero n{i}: "))
                lista.append(num)
                break
            except ValueError:
                print("Valor incorrecto. Vuelva a escribir.")
    
    return lista

def sumar(numeros: list):
    print("Operacion: N1 + N2 + ... + Nn")
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

def restar(numeros: list):
    print("Operacion: N1 - N2 - ... - Nn")
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado

def multiplicar(numeros: list):
    print("Operacion: N1 * N2 * ... * Nn")
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado *= num
    return resultado

def dividir(numeros: list):
    print("Operación: (((N1 / N2) / ...) / Nn)")
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado /= num
    return resultado

# Ejecucion de todas las funciones descritas
while True:
    opcion = imprimirMenu()
    if opcion == '0':
        break
    
    if opcion == '1':
        lista = pedirNumeros()
        num = sumar(lista)
    elif opcion == '2':
        lista = pedirNumeros()
        num = restar(lista)
    elif opcion == '3':
        lista = pedirNumeros()
        num = multiplicar(lista)
    elif opcion == '4':
        lista = pedirNumeros()
        num = dividir(lista)
    else:
        print("Opción incorrecta.")
        continue
    print(f"El resultado es: {num}")

