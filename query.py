#Contains all the logic for handling the query list. As default, this is an xlsx file in the main folder called query.xlsx. It basically just contains one query per row, one parameter per column.


import json
import pandas as pd 
import pyarrow.feather as feather
import datetime
import numpy as np

class Query:
    def __init__(self, downloader):
        self.downloader = downloader
        self.filename = "query.xlsx"
        self.ql_filename = downloader.state.get_qlfilename()

    #def read_json(self, filename):
        #with open(filename) as json_file:
            #qy = json.load(json_file)
        #return qy
    
    
    def read_excel(self, filename):
        query_list = pd.read_excel(filename, sheet_name=0)
        return(query_list)

    #def read_csv(self, filename):
        #pd.read_csv(filename)

    #read the query list in the given format and save it as a pyarrow feather file for quick, but permanent access
    def importq(self):
        ql = self.read_excel(self.filename)
        print(ql)
        with open(self.ql_filename, 'wb') as f:
            feather.write_feather(ql, f)
            f.close()
    
    #Looks at the query list, finds the first row with 0 in 'done' column and returns the query as a dict
    def get_next(self):
        with open(self.ql_filename, 'rb') as f:
            ql = feather.read_feather(f)
            f.close()
            next_row = ql['done'].idxmin() 
            query_df = ql.iloc[[next_row]]

            query_df = query_df.fillna(np.nan).replace([np.nan], [None])

            query_df.astype('str').dtypes

            query = query_df.to_dict(orient='index')
            query = query[next_row]
            return query
        
    #Changes the 'done' column for a given row from 0 to 1    
    def mark_done(self, index):
        with open(self.ql_filename, 'rb') as f:
            ql = feather.read_feather(f)
            f.close()
            ql.at[index, 'done'] = 1
            with open(self.ql_filename, 'wb') as f:
                feather.write_feather(ql, f)
                f.close()


    # with open(ql_filename, 'wb') as f:
    #     feather.write_feather(df, f)

    # with open(ql_filename, 'rb') as f:
    #     read_df = feather.read_feather(f)

    

        
    




    






