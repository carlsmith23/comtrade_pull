from download import Download


class Query:
    def __init__(self):
        pass

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

    def series(self, config, years, countries, imp_exp, codes):
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
                        dl = Download(config, query)
                        dl.get()
