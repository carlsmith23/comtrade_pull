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
    def __init__(self, config, query):
        self.query = query
        self.config = config

    def get(self):
        results_df = comtradeapicall.getFinalData(
            self.config.get_api_key(),
            typeCode=self.query["type_code"],
            freqCode=self.query["freq_code"],
            clCode=self.query["cl_code"],
            period="{}".format(self.query["year"]),
            reporterCode=self.query["reporter_country"],
            cmdCode="{}".format(self.query["code"]),
            flowCode=self.query["flow_direction"],
            partnerCode=self.query["partner_country"],
            partner2Code=self.query["second_partner_country"],
            customsCode=None,
            motCode=None,
            format_output="JSON",
            aggregateBy=None,
            breakdownMode="classic",
            countOnly=None,
            includeDesc=True,
        )

        if self.query["flow_direction"] == "M":
            direction = "Imports"

        if self.query["flow_direction"] == "X":
            direction = "Exports"

        results_df.to_csv(
            "./data/{} {} HS{} {}.csv".format(
                self.query["year"], self.query["reporter_country"], self.query["code"], direction
            )
        )
        tm.sleep(3)
