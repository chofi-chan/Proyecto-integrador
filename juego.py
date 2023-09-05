import readchar
import os
import random

class Juego:
    def __init__(self, path_a_mapas):
        self.path_a_mapas = path_a_mapas
        self.mapa = self.cargar_mapa_aleatorio()
        self.matriz_maze = self.cadena_a_matriz(self.mapa)
        self.posicion_inicio, self.posicion_fin = self.encontrar_posiciones_inicio_y_fin(self.matriz_maze)
        self.px, self.py = self.posicion_inicio

    def cargar_mapa_aleatorio(self):
        archivos_mapa = os.listdir(self.path_a_mapas)
        nombre_archivo = random.choice(archivos_mapa)
        path_completo = os.path.join(self.path_a_mapas, nombre_archivo)
        with open(path_completo, "r") as archivo_mapa:
            return archivo_mapa.read().strip()

    def cadena_a_matriz(self, cadena_maze):
        return list(map(list, cadena_maze.strip().split("\n")))

    def encontrar_posiciones_inicio_y_fin(self, matriz_maze):
        for i in range(len(matriz_maze)):
            for j in range(len(matriz_maze[i])):
                if matriz_maze[i][j] == "P":
                    posicion_inicio = (i, j)
                elif matriz_maze[i][j] == "E":
                    posicion_fin = (i, j)
        return posicion_inicio, posicion_fin

    def jugar(self):
        while (self.px, self.py) != self.posicion_fin:
            self.terminal()
            for fila in self.matriz_maze:
                print("".join(fila))

            tecla = readchar.readkey()
            if tecla == readchar.key.UP:
                nueva_px, nueva_py = self.px - 1, self.py
            elif tecla == readchar.key.DOWN:
                nueva_px, nueva_py = self.px + 1, self.py
            elif tecla == readchar.key.LEFT:
                nueva_px, nueva_py = self.px, self.py - 1
            elif tecla == readchar.key.RIGHT:
                nueva_px, nueva_py = self.px, self.py + 1
            else:
                continue

            if (
                0 <= nueva_px < len(self.matriz_maze)
                and 0 <= nueva_py < len(self.matriz_maze[0])
                and self.matriz_maze[nueva_px][nueva_py] != "#"
            ):
                self.matriz_maze[self.px][self.py] = "."
                self.px, self.py = nueva_px, nueva_py
                self.matriz_maze[self.px][self.py] = "P"

        self.terminal()
        for fila in self.matriz_maze:
            print("".join(fila))
        print("¡Felicidades! ¡Has llegado al final del laberinto!")
        input("Presiona Enter para salir...")

    def terminal(self):
        os.system("cls" if os.name == "nt" else "clear")