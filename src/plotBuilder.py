import matplotlib.pyplot as plt


def buildPlot(xs, ys, residue):
    axes = plt.gca()
    axes.set_title('Ramachandran plot for `' + residue + '` residue')
    axes.set_xlim([-180, 180])
    axes.set_ylim([-180, 180])
    plt.xlabel('phi')
    plt.ylabel('psi')
    plt.plot(xs, ys, 'go', markersize=2)
    plt.axvline(x=0, ymin=-180, ymax=180, color='black', linewidth=0.7)
    plt.axhline(y=0, xmin=-180, xmax=180, color='black', linewidth=0.7)
    plt.show()
