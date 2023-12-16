from osgeo import gdal


def get_raster_info(path: str = None):
    dataset = gdal.Open(path, gdal.GA_ReadOnly)
    print(
        "Driver: {}/{}\n".format(
            dataset.GetDriver().ShortName, dataset.GetDriver().LongName
        )
    )
    print(
        "Size is {} x {} x {}\n".format(
            dataset.RasterXSize, dataset.RasterYSize, dataset.RasterCount
        )
    )
    print("Projection is {}\n".format(dataset.GetProjection()))
    geotransform = dataset.GetGeoTransform()
    if geotransform:
        print("Origin = ({}, {})\n".format(geotransform[0], geotransform[3]))
        print("Pixel Size = ({}, {})\n".format(geotransform[1], geotransform[5]))
    band_count = dataset.RasterCount
    for i in range(1, band_count + 1):
        band = dataset.GetRasterBand(i)
        band_name = band.GetDescription()
        if band_name:
            print(f"Band {i} Name: {band_name}")
        else:
            print(f"Band {i} has no name.")
    dataset = None


# Test
get_raster_info("../data/raster/fcc.tif")
