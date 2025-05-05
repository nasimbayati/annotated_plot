# annotated_plot.py
import numpy as np
import matplotlib.pyplot as plt

class AnnotatedPlot:
    """
    Creates a multi-line plot with formatting, annotations, axis settings,
    and tick mark control to demonstrate publication-style line charts.
    """

    @staticmethod
    def draw():
        x = np.linspace(0.1, 10, 200)
        y1 = np.sinc(x / np.pi) * 20
        y2 = np.log(x + 1) * 10
        y3 = np.cos(x) / x * 30

        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor('#f7f7f7')

        ax.plot(x, y1, linestyle='-', marker='o', markevery=20, color='indianred', label='Sinc Function')
        ax.plot(x, y2, linestyle='--', marker='^', markevery=25, color='steelblue', label='Log Function')
        ax.plot(x, y3, linestyle='-.', marker='s', markevery=30, color='seagreen', label='Cosine / x')

        ax.set_title("Annotated Multi-Line Plot", fontsize=15)
        ax.set_xlabel("X Values")
        ax.set_ylabel("Y Output")

        ax.legend(loc='upper right')
        ax.grid(True, linestyle=':', alpha=0.7)

        ax.set_xlim(0, 10)
        ax.set_ylim(-40, 60)

        # Annotations
        ax.annotate('Global Peak', xy=(1.5, y1[30]), xytext=(2.5, 40),
                    arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, color='maroon')

        ax.annotate('Log Growth', xy=(8, y2[160]), xytext=(6, 50),
                    arrowprops=dict(facecolor='navy', arrowstyle='fancy'), fontsize=10, color='navy')

        ax.annotate('Decay Curve', xy=(5, y3[100]), xytext=(6.5, -20),
                    arrowprops=dict(facecolor='green', arrowstyle='wedge'), fontsize=10, color='darkgreen')

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    AnnotatedPlot.draw()
