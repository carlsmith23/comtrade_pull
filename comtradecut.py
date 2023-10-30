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
from downloader import Downloader

downloader = Downloader()
year = 2000
while year < 2021:
    time = datetime.datetime.now()
    year_str = str(year)
    code = 1
    while code < 10:
        code_str = str(code)
        results_df = comtradeapicall.getFinalData(
            "fb6483764ea64e49a2d1f9364c33ea82",
            typeCode="C",
            freqCode="A",
            clCode="HS",
            period="{}".format(year),
            reporterCode="156",
            cmdCode="0{}".format(code),
            flowCode="M",
            partnerCode=None,
            partner2Code=None,
            customsCode=None,
            motCode=None,
            format_output="JSON",
            aggregateBy=None,
            breakdownMode="classic",
            countOnly=None,
            includeDesc=True,
        )

        results_df.to_csv("./data/{} Imports {}.csv".format(year, code))
        tm.sleep(10)

        results_dfx = comtradeapicall.getFinalData(
            "fb6483764ea64e49a2d1f9364c33ea82",
            typeCode="C",
            freqCode="A",
            clCode="HS",
            period="{}".format(year),
            reporterCode="156",
            cmdCode="0{}".format(code),
            flowCode="X",
            partnerCode=None,
            partner2Code=None,
            customsCode=None,
            motCode=None,
            format_output="JSON",
            aggregateBy=None,
            breakdownMode="classic",
            countOnly=None,
            includeDesc=True,
        )

        results_dfx.to_csv("./data/{} Exports {}.csv".format(year, code))

        tm.sleep(10)
        code += 1
    year += 1
