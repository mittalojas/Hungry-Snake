import pygame,sys,random
from pygame import display, event, draw, time, font
pygame.init()
screen=display.set_mode((800,600))
display.set_caption("Hungry Snake Game")
clock = time.Clock()
lavender=(241,203,255)
green = (0,255,0)
red = (255,0,0)
x1 = 300
y1 = 200
x1_change = 0
y1_change = 0
snake_list = []
snake_length = 1
foodx = int(random.randint(0, 790) / 10) * 10
foody = int(random.randint(0, 590) / 10) * 10
blue = (0,0,255)
text_font = font.Font("freesansbold.ttf", 32)
while True:
  allevents = event.get()
  for myevent in allevents:
    if myevent.type == pygame.QUIT:
      sys.exit()
    if myevent.type == pygame.KEYDOWN:
      if myevent.key == pygame.K_LEFT:
        x1_change = -10
        y1_change = 0
      if myevent.key == pygame.K_RIGHT:
        x1_change = 10
        y1_change = 0
      if myevent.key == pygame.K_UP:
        y1_change = -10
        x1_change = 0
      if myevent.key == pygame.K_DOWN:
        y1_change = 10
        x1_change = 0
  if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0 :
    screen.fill(lavender)
    text_render = text_font.render("GAME OVER", True, blue)
    screen.blit(text_render, (300, 250))
    display.flip()
    time.delay(5000)
    break
  x1 = x1 + x1_change
  y1 = y1 + y1_change
  screen.fill(lavender)
  food_rect = (foodx, foody, 10, 10)
  draw.rect(screen, red, food_rect)
  snake_list.append([x1, y1])
  if len(snake_list) > snake_length:
    del snake_list[0]
  for x in snake_list:
    snake_rect = (x[0], x[1], 10, 10)
    draw.rect(screen, green, snake_rect)
  for x in snake_list[:-1]:
    if x == [x1, y1]:
      screen.fill(lavender)
      text_render = text_font.render("GAME OVER", True, blue)
      screen.blit(text_render, (300, 250))
      display.flip()
      time.delay(5000)
      break
  score = snake_length - 1
  text_render = text_font.render("SCORE: " +str(score), True, blue)
  screen.blit(text_render, (10, 10))
  display.flip()
  if x1 == foodx and y1 == foody:
    foodx = int(random.randint(0, 590) / 10) * 10
    foody = int(random.randint(0, 390) / 10) * 10
    snake_length = snake_length + 1
  clock.tick(3)