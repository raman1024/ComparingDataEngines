# load Libraries
import pandas as pd

# months for which we need data
months = [
    "2026-01",
    "2026-02",
    "2026-03",
    "2026-04",
    "2026-05"
]

# base url from TLC.gov website
base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{}.parquet"

# array to save dataframe of each month
dfs = []

# looping over months and appending data in dataframe array
for month in months:
    url = base_url.format(month)
    df = pd.read_parquet(url,
                         engine="pyarrow")
    dfs.append(df)

# concat all dataframes in single dataframe
df = pd.concat(
    dfs,
    ignore_index=True
)

df.to_parquet(
    "YellowTripData-2026Jan-2026May.parquet",
    engine = "pyarrow",
    index = False
)