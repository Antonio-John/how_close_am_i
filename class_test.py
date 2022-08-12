class Population_Objects():

    # constructor 
    def __init__(self,dataframe):
        self.dataframe=dataframe

    # unique_output_areas method   
    def unique_output_areas(self):
        oa_col = self.dataframe["OA11CD"]
        unique_oa = oa_col.unique()
        return unique_oa


