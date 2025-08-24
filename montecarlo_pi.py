import random
import matplotlib.pyplot as plt

def monte_carlo_pi(num_samples: int = 100000) -> float:
    inside_circle = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []

    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi_estimate = 4 * inside_circle / num_samples

    # Visualization
    plt.figure(figsize=(5, 5))
    plt.scatter(x_inside, y_inside, color="blue", s=1)
    plt.scatter(x_outside, y_outside, color="red", s=1)
    plt.title(f"Monte Carlo Simulation (π ≈ {pi_estimate:.5f})")
    plt.savefig("montecarlo_result.png")
    plt.show()

    return pi_estimate

if __name__ == "__main__":
    estimate = monte_carlo_pi(10000)
    print(f"Estimated value of π: {estimate}")
