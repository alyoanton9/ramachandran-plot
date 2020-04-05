import numpy as np
from math import pi
from cmath import phase


def sub(pair):
    return pair[0] - pair[1]


def vectors(p1, p2, p3, p4):
    """ Makes 3 vectors from 4 points (C, N, CA or CB atoms). """
    a = np.array(list(map(sub, zip(p2, p1))), float)
    b = np.array(list(map(sub, zip(p3, p2))), float)
    c = np.array(list(map(sub, zip(p4, p3))), float)
    return a, b, c


def length(x):
    """ Returns vector's length. """
    return np.linalg.norm(x)


def torsion(a, b, c):
    """ Returns torsion angle for a, b, c vectors (in degrees). """
    b2ac = np.dot(np.multiply(-(length(b) ** 2), a), c)
    abbc = np.dot(a, b) * np.dot(b, c)
    babc = np.dot(np.multiply(length(b), a), np.cross(b, c))
    return phase(complex(b2ac + abbc, babc)) * 180 / pi


def torsionAngles(coords, coeff):
    """ Calculates torsion angles of protein: phi(coeff == 2), psi(coeff == 0)
        phi: Ci-1 -- Ni -- Cai -- Ci
        psi: Ni -- Cai -- Ci -- Ni+1. """
    angles = []
    coord1 = coords[0 + coeff]
    acidsNum = len(coords) // 3
    for i in range(1, acidsNum):
        coord2 = coords[i*3 - 2 + coeff]
        coord3 = coords[i*3 - 1 + coeff]
        coord4 = coords[i*3 + coeff]
        vec1, vec2, vec3 = vectors(coord1, coord2, coord3, coord4)
        angle = torsion(vec1, vec2, vec3)
        angles.append(angle)
        coord1 = coord4
    return angles


def filteredAngles(angles, names, name):
    """ Filters torsion angles by amino acid. """
    angleNames = zip(names, angles)
    newAngleNames = filter(lambda p: p[0] == name, angleNames)
    newAngles = map(lambda p: p[1], newAngleNames)
    return list(newAngles)
