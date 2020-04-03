def cutMiddle(x):
    """ extracts atom's and amino acid's names
        and coordinates:
        N MET 36.886 53.177 21.887"""
    return x[2:4] + x[6:-3]


def isCN(x):
    """ returns True if atom is C or Ca or N """
    return x == 'C' or \
           x == 'CA' or \
           x == 'N'


def triple(x):
    """ converts 3-sized list to triple """
    return x[0], x[1], x[2]


def parseAtoms(filename):
    """ extracts useful info from pdb file """
    with open('../input/' + filename + '.pdb') as f:
        input = f.readlines()
    input = [s.split() for s in input]
    input = filter(lambda x: x[0] == 'ATOM', input)
    input = [cutMiddle(s) for s in input]
    atoms = list(filter(lambda x: isCN(x[0]), input))
    return atoms


def makeXYZ(atoms):
    """ converts atom's info to coordinates (x, y, z) """
    coords = [a[2:] for a in atoms]
    coords = [list(map(float, c)) for c in coords]
    coords = list(filter(lambda x: len(x) == 3, coords))  # otherwise some strange atom
    coords = list(map(triple, coords))
    return coords
