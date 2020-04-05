from reader import makeXYZ, parseAtoms, acidSequence
from analyser import torsionAngles, filteredAngles
from plotBuilder import buildPlot

filename = input("Enter pdb-filename\n")
atoms = parseAtoms(filename)
acids = acidSequence(atoms)

atomsXYZ = makeXYZ(atoms)

phiAngles = torsionAngles(atomsXYZ, 2)
psiAngles = torsionAngles(atomsXYZ, 0)

residue = input('Usage: <3-letter amino acid code> | ALL\n').upper()

if residue == 'ALL':
    plotName = '\'' + filename + '\' protein'
    buildPlot(phiAngles, psiAngles, plotName)
elif residue in acids:
    plotName = residue + ' from ' + '\'' + filename + '\' protein'
    resPhiAngles = filteredAngles(phiAngles, acids[1:], residue)
    resPsiAngles = filteredAngles(psiAngles, acids[:-1], residue)
    buildPlot(resPhiAngles, resPsiAngles, plotName)
else:
    print('No such acid in ' + filename)
