import sys

from osgeo import gdal, osr


class GDALUtilities:
    """
    This class has the following capabilities

    1. Get raster info
    2. Read image band as an array
    3. Reproject a raster
    """
    
    def __init__(self, path):
        self.path = path

    def get_raster_info(self):
        self.dataset = gdal.Open(self.path, gdal.GA_ReadOnly)
        print(
            "Driver: {}/{}\n".format(
                self.dataset.GetDriver().ShortName, self.dataset.GetDriver().LongName
            )
        )
        print(
            "Size is {} x {} x {}\n".format(
                self.dataset.RasterXSize, self.dataset.RasterYSize, self.dataset.RasterCount
            )
        )
        print("Projection is {}\n".format(self.dataset.GetProjection()))
        geotransform = self.dataset.GetGeoTransform()
        if geotransform:
            print("Origin = ({}, {})\n".format(geotransform[0], geotransform[3]))
            print("Pixel Size = ({}, {})\n".format(geotransform[1], geotransform[5]))
        band_count = self.dataset.RasterCount
        for i in range(1, band_count + 1):
            band = self.dataset.GetRasterBand(i)
            band_name = band.GetDescription()
            if band_name:
                print(f"Band {i} Name: {band_name}")
            else:
                print(f"Band {i} has no name.")
        dataset = None

    def read_image(self, band: int = None):
        self.dataset = gdal.Open(self.path, gdal.GA_ReadOnly)
        band = self.dataset.GetRasterBand(band)
        data = band.ReadAsArray()
        self.dataset = None
        return data
    
    def reproject(
    self, output_path: str = None, target_crs: str = None  # EPSG:4326
    ):
        self.dataset = gdal.Open(self.path, gdal.GA_ReadOnly)
        input_dataset = self.dataset
        input_srs = input_dataset.GetProjectionRef()
        target_srs = osr.SpatialReference()
        target_srs.SetFromUserInput(target_crs)
        output_dataset = gdal.Warp(
            output_path, input_dataset, dstSRS=target_srs.ExportToWkt()
        )
        input_dataset = None
        output_dataset = None