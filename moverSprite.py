import pygame

def main():
    pygame.init() #carga los modulos de pygame
    screen = pygame.display.set_mode([640,480])
    imagen = pygame.image.load("balon.png")
    x,y = 0,0 #coordenadas de la imagen
    vx, vy = 0,0 #velocidad en x - y
    arriba, abajo, izq, der = False, False, False, False
    exit = False
    reloj = pygame.time.Clock()
    azul = (0,0,255)


    while exit!= True:  #ciclo principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    arriba = True
                    vy=-10
                if event.key == pygame.K_DOWN:
                    abajo = True
                    vy=10
                if event.key == pygame.K_RIGHT:
                    der = True
                    vx=10
                if event.key == pygame.K_LEFT:
                    izq = True
                    vx=-10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    arriba = False
                    vy=0
                if event.key == pygame.K_DOWN:
                    abajo = False
                    vy=0
                if event.key == pygame.K_RIGHT:
                    der = False
                    vx=0
                if event.key == pygame.K_LEFT:
                    izq = False
                    vx=0               
        x+=vx
        y+=vy            
        screen.fill(azul)
        screen.blit(imagen,(x,y))        
        pygame.display.update() 
        reloj.tick(20)       
    pygame.quit()
   
main()  