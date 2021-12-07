import pygame
import numpy as np

ROJO = np.array([255, 0, 0])
VERDE = np.array([0, 255, 0])
AZUL = np.array([0, 0, 255])
AMARILLO = np.array([250, 250, 0])
BLANCO = np.array([255, 255, 255])
NEGRO = np.array([0, 0, 0])


def dibujarBotones(miVentana,  mouse):
    largoBoton = 80
    anchoBoton = 50
    iconoBotones = ["linea", "cuadrado", "circulo",
                    "triangulo", "libre", "poligono", "limpiar"]
    cantidadBotones = len(iconoBotones)
    # light shade of the button
    color_light = (170, 170, 170)
    # dark shade of the button
    color_dark = (100, 100, 100)
    # defining a font
    smallfont = pygame.font.SysFont('Corbel', 15)

    for i in range(cantidadBotones):
        color = color_dark
        if(0 <= mouse[0] <= largoBoton and i*anchoBoton <= mouse[1] <= anchoBoton*(1+i)):
            color = color_light
        pygame.draw.rect(miVentana, color, pygame.Rect(
            0, i*anchoBoton, largoBoton, anchoBoton-5))
        text = smallfont.render(iconoBotones[i], True, (255, 255, 255))
        miVentana.blit(text, (10, i*anchoBoton+anchoBoton*0.5))


def queBotonSePresiono(boton, pos):
    '''
    largoBoton = 80
    anchoBoton = 50
    iconoBotones = ["linea", "cuadrado", "circulo",
                    "triangulo", "libre", "poligono","limpiar"]
    '''
    botonLinea = [[0, 80], [0, 45]]
    botonCuadrado = [[0, 80], [50, 95]]
    botonCirculo = [[0, 80], [100, 145]]
    botonTriangulo = [[0, 80], [150, 195]]
    botonLibre = [[0, 80], [200, 245]]
    botonPoligono = [[0, 80], [250, 295]]
    botonLimpiar = [[0, 80], [300, 345]]

    if (pygame.mouse.get_pos()[0] <= 80):
        if (botonLinea[0][0] <= pos[0] <= botonLinea[0][1] and botonLinea[1][0] <= pos[1] <= botonLinea[1][1]):
            queBoton = "linea"
            print("presiono linea")
        elif(botonCuadrado[0][0] <= pos[0] <= botonCuadrado[0][1] and botonCuadrado[1][0] <= pos[1] <= botonCuadrado[1][1]):
            print("presiono cuadrado")
            queBoton = "cuadrado"
        elif(botonCirculo[0][0] <= pos[0] <= botonCirculo[0][1] and botonCirculo[1][0] <= pos[1] <= botonCirculo[1][1]):
            print("presiono circulo")
            queBoton = "circulo"
        elif(botonTriangulo[0][0] <= pos[0] <= botonTriangulo[0][1] and botonTriangulo[1][0] <= pos[1] <= botonTriangulo[1][1]):
            print("presiono triangulo")
            queBoton = "triangulo"
        elif(botonTriangulo[0][0] <= pos[0] <= botonLibre[0][1] and botonLibre[1][0] <= pos[1] <= botonLibre[1][1]):
            print("presiono libre")
            queBoton = "libre"
        elif(botonTriangulo[0][0] <= pos[0] <= botonPoligono[0][1] and botonPoligono[1][0] <= pos[1] <= botonPoligono[1][1]):
            print("presiono poligono")
            queBoton = "poligono"
        elif(botonTriangulo[0][0] <= pos[0] <= botonLimpiar[0][1] and botonLimpiar[1][0] <= pos[1] <= botonLimpiar[1][1]):
            print("presiono limpiar")
            queBoton = "limpiar"
        else:
            queBoton = boton
    else:
        queBoton = boton
    return queBoton


def graficar(miVentana, boton, listaPuntosLinea, listaPuntosCuadrado, listaPuntosCirculo, listaPuntosTriangulo):
    if (boton == "ninguno"):
        pass
    elif(boton == "linea"):
        puntosCapturados = len(listaPuntosLinea)
        if puntosCapturados >= 2:
            # pygame.draw.line(
            # miVentana, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), listaPuntosLinea[0], listaPuntosLinea[1], 5)
            pygame.draw.line(
                miVentana, (255, 0, 0), listaPuntosLinea[0], listaPuntosLinea[1], 1)
            listaPuntosLinea.clear()
    elif(boton == "cuadrado"):
        puntosCapturados = len(listaPuntosCuadrado)
        if puntosCapturados >= 2:

            pygame.draw.rect(
                miVentana, (255, 0, 0),  pygame.Rect(
                    listaPuntosCuadrado[0][0], listaPuntosCuadrado[0][1],
                    abs(listaPuntosCuadrado[1][0]-listaPuntosCuadrado[0][0]),
                    abs(listaPuntosCuadrado[1][1]-listaPuntosCuadrado[0][1])), 1)
            listaPuntosCuadrado.clear()

    elif(boton == "circulo"):
        puntosCapturados = len(listaPuntosCirculo)
        if puntosCapturados >= 2:
            pygame.draw.ellipse(miVentana, (255, 0, 0), pygame.Rect(
                listaPuntosCirculo[0][0], listaPuntosCirculo[0][1],
                abs(listaPuntosCirculo[1][0]-listaPuntosCirculo[0][0]),
                abs(listaPuntosCirculo[1][1]-listaPuntosCirculo[0][1])), 1)
            listaPuntosCirculo.clear()
    elif(boton == "triangulo"):
        puntosCapturados = len(listaPuntosTriangulo)
        if puntosCapturados >= 3:
                # pygame.draw.line(
                #    miVentana, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), listaPuntosLinea[0], listaPuntosLinea[1], 5)

            pygame.draw.lines(
                miVentana, (255, 0, 0), True,  listaPuntosTriangulo, 1)
            listaPuntosTriangulo.clear()


if __name__ == "__main__":
    pygame.init()
    miVentana = pygame.display.set_mode((800, 600))
    miVentana.fill(BLANCO)
    running = True

    listaPuntosLinea = []
    listaPuntosCuadrado = []
    listaPuntosTriangulo = []
    listaPuntosCirculo = []
    boton = "ninguno"
    while (running):
        # Barras(miVentana)
        for eventos in pygame.event.get():
            if (eventos.type == pygame.QUIT):
                running = False

            if (eventos.type == pygame.MOUSEBUTTONDOWN):
                boton = queBotonSePresiono(boton, pygame.mouse.get_pos())
                if(boton == "linea"):

                    listaPuntosCuadrado = []
                    listaPuntosTriangulo = []
                    listaPuntosCirculo = []
                    if (pygame.mouse.get_pos()[0] > 80):
                        listaPuntosLinea.append(pygame.mouse.get_pos())

                if(boton == "cuadrado"):
                    listaPuntosLinea = []
                    listaPuntosTriangulo = []
                    listaPuntosCirculo = []
                    if (pygame.mouse.get_pos()[0] > 80):
                        listaPuntosCuadrado.append(pygame.mouse.get_pos())

                if(boton == "circulo"):
                    listaPuntosCuadrado = []
                    listaPuntosTriangulo = []
                    listaPuntosLinea = []
                    if (pygame.mouse.get_pos()[0] > 80):
                        listaPuntosCirculo.append(pygame.mouse.get_pos())

                if(boton == "triangulo"):
                    listaPuntosCuadrado = []
                    listaPuntosLinea = []
                    listaPuntosCirculo = []
                    if (pygame.mouse.get_pos()[0] > 80):
                        listaPuntosTriangulo.append(pygame.mouse.get_pos())
                if(boton == "limpiar"):
                    listaPuntosLinea = []
                    listaPuntosCuadrado = []
                    listaPuntosTriangulo = []
                    listaPuntosCirculo = []
                    miVentana.fill(BLANCO)

        mouse = pygame.mouse.get_pos()
        dibujarBotones(miVentana, mouse)
        graficar(miVentana, boton, listaPuntosLinea, listaPuntosCuadrado,
                 listaPuntosCirculo, listaPuntosTriangulo)
        pygame.display.update()

    exit()
