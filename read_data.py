import pygrib
grbs = pygrib.open('data_2025.grib')
for grb in grbs:
    print(grb)
    data = grb.values  # numpy array of data
    lats, lons = grb.latlons()
grbs.close()