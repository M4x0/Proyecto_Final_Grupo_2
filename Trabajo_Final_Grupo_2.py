#Ejercicio del trabajo final del Grupo 2
def capturar():
    global lista;
    lista = [];
    print ("¿Cuantos elementos va a tener la lista?");
    n = int(input());
    for i in range(0,n):
        print("Ingresa el elemento del índice ", i);
        elemento = input();
        lista.insert(i,elemento);
def mostrar():
    lista_ordenada = sorted(lista);
    print(lista_ordenada);        
def agregar():
    print("Ingrese el elemento que desea agregar");
    elemento = input();
    print ("Ingrese el índice donde desea agregarlo");
    indice = int(input());
    longitud = int(len(lista));
    if (indice > longitud) or (indice < 0):
        print ("El indice debe de estar entre o y ", longitud);
    else:
        lista.insert(indice,elemento);
        print ("Elemento agregado");
capturar();
mostrar();
agregar();