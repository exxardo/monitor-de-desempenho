import pygame
import psutil
import cpuinfo

# Definindo cores
azul = (106, 90, 205)
vermelho = (255, 99, 71)
branco = (255, 255, 255)
preto = (0, 0, 0)

pygame.font.init()
font = pygame.font.Font(None, 32)

# Mostrar uso da memória:
def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2 * 20
    tela.blit(s1, (0, 0)) # Superficies
    pygame.draw.rect(s1, azul, (20, 50, largura_tela-2 * 20, 70)) # Superficies
    larg = larg * mem.percent / 100
    pygame.draw.rect(s1, vermelho, (20, 50, larg, 70)) # Superficies
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    usado = round(mem.used / (1024 * 1024 * 1024), 2)
    disponivel = round(mem.available / (1024 * 1024 * 1024), 2)
    texto_barra = f'Memória Total: {total} GB | Consumido: {usado} GB | Disponível: {disponivel} GB'
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10))

pygame.font.init()
font = pygame.font.Font(None, 32)

# Mostrar uso de CPU:
def mostra_uso_cpu():
    capacidade = psutil.cpu_percent(interval=0)
    info = cpuinfo.get_cpu_info()
    nome = info['brand_raw']
    larg = largura_tela - 2 * 20
    tela.blit(s2, (0, altura_tela/3)) # Superficies
    pygame.draw.rect(s2, azul, (20, 50, largura_tela-2 * 20, 70)) # Superficies
    larg = larg * capacidade / 100
    pygame.draw.rect(s2, vermelho, (20, 50, larg, 70)) # Superficies
    text = font.render(f'Utilização de CPU: {capacidade}% | {nome}', 1, branco)
    tela.blit(text, (20, 210))

pygame.font.init()
font = pygame.font.Font(None, 32)

# Mostrar o uso de disco local
def mostra_uso_disco():
    disco = psutil.disk_usage('.')
    larg = largura_tela - 2 * 20
    tela.blit(s3, (0, 2 * altura_tela/3)) # Superficies
    pygame.draw.rect(s3, azul, (20, 50, largura_tela-2*20, 70)) # Superficies
    larg = larg * disco.percent / 100
    pygame.draw.rect(s3, vermelho, (20, 50, larg, 70)) # Superficies
    total = round(disco.total / (1024 * 1024 * 1024), 2)
    usado = round(disco.used / (1024 * 1024 * 1024), 2)
    disponivel = round(disco.free / (1024 * 1024 * 1024), 2)
    texto_barra = f'Amazenamento Total: {total} GB | Consumido: {usado} GB | Disponível: {disponivel} GB'
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 410))

# Cria relógio
clock = pygame.time.Clock()
cont = 60

# Iniciando a janela principal
largura_tela = 900 # Pixels
altura_tela = 600 # Pixels
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Uso de recursos do computador')
pygame.display.init()

# Varíaveis organização das informações em superficie
s1 = pygame.surface.Surface((largura_tela, altura_tela / 3))
s2 = pygame.surface.Surface((largura_tela, altura_tela / 3))
s3 = pygame.surface.Surface((largura_tela, altura_tela / 3))

terminou = False
while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    if cont == 60:
        mostra_uso_memoria()
        mostra_uso_cpu()
        mostra_uso_disco()
        cont = 0
        
    # Atualiza o desenho na tela
    pygame.display.update()
    # 60 frames por segundo
    clock.tick(60)
    cont += 1

# Finaliza a janela
pygame.display.quit()
