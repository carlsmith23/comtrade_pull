from query import Query
from download import Download
from config import Config

config = Config()
query = Query()

years = [2018, 2019, 2020]
countries = ["156"]
imp_exp = ["M"]
codes = config.get_codes(0, len(config.hs4codes) - 74)
query.series(config, years, countries, imp_exp, codes)
