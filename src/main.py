from reader import makeXYZ, parseAtoms
from analyser import torsionAngles
from plotBuilder import buildPlot

filename = input("Enter pdb-filename\n")
atoms = parseAtoms(filename)

atomsXYZ = makeXYZ(atoms)

phiAngles = torsionAngles(atomsXYZ, 2)
psiAngles = torsionAngles(atomsXYZ, 0)

buildPlot(phiAngles, psiAngles, filename)
