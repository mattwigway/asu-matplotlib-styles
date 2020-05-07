# Create example plots for README

import numpy as np
import matplotlib.pyplot as plt
import os.path

def create_plot (style):
    # make darn sure we're using the styles from the repo, and not the styles that may be installed on the system
    plt.style.use(os.path.join(os.path.dirname(__file__), f'{style}.mplstyle'))
    plt.subplots(1, 3, figsize=(12, 4))

    # line plot
    plt.subplot(1, 3, 1)
    xs = np.arange(4)
    plt.plot(xs, [1, 2, 3.5, 6], label='Arizona State')
    plt.plot(xs, [0.5, 0.3, 0.3, 0.2], label='Arizona')
    plt.plot(xs, [2, 3, 2, 2], label='UCLA')
    plt.plot(xs, [3, 1, 3, 1], label='MIT')
    plt.plot(xs, [2, 2.5, 1, 3], label='Harvard')
    plt.plot(xs, [1, 2.2, 2.4, 1.8], label='Berkeley')
    plt.legend()

    # bar plot
    plt.subplot(1, 3, 2)
    plt.bar(xs - 0.2, [2, 5, 3, 4], label='Sun Devils', width=0.4)
    plt.bar(xs + 0.2, [1, 2, 1, 3], label='Wildcats', width=0.4)
    plt.legend()
    
    # scatter plot
    plt.subplot(1, 3, 3)
    xs = np.arange(15)
    y1 = np.random.normal(size=15) + 5
    y2 = np.random.normal(size=15) + 5

    plt.scatter(xs, y1, label='Tempe')
    plt.scatter(xs, y2, label='Polytechnic')
    plt.legend()

    plt.savefig(f'examples/{style}.png', dpi=300)

create_plot('asu-dark')

