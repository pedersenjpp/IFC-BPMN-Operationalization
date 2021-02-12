import ifcopenshell
import os
import time

"""Path to IFC file"""
timeStart = time.perf_counter()

FindFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model/Duplex_A_20110907_optimized.ifc")
model = ifcopenshell.open(FindFile)
print("\nIt took {} second to load Model\n".format(time.perf_counter()-timeStart))

wall = model.by_type("IfcWall")[0]

for wall in model.by_type("IfcWall"):
    for relDefinesByProperties in wall.IsDefinedBy:    
        for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
            if prop.Name == 'Area':
                print("{} - {} - {}\n".format(wall.Name, prop.Name, prop.NominalValue.wrappedValue))