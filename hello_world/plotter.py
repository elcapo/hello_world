import matplotlib.pyplot as plt

def prepare(ax, xs, ys, ps, title=None, x_label=None, y_label=None):
    ax.plot(xs, ys, label='Reference', color='blue')
    ax.plot(xs, ps, label='Prediction', color='red', linestyle='dashed')
    ax.legend()
    ax.grid()
    if title != None:
        ax.set_title(title)
    if x_label != None:
        ax.set_xlabel(x_label)
    if y_label != None:
        ax.set_ylabel(y_label)    

def plot(xs, ys, ps, title=None, x_label=None, y_label=None):
    fig, ax = plt.subplots()
    prepare(ax, xs, ys, ps, title, x_label, y_label)
    plt.show()
    return fig

def multiplot(plots = []):
    fig, ax = plt.subplots(1, len(plots))
    for i, plot in enumerate(plots):
        prepare(ax[i], plot['xs'], plot['ys'], plot['ps'], plot['title'], plot['x_label'], plot['y_label'])
    plt.show()
    return fig