import matplotlib.pyplot as plt
import seaborn as sns

from src.config import FIGURE_DIR


class ExploratoryDataAnalysis:

    def __init__(self, dataframe, dataset_name, show_plots=False):

        self.df = dataframe.copy()
        self.dataset_name = dataset_name.lower().replace(" ", "_")
        self.show_plots = show_plots

        sns.set_style("whitegrid")

    # =====================================================
    # Helper Function
    # =====================================================

    def save_plot(self, filename):

        plt.tight_layout()

        plt.savefig(
            FIGURE_DIR / f"{self.dataset_name}_{filename}.png",
            dpi=300,
            bbox_inches="tight"
        )

        if self.show_plots:
            plt.show()
        else:
            plt.close()

    # =====================================================
    # Correlation Heatmap
    # =====================================================

    def correlation_heatmap(self):

        numeric_df = self.df.select_dtypes(include="number")

        plt.figure(figsize=(8, 6))

        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            cmap="coolwarm",
            linewidths=0.5,
            fmt=".2f"
        )

        plt.title(f"{self.dataset_name.replace('_', ' ').title()} Correlation Heatmap")

        self.save_plot("correlation_heatmap")

    # =====================================================
    # Generic Scatter Plot
    # =====================================================

    def scatter_plot(self, x, y, title):

        if x not in self.df.columns or y not in self.df.columns:
            return

        plt.figure(figsize=(8, 6))

        sns.scatterplot(
            data=self.df,
            x=x,
            y=y,
            s=90
        )

        plt.title(title)
        plt.xlabel(x)
        plt.ylabel(y)

        self.save_plot(title.lower().replace(" ", "_"))

    # =====================================================
    # Distribution Plots
    # =====================================================

    def distributions(self):

        numeric_columns = self.df.select_dtypes(include="number").columns

        for column in numeric_columns:

            plt.figure(figsize=(7, 5))

            sns.histplot(
                self.df[column],
                kde=True,
                bins=10
            )

            plt.title(f"Distribution of {column}")

            self.save_plot(f"{column}_distribution")

    # =====================================================
    # Boxplots
    # =====================================================

    def boxplots(self):

        numeric_df = self.df.select_dtypes(include="number")

        plt.figure(figsize=(10, 5))

        sns.boxplot(data=numeric_df)

        plt.title("Boxplots")

        self.save_plot("boxplots")

    # =====================================================
    # Pair Plot
    # =====================================================

    def pair_plot(self):

        numeric_df = self.df.select_dtypes(include="number")

        pair = sns.pairplot(numeric_df)

        pair.savefig(
            FIGURE_DIR / f"{self.dataset_name}_pairplot.png",
            dpi=300
        )

        if self.show_plots:
            plt.show()
        else:
            plt.close("all")

    # =====================================================
    # Run Complete EDA
    # =====================================================

    def run(self):

        print(f"\nRunning EDA for {self.dataset_name.replace('_', ' ').title()} Dataset...")

        self.correlation_heatmap()

        self.boxplots()

        self.distributions()

        self.pair_plot()

        if "absorptivity_pct" in self.df.columns:

            self.scatter_plot(
                "P_W",
                "absorptivity_pct",
                "Power vs Absorptivity"
            )

            self.scatter_plot(
                "V_mm_min",
                "absorptivity_pct",
                "Speed vs Absorptivity"
            )

        if "interface_temp_C" in self.df.columns:

            self.scatter_plot(
                "P_W",
                "interface_temp_C",
                "Power vs Temperature"
            )

            self.scatter_plot(
                "line_energy_J_mm",
                "interface_temp_C",
                "Line Energy vs Temperature"
            )

        print("EDA Completed Successfully.")