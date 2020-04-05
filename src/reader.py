def cutMiddle(x):
    """ Extracts atom's and amino acid's names
        and coordinates.
        Cutting indexes depends on data's
        4th and second-to-last columns.
        Ex: N MET 36.886 53.177 21.887 """
    if len(x) == 10:
        return x[2:4] + x[5:-2]
    elif len(x) == 11:
        return x[2:4] + x[5:-3]
    elif len(x) == 12:
        return x[2:4] + x[6:-3]


def filterCN(input):
    """ Filters atoms to calculate torsions.
        N, CA, C in most cases and
        N, CA, CB sometimes. """
    filtered = []
    for i in range(len(input)):
        if input[i][0] == 'N' or input[i][0] == 'CA' or input[i][0] == 'C':
            filtered.append(input[i])
        elif input[i][0] == 'CB' and filtered[-1][0] == 'CA':
            filtered.append(input[i])
    return filtered


def parseAtoms(filename):
    """ Extracts useful info from pdb file. """
    with open('../input/' + filename + '.pdb') as f:
        input = f.readlines()
    input = [s.split() for s in input]
    input = filter(lambda x: x[0] == 'ATOM', input)
    input = [cutMiddle(s) for s in input]
    atoms = filterCN(input)
    return atoms


def makeXYZ(atoms):
    """ Converts atom's info to float coordinates (x, y, z). """
    coords = [a[2:] for a in atoms]
    coords = [list(map(float, c)) for c in coords]
    return coords


def acidSequence(atoms):
    """ Makes acid sequence of protein. """
    acids = []
    for i in range(0, len(atoms), 3):
        acids.append(atoms[i][1])
    return acids
