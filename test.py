from handler import plot_functions
import pandas as pd

plotFunc = plot_functions(file_path1="data/aerodata.csv",file_path2="data/aerodata2.csv")

print(plotFunc.compare_min_max_mean())