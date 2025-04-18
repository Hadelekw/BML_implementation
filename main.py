import numpy as np
import pygame as pg
import random

import settings
from bml import bml, bmlr


def main() -> None:
    screen = pg.display.set_mode((settings.DISPLAY_SIZE, settings.DISPLAY_SIZE))
    pg.display.set_caption('BML')

    base_lattice = np.zeros((settings.LATTICE_SIZE, settings.LATTICE_SIZE))

    while np.sum(base_lattice != 0) / np.sum(base_lattice >= 0) < settings.DENSITY:
        i = random.randint(0, settings.LATTICE_SIZE - 1)
        j = random.randint(0, settings.LATTICE_SIZE - 1)
        base_lattice[i, j] = random.choice([1, 2])

    if settings.RANDOMIZED:
        result = bmlr(base_lattice)
    else:
        result = bml(base_lattice)

    run = True
    for step, lattice in result:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        screen.fill((0, 0, 0))

        for i in range(lattice.shape[0]):
            for j in range(lattice.shape[1]):
                if lattice[i, j] == 1:
                    pg.draw.rect(screen, settings.DISPLAY_COLOR_1, pg.Rect(int(i * settings.SCALE), int(j * settings.SCALE), int(settings.SCALE), int(settings.SCALE)))
                elif lattice[i, j] == 2:
                    pg.draw.rect(screen, settings.DISPLAY_COLOR_2, pg.Rect(int(i * settings.SCALE), int(j * settings.SCALE), int(settings.SCALE), int(settings.SCALE)))

        if not run:
            break

        pg.display.flip()
    pg.quit()


if __name__ == '__main__':
    main()
