import json
import datetime

class State:
    def __init__(self):
        # ### Filenames ###
        self.filename = "state.json"
        self.qlfilename = "query_list"



        

        ### API Info ###
        self.apikey = None
        self.daily_limit = 250

        self.api_count = 0
        self.last_call = None

        self.test_query_status = False
        self.last_test = None

        self.query_list_status = False
        self.write()
        self.read()
        


    def write(self):
        state_dict = {
            "apikey":self.apikey, 
            "daily_limit": self.daily_limit, 
            "api_count": self.api_count, 
            "last_call": self.last_call,
            "test_query": self.test_query_status,
            "last_test": self.last_test,
            "query_list": self.query_list_status
        }
        with open(self.filename, 'w') as outfile:
            json.dump(state_dict, outfile)


    def read(self):
        with open(self.filename) as infile:
            state_dict = json.load(infile)
            infile.close()
            self.apikey = state_dict["apikey"]
            self.daily_limit = state_dict["daily_limit"]
            self.api_count = state_dict["api_count"]
            self.last_call = state_dict["last_call"]
            self.test_query_status = state_dict["test_query"]
            self.last_test = state_dict["last_test"]
            self.query_list_status = state_dict["query_list"]
            return state_dict


    def set_apikey(self, key):
        self.read()
        self.apikey = key
        self.write()

    def get_apikey(self):
        self.read()
        return self.apikey


    def set_daily_limit(self, limit):
        self.read()
        self.daily_limit = limit
        self.write()

    def get_daily_limit(self):
        self.read()
        return self.daily_limit
    

    def set_test_query(self, test):
        self.read()
        self.test_query_status = test
        self.write()

    def get_test_query_status(self):
        self.read()
        return self.test_query_status
    
    def set_last_call(self):
        self.read()
        now = datetime.datetime.today()
        self.last_call = now.strftime("%d%m%Y")
        self.write()

    def get_last_call(self):
        self.read()
        self.last_call = datetime.datetime.strptime(self.last_call, "%d%m%Y").date()
        return self.last_call


    def set_last_test(self, last):
        self.read()
        self.last_test = last
        self.write()

    def get_last_test(self):
        self.read()
        return self.last_test


    def set_query_list(self, list):
        self.read()
        self.query_list_status = list
        self.write()

    def get_query_list_status(self):
        self.read()
        return self.query_list_status
    

    def set_qlfilename(self, name):
        self.read()
        self.qlfilename = name
        self.write()

    def get_qlfilename(self):
        self.read()
        return self.qlfilename


    def set_count(self, count):
        self.read()
        self.api_count = count
        self.write()

    def get_count(self):
        self.read()
        return self.api_count

        
    # def api_count_inc(self):
    #     self.read()
    #     if self.last_call was yesterday or before:
    #         self.api_count = 1
    #         self.last_call = 
    #         return
    #     self.api_count = += 1
    #     self.last_call = 
    #     self.write()



