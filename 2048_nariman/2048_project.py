import random
import pygame
pygame.init()

# размер
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('2048')

# рандомая клетка значение 2
square = pygame.Surface((150, 150))
square.fill('Blue')


# координаты
kletki = [(0, 0), (150, 0), (300, 0), (450, 0), (0, 150), (150, 150), (300, 150), (450, 150), (0, 300), (150, 300), (300, 300), (450, 300),
          (0, 450), (150, 450), (300, 450), (450, 450)]
x = random.choice([0, 150, 300, 450])
y = random.choice([0, 150, 300, 450])

a = 2

# матрица
osnova = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
free_cells = []
for i in range(4):
    for j in range(4):
        if osnova[i][j] == 0:
            free_cells.append((i, j))
i, j = random.choice(free_cells)
osnova[i][j] = a

# пустые клетки
empty_square = pygame.Surface((150, 150))
empty_square.fill((174, 235, 179))

# шрифт - цифры внутри клеток
font = pygame.font.Font(None, 50)

running = True
move = False


def add_two():
    free_cells = []
    for i in range(4):
        for j in range(4):
            if osnova[i][j] == 0:
                free_cells.append((i, j))
    if free_cells:
        i, j = random.choice(free_cells)
        osnova[i][j] = a



# osnova[0][0] = 4
# osnova[0][1] = 4
# osnova[0][2] = 4
# osnova[0][3] = 4
# osnova[0][0] = 4
# osnova[1][0] = 4
# osnova[2][0] = 4
# osnova[3][0] = 4

coor = 0
coor_2 = 0

# font = pygame.font.Font(None, 80)
colors = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

while running:
    for i in range(4):
        for j in range(4):
            screen.blit(empty_square, (j * 150, i * 150))
    for i in range(4):
        for j in range(4):
            value = osnova[i][j]
            if value != 0:
                color = colors.get(value, (60, 58, 50))
                pygame.draw.rect(
                    screen,
                    color,
                    (j * 150, i * 150, 150, 150),
                    border_radius=12)
                text_color = (119, 110, 101) if value <= 4 else (249, 246, 242)
                text = font.render(str(value), True, text_color)

                text_rect = text.get_rect(center=(j * 150 + 75, i * 150 + 75))
                screen.blit(text, text_rect)
    for i in range(1, 4):  # сетка
        pygame.draw.line(screen, 'Black', (i * 150, 0), (i * 150, 600), 2)
        pygame.draw.line(screen, 'Black', (0, i * 150), (600, i * 150), 2)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                for i in range(4):
                    for j in range(4):
                        coor = -1
                        coor_2 = -1
                        for k in range(j - 1, -1, -1):
                            if osnova[i][j] != 0:
                                if osnova[i][k] == 0:
                                    coor = k
                                if osnova[i][j] == osnova[i][k]:
                                    if osnova[i][j - 1] >= 0 and osnova[i][k + 1] >= 0:
                                        coor_2 = k
                                if osnova[i][k] != 0:
                                    break
                        if coor_2 >= 0:
                            osnova[i][coor_2] *= 2
                            osnova[i][j] = 0
                            move = True
                        elif coor >= 0:
                            osnova[i][coor] = osnova[i][j]
                            osnova[i][j] = 0
                            move = True

            elif event.key == pygame.K_RIGHT:
                for i in range(4):
                    for j in range(3, -1, -1):
                        coor = -1
                        coor_2 = -1
                        for k in range(j + 1, 4):
                            if osnova[i][j] != 0:
                                if osnova[i][k] == 0:
                                    coor = k
                                if osnova[i][j] == osnova[i][k]:
                                    if osnova[i][j + 1] >= 0 and osnova[i][k - 1] >= 0:
                                        coor_2 = k
                                if osnova[i][k] != 0:
                                    break
                        if coor_2 >= 0:
                            osnova[i][coor_2] *= 2
                            osnova[i][j] = 0
                            move = True
                        elif coor >= 0:
                            osnova[i][coor] = osnova[i][j]
                            osnova[i][j] = 0
                            move = True

            elif event.key == pygame.K_DOWN:
                for i in range(3, - 1, -1):
                    for j in range(4):
                        coor = -1
                        coor_2 = -1
                        for k in range(i + 1, 4):
                            if osnova[i][j] != 0:
                                if osnova[k][j] == 0:
                                    coor = k
                                if osnova[i][j] == osnova[k][j]:
                                    if osnova[i + 1][j] >= 0 and osnova[k - 1][j] >= 0:
                                        coor_2 = k
                                if osnova[k][j] != 0:
                                    break
                        if coor_2 >= 0:
                            osnova[coor_2][j] *= 2
                            osnova[i][j] = 0
                            move = True
                        elif coor >= 0:
                            osnova[coor][j] = osnova[i][j]
                            osnova[i][j] = 0
                            move = True

            elif event.key == pygame.K_UP:
                for i in range(4):
                    for j in range(4):
                        coor = -1
                        coor_2 = -1
                        for k in range(i - 1, -1, -1):
                            if osnova[i][j] != 0:
                                if osnova[k][j] == 0:
                                    coor = k
                                if osnova[i][j] == osnova[k][j]:
                                    if osnova[i - 1][j] >= 0 and osnova[k + 1][j] >= 0:
                                        coor_2 = k
                                if osnova[k][j] != 0:
                                    break
                        if coor_2 >= 0:
                            osnova[coor_2][j] *= 2
                            osnova[i][j] = 0
                            move = True
                        elif coor >= 0:
                            osnova[coor][j] = osnova[i][j]
                            osnova[i][j] = 0
                            move = True
        if move:
            add_two()
            move = False

