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


    def importq(self, filename):
        ql = self.read_excel(filename)
        print(ql)
        with open(self.ql_filename, 'wb') as f:
            feather.write_feather(ql, f)
            f.close()
    

    def get_next(self):
        with open(self.ql_filename, 'rb') as f:
            ql = feather.read_feather(f)
            f.close()
            next_row = ql['done'].idxmin() 
            query_df = ql.iloc[[next_row]]

            query_df = query_df.fillna(np.nan).replace([np.nan], [None])

            query = query_df.to_dict(orient='index')
            query = query[next_row]

            print(query)
            return query
        
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

    

        
    




    






