# typeCode='C',           #Type of trade: C for commodities and S for service
# freqCode='A',           #Trade frequency: A for annual and M for monthly
# clCode='BEC',           #Trade (IMTS) classifications: HS, SITC, BEC or EBOPS.
# period='202205',        #Year or month. Year should be 4 digit year. Month should be six digit integer with the values of the form YYYYMM
# reporterCode='36',      #Reporter code (Possible values are M49 code of the countries separated by comma (,))
# cmdCode='91',           #Commodity code. Multi value input should be in the form of csv (Codes separated by comma (,))
# flowCode='M',           #Trade flow code. Multi value input should be in the form of csv (Codes separated by comma (,))
# partnerCode=None,       #Partner code (Possible values are M49 code of the countries separated by comma (,))
# partner2Code=None,      #Second partner/consignment code (Possible values are M49 code of the countries separated by comma (,))
# customsCode=None,       #Customs code. Multi value input should be in the form of csv (Codes separated by comma (,))
# motCode=None,           #Mode of transport code. Multi value input should be in the form of csv (Codes separated by comma (,))
# maxRecords=500,         #
# format_output='JSON',   #
# aggregateBy=None,       #Add parameters in csv list on which you want the results to be aggregated
# breakdownMode='classic',#Mode to choose from
# countOnly=None,         #
# includeDesc=True        #

import comtradeapicall
import requests
import datetime
import time as tm


class Download:
    def __init__(self, qy):
        self.qy = qy

    def get(self):
        self.year = self.qy["starting_year"]
        while self.year < self.qy["ending_year"]:
            time = datetime.datetime.now()
            code = 1
            while code < 10:
                code_str = str(code)

                results_df = comtradeapicall.getFinalData(
                    self.qy["api_key"],
                    typeCode=self.qy["type_code"],
                    freqCode=self.qy["freq_code"],
                    clCode=self.qy["cl_code"],
                    period="{}".format(self.year),
                    reporterCode=self.qy["reporter_country"],
                    cmdCode="0{}".format(code),
                    flowCode=self.qy["flow_direction"],
                    partnerCode=self.qy["partner_country"],
                    partner2Code=self.qy["second_partner_country"],
                    customsCode=None,
                    motCode=None,
                    format_output="JSON",
                    aggregateBy=None,
                    breakdownMode="classic",
                    countOnly=None,
                    includeDesc=True,
                )

                results_df.to_csv(
                    "./data/{} Imports TEST {}.csv".format(self.year, code)
                )
                tm.sleep(10)

                code += 1
            year += 1
