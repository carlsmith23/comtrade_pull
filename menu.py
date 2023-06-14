class Menu():
    def __init__(self, downloader):
        self.downloader = downloader


    def info(self):
        apikey = self.downloader.state.get_apikey()
        count = self.downloader.state.get_count()
        test = self.downloader.state.get_test_query_status()
        lasttest = self.downloader.state.get_last_test()
        qlist = self.downloader.state.get_query_list_status()
        lastq = self.downloader.state.get_last_test()
        print("")
        print("")
        print("*************************************************************")
        print("UN Comtrade Data Query")
        print("Current API Key: {}" .format(apikey))
        print("Calls Today: {}" .format(count))
        # print("Successful Test Query: {} ({})" .format(test, lasttest))
        # print("Query List Loaded: {} ({})"  .format(qlist, lastq))
        print("")
    

    def main(self):
        run = True
        while run:
            self.info()
            print("(A)PI Key")
            print("(R)ead query list")
            print("(T)est Query")
            print("E(X)ecute query")
            print("(Q)uit")
            print("")
            prompt = input("?: ")
            if prompt == "Q" or prompt == "q":
                run = False
            elif prompt == "A" or prompt == "a":
                self.api_menu()
            elif prompt == "T" or prompt == "t":
                self.test()
            elif prompt == "R" or prompt == "r":
                self.query_menu()
            elif prompt == "X" or prompt == "x":
                self.execute()


    def api_menu(self):
        api_run = True
        while api_run:
            self.info()
            print("API KEY MENU")
            print("(D)isplay API Key")
            print("(S)et API Key")
            print("(C)lear API Key")
            print("(B)ack")
            print("")

            api_prompt = input("?: ")
            if api_prompt == "B" or api_prompt == "b":
                api_run = False

            elif api_prompt == "D" or api_prompt == "d":
                key = self.downloader.state.get_apikey()
                print(key)

            elif api_prompt == "S" or api_prompt == "s":
                key = input("Enter API Key: ")
                self.downloader.state.set_apikey(key)

            elif api_prompt == "C" or api_prompt == "c":
                self.downloader.state.set_apikey(None)

    def query_menu(self):
        query_run = True
        while query_run:
            self.info()
            print("QUERY LIST MENU")
            print("(I)mport Query List")
            print("(C)lear Imported Query List")
            print("(B)ack")
            print("")

            query_prompt = input("?: ")
            if query_prompt == "B" or query_prompt == "b":
                query_run = False
            elif query_prompt == "I" or query_prompt == "i":
                self.downloader.query.importq()
            elif query_prompt == "C" or query_prompt == "c":
                self.test()


    def test(self):
            test_run = 1
            while test_run:
                self.info()
                print("TEST QUERY MENU")
                print("(S)end test query*")
                print("(C)lear API count")
                print("(B)ack")
                print("")
                test_prompt = input("?: ")
                if test_prompt == "B" or test_prompt == "b":
                    test_run = False
                elif test_prompt == "S" or test_prompt == "s":
                    test_run = False
                elif test_prompt == "C" or test_prompt == "c":
                    self.downloader.state.reset_count()
                    





    def execute(self):
        ex_run = 1
        while ex_run == 1:
            self.info()
            print("EXECUTE QUERY MENU")
            print("(I)nitialize feather)")
            print("Execute (N)umber of queries*")
            print("Execute (A)ll queries")
            print("(B)ack")
            print("")
            prompt = input("?: ")
            if prompt == "B" or prompt == "b":
                run = False
            elif prompt == "I" or prompt == "i":
                self.downloader.state.init_feather()    
            elif prompt == "N" or prompt == "n":
                self.test()
            elif prompt == "A" or prompt == "a":
                self.downloader.API_caller.loop()

   
        
            
            
