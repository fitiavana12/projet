# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:38:59 2023

@author: NewUser
"""


import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre de jeu
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

# Couleurs utilisées dans le jeu
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Taille de la grille du jeu
GRID_SIZE = 20

# Classe pour représenter les segments du serpent
class SnakeSegment:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Classe pour représenter le serpent
class Snake:
    def __init__(self):
        self.segments = [SnakeSegment(5*GRID_SIZE, 5*GRID_SIZE), SnakeSegment(4*GRID_SIZE, 5*GRID_SIZE), SnakeSegment(3*GRID_SIZE, 5*GRID_SIZE)]
        self.direction = "right"

    def move(self):
        # Ajouter un nouveau segment à la tête du serpent
        head = self.segments[0]
        if self.direction == "right":
            new_head = SnakeSegment(head.x + GRID_SIZE, head.y)
        elif self.direction == "left":
            new_head = SnakeSegment(head.x - GRID_SIZE, head.y)
        elif self.direction == "up":
            new_head = SnakeSegment(head.x, head.y - GRID_SIZE)
        elif self.direction == "down":
            new_head = SnakeSegment(head.x, head.y + GRID_SIZE)
        self.segments.insert(0, new_head)

        # Supprimer le dernier segment du serpent
        self.segments.pop()

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(screen, GREEN, (segment.x, segment.y, GRID_SIZE, GRID_SIZE))

    def collides_with_self(self):
        head = self.segments[0]
        for segment in self.segments[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

    def collides_with_wall(self):
        head = self.segments[0]
        if head.x < 0 or head.x >= SCREEN_WIDTH or head.y < 0 or head.y >= SCREEN_HEIGHT:
            return True
        return False

# Classe pour représenter la nourriture du serpent
class Food:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - GRID_SIZE)
        self.y = random.randint(0, SCREEN_HEIGHT - GRID_SIZE)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, GRID_SIZE, GRID_SIZE))

    def collides_with_snake(self, snake):
        for segment in snake.segments:
            if self.x == segment.x and self.y == segment.y:
                return True
        return False

# Création du serpent et de la nourriture
snake = Snake()
food = Food()

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.direction != "left":
                snake.direction = "right"
            elif event.key == pygame.K_LEFT and snake.direction != "right":
                snake.direction = "left"
            elif event.key == pygame.K_UP and snake.direction != "down":
                snake.direction = "up"
            elif event.key == pygame.K_DOWN and snake.direction != "up":
                snake.direction = "down"


           
