import datetime
import comtradeapicall
import requests

class API_Caller():
    def __init__(self, downloader):
        self.downloader = downloader

    def execute(self):
        time = datetime.datetime.now
        qy = self.downloader.query.get_next()
        print(qy)

        qydf = comtradeapicall.getFinalData(self.downloader.state.get_apikey(), typeCode=qy['typeCode'], freqCode=qy['freqCode'], clCode=qy['clCode'], period=qy['period'], reporterCode=qy['reporterCode'], cmdCode=qy['cmdCode'], flowCode=qy['flowCode'], partnerCode=qy['partnerCode'], partner2Code=qy['partner2Code'], customsCode=qy['customsCode'], motCode=qy['motCode'], maxRecords=qy['maxRecords'], format_output=qy['format_output'], aggregateBy=qy['aggregateBy'], breakdownMode=qy['breakdownMode'], countOnly=qy['countOnly'], includeDesc=qy['includeDesc'])

        qydf.to_csv('{}.csv' .format(time))

        index = qy['num'] + 1
        self.downloader.query.mark_done(index)
        self.increment_count()
        self.downloader.state.set_last_call(time)
        
        
    def increment_count(self):
        count = self.downloader.state.get_count()
        print(count)
        
        last = self.downloader.state.get_last_call()
        today = datetime.date.today()
        if last:
            if last < today:
                print("reset count")
                self.downloader.state.set_count(1)
            else:
                print("increment count")
                count += 1
                self.downloader.state.set_count(count)
        else:
            print("nothing")
            return
            