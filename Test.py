import arcpy


arcpy.env.workspace = "D:/KURSEVI/Udemy Python for Geospatial/python/RichlandData"
arcpy.env.overwriteOutput = True
tri = "tri92.shp"
tri_layer = arcpy.MakeFeatureLayer_management(tri("tri_layer"))

schools = "schools.shp"
schools_layer = arcpy.MakeFeatureLayer_management(schools, "schools_layer")

