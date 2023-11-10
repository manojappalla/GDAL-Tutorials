from osgeo import gdal, osr

def reproject(
    input_path:str=None,
    output_path:str=None,
    target_crs:str=None # EPSG:4326
):
    # Open the input raster dataset
    input_dataset = gdal.Open(input_path, gdal.GA_ReadOnly)

    if input_dataset is None:
        print(f"Error: Could not open the input raster file: {input_path}")
        return

    # Get the input raster's spatial reference
    input_srs = input_dataset.GetProjectionRef()

    # Create a SpatialReference object for the target CRS
    target_srs = osr.SpatialReference()
    target_srs.SetFromUserInput(target_crs)

    # Create the output dataset
    output_dataset = gdal.Warp(output_path, input_dataset, dstSRS=target_srs.ExportToWkt())

    if output_dataset is None:
        print("Error: Reprojection failed.")
        return

    # Close datasets
    input_dataset = None
    output_dataset = None

# Test
reproject(input_path="../data/raster/fcc.tif", output_path="../data/raster/fcc_3857.tif", target_crs="EPSG:3857")