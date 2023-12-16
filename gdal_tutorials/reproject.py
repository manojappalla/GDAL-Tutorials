from osgeo import gdal, osr


def reproject(
    input_path: str = None, output_path: str = None, target_crs: str = None  # EPSG:4326
):
    input_dataset = gdal.Open(input_path, gdal.GA_ReadOnly)
    input_srs = input_dataset.GetProjectionRef()
    target_srs = osr.SpatialReference()
    target_srs.SetFromUserInput(target_crs)
    output_dataset = gdal.Warp(
        output_path, input_dataset, dstSRS=target_srs.ExportToWkt()
    )
    input_dataset = None
    output_dataset = None


# Test
reproject(
    input_path="../data/raster/fcc.tif",
    output_path="../data/raster/fcc_3857_new.tif",
    target_crs="EPSG:3857",
)
