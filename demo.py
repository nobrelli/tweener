import pygame as pg
from tweener.tween import Tween, Easing, EasingMode

WIDTH = 600
HEIGHT = 600
TITLE = "Motion Demo"
FPS = 60


if __name__ == '__main__':
    pg.init()
    canvas = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(TITLE)

    running = True
    clock = pg.time.Clock()

    base_canvas = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)

    font = pg.font.SysFont('arialblack', 14)

    BOX_SIZE = 30
    SPACING = 20
    boxes = []
    easings = (
        Easing.LINEAR,
        Easing.SINE,
        Easing.QUAD,
        Easing.CUBIC,
        Easing.QUART,
        Easing.QUINT,
        Easing.EXPO,
        Easing.CIRC,
        Easing.BACK,
        Easing.ELASTIC,
        Easing.BOUNCE
    )
    ease_txt = (
        'linear',
        'sinusoidal',
        'quadratic',
        'cubic',
        'quartic',
        'quintic',
        'exponential',
        'circular',
        'back',
        'elastic',
        'bounce'
    )

    mode = font.render('Mode: IN', True, pg.Color(76, 58, 81))

    for i in range(11):
        boxes.append({
            'rect': pg.Rect(0, (BOX_SIZE + SPACING) * i, BOX_SIZE, BOX_SIZE),
            'tween': Tween(0, WIDTH - BOX_SIZE,
                           duration=2000,
                           easing=easings[i],
                           easing_mode=EasingMode.IN,
                           boomerang=True,
                           loop=True,
                           reps=0),
            'text': font.render(ease_txt[i], True, pg.Color(119, 67, 96))
        })

    # You can't use special functions in colors
    alpha_tween = Tween(255, 0,
                        duration=2000,
                        easing=Easing.QUAD,
                        easing_mode=EasingMode.IN_OUT,
                        boomerang=True,
                        loop=True,
                        reps=0)

    FPS = 60

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYUP:
                match event.key:
                    case pg.K_SPACE:
                        for box in boxes:
                            box['tween'].start()
                        alpha_tween.start()
                    case pg.K_p:
                        for box in boxes:
                            box['tween'].pause()
                        alpha_tween.pause()
                    case pg.K_r:
                        for box in boxes:
                            box['tween'].resume()
                        alpha_tween.resume()
                    case pg.K_1:
                        for box in boxes:
                            box['tween'].easing_mode = EasingMode.IN
                        mode = font.render('Mode: IN', True, pg.Color(119, 67, 96))
                    case pg.K_2:
                        for box in boxes:
                            box['tween'].easing_mode = EasingMode.OUT
                        mode = font.render('Mode: OUT', True, pg.Color(119, 67, 96))
                    case pg.K_3:
                        for box in boxes:
                            box['tween'].easing_mode = EasingMode.IN_OUT
                        mode = font.render('Mode: IN_OUT', True, pg.Color(119, 67, 96))


        canvas.fill(pg.Color(255, 255, 255))

        # Update
        step = font.render(f'Step: {boxes[0]["tween"].step:.3f}', True, pg.Color(76, 58, 81))

        for box in boxes:
            box['tween'].update()
            box['rect'].x = box['tween'].value

            # Render
            canvas.blit(box['text'], (WIDTH / 2 - box['text'].get_width() / 2, box['rect'].y))
            pg.draw.rect(canvas, pg.Color(76, 58, 81), box['rect'])

        canvas.blit(mode, (20, 540))
        canvas.blit(step, (20, 560))

        pg.display.flip()
        clock.tick(FPS)

    pg.quit()
