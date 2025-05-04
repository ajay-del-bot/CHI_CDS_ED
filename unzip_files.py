import zipfile

# with zipfile.ZipFile("data/climate/era5_pressure_level_daily_2019.nc", "r") as zip_ref:
#     zip_ref.extractall("data/climate/era5_2019_unzipped")

# with zipfile.ZipFile("data/climate/era5_pressure_level_daily_2020", "r") as zip_ref:
#     zip_ref.extractall("data/climate/era5_2020_unzipped")


# with zipfile.ZipFile("data/climate/era5_pressure_level_daily_2018", "r") as zip_ref:
#     zip_ref.extractall("data/climate/era5_2018_unzipped")

with zipfile.ZipFile("data/climate/utci_mrt_variables/era5_utci_mrt_daily_2014_2018.zip", "r") as zip_ref:
    zip_ref.extractall("data/climate/utci_mrt_variables/era5_utci_mrt_daily_2014_2018_zipped")