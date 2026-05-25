from src.data_loader import load_data
from src.cleaning_data import clean_data
from src.feature_engineering import hotel_fe, flight_fe, rating_fe
from pathlib import Path


def main():

    dataset_type = input("Enter dataset type (hotel / flight / rating): ").strip().lower()
    file_path = input("Enter the file path: ").strip()

    data = load_data(file_path)
    data = clean_data(data)

    if dataset_type == "hotel":
        data = hotel_fe(data)

    elif dataset_type == "flight":
        data = flight_fe(data)

    elif dataset_type == "rating":
        data = rating_fe(data)

    else:
        print("Unknown dataset type")
        return

    output_path = Path("data") / "processed" / f"{dataset_type}_processed.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    data.to_csv(output_path, index=False)
    print("Saved:", output_path)


if __name__ == "__main__":
    main()