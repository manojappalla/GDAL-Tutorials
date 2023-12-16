from gdal_utilities import GDALUtilities

# TESTING
gu = GDALUtilities(path="../data/raster/fcc.tif")
print("------------------- Printing Raster Info -------------------")
gu.get_raster_info()
print("\n------------------- Printing Band As Array -------------------")
print(gu.read_image(band=1))
print("\n------------------- Reprojecting Raster -------------------") 
gu.reproject(output_path="../data/raster/fcc_3857.tif", target_crs="EPSG:3857")