import pandas as pd

def load_data(filepath):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    """
    df = pd.read_csv(filepath)
    return df

if __name__ == "__main__":
    df = load_data("data/raw/train.csv")
    print("Data Size:" ,df.shape)
    print("Data Columns:", df.columns.tolist())