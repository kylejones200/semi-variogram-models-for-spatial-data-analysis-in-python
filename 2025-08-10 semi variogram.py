"""Generated from Jupyter notebook: 2025-08-10 semi variogram

Magics and shell lines are commented out. Run with a normal Python interpreter."""

import matplotlib.pyplot as plt
import numpy as np


def de_wijsian(h, A=0.8, B=0.2):
    h_safe = np.where(h == 0, 1e-09, h)
    return A * np.log(h_safe) + B


def exponential(h, C0=0.05, C=1.0, a=10.0):
    return C0 + C * (1 - np.exp(-h / a))


def gaussian(h, C0=0.05, C=1.0, a=10.0):
    return C0 + C * (1 - np.exp(-3 * h**2 / a**2))


def hole_effect(h, C=1.0, a=0.7):
    x = a * h
    sinc = np.where(x == 0, 1.0, np.sin(x) / x)
    return C * (1 - sinc)


def linear(h, A=0.06, B=0.0):
    return A * h + B


def log_log(h, A=0.6, B=0.1):
    return B + h**A


def plot_model(h, gamma, name, fname, ylim=None):
    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.plot(h, gamma, linewidth=2)
    style_ax(ax)
    ax.set_title(name)
    if ylim is not None:
        ax.set_ylim(*ylim)
    ax.margins(x=0)
    fig.tight_layout()
    plt.savefig(fname, dpi=200, bbox_inches="tight")
    plt.show()


def spherical(h, C0=0.05, C=1.0, a=10.0):
    y = np.empty_like(h, dtype=float)
    inside = h <= a
    x = h[inside] / a
    y[inside] = C0 + C * (1.5 * x - 0.5 * x**3)
    y[~inside] = C0 + C
    return y


def style_ax(ax, xlabel="h", ylabel="γ(h)"):
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.spines["left"].set_position(("outward", 6))
    ax.spines["bottom"].set_position(("outward", 6))
    ax.tick_params(axis="both", which="both", direction="out")
    ax.margins(x=0)
    return ax


def minimalist_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "serif",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": False,
        }
    )
    if __name__ == "__main__":
        h_ns = np.linspace(0.001, 30, 600)
        plot_model(
            h_ns,
            de_wijsian(h_ns, A=0.8, B=0.2),
            "De Wijsian",
            "semivariogram_de_wijsian.png",
        )
        plot_model(
            h_ns, linear(h_ns, A=0.06, B=0.0), "Linear", "semivariogram_linear.png"
        )
        plot_model(
            h_ns, log_log(h_ns, A=0.6, B=0.1), "Log–Log", "semivariogram_loglog.png"
        )
        a = 10.0
        h_s = np.linspace(0, 3 * a, 600)
        plot_model(
            h_s,
            exponential(h_s, C0=0.05, C=1.0, a=a),
            "Exponential",
            "semivariogram_exponential.png",
            ylim=(0, 1.2),
        )
        plot_model(
            h_s,
            hole_effect(h_s, C=1.0, a=0.7),
            "Hole Effect",
            "semivariogram_hole_effect.png",
        )
        plot_model(
            h_s,
            spherical(h_s, C0=0.05, C=1.0, a=a),
            "Spherical",
            "semivariogram_spherical.png",
            ylim=(0, 1.2),
        )
        plot_model(
            h_s,
            gaussian(h_s, C0=0.05, C=1.0, a=a),
            "Gaussian",
            "semivariogram_gaussian.png",
            ylim=(0, 1.2),
        )


def minimalist_style_2() -> None:
    plt.rcParams.update(
        {
            "font.family": "serif",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": False,
        }
    )
    if __name__ == "__main__":
        a = 10.0
        h = np.linspace(0, 3 * a, 800)
        fig, ax = plt.subplots(figsize=(7.5, 4))
        ax.plot(h, de_wijsian(h), linewidth=2, label="De Wijsian")
        ax.plot(h, linear(h), linewidth=2, label="Linear")
        ax.plot(h, log_log(h), linewidth=2, label="Log–Log")
        ax.plot(h, exponential(h, a=a), linewidth=2, label="Exponential")
        ax.plot(h, hole_effect(h), linewidth=2, label="Hole Effect")
        ax.plot(h, spherical(h, a=a), linewidth=2, label="Spherical")
        ax.plot(h, gaussian(h, a=a), linewidth=2, label="Gaussian")
        style_ax(ax)
        ax.set_title("Semi-variogram Models")
        ax.set_ylim(0, 1.25)
        ax.legend(frameon=False, ncol=3, fontsize=9)
        fig.tight_layout()
        plt.savefig("semivariogram_overlay.png", dpi=220, bbox_inches="tight")
        plt.show()


def main() -> None:
    minimalist_style()
    minimalist_style_2()


if __name__ == "__main__":
    main()
