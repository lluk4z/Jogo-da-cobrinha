import pygame
from random import randint

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

pygame.init()

largura = 320
altura = 280
tamanho = 10
placar = 40

relogio = pygame.time.Clock()

#criar a tela do jogo
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    #Desenha um texto numa nova superfície
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])

def cobra(CobraXY):
    for XY in CobraXY:
        #desenha o retângulo(cobra). .rect(surface, cor, Rect, width)
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho])

def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])

#criar a função onde meu jogo todo estará
def jogo():
    #Criação de um loop infinito para dar a sensação de movimento
    #e de que as coisas estão acontecendo no jogo
    sair = True
    fimdejogo = False
    pos_x = randint(0, (largura-tamanho)/10)*10
    pos_y = randint(0, (altura-tamanho-placar)/10)*10
    maca_x = randint(0, (largura-tamanho)/10)*10
    maca_y = randint(0, (altura-tamanho-placar)/10)*10
    velocidade_x=0
    velocidade_y=0
    cobraXY = []
    cobraComp = 1
    pontos = 0
    while sair:
        while fimdejogo:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        #jogo() #recursivamente
                        sair = True
                        fimdejogo = False
                        pos_x = randint(0, (largura-tamanho)/10)*10
                        pos_y = randint(0, (altura-tamanho-placar)/10)*10
                        maca_x = randint(0, (largura-tamanho)/10)*10
                        maca_y = randint(0, (altura-tamanho-placar)/10)*10
                        velocidade_x=0
                        velocidade_y=0
                        cobraXY = []
                        cobraComp = 1
                        pontos = 0
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    
                    if x > 45 and y > 120 and x < 180 and y < 147:
                        sair = True
                        fimdejogo = False
                        pos_x = randint(0, (largura-tamanho)/10)*10
                        pos_y = randint(0, (altura-tamanho-placar)/10)*10
                        maca_x = randint(0, (largura-tamanho)/10)*10
                        maca_y = randint(0, (altura-tamanho-placar)/10)*10
                        velocidade_x=0
                        velocidade_y=0
                        cobraXY = []
                        cobraComp = 1
                        pontos = 0
                    elif x > 190 and y > 120 and x < 275 and y < 147:
                        sair = False
                        fimdejogo = False

            fundo.fill(branco)
            texto("Fim de jogo", vermelho, 50, 65, 30)
            texto("Pontuação Final: "+str(pontos), preto, 30, 70, 80)
            #Botão
            pygame.draw.rect(fundo, preto, [45, 120, 135, 27])
            texto("Continuar(C)", branco, 30, 50, 125)
            pygame.draw.rect(fundo, preto, [190, 120, 75, 27])
            texto("Sair(S)", branco, 30, 195, 125)
            #atualiza a tela e mostra isso daí
            pygame.display.update()
                        
        #vou varrer todos os eventos que estao acontecendo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho

        

                    
        #o fill preenche a superficie com uma cor escolhida
        fundo.fill(branco)

        pos_x+=velocidade_x
        pos_y+=velocidade_y

        #comer a maçã
        if pos_x == maca_x and pos_y == maca_y:
            maca_x = randint(0, (largura-tamanho)/10)*10
            maca_y = randint(0, (altura-tamanho-placar)/10)*10
            cobraComp += 1
            pontos += 1

        #para quando chegar num extremo sair pelo outro
#        if pos_x + tamanho > largura:
#            pos_x = 0
#        if pos_x < 0:
#            pos_x = largura-tamanho
#        if pos_y + tamanho > altura - placar:
#            pos_y = 0
#        if pos_y < 0:
#            pos_y = altura-tamanho - placar

        #Quando bater na borda perder
        if pos_x + tamanho> largura:
            fimdejogo = True
        if pos_x < 0:
            fimdejogo = True
        if pos_y + tamanho > altura - placar:
            fimdejogo = True
        if pos_y < 0:
            fimdejogo = True


        
        cobraInicio = []
        cobraInicio.append(pos_x)
        cobraInicio.append(pos_y)
        cobraXY.append(cobraInicio)
        if len(cobraXY) > cobraComp:
            del cobraXY[0]

        #colisão da cobra
        if any(Bloco == cobraInicio for Bloco in cobraXY[:-1]):
            fimdejogo = True

        pygame.draw.rect(fundo, preto, [0, altura-placar, largura, placar])
        texto("Pontuação: "+str(pontos), branco, 20, 10, altura-30)
        
        #chamar função que desenha a cobra
        cobra(cobraXY) #referencia as variáveis pos_x e pos_y criadas na função

        

        #chamar a função que desenha a maçã
        maca(maca_x, maca_y)
     
        #atualiza porções da tela para que o software mostre
        pygame.display.update()

        #Nunca vai ultrapassar a velocidade do valor de dentro dos parênteses
        relogio.tick(15)



#chamar a função jogo
jogo()

#para que eu possa fechar o jogo
pygame.quit()
