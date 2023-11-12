import sys, traceback
from osgeo import gdal, osr

def reproject(
    input_path:str=None,
    output_path:str=None,
    target_crs:str=None # EPSG:4326
):
    try:
        input_dataset = gdal.Open(input_path, gdal.GA_ReadOnly)
        input_srs = input_dataset.GetProjectionRef()
        target_srs = osr.SpatialReference()
        target_srs.SetFromUserInput(target_crs)
        output_dataset = gdal.Warp(output_path, input_dataset, dstSRS=target_srs.ExportToWkt())
        input_dataset = None
        output_dataset = None
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        stk = traceback.extract_tb(exc_tb, 1)
        fname = stk[0][2]
        print(f"\nException: {str(e)}\nFile Name: {file_name}\nFunction Name: {fname}\nLine No: {exc_tb.tb_lineno}\n")

# Test
reproject(input_path="../data/raster/fcc.tif", output_path="../data/raster/fcc_3857_new.tif", target_crs="EPSG:3857")