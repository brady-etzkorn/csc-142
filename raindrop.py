import pygame
import random

class RainDrop():
    __slots__ = ['x', 'y', 'radius']
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1

    def update(self):
        self.radius += 1
    
    def draw(self, screen):
        pygame.draw.circle(screen, (0,0,255), (self.x, self.y), self.radius)

class RainDropManager:
    RAIN_RATE = 350
    MAX_RADIUS = 50
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))

        self.clock = pygame.time.Clock()
        self.running = True

        self.width = width
        self.height = height

        self.raindrops = []
        self.last_spawn_time = 0

    def spawn_raindrop(self):
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        self.raindrops.append(RainDrop(x, y))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        current_time = pygame.time.get_ticks()

        # Spawn raindrops based on RAIN_RATE
        if current_time - self.last_spawn_time > self.RAIN_RATE:
            self.spawn_raindrop()
            self.last_spawn_time = current_time

        # Update raindrops
        for drop in self.raindrops:
            drop.update()

        # Remove raindrops that leave the screen
        self.raindrops = [d for d in self.raindrops if d.radius < RainDropManager.MAX_RADIUS]

    def draw(self):
        self.screen.fill((255,255,255))  # background (glass)

        for drop in self.raindrops:
            drop.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()









# --- Driver Code ---
if __name__ == "__main__":
    manager = RainDropManager()
    manager.run()