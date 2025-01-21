# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	print(f"Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	clock = pygame.time.Clock()
	dt=0
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	gamer = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
	game_field = AsteroidField()
	
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for item in updatable:
			item.update(dt)
		for asteroid in asteroids :
			if asteroid.collisions_check(gamer) == True :
				print(f"Game over!")
				return
		for drawing in drawable:
			drawing.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
