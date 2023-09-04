from juego_archivo import JuegoArchivo

if __name__ == "__main__":
    path_a_mapas = "C:/Users/Luchito17/Desktop/mapa"  # Ruta a la carpeta que contiene los mapas
    nombre_jugador = input("Por favor, ingresa tu nombre: ")
    juego = JuegoArchivo(path_a_mapas)
    juego.terminal()
    print("¡Bienvenido, " + nombre_jugador + "! Este es el Proyecto Integrador.")
    juego.jugar()
