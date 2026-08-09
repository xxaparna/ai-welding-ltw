from src.data_loader import (
    load_absorptivity_data,
    load_interface_temperature_data,
)
from src.model_metadata import ModelMetadata
from src.preprocess import DataPreprocessor
from src.eda import ExploratoryDataAnalysis
from src.feature_engineering import FeatureEngineer
from src.dataset_builder import DatasetBuilder
from src.model_training import ModelTrainer
from src.model_evaluation import ModelEvaluator
from src.physics_generator import PhysicsGenerator
from src.synthetic_data_generator import SyntheticDataGenerator


from src.config import (
    ABSORPTIVITY_MODEL,
    TEMPERATURE_MODEL,
)

from src.config import (
    SHOW_PLOTS,
    ABSORPTIVITY_FEATURES,
    TEMPERATURE_FEATURES,
    ABSORPTIVITY_TARGET,
    TEMPERATURE_TARGET,
)
import joblib

from src.config import (
    ABSORPTIVITY_SCALER,
    TEMPERATURE_SCALER,
)


def print_heading(title):
    print("\n")
    print("=" * 70)
    print(title)
    print("=" * 70)

def load_datasets():
    absorptivity_df = load_absorptivity_data()

    interface_df = load_interface_temperature_data()

    return absorptivity_df, interface_df

def run_preprocessing(
    absorptivity_df,
    interface_df
):

    print_heading("ABSORPTIVITY DATASET REPORT")

    DataPreprocessor(
        absorptivity_df
    ).report()

    print_heading("INTERFACE TEMPERATURE DATASET REPORT")

    DataPreprocessor(
        interface_df
    ).report()

def run_eda(
    absorptivity_df,
    interface_df
):

    print_heading("EDA : ABSORPTIVITY DATASET")

    ExploratoryDataAnalysis(
        dataframe=absorptivity_df,
        dataset_name="Absorptivity",
        show_plots=SHOW_PLOTS
    ).run()

    print_heading("EDA : INTERFACE TEMPERATURE DATASET")

    ExploratoryDataAnalysis(
        dataframe=interface_df,
        dataset_name="Interface Temperature",
        show_plots=SHOW_PLOTS
    ).run()

    print_heading("EDA COMPLETED SUCCESSFULLY")

def run_feature_engineering(
    absorptivity_df,
    interface_df
):

    print_heading("FEATURE ENGINEERING")

    absorptivity_df = FeatureEngineer(
        absorptivity_df
    ).engineer()

    interface_df = FeatureEngineer(
        interface_df
    ).engineer()

    return absorptivity_df, interface_df

def run_physics_model(
    absorptivity_df,
    interface_df
):

    print_heading("PHYSICS MODEL")

    physics = PhysicsGenerator(
        absorptivity_df,
        interface_df
    )

    physics.fit()

    return physics

def run_synthetic_generation(
    physics
):

    print_heading("SYNTHETIC DATA GENERATION")

    generator = SyntheticDataGenerator(
        physics
    )

    synthetic_df = generator.save()

    synthetic_df = FeatureEngineer(
        synthetic_df
    ).engineer()

    print_heading(
        "FEATURE ENGINEERING (SYNTHETIC DATASET)"
    )

    print(synthetic_df.head())

    return synthetic_df

def run_dataset_preparation(synthetic_df):

    print_heading("DATASET PREPARATION")

    # =====================================================
    # Absorptivity Dataset
    # =====================================================

    abs_builder = DatasetBuilder(
        dataframe=synthetic_df,
        feature_columns=ABSORPTIVITY_FEATURES,
        target_column=ABSORPTIVITY_TARGET,
    )

    (
        X_train_abs,
        X_test_abs,
        y_train_abs,
        y_test_abs,
        scaler_abs,
    ) = abs_builder.scale()

    print("\nAbsorptivity Dataset")

    print(f"Training Samples : {len(X_train_abs)}")
    print(f"Testing Samples  : {len(X_test_abs)}")
    print(f"Number of Features : {X_train_abs.shape[1]}")

    # =====================================================
    # Temperature Dataset
    # =====================================================

    temp_builder = DatasetBuilder(
        dataframe=synthetic_df,
        feature_columns=TEMPERATURE_FEATURES,
        target_column=TEMPERATURE_TARGET,
    )

    (
        X_train_temp,
        X_test_temp,
        y_train_temp,
        y_test_temp,
        scaler_temp,
    ) = temp_builder.scale()

    print("\nInterface Temperature Dataset")

    print(f"Training Samples : {len(X_train_temp)}")
    print(f"Testing Samples  : {len(X_test_temp)}")
    print(f"Number of Features : {X_train_temp.shape[1]}")

    print_heading("DATASET PREPARATION COMPLETED")

    return (
        X_train_abs,
        X_test_abs,
        y_train_abs,
        y_test_abs,
        scaler_abs,
        X_train_temp,
        X_test_temp,
        y_train_temp,
        y_test_temp,
        scaler_temp,
    )

def run_model_training(

    X_train_abs,
    X_test_abs,
    y_train_abs,
    y_test_abs,

    X_train_temp,
    X_test_temp,
    y_train_temp,
    y_test_temp

):

    print_heading("MODEL TRAINING")

    # =====================================================
    # Absorptivity Model
    # =====================================================

    trainer_abs = ModelTrainer(
        X_train_abs,
        y_train_abs,
        model_name="linear"
    )

    model_abs = trainer_abs.train()

    trainer_abs.save(
        ABSORPTIVITY_MODEL
    )

    evaluator_abs = ModelEvaluator(
        model_abs,
        X_test_abs,
        y_test_abs,
        model_name="absorptivity"
    )

    evaluator_abs.evaluate()

    # =====================================================
    # Temperature Model
    # =====================================================

    trainer_temp = ModelTrainer(
        X_train_temp,
        y_train_temp,
        model_name="linear"
    )

    model_temp = trainer_temp.train()

    trainer_temp.save(
        TEMPERATURE_MODEL
    )

    evaluator_temp = ModelEvaluator(
        model_temp,
        X_test_temp,
        y_test_temp,
        model_name="temperature"
    )

    evaluator_temp.evaluate()


def main():

    # =====================================================
    # PROJECT TITLE
    # =====================================================

    print_heading("AI DRIVEN LASER TRANSMISSION WELDING")

    # =====================================================
    # LOAD DATASETS
    # =====================================================

    absorptivity_df, interface_df = load_datasets()

    # =====================================================
    # PREPROCESSING
    # =====================================================

    run_preprocessing(
        absorptivity_df,
        interface_df
    )

    # =====================================================
    # EDA
    # =====================================================

    run_eda(
        absorptivity_df,
        interface_df
    )

    # =====================================================
    # FEATURE ENGINEERING
    # =====================================================

    absorptivity_df, interface_df = run_feature_engineering(
        absorptivity_df,
        interface_df
    )

    print("\nAbsorptivity Dataset After Feature Engineering")
    print(absorptivity_df.head())

    print("\nInterface Temperature Dataset After Feature Engineering")
    print(interface_df.head())

    # =====================================================
    # PHYSICS MODEL
    # =====================================================

    physics = run_physics_model(
        absorptivity_df,
        interface_df
    )

    # =====================================================
    # SYNTHETIC DATASET
    # =====================================================

    synthetic_df = run_synthetic_generation(
        physics
    )

    (
        X_train_abs,
        X_test_abs,
        y_train_abs,
        y_test_abs,
        scaler_abs,
        X_train_temp,
        X_test_temp,
        y_train_temp,
        y_test_temp,
        scaler_temp
    ) = run_dataset_preparation(
        synthetic_df
    )

    run_model_training(
        X_train_abs,
        X_test_abs,
        y_train_abs,
        y_test_abs,
        X_train_temp,
        X_test_temp,
        y_train_temp,
        y_test_temp
    )
    joblib.dump(
        scaler_abs,
        ABSORPTIVITY_SCALER
    )

    joblib.dump(
        scaler_temp,
        TEMPERATURE_SCALER
    )

    print("\nScalers saved successfully.")



    ModelMetadata.save(
        ABSORPTIVITY_FEATURES,
        TEMPERATURE_FEATURES
    )

    print("\nTraining Pipeline Completed Successfully.")

if __name__ == "__main__":
    main()