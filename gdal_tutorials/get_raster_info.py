import sys, traceback
from osgeo import gdal


def get_raster_info(path: str = None):
    try:
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
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        stk = traceback.extract_tb(exc_tb, 1)
        fname = stk[0][2]
        print(
            f"\nException: {str(e)}\nFile Name: {file_name}\nFunction Name: {fname}\nLine No: {exc_tb.tb_lineno}\n"
        )


# Test
get_raster_info("../data/raster/fcc.tif")
