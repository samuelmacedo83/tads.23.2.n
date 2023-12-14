import yfinance as yf
import pandas as pd

def download_data(ticker:str) -> pd.DataFrame:
    """ Download data from Yahoo Finance

    Args:
        ticker (str): The ticker of financial asset.

    Returns:
        pd.DataFrame: A dataframe retrieved from Yahoo Finance.
    """
    
    data = yf.download(ticker)

    return data 