import numpy as np
import pygame as pg
import random

import settings
from bml import klein_bml, klein_bmlr


def main() -> None:
    screen = pg.display.set_mode((settings.DISPLAY_SIZE, settings.DISPLAY_SIZE))
    pg.display.set_caption('BML')

    base_lattice = np.zeros((settings.LATTICE_SIZE, settings.LATTICE_SIZE, 2))

    while np.sum(base_lattice != 0) / np.sum(base_lattice >= 0) < settings.DENSITY:
        i = random.randint(0, settings.LATTICE_SIZE - 1)
        j = random.randint(0, settings.LATTICE_SIZE - 1)
        k = random.randint(0, 1)
        base_lattice[i, j, k] = random.choice([1, 2])

    if settings.RANDOMIZED:
        result = klein_bmlr(base_lattice)
    else:
        result = klein_bml(base_lattice)

    run = True
    for step, lattice in result:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        screen.fill((0, 0, 0))

        for i in range(lattice.shape[0]):
            for j in range(lattice.shape[1]):
                rect = pg.Rect(int(i * settings.SCALE), int(j * settings.SCALE), int(settings.SCALE), int(settings.SCALE))
                if lattice[i, j, 0] == 1:
                    pg.draw.rect(screen, settings.DISPLAY_COLOR_1, rect)
                elif lattice[i, j, 0] == 2:
                    pg.draw.rect(screen, settings.DISPLAY_COLOR_2, rect)
                elif lattice[i, j, 1] == 1:
                    pg.draw.rect(screen, [c // 3 for c in settings.DISPLAY_COLOR_1], rect)
                elif lattice[i, j, 1] == 2:
                    pg.draw.rect(screen, [c // 3 for c in settings.DISPLAY_COLOR_2], rect)

        if not run:
            break

        pg.display.flip()
    pg.quit()


if __name__ == '__main__':
    main()
