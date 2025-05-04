import cdsapi

dataset = "derived-utci-historical"

request = {
    "variable": [
        "universal_thermal_climate_index",
        "mean_radiant_temperature"
    ],
    "version": "1_1",
    "product_type": "consolidated_dataset",
    "year": [
        "2014", "2015", "2016",
        "2017", "2018"
    ],
    "month": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12"
    ],
    "day": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10"
    ],
    "area": [42.15, -88.2667, 41.45, -87.5167]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()
