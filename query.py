from download import Download
from config import Config


class Query:
    def __init__(self):
        self.config = Config()
        
    def test(self):
        years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020] 
        countries = self.config.get_countries()
        imp_exp = ["M"]
        codes = self.config.get_codes()
        self.series(years, countries, imp_exp, codes)    


    def single(self, config, years, countries, imp_exp, codes):
        query = {
            "type_code": "C",
            "freq_code": "A",
            "flow_direction": imp_exp[0],
            "cl_code": "HS",
            "code": codes[0],
            "year": years[0],
            "reporter_country": countries[0],
            "partner_country": None,
            "second_partner_country": None,
        }
        dl = Download(query)
        dl.get()

    def series(self, years, countries, imp_exp, codes):
        for country in countries:
            for year in years:
                for code in codes:
                    for i in imp_exp:
                        query = {
                            "type_code": "C",
                            "freq_code": "A",
                            "flow_direction": i,
                            "cl_code": "HS",
                            "code": code,
                            "year": year,
                            "reporter_country": country,
                            "partner_country": None,
                            "second_partner_country": None,
                        }
                        dl = Download(self.config, query)
                        dl.get()


query = Query()
query.test()
