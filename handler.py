import numpy as np
import pandas as pd
from scipy import stats
import plotly
import matplotlib

class math_functions:
        
        def __init__(self, integer1: int, integer2: int, file_path: str) -> None:
                self.integer1 = integer1
                self.integer2 = integer2
                self.file_path = file_path
        
        def clean_data(self) -> pd.DataFrame:
                threshold = 2

                df = pd.read_csv(self.file_path)

                # Remove rows with all zeros
                data_without_zeros = df[~(df == 0).any(axis=1)]

                cleaned_dataframes = pd.DataFrame()

                # Iterate through each column to remove outliers
                for column in data_without_zeros.columns:
                        z_score = stats.zscore(data_without_zeros[column])
                        outlier_removed = data_without_zeros[abs(z_score) < threshold]
                        cleaned_dataframes.append(outlier_removed)

                cleaned_dataframe = pd.concat(cleaned_dataframes, ignore_index=True)

                return cleaned_dataframe


