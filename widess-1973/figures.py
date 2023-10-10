import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray


def figure1(
    times: NDArray,
    amplitude_r1: NDArray,
    amplitude_r2: NDArray,
    amplitude_rd: NDArray,
    shift: float,
    dpi: int,
) -> None:
    """Generate Figure 1 of Widess, 1973."""
    fig, (fig_1a, fig_1b, fig_1c) = plt.subplots(3, 1, dpi=dpi)
    arrow_props = dict(facecolor="black", width=0.001, headwidth=5, headlength=5)

    # Panel a.
    fig_1a.plot(times, amplitude_r1, "black")
    fig_1a.plot(times, amplitude_r2, "black")
    fig_1a.fill_between(
        times,
        amplitude_r1,
        amplitude_r2,
        facecolor="none",
        edgecolor="black",
        hatch="|||||",
    )
    fig_1a.grid(True, "major", axis="x")
    fig_1a.set_xticks(np.arange(shift / 2, 1, 0.165) - 0.5)
    fig_1a.annotate(
        text="$R_1$",
        xy=(times[25], amplitude_r1[25]),
        xytext=(-0.35, 0.5),
        arrowprops=arrow_props,
    )
    fig_1a.annotate(
        text="$-R_2$",
        xy=(times[25], amplitude_r2[25]),
        xytext=(-0.15, -0.5),
        arrowprops=arrow_props,
    )
    # Panel b.
    fig_1b.plot(times, amplitude_rd, "black")
    fig_1b.grid(True, "major")
    fig_1b.set_xticks(np.arange(shift / 2, 1, 0.165) - 0.5)
    fig_1b.set_yticks([0])
    fig_1b.annotate(
        text="$R_d$",
        xy=(times[40], amplitude_rd[40]),
        xytext=(-0.25, -0.5),
        arrowprops=arrow_props,
    )

    # Panel c (left side)
    fig_1c.plot([-0.25, -0.25], [-0.5, 0.5], "black")
    fig_1c.plot(
        [-0.2, -0.2, -0.15, -0.15, -0.2, -0.2],
        [-0.5, -0.25, -0.25, 0.25, 0.25, 0.5],
        "black",
    )
    fig_1c.annotate(
        text="VELOCITY",
        xy=(-0.1, 1),
        xytext=(-0.35, 1),
        arrowprops=arrow_props,
        verticalalignment="center",
    )
    fig_1c.annotate(
        text="DEPTH",
        xy=(-0.3, -0.5),
        xytext=(-0.3, -0.1),
        arrowprops=arrow_props,
        horizontalalignment="center",
        rotation=90,
    )

    fig_1c.text(x=-0.21, y=0.6, s="$V_1$")
    fig_1c.text(x=-0.15, y=0.3, s="$V_2=V_b$")
    fig_1c.text(x=-0.21, y=-0.75, s="$V_3=V_1$")

    fig_1c.text(
        x=-0.225,
        y=-1,
        s="VELOCITY GRAPH",
        horizontalalignment="center",
        verticalalignment="center",
    )

    # Panel c (right side)
    fig_1c.fill_between(
        [0.1, 0.4],
        [0.25, 0.25],
        [-0.25, -0.25],
        facecolor="none",
        edgecolor="black",
        hatch="//////",
    )
    fig_1c.text(x=0.4, y=0.45, s="$V_1$", verticalalignment="center")
    fig_1c.text(
        x=0.37,
        y=0.0,
        s="$V_2=V_b$",
        verticalalignment="center",
        bbox=dict(facecolor="white", edgecolor="none", pad=0),
    )
    fig_1c.text(x=0.4, y=-0.45, s="$V_3=V_1$", verticalalignment="center")

    fig_1c.arrow(0.2, 0.45, 0.05, -0.9, head_width=0.01, head_length=0.1, fc="black")
    fig_1c.arrow(0.21, 0.25, 0.02, 0.4, head_width=0.01, head_length=0.1, fc="black")
    fig_1c.arrow(0.24, -0.25, 0.044, 0.88, head_width=0.01, head_length=0.1, fc="black")

    fig_1c.text(
        x=0.25,
        y=-1,
        s="REFLECTION RAY DIAGRAM",
        horizontalalignment="center",
        verticalalignment="center",
    )

    # Common plot formatting
    for ax in [fig_1a, fig_1b, fig_1c]:
        ax.set_xlim(-0.5, 0.5)
        ax.set_ylim(-1, 1)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.tick_params(axis="both", which="both", length=0)

        for spine in ["left", "right", "top", "bottom"]:
            ax.spines[spine].set_visible(False)
