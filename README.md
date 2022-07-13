
# Tweener

Helper functions for easing and tweening


## Installation

```
  pip install tweener
```
    
## Reference

#### Tween object

```python
Tween(begin, end, duration, easing, easing_mode, boomerang, loop, reps)
```

| Parameter | Type     | Description                                         |
| :-------- | :------- | :-------------------------------------------------- |
| `begin`   | `float`  | The beginning value of a property (default: `0.0`)  |
| `end`     | `float`  | The end value of a property (default: `1.0`)        |
| `duration`| `int`    | The length of time that an animation takes to complete (default: `600 ms`) |
| `easing`  | `Easing` | The type of easing to apply. (default: `Easing.LINEAR`) |
| `easing_mode` | `EasingMode` | The mode of easing `IN`, `OUT`, `IN_OUT`, (default: `IN`) |
| `boomerang` | `bool` | Returns the animation back to its starting point and vice versa. (default: `False`) |
| `loop`    | `bool`  | Loops the animation. When used with `boomerang`, it does the back and forth animation. (default: `False`) |
| `reps`  | `int` | Number of times the animation will be repeated. Zero means infinite. (default: `0`) |

#### Starts the animation

```python
Tween().start()
```

#### Updates the animation state

```python
Tween().update()
```

#### Pauses the animation

```python
Tween().pause()
```

#### Resumes the animation

```python
Tween().resume()
```

### Easing types
    LINEAR
    SINE
    QUAD
    CUBIC
    QUART
    QUINT
    EXPO
    CIRC
    BACK
    ELASTIC
    BOUNCE

### Easing modes (except linear)
    IN
    OUT
    IN_OUT

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


## Demo
https://user-images.githubusercontent.com/44640489/178249122-dbb962c0-eefd-4193-9fee-a001cf4e51a8.mp4
## Contributing

Contributions are always welcome!

## References

- https://easings.net/
- http://robertpenner.com/easing/
