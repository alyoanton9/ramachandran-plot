import matplotlib.pyplot as plt


def buildPlot(xs, ys, marker):
    """ If marker == 'ALL',
        builds Ramachandran plot for the whole protein,
        otherwise
        builds Ramachandran plot for the exact amino acid. """
    axes = plt.gca()
    axes.set_title(marker)
    axes.set_xlim([-180, 180])
    axes.set_ylim([-180, 180])
    plt.xlabel('phi')
    plt.ylabel('psi')

    if len(xs) < len(ys):
        # acid is 1st in sequence, 1st phi is not calculated
        ys = ys[1:]
    elif len(xs) > len(ys):
        # acid is last in sequence, last psi is not calculated
        xs = xs[:-1]

    plt.plot(xs, ys, 'go', markersize=1.5)
    plt.axvline(x=0, ymin=-180, ymax=180, color='black', linewidth=0.7)
    plt.axhline(y=0, xmin=-180, xmax=180, color='black', linewidth=0.7)
    plt.show()
