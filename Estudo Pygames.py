import pygame
from random import randint

# Inicializando o Pygames

try:
    pygame.init()

except:
    print("O Pygame não foi inicializado com sucesso")

# Variaveis Globais

branco = (255, 255, 255)  # Cor RGB Branca
preto = (0, 0, 0)  # Cor RGB Preta
verde = (0, 255, 0)  # Cor RGB Verde
azul = (0, 0, 255)  # Cor RGB Azul
vermelho = (255, 0, 0)  # Cor RGB Vermelha

largura = 700  # Largura da tela
altura = 700  # Altura da tela
tamanho = 10  # Define 10 pixels para o tamanho da cobra

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))  # Criar janela do jogo
pygame.display.set_caption("Jogo da Cobrinha")  # Definir  titulo da janela do jogo


def cobra(CobraXY):
    # Cria um quadrado preto na posição x e y com 10 pixels de altura e 10 de largura
    for XY in CobraXY:
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho])


def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])


def jogo():
    sair = True
    pos_x = randint(0,
                    (largura - tamanho) / tamanho) * tamanho  # Define a posição inicial aleatoria do quadrado no eixo x
    pos_y = randint(0,
                    (altura - tamanho) / tamanho) * tamanho  # Define a posição inicial aleatoria do quadrado no eixo y
    velocidade_x = 0  # Define a velocidade inicial do quadrado no eixo x
    velocidade_y = 0  # Define a velocidade inicial do quadrado no eixo y

    maca_x = randint(0, (largura - tamanho) / tamanho) * tamanho
    maca_y = randint(0, (altura - tamanho) / tamanho) * tamanho

    CobraXY = []
    CobraComp = 1

    while sair:
        for event in pygame.event.get():
            # Habilita o "X" para fechar o jogo
            if event.type == pygame.QUIT:
                sair = False

            # Realiza todos os movimentos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                elif event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                elif event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                elif event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho

        fundo.fill(branco)  # Atualiza a cor de fundo para branco

        pos_x += velocidade_x
        pos_y += velocidade_y

        CobraInicio = [pos_x, pos_y]
        CobraXY.append(CobraInicio)

        if len(CobraXY) > CobraComp:
            del CobraXY[0]

        if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
            pass

        cobra(CobraXY)

        if pos_x == maca_x and pos_y == maca_y:
            maca_x = randint(0, (largura - tamanho) / tamanho) * tamanho
            maca_y = randint(0, (largura - tamanho) / tamanho) * tamanho
            CobraComp += 1

        maca(maca_x, maca_y)

        # Faz com que o jogo feche caso o quadrado saia da tela
        pygame.display.update()
        relogio.tick(15)
        if pos_x > largura:
            sair = False
        elif pos_x < 0:
            sair = False
        elif pos_y > altura:
            sair = False
        elif pos_y < 0:
            sair = False


jogo()
pygame.quit()
