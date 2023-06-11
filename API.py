import datetime
import comtradeapicall
import requests

class API():
    def __init__(self, downloader):
        self.downloader = downloader

    def get(self, query):
        pass


    def execute(self):
        qy = self.downloader.query.get_next()

        qydf = comtradeapicall.getFinalData(self.downloader.state.get_apikey(), typeCode=qy['typeCode'], freqCode=qy['freqCode'], clCode=qy['clCode'], period=qy['period'], reporterCode=qy['reporterCode'], cmdCode=qy['cmdCode'], flowCode=qy['flowCode'], partnerCode=qy['partnerCode'], partner2Code=qy['partner2Code'], customsCode=qy['customsCode'], motCode=qy['motCode'], maxRecords=qy['maxRecords'], format_output=qy['format_output'], aggregateBy=qy['aggregateBy'], breakdownMode=qy['breakdownMode'], countOnly=qy['countOnly'], includeDesc=qy['includeDesc'])
        qydf.to_csv('q.csv')
        self.downloader.query.mark_done((qy['num']) + 1)
        
        
    # def counter(self):
    #     count = self.downloader.state.get_count()
    #     last = self.downloader.state.get_last_call()
    #     current = datetime.now()

    #     if last call was yesterday, set to 1
    #     else increment
            