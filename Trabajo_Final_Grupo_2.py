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
capturar();