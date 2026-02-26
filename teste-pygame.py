import pygame
import sys
import random

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Teste Pygame")

AZUL = (0, 0, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)

tamanho_fonte = 50
fonte = pygame.font.SysFont("Arial", tamanho_fonte)
texto = fonte.render("Joao", True, BRANCO)
texto_rect = texto.get_rect(center=(largura // 2, altura // 2))

texto2 = fonte.render("Vitor", True, BRANCO)
texto2_rect = texto2.get_rect(center=(largura // 3, altura // 3))

velocidade2_x = random.choice([-1, 1])
velocidade2_y = random.choice([-1, 1])

clock = pygame.time.Clock()

#velocidade_x = 1
#velocidade_y = 1
velocidade_x = random.choice([-1, 1])
velocidade_y = random.choice([-1, 1])




rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((PRETO))
    tela.blit(texto, texto_rect)
    tela.blit(texto2, texto2_rect)
    texto_rect.x += velocidade_x
    texto_rect.y += velocidade_y 
    texto2_rect.x += velocidade2_x
    texto2_rect.y += velocidade2_y

    #clock.tick(30)
    if texto_rect.right >= largura or texto_rect.left <= 0:
        velocidade_x *= -1
        velocidade_y *= random.choice([-1, 1]) 
        texto = fonte.render("Joao", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))    
    if texto_rect.bottom >= altura or texto_rect.top <= 0:
        velocidade_y *= -1
        velocidade_x *= random.choice([-1, 1])
        texto = fonte.render("Joao", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    if texto2_rect.right >= largura or texto2_rect.left <= 0:
       velocidade2_x *= -1
       velocidade_y *= random.choice([-1, 1])
       texto2 = fonte.render("Vitor", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    if texto2_rect.bottom >= altura or texto2_rect.top <= 0:
        velocidade2_y *= -1
        velocidade2_x *= random.choice([-1, 1])
        texto2 = fonte.render("Vitor", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    if texto_rect.colliderect(texto2_rect):
        velocidade_x *= -1
        velocidade_y *= -1
        velocidade2_x *= -1
        velocidade2_y *= -1

    pygame.display.flip()
    

pygame.quit()
sys.exit()
    
