import pygame
import numpy as np

COLORES = {
    "Rojo":  np.array([255, 0, 0]),
    "Verde": np.array([0, 255, 0]),
    "Azul": np.array([0, 0, 255]),
    "Amarillo": np.array([250, 250, 0]),
    "Blanco": np.array([255, 255, 255]),
    "Negro":  np.array([0, 0, 0]),
    "Morado": np.array([163, 73, 164])
}

RELLENO = {
    "SinR": 3,
    "ConR": 0,
}

LARGO_BOTON = 100
ANCHO_BOTON = 70


def dibujarBotonesColor(miVentana, mouse, boton):

    iconoBotones = ["Amarillo", "Azul", "Rojo",
                    "Negro", "Blanco", "Verde", "Morado"]
    cantidadBotones = len(iconoBotones)
    # light shade of the button
    color_light = (170, 170, 170)
    # dark shade of the button
    color_dark = (100, 100, 100)
    # defining a font
    smallfont = pygame.font.SysFont('Corbel', 15)

    for i in range(cantidadBotones):
        text = smallfont.render(iconoBotones[i], True, (0, 0, 0))

        color = color_light
        if boton == iconoBotones[i]:
            color = color_dark
        pygame.draw.rect(miVentana, color, pygame.Rect(
            i*LARGO_BOTON+LARGO_BOTON+5, 0, LARGO_BOTON-5, ANCHO_BOTON-5))

        mitadX = LARGO_BOTON/2 - \
            text.get_rect()[2]/2 + i*(LARGO_BOTON) - 2.5 + LARGO_BOTON+5
        mitadY = ANCHO_BOTON/2 - text.get_rect()[3]/2
        miVentana.blit(text, (mitadX, mitadY))


def dibujarBotonesControl(miVentana, mouse, botonColor, botonRelleno="SinR"):

    iconoBotones = ["Linea", "Cuadrado", "Circulo",
                    "Triangulo", "Lapiz", "Poligono", "Limpiar", "ConR", "SinR"]
    cantidadBotones = len(iconoBotones)
    # light shade of the button
    color_light = (170, 170, 170)
    # dark shade of the button
    color_dark = (100, 100, 100)
    # defining a font
    smallfont = pygame.font.SysFont('Corbel', 15)

    for i in range(cantidadBotones):
        text = smallfont.render(iconoBotones[i], True, (0, 0, 0))
        #print(iconoBotones[i] + " " + str(text.get_rect()))
        color = color_light
        if boton == iconoBotones[i] or botonRelleno == iconoBotones[i]:
            color = color_dark

        if(iconoBotones[i] == "ConR"):
            pygame.draw.rect(miVentana, color, pygame.Rect(
                0, i*ANCHO_BOTON+ANCHO_BOTON+5, LARGO_BOTON/2-5, ANCHO_BOTON/2 - 5))

            mitadX = LARGO_BOTON/4 - text.get_rect()[2]/2

            mitadY = ANCHO_BOTON/4 - \
                text.get_rect()[3]/2 + i*(ANCHO_BOTON) - 2.5 + ANCHO_BOTON+5
            miVentana.blit(text, (mitadX, mitadY))

        elif(iconoBotones[i] == "SinR"):
            pygame.draw.rect(miVentana, color, pygame.Rect(
                LARGO_BOTON/2+5, (i-1)*ANCHO_BOTON+ANCHO_BOTON+5, LARGO_BOTON/2-5, ANCHO_BOTON/2 - 5))

            mitadX = LARGO_BOTON/4 - text.get_rect()[2]/2 + LARGO_BOTON/2

            mitadY = ANCHO_BOTON/4 - \
                text.get_rect()[3]/2 + (i-1)*(ANCHO_BOTON) - \
                2.5 + ANCHO_BOTON+5
            miVentana.blit(text, (mitadX, mitadY))
        else:
            pygame.draw.rect(miVentana, color, pygame.Rect(
                0, i*ANCHO_BOTON+ANCHO_BOTON+5, LARGO_BOTON, ANCHO_BOTON - 5))

            mitadX = LARGO_BOTON/2 - text.get_rect()[2]/2

            mitadY = ANCHO_BOTON/2 - \
                text.get_rect()[3]/2 + i*(ANCHO_BOTON) - 2.5 + ANCHO_BOTON+5
            miVentana.blit(text, (mitadX, mitadY))


def queBotonRellenoSePresiono(botonRelleno, pos):
    '''
    iconoBotones = ["ConR","SinR"]
    '''
    #               x0, x1             y0,y1
    botonConR = [[0, LARGO_BOTON/2-5], [7*ANCHO_BOTON +
                                        ANCHO_BOTON+5, 7*ANCHO_BOTON+ANCHO_BOTON+5 + ANCHO_BOTON/2]]
    botonSinR = [[LARGO_BOTON/2+5, LARGO_BOTON],
                 [7*ANCHO_BOTON+ANCHO_BOTON+5, 7*ANCHO_BOTON+ANCHO_BOTON+5 + ANCHO_BOTON/2]]

    if (pygame.mouse.get_pos()[0] <= LARGO_BOTON):
        if (botonConR[0][0] <= pos[0] <= botonConR[0][1] and botonConR[1][0] <= pos[1] <= botonConR[1][1]):
            botonRelleno = "ConR"
            print("presiono ConR")
        elif(botonSinR[0][0] <= pos[0] <= botonSinR[0][1] and botonSinR[1][0] <= pos[1] <= botonSinR[1][1]):
            print("presiono SinR")
            botonRelleno = "SinR"
    return botonRelleno


def queBotonSePresiono(boton, pos):
    '''
    largoBoton = 80
    anchoBoton = 50
    iconoBotones = ["Linea", "Cuadrado", "Circulo",
                    "Triangulo", "Lapiz", "Poligono","Limpiar"]
    '''
    #               x0, x1             y0,y1
    botonLinea = [[0, LARGO_BOTON], [0*ANCHO_BOTON +
                                     ANCHO_BOTON+5, 1*ANCHO_BOTON-5+ANCHO_BOTON+5]]
    botonCuadrado = [[0, LARGO_BOTON], [1*ANCHO_BOTON +
                                        ANCHO_BOTON+5, 2*ANCHO_BOTON-5+ANCHO_BOTON+5]]
    botonCirculo = [[0, LARGO_BOTON], [2*ANCHO_BOTON +
                                       ANCHO_BOTON+5, 3*ANCHO_BOTON-5+ANCHO_BOTON+5]]
    botonTriangulo = [[0, LARGO_BOTON], [3*ANCHO_BOTON +
                                         ANCHO_BOTON+5, 4*ANCHO_BOTON-5+ANCHO_BOTON+5]]
    botonLibre = [[0, LARGO_BOTON], [4*ANCHO_BOTON +
                                     ANCHO_BOTON+5, 5*ANCHO_BOTON-5+ANCHO_BOTON+5]]
    botonPoligono = [[0, LARGO_BOTON], [5*ANCHO_BOTON +
                                        ANCHO_BOTON+5, 6*ANCHO_BOTON-5+ANCHO_BOTON+5]]
    botonLimpiar = [[0, LARGO_BOTON], [6*ANCHO_BOTON +
                                       ANCHO_BOTON+5, 7*ANCHO_BOTON-5+ANCHO_BOTON+5]]

    if (pygame.mouse.get_pos()[0] <= LARGO_BOTON):
        if (botonLinea[0][0] <= pos[0] <= botonLinea[0][1] and botonLinea[1][0] <= pos[1] <= botonLinea[1][1]):
            boton = "Linea"
            print("presiono linea")
        elif(botonCuadrado[0][0] <= pos[0] <= botonCuadrado[0][1] and botonCuadrado[1][0] <= pos[1] <= botonCuadrado[1][1]):
            print("presiono cuadrado")
            boton = "Cuadrado"
        elif(botonCirculo[0][0] <= pos[0] <= botonCirculo[0][1] and botonCirculo[1][0] <= pos[1] <= botonCirculo[1][1]):
            print("presiono circulo")
            boton = "Circulo"
        elif(botonTriangulo[0][0] <= pos[0] <= botonTriangulo[0][1] and botonTriangulo[1][0] <= pos[1] <= botonTriangulo[1][1]):
            print("presiono triangulo")
            boton = "Triangulo"
        elif(botonLibre[0][0] <= pos[0] <= botonLibre[0][1] and botonLibre[1][0] <= pos[1] <= botonLibre[1][1]):
            print("presiono lapiz")
            boton = "Lapiz"
        elif(botonPoligono[0][0] <= pos[0] <= botonPoligono[0][1] and botonPoligono[1][0] <= pos[1] <= botonPoligono[1][1]):
            print("presiono poligono")
            boton = "Poligono"
        elif(botonLimpiar[0][0] <= pos[0] <= botonLimpiar[0][1] and botonLimpiar[1][0] <= pos[1] <= botonLimpiar[1][1]):
            print("presiono limpiar")
            boton = "Limpiar"
        else:
            return boton
    else:
        return boton
    return boton


def queBotonColorSePresiono(botonColor, pos):
    '''
    iconoBotones = ["Amarillo", "Azul", "Rojo",
                    "Negro", "Blanco", "Verde", "Morado"]
    '''
    #print("se ejecuta con ", pos, botonColor)
    #               x0, x1             y0,y1
    botonAmarillo = [[0*LARGO_BOTON + LARGO_BOTON+5, 1 *
                      LARGO_BOTON-5+LARGO_BOTON+5], [0, ANCHO_BOTON]]
    botonAzul = [[1*LARGO_BOTON + LARGO_BOTON+5, 2 *
                  LARGO_BOTON-5+LARGO_BOTON+5], [0, ANCHO_BOTON]]
    botonRojo = [[2*LARGO_BOTON + LARGO_BOTON+5, 3 *
                  LARGO_BOTON-5+LARGO_BOTON+5], [0, ANCHO_BOTON]]
    botonNegro = [[3*LARGO_BOTON + LARGO_BOTON+5, 4 *
                   LARGO_BOTON-5+LARGO_BOTON+5], [0, ANCHO_BOTON]]
    botonBlanco = [[4*LARGO_BOTON + LARGO_BOTON+5, 5 *
                    LARGO_BOTON-5+LARGO_BOTON+5], [0, ANCHO_BOTON]]
    botonVerde = [[5*LARGO_BOTON + LARGO_BOTON+5, 6 *
                   LARGO_BOTON-5+LARGO_BOTON+5], [0, ANCHO_BOTON]]
    botonMorado = [[6*LARGO_BOTON + LARGO_BOTON+5, 7 *
                    LARGO_BOTON-5+LARGO_BOTON+5], [0, ANCHO_BOTON]]

    if (pygame.mouse.get_pos()[1] <= ANCHO_BOTON):
        if (botonAmarillo[0][0] <= pos[0] <= botonAmarillo[0][1] and botonAmarillo[1][0] <= pos[1] <= botonAmarillo[1][1]):
            botonColor = "Amarillo"
            print("presiono Amarillo")
        elif(botonAzul[0][0] <= pos[0] <= botonAzul[0][1] and botonAzul[1][0] <= pos[1] <= botonAzul[1][1]):
            print("presiono Azul")
            botonColor = "Azul"
        elif(botonRojo[0][0] <= pos[0] <= botonRojo[0][1] and botonRojo[1][0] <= pos[1] <= botonRojo[1][1]):
            print("presiono Rojo")
            botonColor = "Rojo"
        elif(botonNegro[0][0] <= pos[0] <= botonNegro[0][1] and botonNegro[1][0] <= pos[1] <= botonNegro[1][1]):
            print("presiono Negro")
            botonColor = "Negro"
        elif(botonBlanco[0][0] <= pos[0] <= botonBlanco[0][1] and botonBlanco[1][0] <= pos[1] <= botonBlanco[1][1]):
            print("presiono Blanco")
            botonColor = "Blanco"
        elif(botonVerde[0][0] <= pos[0] <= botonVerde[0][1] and botonVerde[1][0] <= pos[1] <= botonVerde[1][1]):
            print("presiono Verde")
            botonColor = "Verde"
        elif(botonMorado[0][0] <= pos[0] <= botonMorado[0][1] and botonMorado[1][0] <= pos[1] <= botonMorado[1][1]):
            print("presiono Morado")
            botonColor = "Morado"
        else:
            return botonColor
    else:
        return botonColor
    return botonColor


def graficar(miVentana, boton, listaPuntosLinea, listaPuntosCuadrado,
             listaPuntosCirculo, listaPuntosTriangulo, listaPuntosLibre,
             colorElegido=(0, 255, 0), Relleno=0):
    if (boton == "ninguno"):
        pass
    elif(boton == "Linea"):
        puntosCapturados = len(listaPuntosLinea)
        if puntosCapturados >= 2:
            # pygame.draw.line(
            # miVentana, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), listaPuntosLinea[0], listaPuntosLinea[1], 5)
            pygame.draw.line(
                miVentana, colorElegido, listaPuntosLinea[0], listaPuntosLinea[1], 3)
            listaPuntosLinea.clear()
    elif(boton == "Cuadrado"):
        puntosCapturados = len(listaPuntosCuadrado)
        if puntosCapturados >= 2:
            ancho = abs(listaPuntosCuadrado[0][0] - listaPuntosCuadrado[1][0])
            alto = abs(listaPuntosCuadrado[0][1]-listaPuntosCuadrado[1][1])
            if (listaPuntosCuadrado[0][0] < listaPuntosCuadrado[1][0]):
                if(listaPuntosCuadrado[0][1] < listaPuntosCuadrado[1][1]):
                    pygame.draw.rect(
                        miVentana, colorElegido,  pygame.Rect(
                            listaPuntosCuadrado[0][0], listaPuntosCuadrado[0][1], ancho, alto), Relleno
                    )
                else:
                    pygame.draw.rect(
                        miVentana, colorElegido,  pygame.Rect(
                            listaPuntosCuadrado[0][0], listaPuntosCuadrado[1][1], ancho, alto), Relleno
                    )
            else:
                if(listaPuntosCuadrado[0][1] < listaPuntosCuadrado[1][1]):
                    pygame.draw.rect(
                        miVentana, colorElegido,  pygame.Rect(
                            listaPuntosCuadrado[1][0], listaPuntosCuadrado[0][1], ancho, alto), Relleno
                    )
                else:
                    pygame.draw.rect(
                        miVentana, colorElegido,  pygame.Rect(
                            listaPuntosCuadrado[1][0], listaPuntosCuadrado[1][1], ancho, alto), Relleno
                    )

            listaPuntosCuadrado.clear()
    elif(boton == "Circulo"):
        puntosCapturados = len(listaPuntosCirculo)
        if puntosCapturados >= 2:
            ancho = abs(listaPuntosCirculo[0][0] - listaPuntosCirculo[1][0])
            alto = abs(listaPuntosCirculo[0][1]-listaPuntosCirculo[1][1])
            if (listaPuntosCirculo[0][0] < listaPuntosCirculo[1][0]):
                if(listaPuntosCirculo[0][1] < listaPuntosCirculo[1][1]):
                    pygame.draw.ellipse(
                        miVentana, colorElegido,  pygame.Rect(
                            listaPuntosCirculo[0][0], listaPuntosCirculo[0][1], ancho, alto), Relleno
                    )
                else:
                    pygame.draw.ellipse(
                        miVentana, colorElegido,  pygame.Rect(
                            listaPuntosCirculo[0][0], listaPuntosCirculo[1][1], ancho, alto), Relleno
                    )
            else:
                if(listaPuntosCirculo[0][1] < listaPuntosCirculo[1][1]):
                    pygame.draw.ellipse(
                        miVentana, colorElegido,  pygame.Rect(
                            listaPuntosCirculo[1][0], listaPuntosCirculo[0][1], ancho, alto), Relleno
                    )
                else:
                    pygame.draw.ellipse(
                        miVentana, colorElegido,  pygame.Rect(
                            listaPuntosCirculo[1][0], listaPuntosCirculo[1][1], ancho, alto), Relleno
                    )
            listaPuntosCirculo.clear()
    elif(boton == "Triangulo"):
        puntosCapturados = len(listaPuntosTriangulo)
        if puntosCapturados >= 3:
                # pygame.draw.line(
                #    miVentana, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), listaPuntosLinea[0], listaPuntosLinea[1], 5)
            pygame.draw.polygon(
                miVentana, colorElegido, listaPuntosTriangulo, Relleno)
            listaPuntosTriangulo.clear()
    elif(boton == "Lapiz"):

        puntosCapturados = len(listaPuntosLibre)
        if puntosCapturados > 0:
            # pygame.draw.line(
            # miVentana, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), listaPuntosLinea[0], listaPuntosLinea[1], 5)
            pygame.draw.lines(
                miVentana, colorElegido, False, listaPuntosLibre)


def limpiarListas(*args):
    for i in args:
        i.clear()


if __name__ == "__main__":
    pygame.init()
    miVentana = pygame.display.set_mode((800, 600))
    miVentana.fill(COLORES["Blanco"])
    running = True

    listaPuntosLinea = []
    listaPuntosCuadrado = []
    listaPuntosTriangulo = []
    listaPuntosCirculo = []
    listaPuntosLibre = []
    boton = "ninguno"
    botonColor = "Negro"
    botonRelleno = "ConR"

    while (running):

        for eventos in pygame.event.get():
            if (eventos.type == pygame.QUIT):
                running = False
            if (eventos.type == pygame.MOUSEMOTION):  # si el mouse está en movimiento
                # print(pygame.mouse.get_pressed())
                if not (pygame.mouse.get_pressed()[0]) and boton == "Lapiz":
                    listaPuntosLibre = []

                # si se presiona el click izquierdo y estoy en lapiz
                if pygame.mouse.get_pressed()[0] and boton == "Lapiz":
                    # print("presion continua")
                    if (pygame.mouse.get_pos()[0] >= LARGO_BOTON and pygame.mouse.get_pos()[1] >= ANCHO_BOTON-5):

                        listaPuntosLibre.append(pygame.mouse.get_pos())
                        listaPuntosLibre.append(pygame.mouse.get_pos())

                    limpiarListas(listaPuntosLinea, listaPuntosCuadrado,
                                  listaPuntosTriangulo, listaPuntosCirculo)

            if (eventos.type == pygame.MOUSEBUTTONDOWN):

                boton = queBotonSePresiono(boton, pygame.mouse.get_pos())
                botonColor = queBotonColorSePresiono(
                    botonColor, pygame.mouse.get_pos())
                botonRelleno = queBotonRellenoSePresiono(
                    botonRelleno, pygame.mouse.get_pos())

                if(boton == "Linea"):

                    limpiarListas(listaPuntosCuadrado, listaPuntosTriangulo,
                                  listaPuntosCirculo, listaPuntosLibre)
                    if (pygame.mouse.get_pos()[0] >= LARGO_BOTON and pygame.mouse.get_pos()[1] >= ANCHO_BOTON-5):
                        listaPuntosLinea.append(pygame.mouse.get_pos())

                if(boton == "Cuadrado"):
                    limpiarListas(
                        listaPuntosLinea,
                        listaPuntosTriangulo,
                        listaPuntosCirculo,
                        listaPuntosLibre
                    )
                    if (pygame.mouse.get_pos()[0] >= LARGO_BOTON and pygame.mouse.get_pos()[1] >= ANCHO_BOTON-5):
                        listaPuntosCuadrado.append(pygame.mouse.get_pos())

                if(boton == "Circulo"):
                    limpiarListas(
                        listaPuntosCuadrado,
                        listaPuntosTriangulo,
                        listaPuntosLinea,
                        listaPuntosLibre
                    )
                    if (pygame.mouse.get_pos()[0] >= LARGO_BOTON and pygame.mouse.get_pos()[1] >= ANCHO_BOTON-5):
                        listaPuntosCirculo.append(pygame.mouse.get_pos())

                if(boton == "Triangulo"):
                    limpiarListas(
                        listaPuntosCuadrado,
                        listaPuntosLinea,
                        listaPuntosCirculo,
                        listaPuntosLibre
                    )
                    if (pygame.mouse.get_pos()[0] >= LARGO_BOTON and pygame.mouse.get_pos()[1] >= ANCHO_BOTON-5):
                        listaPuntosTriangulo.append(pygame.mouse.get_pos())

                if(boton == "Limpiar"):
                    limpiarListas(
                        listaPuntosLinea,
                        listaPuntosCuadrado,
                        listaPuntosTriangulo,
                        listaPuntosCirculo,
                        listaPuntosLibre
                    )
                    miVentana.fill(COLORES["Blanco"])

        mouse = pygame.mouse.get_pos()
        dibujarBotonesControl(miVentana, mouse, boton, botonRelleno)
        dibujarBotonesColor(miVentana, mouse, botonColor)
        graficar(miVentana, boton, listaPuntosLinea, listaPuntosCuadrado,
                 listaPuntosCirculo, listaPuntosTriangulo, listaPuntosLibre, COLORES[botonColor], RELLENO[botonRelleno])

        pygame.display.update()

    exit()
