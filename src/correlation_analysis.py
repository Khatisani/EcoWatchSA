import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def compute_correlations(db_path: str = "data/processed/ecowatch.db"):
    """
    Computes statistical summaries and correlation matrices for environmental metrics.
    """
    print("Loading data from database for correlation analysis...")

    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT temperature_2m, precipitation, solar_radiation FROM environmental_metrics;", conn)
    conn.close()
    
    df_clean = df.dropna()
    
    print("\n--- Detailed Statistical Summary ---")
    print(df_clean.describe())
    

    corr_matrix = df_clean.corr()
    print("\n--- Correlation Matrix ---")
    print(corr_matrix)
    
    os.makedirs("data/processed/plots", exist_ok=True)
    
    plt.figure(figsize=(8, 6))
    plt.imshow(corr_matrix, cmap="coolwarm", vmin=-1, vmax=1)

    plt.colorbar(label="Correlation Coefficient")
    plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45, ha="right")
    plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)

    plt.title("EcoWatch SA: Environmental Variables Correlation Matrix")
    

    for i in range(len(corr_matrix.columns)):
        for j in range(len(corr_matrix.columns)):
            text = plt.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}",
                           ha="center", va="center", color="black" if abs(corr_matrix.iloc[i, j]) < 0.6 else "white")
                           
    plt.tight_layout()
    corr_plot_path = "data/processed/plots/correlation_matrix.png"
    plt.savefig(corr_plot_path)

    plt.close()
    
    print(f"\nSaved correlation heatmap plot to {corr_plot_path}")

if __name__ == "__main__":
    compute_correlations()