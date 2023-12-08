import matplotlib.pyplot as plt

def prepare(ax, xs, ys, ps, title=None):
    ax.plot(xs, ys, label='Reference', color='blue')
    ax.plot(xs, ps, label='Prediction', color='red', linestyle='dashed')
    ax.legend()
    ax.grid()
    if title != None:
        ax.set_title(title)

def plot(xs, ys, ps, title=None):
    fig, ax = plt.subplots()
    prepare(ax, xs, ys, ps, title)
    plt.show()

def multiplot(plots = []):
    fig, ax = plt.subplots(1, len(plots))
    for i, plot in enumerate(plots):
        prepare(ax[i], plot['xs'], plot['ys'], plot['ps'], plot['title'])
    plt.show()