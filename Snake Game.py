import pygame
from random import randrange

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

largura = 500  # Largura da tela
altura = 540  # Altura da tela
tamanho = 10  # Define 10 pixels para o tamanho da cobra

placar = [40, 40]
pos_placar = [0, altura - placar[1], largura, placar[0]]

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))  # Criar janela do jogo
pygame.display.set_caption("Jogo da Cobrinha")  # Definir  titulo da janela do jogo


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    text1 = font.render(msg, True, cor)
    fundo.blit(text1, [x, y])


def cobra(CobraXY):
    # Cria um quadrado preto na posição x e y com 10 pixels de altura e 10 de largura
    for XY in CobraXY:
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho])


def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])


def jogo():
    sair = True
    fimdejogo = False
    pos_x = randrange(0, largura - tamanho, tamanho)  # Define a posição inicial aleatoria do quadrado no eixo x
    pos_y = randrange(0, altura - tamanho - placar[1], tamanho)  # Define a posição inicial aleatoria do quadrado no eixo y
    velocidade_x = 0  # Define a velocidade inicial do quadrado no eixo x
    velocidade_y = 0  # Define a velocidade inicial do quadrado no eixo y

    maca_x = randrange(0, largura - tamanho, tamanho)
    maca_y = randrange(0, largura - tamanho - placar[1], tamanho)

    CobraXY = []
    CobraComp = 1
    pontos = 0

    while sair:
        while fimdejogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = not fimdejogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        fimdejogo = not fimdejogo
                        sair = False
                    elif event.key == pygame.K_c:
                        sair = True
                        fimdejogo = False
                        pos_x = randrange(0, largura - tamanho,
                                          tamanho)  # Define a posição inicial aleatoria do quadrado no eixo x
                        pos_y = randrange(0, altura - tamanho,
                                          tamanho)  # Define a posição inicial aleatoria do quadrado no eixo y
                        velocidade_x = 0  # Define a velocidade inicial do quadrado no eixo x
                        velocidade_y = 0  # Define a velocidade inicial do quadrado no eixo y

                        maca_x = randrange(0, largura - tamanho, tamanho)
                        maca_y = randrange(0, largura - tamanho - placar[1], tamanho)

                        CobraXY = []
                        CobraComp = 1
                        pontos = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if 120 + 100 > x > 100 and 300 + 27 > y > 300:
                        sair = True
                        fimdejogo = False
                        pos_x = randrange(0, largura - tamanho,
                                          tamanho)  # Define a posição inicial aleatoria do quadrado no eixo x
                        pos_y = randrange(0, altura - tamanho,
                                          tamanho)  # Define a posição inicial aleatoria do quadrado no eixo y
                        velocidade_x = 0  # Define a velocidade inicial do quadrado no eixo x
                        velocidade_y = 0  # Define a velocidade inicial do quadrado no eixo y

                        maca_x = randrange(0, largura - tamanho, tamanho)
                        maca_y = randrange(0, largura - tamanho - placar[1], tamanho)

                        CobraXY = []
                        CobraComp = 1
                        pontos = 0
                    elif 300 + 100 > x > 300 and 300 + 27 > y > 300:
                        fimdejogo = not fimdejogo
                        sair = False
            fundo.fill(branco)
            texto("FIM DE JOGO!", vermelho, 50, largura / 3.8, 100)
            texto("Pontuação Final: " + str(pontos), preto, 25, 180, 150)
            pygame.draw.rect(fundo, preto, [120, 300, 100, 27])
            texto("Continuar(C)", branco, 22, 122, 305)
            pygame.draw.rect(fundo, preto, [300, 300, 100, 27])
            texto("Sair(S)", branco, 22, 325, 305)
            texto("Para continuar tecle C ou S para sair", preto, 22, largura / 4, altura / 2.3 + 20)
            pygame.display.update()
        for event in pygame.event.get():
            # Habilita o "X" para fechar o jogos
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
                elif event.key == pygame.K_r:
                    jogo()

        if sair:

            fundo.fill(branco)  # Atualiza a cor de fundo para branco

            pos_x += velocidade_x
            pos_y += velocidade_y

            if pos_x == maca_x and pos_y == maca_y:
                maca_x = randrange(0, largura - tamanho, tamanho)
                maca_y = randrange(0, largura - tamanho, tamanho)
                CobraComp += 1
                pontos += 1

            # Faz com que o jogo feche caso o quadrado saia da tela

            if pos_x + tamanho > largura:
                fimdejogo = not fimdejogo
            elif pos_x + tamanho < 0:
                fimdejogo = not fimdejogo
            elif pos_y + tamanho > altura - placar[1]:
                fimdejogo = not fimdejogo
            elif pos_y + tamanho < 0:
                fimdejogo = not fimdejogo

            CobraInicio = [pos_x, pos_y]
            CobraXY.append(CobraInicio)

            if len(CobraXY) > CobraComp:
                del CobraXY[0]

            if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
                fimdejogo = not fimdejogo

            pygame.draw.rect(fundo, preto, pos_placar)
            texto("Pontuação: " + str(pontos), branco, 20, 10, altura - (placar[1] - 10))

            cobra(CobraXY)
            maca(maca_x, maca_y)
            pygame.display.update()
            relogio.tick(15)


jogo()
pygame.quit()
