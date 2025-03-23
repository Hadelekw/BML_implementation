import numpy as np
import random

import settings


def main() -> None:
    lattice = np.zeros(settings.LATTICE_SIZE)

    while np.sum(lattice != 0) / np.sum(lattice == 0) < settings.DENSITY:
        i = random.randint(0, settings.LATTICE_WIDTH - 1)
        j = random.randint(0, settings.LATTICE_HEIGHT - 1)
        lattice[i, j] = random.choice([1, 2])

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
            print(lattice)


if __name__ == '__main__':
    main()
