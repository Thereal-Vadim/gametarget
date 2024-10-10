import pygame
import random
import time

pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)

# Инициализация экрана
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game Target')
icon = pygame.image.load('Game_Icon.jpg')
pygame.display.set_icon(icon)

# Загрузка изображений
target_img = pygame.image.load('target_images.png')
target_width = 225
target_height = 225

# Начальные параметры
score = 0
game_time = 30  # Время игры в секундах
start_time = time.time()


# Функция для перемещения цели
def reset_target():
    return random.randint(0, SCREEN_WIDTH - target_width), random.randint(0, SCREEN_HEIGHT - target_height)


target_x, target_y = reset_target()

running = True

while running:
    SCREEN.fill(WHITE)

    # Проверка времени
    elapsed_time = time.time() - start_time
    if elapsed_time > game_time:
        running = False
        continue  # Завершить игру, если время вышло

    # Отображение счетчика
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    time_text = font.render(f'Time left: {max(0, game_time - int(elapsed_time))}', True, (0, 0, 0))
    SCREEN.blit(score_text, (10, 10))
    SCREEN.blit(time_text, (10, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x, target_y = reset_target()

    # Отображение цели
    SCREEN.blit(target_img, (target_x, target_y))

    # Обновление экрана
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

# Вывод финального счета
SCREEN.fill(WHITE)
final_score_text = font.render(f'Final Score: {score}', True, (0, 0, 0))
SCREEN.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
pygame.display.update()
time.sleep(3)

pygame.quit()
