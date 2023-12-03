import sys, traceback
from osgeo import gdal


def read_raster(path: str = None, band: int = None):
    try:
        dataset = gdal.Open(path, gdal.GA_ReadOnly)
        band = dataset.GetRasterBand(band)
        data = band.ReadAsArray()
        dataset = None
        return data
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        stk = traceback.extract_tb(exc_tb, 1)
        fname = stk[0][2]
        print(
            f"\nException: {str(e)}\nFile Name: {file_name}\nFunction Name: {fname}\nLine No: {exc_tb.tb_lineno}\n"
        )


# Test
print(read_raster("../data/raster/fcc.tif", 3))
