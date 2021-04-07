import pygame  # 파이게임 모듈 임포트하기
import time

SCREEN_WIDTH = 400  # 게임 화면 너비
SCREEN_HEIGHT = 400  # 게임 화면 높이
BLOCK_SIZE = 20  # 뱀 게임 한 블록 크기


def draw_background(screen):
    """게임의 배경을 그린다"""
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)


def draw_block(screen, color, position):
    """position 위치에 color 색깔의 블록을 그린다"""
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


pygame.init()  # 파이 게임 사용 전 초기화

# 색깔 정의
RED = 255, 0, 0        # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0      # 녹색:   적   0, 녹 255, 청   0
WHITE = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255

# 지정한 크기의 게임 화면 창을 오픈
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

block_position = [0, 0]  # 블록 위치 (y, x)

# 종료 이벤트가 발생할 때까지 게임을 계속 진행한다
while True:
    events = pygame.event.get()             # 발생한 이벤트 목록을 읽어드린다
    for event in events:                    # 이벤트 목록을 순회하며 각 이벤트를 처리한다
        if event.type == pygame.QUIT:       # 종료 이벤트가 발생한 경우
            exit()                          # 게임을 종료한다
        if event.type == pygame.KEYDOWN:    # 이벤트 종류가 키 입력 이벤트이면 이동 방향 position 정의
            if event.key == pygame.K_UP:
                block_position[0] -= 1
            elif event.key == pygame.K_DOWN:
                block_position[0] += 1
            elif event.key == pygame.K_LEFT:
                block_position[1] -= 1
            elif event.key == pygame.K_RIGHT:
                block_position[1] += 1

    # 화면을 계속 새로 그린다
    draw_background(screen)
    draw_block(screen, GREEN, block_position)
    pygame.display.update()