from query import Query
from menu import Menu
from state import State
from API import API
from log import Log
import random


class Downloader:
  def __init__(self):
    self.agents = []
    self.state = State()
    self.log = Log()
    self.query = Query(self)
    self.API = API(self)


  def run(self):
    Menu(self).main()