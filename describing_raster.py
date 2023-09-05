import arcpy

raster_path = r"D:\MSC\sem_3\ProgGIS#3\P2_Describing_Data\Practical_2_ProProject\RASTER_DATA\erelev"

desc_obj = arcpy.Describe(raster_path)

dataset_type = desc_obj.datasetType

print(dataset_type)

# The number of bands in raster dataset
print(desc_obj.bandCount)

# Possible values are Grid, ERDAS IMAGINE, TIFF
print(desc_obj.format)

# Raster band pixel type : value indicates signed and unsigned pixel types from 1 bit through 32 bit
print(desc_obj.pixelType)

# Usigned integer is always non-negative, But a signed integer may store negative values
