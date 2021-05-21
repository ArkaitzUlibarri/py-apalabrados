import pygame
import datetime
import os
from tile import Tile
import yaml

with open("config/config.yml", 'r') as yml_file:
    config = yaml.load(yml_file)

BONUS = config['bonus']
APP_NAME = config['app_name']
FONT_SIZE = config['font']['size']
DEFAULT_FONT = config['font']['type']
FONT_BOLD = config['font']['bold']
GRID_COLOR = BLACK = (0, 0, 0)

USER_TOKENS = 7
SIZE = WIDTH, HEIGHT = 600, 600
MAP_SIZE = 15
SQUARE_SIZE = (WIDTH / MAP_SIZE)
MEDIUM = SQUARE_SIZE / 2

Types = ["Normal", "DL", "DP", "TL", "TP", "Start", "Letter"]
Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Ñ", "O", "P", "Q",
           "R", "S", "T", "U", "V", "X", "Y", "Z", "*"]
Values = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 1, 3, 1, 8, 1, 3, 5, 1, 1, 1, 1, 4, 8, 4, 10, 0]
Tiles = [12, 2, 4, 5, 12, 1, 2, 2, 6, 1, 4, 2, 5, 1, 9, 2, 1, 5, 6, 4, 5, 1, 1, 1, 1, 2]

Quantity = len(Letters)
totalTiles = sum(Tiles)

letters = {'A': [1, 12], 'B': [3, 2], 'C': [3, 4], 'D': [2, 5], 'E': [1, 12], 'F': [4, 1], 'G': [2, 2], 'H': [4, 2],
           'I': [1, 6], 'J': [8, 1], 'L': [1, 4], 'M': [3, 2], 'N': [1, 5], 'Ñ': [8, 1], 'O': [1, 9], 'P': [3, 2],
           'Q': [5, 1], 'R': [1, 5], 'S': [1, 6], 'T': [1, 4], 'U': [1, 5], 'V': [4, 1], 'X': [8, 1], 'Y': [4, 1],
           'Z': [10, 1], '*': [0, 2]}


def multiply_letter(square_type, letter_value):
    if square_type == "DL":
        return 2 * letter_value
    elif square_type == "TL":
        return 3 * letter_value
    else:
        return letter_value


def multiply_word(square_type, word_value):
    if square_type == "DP":
        return 2 * word_value
    elif square_type == "TP":
        return 3 * word_value
    else:
        return word_value


def apply_bonus(word_value):
    return word_value + BONUS


def type_mapping(number):
    return Types[number]


def load_map(filename="assets/map"):
    if not os.path.isfile(filename):
        return False

    f = open(filename, "r")
    data = f.read().split("\n")

    matrix = []
    for index, row in enumerate(data):
        matrix.append([row])

    return matrix


def draw_grid(surface):
    square_size = WIDTH // MAP_SIZE
    x = 0
    y = 0
    for element in range(MAP_SIZE):
        x = x + square_size
        y = y + square_size

    pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, WIDTH))
    pygame.draw.line(surface, GRID_COLOR, (0, y), (WIDTH, y))


def main():
    pygame.init()

    font = pygame.font.SysFont(DEFAULT_FONT, FONT_SIZE, FONT_BOLD)
    screen = pygame.display.set_mode(SIZE)  # Create canvas to draw the objects of the game
    pygame.display.set_caption(APP_NAME)  # Change window title

    main_map = load_map()

    squares = []
    for rowIndex, row_value in enumerate(main_map):
        row_value = row_value[0].split(',')
        for colIndex, colValue in enumerate(row_value):
            square_type = type_mapping(int(colValue))
            point = (MEDIUM + int(rowIndex) * SQUARE_SIZE, MEDIUM + int(colIndex) * SQUARE_SIZE)
            new_tile = Tile(square_type, font, point)
            squares.append(new_tile)

    sprites = pygame.sprite.Group(squares)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        sprites.update()  # Update and draw in screen all the sprites
        sprites.draw(screen)
        draw_grid(screen)
        pygame.display.update()


# We call main when the file is invoked as a program
if __name__ == '__main__':
    os.system("cls")
    print("Game Start: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    main()
    print("Game End: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
