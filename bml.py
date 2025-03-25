import numpy as np
import random

import settings


def bml(lattice : np.ndarray) -> tuple:
    for step in range(settings.SIMULATION_STEPS):
        if step % 2 == 0:
            for i, j in zip(*np.where(lattice == 1)):
                if i < settings.LATTICE_SIZE - 1:
                    if lattice[i + 1, j] == 0:
                        lattice[i + 1, j] = 1
                        lattice[i, j] = 0
                else:
                    if lattice[0, j] == 0:
                        lattice[0, j] = 1
                        lattice[i, j] = 0
        elif step % 2 != 0:
            for i, j in zip(*np.where(lattice == 2)):
                if j < settings.LATTICE_SIZE - 1:
                    if lattice[i, j + 1] == 0:
                        lattice[i, j + 1] = 2
                        lattice[i, j] = 0
                else:
                    if lattice[i, 0] == 0:
                        lattice[i, 0] = 2
                        lattice[i, j] = 0
        yield step, lattice


def bmlr(lattice : np.ndarray) -> tuple:
    for step in range(settings.SIMULATION_STEPS):
        coords = [
            (random.randint(0, settings.LATTICE_SIZE - 1),
             random.randint(0, settings.LATTICE_SIZE - 1)) for _ in range(settings.LATTICE_SIZE**2)
        ]
        for (i, j) in coords:
            if lattice[i, j] == 1:
                if i < settings.LATTICE_SIZE - 1:
                    if lattice[i + 1, j] == 0:
                        lattice[i + 1, j] = 1
                        lattice[i, j] = 0
                else:
                    if lattice[0, j] == 0:
                        lattice[0, j] = 1
                        lattice[i, j] = 0
            elif lattice[i, j] == 2:
                if j < settings.LATTICE_SIZE - 1:
                    if lattice[i, j + 1] == 0:
                        lattice[i, j + 1] = 2
                        lattice[i, j] = 0
                else:
                    if lattice[i, 0] == 0:
                        lattice[i, 0] = 2
                        lattice[i, j] = 0
        yield step, lattice


def loop_klein(x) -> int:
    return settings.LATTICE_SIZE - x - 1


def klein_bml(lattice : np.ndarray) -> tuple:
    for step in range(settings.SIMULATION_STEPS):
        if step % 2 == 0:
            for i, j, k in zip(*np.where(lattice == 1)):
                if i < settings.LATTICE_SIZE - 1:
                    if lattice[i + 1, j, k] == 0:
                        lattice[i + 1, j, k] = 1
                        lattice[i, j, k] = 0
                else:
                    if k == 0:
                        if lattice[0, loop_klein(j), 1] == 0:
                            lattice[0, loop_klein(j), 1] = 1
                            lattice[i, j, k] = 0
                    else:
                        if lattice[0, loop_klein(j), 0] == 0:
                            lattice[0, loop_klein(j), 0] = 1
                            lattice[i, j, k] = 0
        elif step % 2 != 0:
            for i, j, k in zip(*np.where(lattice == 2)):
                if j < settings.LATTICE_SIZE - 1:
                    if lattice[i, j + 1, k] == 0:
                        lattice[i, j + 1, k] = 2
                        lattice[i, j, k] = 0
                else:
                    if k == 0:
                        if lattice[loop_klein(i), 0, 1] == 0:
                            lattice[loop_klein(i), 0, 1] = 2
                            lattice[i, j, k] = 0
                    else:
                        if lattice[loop_klein(i), 0, 0] == 0:
                            lattice[loop_klein(i), 0, 0] = 2
                            lattice[i, j, k] = 0
        yield step, lattice


def klein_bmlr(lattice : np.ndarray) -> tuple:
    for step in range(settings.SIMULATION_STEPS):
        coords = [
            (random.randint(0, settings.LATTICE_SIZE - 1),
             random.randint(0, settings.LATTICE_SIZE - 1),
             random.randint(0, 1)) for _ in range(settings.LATTICE_SIZE**2)
        ]
        for (i, j, k) in coords:
            if lattice[i, j, k] == 1:
                if i < settings.LATTICE_SIZE - 1:
                    if lattice[i + 1, j, k] == 0:
                        lattice[i + 1, j, k] = 1
                        lattice[i, j, k] = 0
                else:
                    if k == 0:
                        if lattice[0, loop_klein(j), 1] == 0:
                            lattice[0, loop_klein(j), 1] = 1
                            lattice[i, j, k] = 0
                    else:
                        if lattice[0, loop_klein(j), 0] == 0:
                            lattice[0, loop_klein(j), 0] = 1
                            lattice[i, j, k] = 0
            elif lattice[i, j, k] == 2:
                if j < settings.LATTICE_SIZE - 1:
                    if lattice[i, j + 1, k] == 0:
                        lattice[i, j + 1, k] = 2
                        lattice[i, j, k] = 0
                else:
                    if k == 0:
                        if lattice[loop_klein(i), 0, 1] == 0:
                            lattice[loop_klein(i), 0, 1] = 2
                            lattice[i, j, k] = 0
                    else:
                        if lattice[loop_klein(i), 0, 0] == 0:
                            lattice[loop_klein(i), 0, 0] = 2
                            lattice[i, j, k] = 0
        yield step, lattice
