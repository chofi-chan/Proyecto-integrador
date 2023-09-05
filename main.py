from juego_archivo import JuegoArchivo

if __name__ == "__main__":
    # Ruta a la carpeta que contiene los mapas
    path_a_mapas = "C:/Users/Luchito17/Desktop/mapa"
    nombre_jugador = input("Por favor, ingresa tu nombre: ")
    juego = JuegoArchivo(path_a_mapas)
    juego.terminal()
    print("¡Bienvenido, " + nombre_jugador +
          "! Este es el Proyecto Integrador.")
    juego.jugar()
