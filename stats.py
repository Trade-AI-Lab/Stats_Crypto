import sys, os

absolute_path = os.path.abspath(__file__)[
    : os.path.abspath(__file__).find("Stats_Crypto") + len("Stats_Crypto")
]
sys.path.append(absolute_path)
from src.utils.utils_df import open_dataframe

PATH = r"data\ETHUSDT-1m-without-aggr.zip"
df = open_dataframe(PATH=PATH).drop("unnamed: 0", axis=1)
print(df.head())
