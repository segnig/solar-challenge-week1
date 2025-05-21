import pandas as pd
import os

def load_data() -> pd.DataFrame:
    # Base directory: adjusts to current file's location
    base_path = os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'Data')

    # Load the CSVs with platform-independent paths
    togo_df = pd.read_csv(os.path.join(base_path, 'cleaned_togo.csv'))
    benin_df = pd.read_csv(os.path.join(base_path, 'benin_cleaned.csv'))
    sierra_df = pd.read_csv(os.path.join(base_path, 'sierra_cleaned.csv'))

    # Add country column to each
    togo_df['country'] = 'Togo' 
    benin_df['country'] = 'Benin'
    sierra_df['country'] = 'Sierra Leone'

    # Combine the DataFrames
    combined_df = pd.concat([togo_df, benin_df, sierra_df], ignore_index=True)

    return combined_df


def get_country_data(df: pd.DataFrame, country: str) -> pd.DataFrame:
    """
    Filter the DataFrame for a specific country.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to filter.
    country (str): The country to filter by.
    
    Returns:
    pd.DataFrame: The filtered DataFrame.
    """
    return df[df['country'] == country]

def get_country_list(df: pd.DataFrame) -> list:
    """
    Get a list of unique countries from the DataFrame.
    
    """
    return df['country'].unique().tolist()

def compute_summary(df: pd.DataFrame) -> pd.DataFrame:
    
    return df.groupby('country')[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"]).round(2)