# core import 
import os

# third party
import pandas as pd
import geopandas as gpd

# modules
import class_test


# current working directory
CWD = os.getcwd()
CENTROID_YEAR = "2011"
LA_YEAR = "2020"

# output area paths
oa_path = os.path.join(CWD,"data","pop_weighted_centroids",
                        CENTROID_YEAR)

# output area dataframe
oa_geo = gpd.read_file(oa_path)

example = class_test.Population_Objects(oa_geo)
example.unique_output_areas()

# pop estimates for OA output path
pop_path = os.path.join(CWD,"data","population_estimates",
                        f"whole_nation_{LA_YEAR}.feather" )

# population estimates
population = pd.read_feather(pop_path)

# oa to la lookup
oa_la_lookup_path = os.path.join("data", "oa_la_mapping", LA_YEAR, 
"Output_Area_to_Lower_Layer_Super_Output_Area_to_Middle_Layer_Super_Output_Area_to_Local_Authority_District__December_2020__Lookup_in_England_and_Wales.csv")

oa_la_lookup = pd.read_csv(oa_la_lookup_path)
print(oa_la_lookup)

# merge together
oa_centroids_and_pop = oa_geo.merge(population,on="OA11CD")


# read in potential data

# package up









