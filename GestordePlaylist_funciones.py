import random
import json
import os
ARCHIVO = "playlist.json"
playlist = []

def menu():
    print("1: Agregar musica")
    print("2: Ver playlist")
    print("3- Selección aleatoria")
    print("4: Buscar en la playlist")
    print("5: Eliminar de la playlist")
    print("6- Guardar .JSON")
    print("7- Cargar .JSON")
    print("8- Salir")

def agregar_musica():
    cantidadcanciones = int(input("¿Cuantas canciones?: "))
    for i in range(cantidadcanciones):
        nombre = input("Nombre de la canción: ")
        artista = input("Compositor: ")
        cancion = {"nombre": nombre, "artista": artista}
        playlist.append(cancion)
        print("Agregada.\n")

def ver_playlist():
    print("\nCanciones registradas:")
    
    if not playlist:
        print("La playlist esta vacia.\n")
        return
    
    for cancion in playlist:
        print("Nombre:", cancion["nombre"], "| Artista:", cancion["artista"])
        print("")

def aleatorio():
     if not playlist:
        print("La playlist esta vacia.\n")
        return
     
     print("\nTe recomendamos escuchar: ", random.choice(playlist))

def buscar_en_playlist():
    busqueda = input("Musica buscada: ")
    encontrado = False

    for cancion in playlist:
        if busqueda.lower() == cancion["nombre"].lower():
            print("\n-Canción encontrada-")
            print("Nombre:", cancion["nombre"], "| Artista:", cancion["artista"])
            encontrado = True
            
            if encontrado == False:
                 print("No se encontro.\n")

def eliminar_en_playlist():
    elimbusqueda = input("Musica que quiere eliminar: ")
    elimencontrado = False

    for cancion in playlist:
        if elimbusqueda.lower() == cancion["nombre"].lower():
            playlist.remove(cancion)
            print("\n-Se quito de la playlist-")
            print("Nombre:", cancion["nombre"], "| Artista:", cancion["artista"])
            elimencontrado = True
            break
        
        if elimencontrado == False:
             print("No se encontro.\n")

def guardar_json(lista, ruta=ARCHIVO):
     with open(ruta, "w", encoding="utf-8") as archivo:
          json.dump(lista, archivo, indent=4, ensure_ascii=False)
          print("JSON guardado con exito.\n")
     return True

def cargar_json(ruta=ARCHIVO):
     if not os.path.exists(ruta):
          return []
     try:
         with open(ruta, "r", encoding="utf-8") as archivo:
             return json.load(archivo)
     except json.JSONDecodeError:
          return []