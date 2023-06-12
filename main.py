
# comtrade_pull is a small script to automate querying and pulling data from UN Comtrade via the python API.

# 1. All config, query, and result data are stored as files so processes can always be resumed. I don't know if this is implemented in the best way, but it does work and I have not lost any data yet.

# 2. Queries are taken from an excel file named query.xlsx. A template is included in the main directory. Plans to also implement this in CSV or JSON in the future.

# 3. Because free accounts are limited in the number of API calls they can make a day, all calls are counted and reset at midnight UTF. If you have premium API access, lucky you. 

# 4. Run main.py, add your API key, import your query file and you should be ready to execute order 66, er, I mean your query.

# 5.Each query result is added to the main results dataframe, which is stored as a file. Each individual result is written to its own csv file (named by timestamp) for redundancy

from downloader import Downloader
import datetime
# def main():
downloader = Downloader()
#   downloader.run()


# if __name__ == "__main__":
#   main()

time = datetime.datetime.now
downloader.state.set_last_call()

for i in range(20):
  downloader.API.increment_count()