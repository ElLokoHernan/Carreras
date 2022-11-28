import pygame
import sys
import random
#primeros pasos con git 
#constantes  
ANCHO = 400
ALTO = 600
color_rojo = (255,0,0)
color_negro = (0,0,0)
color_azul = (0,0,255)

#JUGADOR
car = pygame.image.load('car/R.png')
car = pygame.transform.scale(car,(100,100))
jugador_size = 50
jugador_pos = [ANCHO/2,ALTO - jugador_size * 2]
jugador_pos1 = [ANCHO/2,ALTO - jugador_size * 2]
vida = 100

#enemigo
ene = pygame.image.load('car/E.png')
ene = pygame.transform.scale(ene,(100,100))
enemigo_size = 50
enemigo_pos = [random.randint(0, ANCHO -enemigo_size),0]

#ventana 
wn = pygame.display.set_mode((ANCHO,ALTO))
game_over = False
clock = pygame.time.Clock()
fondo = pygame.image.load('street/fondo.jpg')
fondo = pygame.transform.scale(fondo,(ANCHO,ALTO))
pygame.mixer.init()
pygame.mixer.music.load('music/WhatsApp Audio 2022-11-13 at 21.53.11.mpeg')
pygame.mixer.music.play()
score = 0

def detectar_colision(jugador_pos,enemigo_pos):
    jx = jugador_pos[0]
    jy = jugador_pos [1]
    ex = enemigo_pos[0]
    ey = enemigo_pos[1]

    if(ex >= jx and ex <(jx + jugador_size)) or(jx >= ex and jx < (ex + enemigo_size)):
        if  (ey >= jy and ey <(jy + jugador_size)) or(jy >= ex and jy < (ey + enemigo_size)):
            return True
    return False

def texto(surface,text,size,x,y):
    pygame.font.init()
    font = pygame.font.SysFont("serif",50)
    text_surface = font.render(text,True, color_negro)
    text_rect = text_surface.get_rect()
    text_rect.midtop =(x,y)
    surface.blit(text_surface, text_rect)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
         
        if event.type == pygame.KEYDOWN:
            y = jugador_pos[1]
            x = jugador_pos[0]
            if event.key == pygame.K_UP:
                y -= jugador_size
                jugador_pos[1] = y
            if event.key == pygame.K_DOWN:
               y += jugador_size
               jugador_pos[1] = y
            if event.key == pygame.K_RIGHT:
               x += jugador_size
               jugador_pos[0] = x
            if event.key == pygame.K_LEFT:
               x -= jugador_size
               jugador_pos[0] = x
            
            if jugador_pos[0] > 330:
                jugador_pos[0] = 330
            if jugador_pos[0] < 0:
                jugador_pos[0] = 0
            if jugador_pos[1] > 500:
                jugador_pos[1] = 500
            if jugador_pos[1] < 10:
                jugador_pos[1] = 10
            
            




                
    
    wn.fill(color_negro)
    wn.blit(fondo, (0,0))
    if enemigo_pos[1] >= 0 and enemigo_pos[1]<ALTO:
        enemigo_pos[1] += 20
        
    else:
        enemigo_pos[0] = random.randint(0,ANCHO - enemigo_size)
        enemigo_pos[1] = 0
        score += 10
    if detectar_colision(jugador_pos,enemigo_pos):
        vida -= 1
        wn.blit(ene,(enemigo_pos[0],enemigo_pos[1],enemigo_size,enemigo_size))
        pygame.display.update()
        print("jajajajajajaj",score,"vidas restantes",vida)
   
    if vida < 0:
         texto(wn,str(vida),40,ANCHO // 100,100)  
         pygame.display.update()
         game_over = True   
         pygame.display.update()
    #if seft.rect.left < 0:
     #   self.rect = 0
    #if seflt.rect.right > ANCHO:
     #   self.rect.right = ANCHO
    #enemigo
    wn.blit(ene,(enemigo_pos[0],enemigo_pos[1],enemigo_size,enemigo_size))
   # pygame.draw.rect(wn,color_azul,(enemigo_pos[0],
    #                                enemigo_pos[1],
     #                               enemigo_size,
      #                              enemigo_size))
    #jugador
    wn.blit(car, (jugador_pos[0],jugador_pos[1],jugador_size,jugador_size))
    #pygame.draw.rect(wn,color_rojo,(jugador_pos[0],
     #                               jugador_pos[1],
      #                              jugador_size,
       #                             jugador_size))
    #marcador
    #limites(0,400,500)
    texto(wn,str("vida"),50, 40 ,5 ) 
    texto(wn,str(vida),50, 40 ,40 )  
    texto(wn,str("puntos"),50, 160 ,5 )   
    texto(wn,str(score),50,160, 40)    
    clock.tick(30)
    pygame.display.update()
#steitmens
