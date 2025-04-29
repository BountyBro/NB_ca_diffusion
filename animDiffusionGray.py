import reflectingLat, Diffusion, initBar, applyDiffusionExtended
import matplotlib.pyplot as plt
from initBar import applyHotCold
import matplotlib.animation as animation

def diffusionSim(m, n, diff_r, t):
    bar = initBar(m, n, hotSites=[], coldSites=[])
    grids = [bar]
    
    for i in range(t):
        barExtended = reflectingLat(bar)
        
        bar = applyDiffusionExtended(diff_r, barExtended)        
        bar = applyHotCold(bar, hotSites=[], coldSites=[])

        grids.append(bar)
    
    return grids

def animDiffusionGray():
    n = 50
    m = 100
    diff_r = 0.1
    t = 100
    grids = diffusionSim(m, n, diff_r, t)

    fig, ax = plt.subplots()
    im = ax.imshow(grids[0], cmap='gray', interpolation='nearest')

    ani = animation.FuncAnimation(
        fig, lambda frame: [im.set_array(grids[frame])],
        frames=len(grids), interval=50, blit=True
    )
    plt.show()
