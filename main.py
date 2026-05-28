from pathlib import Path

from src.data_loader import load_data
from src.cleaning_data import clean_data
from src.feature_engineering import (
    hotel_fe,
    flight_fe,
    rating_fe
)
from src.encouding import encouder
from src.split_data import split_data


def main():

    dataset_type = input(
        "Enter dataset type (hotel / flight / rating): "
    ).strip().lower()

    file_path = input(
        "Enter the file path: "
    ).strip()

    # Load data
    data = load_data(file_path)

    # Clean data
    data = clean_data(data)

    # Feature engineering
    if dataset_type == "hotel":
        data = hotel_fe(data)

    elif dataset_type == "flight":
        data = flight_fe(data)

    elif dataset_type == "rating":
        data = rating_fe(data)

    else:
        print("Unknown dataset type")
        return

    # Split data
    train_data, test_data = split_data(data)

    # Encode data
    train_data = encouder(train_data)
    test_data = encouder(test_data)

    # Create output folder
    output_dir = Path("data") / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save files
    train_data.to_csv(
        output_dir / "train_data.csv",
        index=False
    )

    test_data.to_csv(
        output_dir / "test_data.csv",
        index=False
    )

    print("Train and test data saved successfully.")


if __name__ == "__main__":
    main()