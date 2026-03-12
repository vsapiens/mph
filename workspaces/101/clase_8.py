import pygame

ancho = 500
altura = 500


def main():
    x = 250
    y = 250
    velocidad = 10
    pygame.init()
    pygame.display.set_caption("Demo de Pygame")
    pantalla = pygame.display.set_mode((ancho, altura))

    ejecutando = True
    while ejecutando:
        # Delay de renderizado
        pygame.time.delay(50)
        # Consumo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                print("Fin del juego")
                ejecutando = False
        # Eventos de teclas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            y -= velocidad
        elif teclas[pygame.K_DOWN]:
            y += velocidad
        elif teclas[pygame.K_LEFT]:
            x -= velocidad
        elif teclas[pygame.K_RIGHT]:
            x += velocidad      
        # Renderizado de elementos
        pantalla.fill((0, 0, 0))
        pygame.draw.circle(pantalla,  (255,0,0), (x,y), 200)
        #pygame.draw.rect(pantalla, (0, 255, 0), (x-100, y-100, 200, 200))
        # Actualización de pantalla
        pygame.display.update()
main()