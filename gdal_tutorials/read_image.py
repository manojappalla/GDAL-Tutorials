from osgeo import gdal


def read_raster(path: str = None, band: int = None):
    dataset = gdal.Open(path, gdal.GA_ReadOnly)
    band = dataset.GetRasterBand(band)
    data = band.ReadAsArray()
    dataset = None
    return data


# Test
print(read_raster("../data/raster/fcc.tif", 3))
