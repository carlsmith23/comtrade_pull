from query import Query
from menu import Menu
from state import State
from API_caller import API_Caller
from log import Log
import random


class Downloader:
  def __init__(self):
    self.agents = []
    self.state = State()
    self.log = Log()
    self.query = Query(self)
    self.API_caller = API_Caller(self)


  def run(self):
    Menu(self).main()