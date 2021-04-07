import pygame  # 파이게임 모듈 임포트하기
import time

SCREEN_WIDTH = 400  # 게임 화면 너비
SCREEN_HEIGHT = 80  # 게임 화면 높이

pygame.init()  # 파이 게임 사용 전 초기화

# 지정한 크기의 게임 화면 창을 오픈
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

time.sleep(3)  # 3초동안 기다려준다

# 색깔 정의
RED = 255, 0, 0        # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0      # 녹색:   적   0, 녹 255, 청   0
WHITE = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255

# 화면 전체에 하얀 사각형 그리기
rect = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.draw.rect(screen, WHITE, rect)

# 화면 왼쪽 위에 녹색 정사각형 그리기
rect = pygame.Rect((0, 0), (40, 40))
pygame.draw.rect(screen, GREEN, rect)

# 화면 오른쪽 아래에 적색 직사각형 그리기
rect = pygame.Rect((340, 60), (60, 20))
pygame.draw.rect(screen, RED, rect)

pygame.display.update()  # 화면 새로 고침

time.sleep(3)
