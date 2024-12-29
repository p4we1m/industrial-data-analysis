import pandas as pd
import numpy as np

def generate_synthetic_data(output_file="synthetic_machine_data.csv", n_samples=10000):
    np.random.seed(42)
    timestamps = pd.date_range(start="2023-01-01", periods=n_samples, freq="H")

    data = {
        "timestamp": timestamps,
        "temperature": np.random.normal(loc=70, scale=5, size=n_samples),
        "vibration": np.random.normal(loc=0.5, scale=0.1, size=n_samples),
        "pressure": np.random.normal(loc=30, scale=2, size=n_samples),
        "failure": np.random.choice([0, 1], size=n_samples, p=[0.98, 0.02])  # 2% awarii
    }

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Synthetic data saved to {output_file}")

if __name__ == "__main__":
    generate_synthetic_data()
