def my_missings(datos):
    print("% de missings en columnas:")
    aux = 100*datos.isnull().mean()
    display(aux[aux>0])

def my_message():
    print("Hola")
