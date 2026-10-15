import importlib.metadata
import sys


def is_installed(package_name: str) -> bool:
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False


def get_version(package_name: str) -> str:
    return importlib.metadata.version(package_name)


def print_dependency_status(package_name: str, description: str) -> None:
    if is_installed(package_name):
        version = get_version(package_name)
        print(f"[OK] {package_name} ({version}) - {description}")
    else:
        print(f"[MISSING] {package_name} - {description}")


def print_install_instructions() -> None:
    print("Missing dependencies detected.")
    print("Install with pip:")
    print("pip install -r requirements.txt")
    print("or install with Poetry:")
    print("poetry install")


def print_manager_info() -> None:
    print("\nPackage manager check:")
    if "pypoetry" in sys.prefix:
        print("Running inside a Poetry-managed virtual environment.")
        print(f"Current Python: {sys.executable}")
        print("Poetry created this venv automatically and pinned every")
        print("dependency's exact version in poetry.lock.")
    else:
        print(f"Current Python: {sys.executable}")
        print("Not a Poetry-managed environment. If installed with pip,")
        print("only the ranges in requirements.txt were enforced - no")
        print("lock file guarantees which exact versions are running.")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    install_dict = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
    }
    for key, description in install_dict.items():
        print_dependency_status(key, description)
    requires = ["pandas", "numpy", "matplotlib"]
    for require in requires:
        if not is_installed(require):
            print_install_instructions()
            return
    print_manager_info()
    print("\nAnalyzing Matrix data...")
    import numpy as np
    import pandas as pd
    rng = np.random.default_rng(seed=42)
    n = 1000
    df = pd.DataFrame(
        {"sector_id": rng.integers(1, 4, size=n),
         "signal_strength": rng.normal(50, 15, size=n)}
    )
    print(f"Processing {len(df)} data points...")
    summary = df.groupby("sector_id").mean(numeric_only=True)
    print("\nAverage readings per sector:")
    print(summary)
    print("\nGenerating visualization...")
    output_path = "matrix_analysis.png"
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        plt.figure()
        plt.bar(summary.index, summary["signal_strength"])
        plt.title("Matrix Sector Analysis")
        plt.xlabel("sector_id")
        plt.ylabel("average_signal_strength")
        plt.savefig(output_path)
        plt.close()
    except OSError as e:
        print(f"Failed to save visualization: {e}")
        return
    print("\nAnalysis complete!")
    print(f"Results saved to: {output_path}")


if __name__ == "__main__":
    main()
