import arcpy
import os

gdb_path = r"D:\MSC\sem_3\ProgGIS#3\P2_Describing_Data\Practical_2_ProProject\02_Describing_Data.gdb"
fc_name_list = ["MajorAttractions", "Freeways"]

for fc in fc_name_list:
    fc_path = os.path.join(gdb_path, fc)
    desc_obj = arcpy.Describe(fc_path)

    # The type of geometrey are Point, Line, Polygon, Multipoint
    shape_type = desc_obj.shapeType
    print("The geometry type of feature class :{} is {}".format( fc, shape_type))

    fc_name = desc_obj.name


    # Type of dataset . possible values - FeatureDataset, FeatureClass, RasterDataset, Table
    dataset_type = desc_obj.datasetType
    print("The dataset type of the variable :{} is {}".format( fc, dataset_type))

    sr_obj = desc_obj.spatialReference
    print(sr_obj.name)
    print(sr_obj.type)

    field_list = desc_obj.fields
    for field in field_list:

        print("The field name is {} and the type is {}".format( field.name, field.type))


print("Process completed!!")