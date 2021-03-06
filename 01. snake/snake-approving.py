import pygame  # 파이게임 모듈 임포트하기
from datetime import datetime
from datetime import timedelta
import random


SCREEN_WIDTH = 400  # 게임 화면 너비
SCREEN_HEIGHT = 400  # 게임 화면 높이
BLOCK_SIZE = 20  # 뱀 게임 한 블록 크기

pygame.init()  # 파이 게임 사용 전 초기화

# 색깔 정의
RED = 255, 0, 0        # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0      # 녹색:   적   0, 녹 255, 청   0
WHITE = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255

# 지정한 크기의 게임 화면 창을 오픈
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_background(screen):
    """게임의 배경을 그린다"""
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)


def draw_block(screen, color, position):
    """position 위치에 color 색깔의 블록을 그린다"""
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


class Snake:
    """뱀 클래스"""
    color = GREEN  # 뱀의 색

    def __init__(self):
        self.positions = [(9, 6), (9, 7), (9, 8), (9, 9)]  # 뱀의 위치
        self.direction = 'north'  # 뱀의 방향

    def draw(self, screen):
        """뱀을 화면에 그린다"""
        for position in self.positions:  # 뱀의 몸 블록들을 순회하며
            draw_block(screen, self.color, position)  # 각 블록을 그린다

    def crawl(self):
        """뱀이 현재 방향으로 한 칸 기어간다"""
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'north':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'south':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'west':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'east':
            self.positions = [(y, x + 1)] + self.positions[:-1]

    def turn(self, direction):
        """뱀의 방향을 바꾼다"""
        if self.direction == 'north':
            if direction != 'south':
                self.direction = direction
        if self.direction == 'south':
            if direction != 'north':
                self.direction = direction
        if self.direction == 'west':
            if direction != 'east':
                self.direction = direction
        if self.direction == 'east':
            if direction != 'west':
                self.direction = direction

    def grow(self):
        """뱀이 한 칸 자라나게 한다"""
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'north':
            self.positions = [(y - 1, x)] + self.positions
        elif self.direction == 'south':
            self.positions = [(y + 1, x)] + self.positions
        elif self.direction == 'west':
            self.positions = [(y, x - 1)] + self.positions
        elif self.direction == 'east':
            self.positions = [(y, x + 1)] + self.positions


class Apple:
    """사과 클래스"""
    color = RED  # 사과의 색

    def __init__(self):
        self.position = [(5, 5), (13, 8), (18, 17)]  # 사과의 위치

    def draw(self, screen):
        """사과를 화면에 그린다"""
        for position in self.position:
            draw_block(screen, self.color, position)


class GameBoard:
    """게임판 클래스"""
    width = 20  # 게임판의 너비
    height = 20  # 게임판의 높이

    def __init__(self):
        self.snake = Snake()  # 게임판 위의 뱀
        self.apple = Apple()  # 게임판 위의 사과

    def draw(self, screen):
        """화면에 게임판의 구성 요소를 그린다"""
        self.apple.draw(screen)  # 게임판 위에 사과를 그린다
        self.snake.draw(screen)  # 게임판 위에 뱀을 그린다

    def process_turn(self):
        """게임을 한 차례 진행한다"""
        # 뱀의 머리와 사과가 닿았으면
        if self.snake.positions[0] in self.apple.position:
            self.put_new_apple()  # 사과를 새로 놓는다
            self.snake.grow()  # 뱀을 한 칸 자라게 한다
        else:
            self.snake.crawl()  # 뱀이 한 칸 기어간다

            # 뱀의 머리가 뱀의 몸과 부딛혔으면
            if self.snake.positions[0] in self.snake.positions[1:]:
                raise SnakeCollisionException()  # 뱀 충돌 예외를 일으킨다

            # 뱀의 머리가 게임판 밖으로 나가면
            y, x = self.snake.positions[0]
            if y > 19 or y < 0 or x > 19 or x < 0:
                raise SnakeCollisionException()

        if len(self.snake.positions) > 30:
            raise UpgradeHardness3()
        elif len(self.snake.positions) > 20:
            raise UpgradeHardness2()
        elif len(self.snake.positions) > 10:
            raise UpgradeHardness1()

    def put_new_apple(self):
        """게임판에 새 사과를 놓는다"""
        if (len(self.apple.position) + len(self.snake.positions)) >= (game_board.width * game_board.height):
            raise SnakeCollisionException()
        self.apple.position.remove(self.snake.positions[0])
        self.apple.position.append((random.randint(0, 19), random.randint(0, 19)))
        for position in self.snake.positions:       # 뱀 블록을 확인하여
            if self.apple.position[0] == position:  # 사과가 뱀 위치에 놓인 경우
                self.put_new_apple()                # 사과를 새로 놓는다
                break
        for position in self.apple.position:
            if self.apple.position[0] == position[1:]:
                self.put_new_apple()
                break


class SnakeCollisionException(Exception):
    """뱀 충돌 예외"""
    pass


class UpgradeHardness1(Exception):
    """난이도 상승1"""
    pass


class UpgradeHardness2(Exception):
    """난이도 상승2"""
    pass


class UpgradeHardness3(Exception):
    """난이도 상승3"""
    pass


TURN_INTERVAL = timedelta(seconds=0.3)  # 게임 진행 간격을 0.3초로 정의

game_board = GameBoard()  # 게임판 인스턴스 생성

# 방향키 입력에 따라 바꿀 블록의 방향
DIRECTION_ON_KEY = {
    pygame.K_UP: 'north',
    pygame.K_DOWN: 'south',
    pygame.K_LEFT: 'west',
    pygame.K_RIGHT: 'east'
}

block_direction = 'east'  # 블록의 방향
block_position = [0, 0]  # 블록 위치 (y, x)
last_turn_time = datetime.now()  # 마지막으로 블록을 움직인 때

# 종료 이벤트가 발생할 때까지 게임을 계속 진행한다
while True:
    events = pygame.event.get()             # 발생한 이벤트 목록을 읽어드린다
    for event in events:                    # 이벤트 목록을 순회하며 각 이벤트를 처리한다
        if event.type == pygame.QUIT:       # 종료 이벤트가 발생한 경우
            exit()                          # 게임을 종료한다
        if event.type == pygame.KEYDOWN:    # 화살표 키가 입력되면 뱀의 방향을 바꾼다
            if event.key in DIRECTION_ON_KEY:
                game_board.snake.turn(DIRECTION_ON_KEY[event.key])

    # 시간이 TURN_INTERVAL 만큼 지날 때마다 게임을 한 차례씩 진행한다
    if TURN_INTERVAL < datetime.now() - last_turn_time:
        try:
            game_board.process_turn()
        except SnakeCollisionException:
            exit()
        except UpgradeHardness1:
            TURN_INTERVAL = timedelta(seconds=0.25)
        except UpgradeHardness2:
            TURN_INTERVAL = timedelta(seconds=0.20)
        except UpgradeHardness3:
            TURN_INTERVAL = timedelta(seconds=0.15)
        last_turn_time = datetime.now()

    # 화면을 계속 새로 그린다
    draw_background(screen)
    game_board.draw(screen)  # 화면에 게임판을 그린다
    pygame.display.update()
