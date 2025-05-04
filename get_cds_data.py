import cdsapi

dataset = "derived-era5-pressure-levels-daily-statistics"

years = range(2014, 2015)

for year in years:
    request = {
        "product_type": "reanalysis",
        "variable": [
            "ozone_mass_mixing_ratio",
            "relative_humidity",
            "specific_humidity",
            "temperature"
        ],
        "year": str(year),
        "month": [
            "01", "02", "03",
            "04", "05", "06",
            "07", "08", "09",
            "10", "11", "12"
        ],
        "day": [
            "01", "02", "03",
            "04", "05"
        ],
        "pressure_level": ["1000"],
        "daily_statistic": "daily_mean",
        "time_zone": "utc+00:00",
        "frequency": "6_hourly",
        "area": [42.15, -88.2667, 41.45, -87.5167]
    }

    client = cdsapi.Client()
    filename = f"era5_pressure_level_daily_{year}"
    client.retrieve(dataset, request).download(filename)
    print(f"Downloaded data for {year} to {filename}")
