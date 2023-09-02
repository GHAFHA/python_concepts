import numpy as np
import pandas as pd
from scipy import stats
import plotly.express as px
import matplotlib
from typing import Final

# if self.data.loc[i, "Raw Downforce Mean"] == 0: then self.data.drop(i, inplace=True)

class math_functions:
        
        def __init__(self, file_path: str) -> None:
                self.HEAVE_MIN: Final = -1.0
                self.HEAVE_MAX: Final = 1.0
                self.file_path = file_path
                self.CHASSIS_ANGLE_MIN: Final = -1.8131
                self.CHASSIS_ANGLE_MAX: Final = 0.8076
                self.folder = "2024V3\\"
                self.aeromap_df = pd.DataFrame(pd.read_csv(self.file_path, delimiter=','))

        
        def clean_data(self) -> pd.DataFrame:
                threshold = 2
                df = pd.read_csv(self.file_path) #converting a file into a dataframe

                for column in df.columns:
                        df.loc[df[column] == 0, column] = pd.NA

                df.dropna(inplace=True)

                return df
        
        def calculate_ride_height_combinations(self) -> int:
                ride_height_combinations = pd.DataFrame(columns=["Chassis Heave", "Chassis Angle", "Front Ride Height", "Rear Ride Height"])
                num_heaves = 36
                num_angles = 36
                heave_increment = (self.HEAVE_MAX + abs(self.HEAVE_MIN)) / (num_heaves - 1)
                angle_increment = (self.CHASSIS_ANGLE_MAX + abs(self.CHASSIS_ANGLE_MIN)) / (num_angles - 1)
                iteration = 0
                for i in range(0, 1):
                        for j in range(0, num_angles):
                                #chassis_heave = np.round(self.HEAVE_MIN + (i * heave_increment), 5)
                                chassis_heave = np.round(-0.1429, 5)
                                chassis_angle = np.round(self.CHASSIS_ANGLE_MIN + (j * angle_increment), 5)
                                front_ride_height = 4.88 + (chassis_heave - 49.50) * np.sin(chassis_angle * (np.pi / 180))
                                read_ride_height = 5.55 + (chassis_heave + 46.04) * np.sin(chassis_angle * (np.pi / 180))
                                ride_height_combinations.loc[iteration, "Chassis Heave"] = chassis_heave
                                ride_height_combinations.loc[iteration, "Chassis Angle"] = chassis_angle
                                ride_height_combinations.loc[iteration, "Front Ride Height"] = front_ride_height
                                ride_height_combinations.loc[iteration, "Rear Ride Height"] = read_ride_height
                                iteration += 1
                # print(ride_height_combinations)
                fig = px.scatter(ride_height_combinations, x="Front Ride Height", y="Rear Ride Height")
                fig.show()
                ride_height_combinations.to_csv("Ride_Heights.csv", index=False)

                return front_ride_height, read_ride_height



                
