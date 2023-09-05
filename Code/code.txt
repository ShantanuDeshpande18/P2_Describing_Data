import arcpy
import os
# Path to the gdb

file_GDB_path = r"D:\MSC\sem_3\ProgGIS#3\P2_Describing_Data\Practical_2_ProProject\02_Describing_Data.gdb"

freeways_fc_name = "Freeways"

majorAttractions_fc_name = "MajorAttractions"
majorAttractions_fc_full_path = os.path.join(file_GDB_path, majorAttractions_fc_name)
print (majorAttractions_fc_full_path)
freeways_fc_full_path = os.path.join(file_GDB_path, freeways_fc_name)


majorAttractions_desc_obj = arcpy.Describe(majorAttractions_fc_full_path)
freeways_desc_obj = arcpy.Describe(freeways_fc_full_path)
print("The type of shape is {}".format(majorAttractions_desc_obj.shapeType))
print(freeways_desc_obj.shapeType)