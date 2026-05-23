from src.data_loader import load_data
from src.cleaning_data import clean_data
from pathlib import Path


def main():
    file_path = input("Enter the file path: ")
    
    data = load_data(file_path)
    
    cleaned_data = clean_data(data)
    
    print(cleaned_data.head())
    
    output_path = Path("data") / "processed" / "cleaned_data.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cleaned_data.to_csv(output_path, index=False)


if __name__ == "__main__":
    main() 
    