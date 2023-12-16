import sys

from osgeo import gdal, osr


class GDAL:
    def __init__(self, path):
        self.path = path
        self.dataset = gdal.Open(path)

    def get_raster_info(self):
        dataset = gdal.Open(self.path, gdal.GA_ReadOnly)
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

    def read_image(self, band: int = None):
        dataset = gdal.Open(self.path, gdal.GA_ReadOnly)
        band = dataset.GetRasterBand(band)
        data = band.ReadAsArray()
        dataset = None
        return data
    
    def reproject(
    self, output_path: str = None, target_crs: str = None  # EPSG:4326
    ):
        input_dataset = gdal.Open(self.path, gdal.GA_ReadOnly)
        input_srs = input_dataset.GetProjectionRef()
        target_srs = osr.SpatialReference()
        target_srs.SetFromUserInput(target_crs)
        output_dataset = gdal.Warp(
            output_path, input_dataset, dstSRS=target_srs.ExportToWkt()
        )
        input_dataset = None
        output_dataset = None
    