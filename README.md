
## Example
I used Python version **3.10.5** and **pygame 2.1.2**
```python
import pygame
from tweener import *

WIDTH = 600
HEIGHT = 600
TITLE = "Motion Demo"
FPS = 60

pygame.init()
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

running = True
clock = pygame.time.Clock()

rect = pg.Rect(0, 100, 100, 100)
anim_y = Tween(begin=0, 
               end=WIDTH-100,
               duration=1000,
               easing=Easing.BOUNCE,
               easing_mode=EasingMode.OUT,
               boomerang=True, 
               loop=True)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_SPACE:
                    anim_y.start()
                case pygame.K_p:
                    anim_y.pause()
                case pygame.K_r:
                    anim_y.resume()

    canvas.fill(pygame.Color(255, 255, 255))

    # Update
    anim_y.update()
    rect.x = anim_y.value

    # Render
    pygame.draw.rect(canvas, (255, 0, 0), rect)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
```

