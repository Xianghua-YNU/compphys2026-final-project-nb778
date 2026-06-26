import numpy as np

def monte_carlo_random_walk(num_particles, num_steps, step_size):
    """
    一维无偏随机游走

    更新公式：
        x_{n+1} = x_n + a * ξ

    其中：
        ξ = +1 或 -1
        P(+1)=0.5, P(-1)=0.5
    """

    positions = np.zeros((num_particles, num_steps))

    for particle in range(num_particles):
        x = 0

        for step in range(num_steps):
            direction = np.random.choice([-1, 1])
            x += step_size * direction
            positions[particle, step] = x

    return positions