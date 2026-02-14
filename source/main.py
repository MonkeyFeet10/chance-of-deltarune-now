#Asyncio is purely for python3/pygame-ce -> browser support, the script itself does not depend on asyncio.
import asyncio
from typing import Callable

async def main():
	import pygame, time
	pygame.init()

	delta_rune = pygame.image.load("delta_rune.png")
	pygame.display.set_icon(delta_rune)
	pygame.display.set_caption("Chance of Deltarune Now")
	screen = pygame.surface.Surface((960, 720), pygame.SRCALPHA)
	running = True
	font = pygame.font.Font("arial.ttf", 125)
	font_small = pygame.font.Font("arial.ttf", 35)
	#Animation 0: 5 FPS, 5 Frames
	#Animation 1: 15 FPS, 31 Frames
	ANIMATION = 1
	FPS = 15
	FRAMES = 31
	frames = [pygame.image.load(f"frame{ANIMATION}_{i}.png") for i in range(FRAMES)]
	window = pygame.display.set_mode(frames[0].get_size())
	days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
	months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
	convert: Callable[[int], str] = lambda integer: f"0{integer}" if integer < 10 else f"{integer}"
	rect = pygame.Rect(4, 4, 56, 56)
	delta_rune = pygame.transform.scale(delta_rune, rect.size)
	floofy_boi = pygame.transform.scale(pygame.image.load("ralsei.png"), rect.size)
	floof = 0
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if rect.collidepoint(event.pos):
					floof = 1 - floof
					pygame.display.set_icon(floofy_boi if floof else delta_rune)
					pygame.display.set_caption("Chance of Floofy Boi Now" if floof else "Chance of Deltarune Now")
		screen.fill((0, 0, 0, 0))
		utc = time.gmtime()
		current = time.time_ns() - 1767225600000000000
		text = font.render("There is a", True, "white")
		screen.blit(text, (480 - text.get_width() / 2, 75 - text.get_height() / 2))
		if floof:
			result = current / 7776000000000000 * 100
		else:
			result = current / 31536000000000000 * 100
		string = f"{result:.97f}".rstrip('0')
		if string[-1] == '.':
			string = string.removesuffix('.')
		string += "% chance"
		text = font.render(string, True, "white")
		text = pygame.transform.scale_by(text, 960 / text.get_width())
		if text.get_height() > 100:
			text = font.render(string, True, "white")
		screen.blit(text, (480 - text.get_width() / 2, 200 - text.get_height() / 2))
		text = font.render("of the floofy" if floof else "of deltarune", True, "white")
		screen.blit(text, (480 - text.get_width() / 2, 325 - text.get_height() / 2))
		text = font.render("boi arriving now." if floof else "releasing now.", True, "white")
		screen.blit(text, (480 - text.get_width() / 2, 450 - text.get_height() / 2))
		text = font_small.render(f"Time (UTC): {days[utc.tm_wday]}, {months[utc.tm_mon - 1]} {convert(utc.tm_mday)}, {utc.tm_year} @ {convert(utc.tm_hour)}:{convert(utc.tm_min)}:{convert(utc.tm_sec)}", True, "white")
		screen.blit(text, (480 - text.get_width() / 2, 680 - text.get_height()))
		window.fill("black")
		window.blit(frames[round(current / 1000000000 * FPS) % FRAMES], (0, 0))
		window.blit(pygame.transform.scale(screen, (window.get_width(), window.get_height())), (0, 0))
		if floof:
			window.blit(delta_rune, rect)
		else:
			window.blit(floofy_boi, rect)
		pygame.display.flip()
		await asyncio.sleep(0)
	pygame.quit()

asyncio.run(main())