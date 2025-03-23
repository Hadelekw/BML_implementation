import numpy as np
import pygame as pg
import random

import settings


def bml(lattice : np.ndarray) -> np.ndarray:
    if settings.RANDOMIZED:
        pass  # TODO: add BML-R variant.
    else:
        for step in range(settings.SIMULATION_STEPS):
            if step % 2 == 0:
                for i, j in zip(*np.where(lattice == 1)):
                    if i < settings.LATTICE_WIDTH - 1:
                        if lattice[i + 1, j] == 0:
                            lattice[i + 1, j] = 1
                            lattice[i, j] = 0
                    else:
                        if lattice[0, j] == 0:
                            lattice[0, j] = 1
                            lattice[i, j] = 0
            elif step % 2 != 0:
                for i, j in zip(*np.where(lattice == 2)):
                    if j < settings.LATTICE_WIDTH - 1:
                        if lattice[i, j + 1] == 0:
                            lattice[i, j + 1] = 2
                            lattice[i, j] = 0
                    else:
                        if lattice[i, 0] == 0:
                            lattice[i, 0] = 2
                            lattice[i, j] = 0
            yield step, lattice


def main() -> None:
    screen = pg.display.set_mode(settings.DISPLAY_SIZE)
    base_lattice = np.zeros(settings.LATTICE_SIZE)

    while np.sum(base_lattice != 0) / np.sum(base_lattice == 0) < settings.DENSITY:
        i = random.randint(0, settings.LATTICE_WIDTH - 1)
        j = random.randint(0, settings.LATTICE_HEIGHT - 1)
        base_lattice[i, j] = random.choice([1, 2])

    result = bml(base_lattice)

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

        pg.display.flip()
    pg.quit()


if __name__ == '__main__':
    main()
