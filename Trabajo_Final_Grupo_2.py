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
def eliminar():
    print ("Ingrese el índice del elemento que desea eliminar");
    indice = int(input());
    longitud = int(len(lista));
    if (indice > longitud or indice < 0):
        print ("El indice debe de estar entre o y ", longitud-1);
    else:
        del lista[indice];
        print ("Elemento eliminado");        
def modificar():
    print ("Ingrese el índice del elemento que desea modificar");
    indice = int(input());
    print ("Ingrese el nuevo valor del elemento");
    elemento = input();
    longitud = int(len(lista));
    if (indice > longitud or indice < 0):
        print ("El indice debe de estar entre o y ", longitud-1);
    else:
        lista[indice] = elemento;
        print ("Elemento modificado");
def mayor():
    mayor = max(lista);
    print ("El elemento mayor es: ", mayor);
def menor():
    menor = min(lista);
    print ("El elemento menor es: ", menor);
def principal():
    opcion = "1";
    print ("  MANIPULACIÓN DE UNA LISTA  ");
    print ("="*30);
    while (opcion != "8"):
        print ("¿Qué deseas hacer?");
        print ("1) Capturar lista");
        print ("2) Mostrar lista");
        print ("3) Mostrar el elemento mayor");
        print ("4) Mostrar el elemento menor");
        print ("5) Agregar un elemento a la lista");
        print ("6) Eliminar un elemento de la lista");
        print ("7) Modificar un elemento de la lista");
        print ("8) Salir");
        opcion = input();
        #Evaluando el valor de opción:
        if (opcion == "1"):
            capturar();
        elif (opcion == "2"):
            mostrar();
        elif (opcion == "3"):
            mayor();
        elif (opcion == "4"):
            menor();
        elif (opcion == "5"):
            agregar();
        elif (opcion == "6"):
            eliminar();
        elif (opcion == "7"):
            modificar();
        elif (opcion == "8"):
            print ("Saliendo...");
            print ("¡PROGRAMA TERMINADO!");
        else:
            print ("¡Opción incorrecta!");
principal();