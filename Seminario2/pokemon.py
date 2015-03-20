# Practica 2 de Sistemas Distribuidos

# Realizada por Francisco Tomas Cruz Molina y Julian Rodriguez Carave

# Este programa intenta encontrar la lista mas larga posible de palabras de manera que la ultima letra de 
#   una palabra coincida con la primera de la siguiente palabra, de una lista de palabras dadas.
#   En este caso, dicha lista dada se encuentra en un fichero de texto llamado 'pokemon.txt'. Si encontramos
#   mas de una lista de palabras de la misma longitud, nos quedaremos con la primera.



fichero = open("pokemon.txt", "r")  #Abrimos el fichero y lo guardamos en la variable
contenido = fichero.read()
lista_base = contenido.split()   #Copiamos el contenido del fichero en una lista
fichero.close()

cont_final = 0

for i in range(len(lista_base)):    #Recorremos la lista de palabras n veces, siendo n el numero de palabras de esta
    primera_palabra = lista_base[i]    
    lista_aux = []
    lista_aux.append(primera_palabra)   #Metemos la primera palabra a la lista auxiliar
    cont_aux = 1
    puntero = 0
    ultima_letra = primera_palabra[len(primera_palabra)-1]  #Y guardamos la ultima letra de la primera palabra, para comparar

    #Ahora recorreremos toda la lista de palabras, de principio a fin, buscando que se cumpla lo que buscamos,
    #   y cada vez que sumemos una nueva palabra a la lista, empezamos a recorrer de nuevo, ya que esa nueva
    #   palabra tendra a su vez una nueva letra final, que usaremos para comparar con la primera de las siguientes.
    #   Siempre tenemos como condicion que cada nueva palabra con la que comparamos no este ya en la lista.
    while(puntero <= len(lista_base)-1):    
        palabra_aux = lista_base[puntero]
        if(palabra_aux not in lista_aux and ultima_letra == palabra_aux[0]):
            lista_aux.append(palabra_aux)
            cont_aux+=1
            ultima_letra = palabra_aux[len(palabra_aux)-1]
            puntero = 0
        else:
            puntero+=1

    #Despues de haber recorrido las veces que sean necesarias la lista, habremos obtenido una lista auxiliar con
    #   un numero determinado de palabras que cumplen lo requerido. Es ahora cuando comparamos que sea la mayor
    #   lista de palabras hasta el momento. Si es asi nos quedamos con ella, sino la desechamos y empezamos de nuevo.
    if(cont_aux > cont_final):
        cont_final = cont_aux
        lista_final = lista_aux

for j in lista_final:
    print j

print "\nLa lista final mas larga encontrada tiene", len(lista_final), "elementos.\n"
