import matplotlib.pyplot as plt
import matplotlib.animation as animation


def visualize(arr, generator, title):

    fig, ax = plt.subplots()

    bars = ax.bar(range(len(arr)), arr)

    ax.set_title(title)

    def update(new_arr):

        for rect, val in zip(bars, new_arr):
            rect.set_height(val)

    ani = animation.FuncAnimation(
        fig,
        func=update,
        frames=generator,
        interval=100,
        repeat=False
    )

    plt.show()