

def mayusculasMinuscula(valor):
    print(valor.upper())
    print(valor.lower())
    print(valor.capitalize())

mayusculasMinuscula(texto)

def longitudMensaje(valor):
    print("La longitud del mensaje es: ", len(valor))

def eliminarEspacios(valor):
    print(valor.strip())

def arregloPalabras(valor):
    print(valor.split())

def palabraDeArreglo():
    nombres = ["Luis","Carlos","Maria","Pedro"]
    print("".join(nombres))

def otrasFunciones(valor):
    print(valor.replace("Python", "Luis Angel"))
    print(valor.find("mundo"))
    print(valor.count("Python"))