import numpy as np
import matplotlib.pyplot as plt

def plot_single_trajectory(trajectory):
    plt.figure(figsize=(8, 4))
    plt.plot(trajectory)
    plt.xlabel("Time Step")
    plt.ylabel("Position")
    plt.title("Single Particle Random Walk")
    plt.grid()
    plt.show()


def compute_msd(trajectories):
    """
    MSD:
        <x²(t)> = (1/N) Σ x_i²
    """
    return np.mean(trajectories ** 2, axis=0)


def fit_diffusion(msd):
    """
    理论关系：
        <x²> = 2Dt

    线性拟合：
        slope = 2D
    """
    t = np.arange(len(msd))
    slope, intercept = np.polyfit(t, msd, 1)
    D = slope / 2
    return D


def plot_msd(msd, D):
    t = np.arange(len(msd))
    theory = 2 * D * t

    plt.figure(figsize=(8, 4))
    plt.plot(t, msd, label="Simulation")
    plt.plot(t, theory, '--', label="Linear Fit")
    plt.xlabel("Time")
    plt.ylabel("MSD")
    plt.title("Mean Square Displacement")
    plt.legend()
    plt.grid()
    plt.show()


def plot_distribution(final_positions):
    plt.figure(figsize=(8, 4))
    plt.hist(final_positions, bins=50, density=True)
    plt.xlabel("Position")
    plt.ylabel("Probability Density")
    plt.title("Final Position Distribution")
    plt.grid()
    plt.show()