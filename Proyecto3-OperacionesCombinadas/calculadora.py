def menu():
    print('''
        **********************************************************
                                Calculadora
        **********************************************************
          Escriba la operacion:
          ''')
    retorno = input("")
    return retorno
    
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def separarExp(expresion: str):
    retorno = list()
    i = 0 # indice
    while i < len(expresion):
        num = ""
        esNum = False # es numero
        while i < len(expresion) and expresion[i].isdigit():
            esNum = True
            num = num + expresion[i]
            i = i + 1
        else:
            if esNum:
                retorno.append(num)
            if i < len(expresion):
                retorno.append(expresion[i])
            i = i + 1
    return retorno
            
def esOperando(o: str):
    return o == '+' or o == '-' or o == '*' or o == '/'

# Esta funcion se complementa con la funcion resolver()
def ejecutarPilas(pila1: list, pila2: list, todo: bool):
    operacion = pila2.pop()
    num2 = pila1.pop()
    num1 = pila1.pop()
    if operacion == '+':
        pila1.append(suma(num1, num2))
    elif operacion == '-':
        pila1.append(resta(num1, num2))
    elif operacion == '*':
        pila1.append(mul(num1, num2))
    elif operacion == '/':
        pila1.append(div(num1, num2))
    
    if todo == True and len(pila2)!=0:
        ejecutarPilas(pila1, pila2, len(pila1)>2)

def resolver(expresion: str):
    expresion = expresion.replace(" ","")
    expresion = separarExp(expresion)
    i = 0 # indice
    pila1 = list()
    pila2 = list()
    while i < len(expresion):
        if expresion[i].isdigit():
            pila1.append(int(expresion[i]))
        elif esOperando(expresion[i]):
            pila2.append(expresion[i])
        
        if expresion[i] == ')':
            ejecutarPilas(pila1, pila2, False)
        if i == len(expresion)-1:
            ejecutarPilas(pila1, pila2, True)
        
        i = i + 1
    return pila1.pop()
            

# EJECUCION
exp = "(3*2) - (7-2) + (8+2)"
print(resolver(exp))