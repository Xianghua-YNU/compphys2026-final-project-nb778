from physics import monte_carlo_random_walk
from analysis import (
    plot_single_trajectory,
    compute_msd,
    fit_diffusion,
    plot_msd,
    plot_distribution
)

# =========================
# 物理参数（集中定义）
# =========================
NUM_PARTICLES = 5000
NUM_STEPS = 1000
STEP_SIZE = 1.0

def main():
    # 运行模拟
    trajectories = monte_carlo_random_walk(
        num_particles=NUM_PARTICLES,
        num_steps=NUM_STEPS,
        step_size=STEP_SIZE
    )

    # 单粒子轨迹图
    plot_single_trajectory(trajectories[0])

    # MSD计算
    msd = compute_msd(trajectories)

    # 拟合扩散系数
    D = fit_diffusion(msd)

    # MSD图
    plot_msd(msd, D)

    # 最终位置分布
    plot_distribution(trajectories[:, -1])

    print(f"Estimated diffusion coefficient D = {D:.4f}")


if __name__ == "__main__":
    main()