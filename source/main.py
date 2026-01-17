#Asyncio is purely for python3/pygame-ce -> browser support, the script itself does not depend on asyncio.
import asyncio

async def main():
	import pygame, time
	pygame.init()

	pygame.display.set_icon(pygame.image.load("delta_rune.png"))
	pygame.display.set_caption("Chance of Deltarune Now")
	screen = pygame.surface.Surface((960, 720), pygame.SRCALPHA)
	running = True
	font = pygame.font.SysFont("Arial", 125)
	#Animation 0: 5 FPS, 5 Frames
	#Animation 1: 15 FPS, 31 Frames
	ANIMATION = 1
	FPS = 15
	FRAMES = 31
	frames = [pygame.image.load(f"frame{ANIMATION}_{i}.png") for i in range(FRAMES)]
	window = pygame.display.set_mode(frames[0].get_size())

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		screen.fill((0, 0, 0, 0))
		current = time.time_ns() - 1767225600000000000
		text = font.render("There is a", True, "white")
		screen.blit(text, (480 - text.get_width() / 2, 75 - text.get_height() / 2))
		result = current / 31557600000000000 * 100
		string = f"{result:.97f}".rstrip('0')
		if string[-1] == '.':
			string = string.removesuffix('.')
		string += "% chance"
		text = font.render(string, True, "white")
		text = pygame.transform.scale_by(text, 960 / text.get_width())
		if text.get_height() > 100:
			text = font.render(string, True, "white")
		screen.blit(text, (480 - text.get_width() / 2, 200 - text.get_height() / 2))
		text = font.render("of deltarune", True, "white")
		screen.blit(text, (480 - text.get_width() / 2, 325 - text.get_height() / 2))
		text = font.render("releasing now.", True, "white")
		screen.blit(text, (480 - text.get_width() / 2, 450 - text.get_height() / 2))
		window.fill("black")
		window.blit(frames[round(current / 1000000000 * FPS) % FRAMES], (0, 0))
		window.blit(pygame.transform.scale(screen, (window.get_width(), window.get_height())), (0, 0))
		pygame.display.flip()
		await asyncio.sleep(0)
	pygame.quit()

asyncio.run(main())