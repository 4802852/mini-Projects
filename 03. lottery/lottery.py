import pygame
import random

# 화면 크기
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 100

# 초기화
pygame.init()
pygame.font.init()

# 색깔 정의
WHITE = 255, 255, 255
BLACK = 0, 0, 0
L_GREEN = 153, 254, 101

# 폰트 정의
myfont = pygame.font.Font(None, 50)

# 스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 글자 위치 정의
positions = []
y_position = 33
initial_x_position = 40
delta = 80
x_position = initial_x_position
for i in range(7):
    positions.append((x_position, y_position))
    x_position += delta

# 공 위치
circle_positions = []
y_position = SCREEN_HEIGHT / 2
initial_x_position = 60
delta = 80
x_position = initial_x_position
for i in range(len(positions)):
    circle_positions.append((x_position, y_position))
    x_position += delta


def draw_background(screen):
    """돌림판의 배경을 그린다"""
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)
    for i in range(len(positions)):
        pygame.draw.circle(screen, L_GREEN, circle_positions[i], 30)


def generate_number():
    """random 숫자 7개를 generate 한다"""
    number_array = []
    while len(number_array) <= len(positions):
        new_num = random.randint(1, 45)
        if new_num in number_array:
            pass
        else:
            number_array.append(new_num)

    number_array.sort()
    return number_array


def process_turn(screen, number_array):
    """생성된 숫자 7개를 화면에 표시"""
    for i in range(len(positions)):
        number = myfont.render(str(number_array[i]), False, BLACK)
        if number_array[i] < 10:
            x, y = positions[i]
            x += 10
            screen.blit(number, (x, y))
        else:
            screen.blit(number, positions[i])


draw_background(screen)
process_turn(screen, generate_number())
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_SPACE:
                draw_background(screen)
                process_turn(screen, generate_number())
    pygame.display.update()
