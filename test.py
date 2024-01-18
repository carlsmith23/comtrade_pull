from query import Query
from download import Download
from config import Config

config = Config()
query = Query()
#         
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020] 
countries = config.get_countries()
imp_exp = ["M"]
codes = config.get_codes()
query.series(config, years, countries, imp_exp, codes)
