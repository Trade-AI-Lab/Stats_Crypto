import sys, os

absolute_path = os.path.abspath(__file__)[
    : os.path.abspath(__file__).find("Stats_Crypto") + len("Stats_Crypto")
]
sys.path.append(absolute_path)
from src.utils.utils_df import open_dataframe, filter_dataframe_by_date_range

PATH = r"data\ETHUSDT-1m-without-aggr.zip"
df = filter_dataframe_by_date_range(
    open_dataframe(PATH=PATH).drop("unnamed: 0", axis=1),
    begin_date="2023-04-03",
    end_date="2023-05-06",
)

print(df.head())
