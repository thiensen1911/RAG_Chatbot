import random
import pygame

pygame.init()

CELL = 20
COLS, ROWS = 30, 20
screen = pygame.display.set_mode((COLS * CELL, ROWS * CELL))
pygame.display.set_caption("Ran san moi")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)


def new_food(snake):
    while True:
        pos = (random.randrange(COLS), random.randrange(ROWS))
        if pos not in snake:
            return pos


def reset():
    snake = [(COLS // 2, ROWS // 2)]
    return snake, (1, 0), new_food(snake), 0


snake, direction, food, score = reset()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            dx, dy = direction
            if event.key in (pygame.K_UP, pygame.K_w) and dy == 0:
                direction = (0, -1)
            elif event.key in (pygame.K_DOWN, pygame.K_s) and dy == 0:
                direction = (0, 1)
            elif event.key in (pygame.K_LEFT, pygame.K_a) and dx == 0:
                direction = (-1, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d) and dx == 0:
                direction = (1, 0)

    # Di chuyển rắn
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Đụng tường hoặc đụng thân -> chơi lại
    if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS) or head in snake:
        snake, direction, food, score = reset()
        continue

    snake.insert(0, head)
    if head == food:
        score += 1
        food = new_food(snake)
    else:
        snake.pop()

    # Vẽ
    screen.fill((20, 20, 20))
    pygame.draw.rect(screen, (220, 50, 50), (food[0] * CELL, food[1] * CELL, CELL, CELL))
    for x, y in snake:
        pygame.draw.rect(screen, (50, 200, 80), (x * CELL, y * CELL, CELL - 1, CELL - 1))
    screen.blit(font.render(f"Diem: {score}", True, (255, 255, 255)), (8, 6))
    pygame.display.flip()

    clock.tick(10)  # tốc độ: tăng số này để rắn chạy nhanh hơn

pygame.quit()
