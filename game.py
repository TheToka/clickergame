import pygame
import math
import time
from pygame.locals import *


pygame.init()
x_pos = 800
y_pos = 600
win = pygame.display.set_mode((x_pos, y_pos))

pygame.display.set_caption("clicker")

PyIL = pygame.image.load

bg = PyIL('bg.jpg')
button = PyIL('buttonStock1h.png')
enemy = PyIL('enemy.png')

clock = pygame.time.Clock()



automoney = 0.4
fps = 60
money = 0
animCount = 0
CoefficientClick = 1
click = False

shop1money = 10
shop1value = 0.1
shop2money = 300

font = pygame.font.Font('FreeMono.ttf', 36)

def drawWindow():
	global animCount
	global b1, b2, enemysprt

	win.blit(bg, (0, 0))

	if animCount + 1 >= fps:
		animCount = 0

	textMoney = "money = " + str(money) + " a+" + str(round(automoney-0.4,2))
	tmoney = font.render(textMoney, 1, (1, 1, 155))
	win.blit(tmoney, (40, 20))

	enemysprt = win.blit(enemy, (400,300))

	b1 = win.blit(button, (40,80))
	shop1 = font.render("m=" + str(shop1money) + " v+" + str(shop1value), 1, (51, 221, 51))
	win.blit(shop1, (40, 80))

	b2 = win.blit(button, (40,120))
	shop2 = font.render("m=" + str(shop2money), 1, (51, 221, 51))
	win.blit(shop2, (40, 120))



	pygame.display.update()





run = True
while run:
	clock.tick(fps)
	money = round(automoney/100+money,2)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			if not click and enemysprt.collidepoint(pos):
				money = round(money+CoefficientClick,2)
				click = True

		if event.type == pygame.MOUSEBUTTONUP:
			click = False

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			pos = pygame.mouse.get_pos()
			if b1.collidepoint(pos) and money > shop1money:
				money = round(money-shop1money,2)
				CoefficientClick = round(CoefficientClick+shop1value,2)
				shop1money = round(shop1money*1.2,2)
				shop1value = round(shop1value*1.1,2)

			if b2.collidepoint(pos) and money > shop2money:
				money = round(money-shop2money,2)
				automoney = round(automoney+0.3,2)
				shop2money = round(shop2money*1.2,2)
				if automoney > 1:
					automoney = round(automoney+0.3,2)
					if automoney > 5:
						automoney = round(automoney+0.9,2)
				




	keys = pygame.key.get_pressed()

	if keys[pygame.K_ESCAPE]:
		pygame.quit()


	drawWindow()


pygame.quit()