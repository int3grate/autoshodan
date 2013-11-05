#
#  AutoShodan API Handling / Query Class
#
#  Author: Nicholas Miles
#
from config import *
from protocol import *
from shodan import WebAPI

class CachedQueries:

  cached_queries = []

  def add_query(self, protocols, query_str):  
    self.cached_queries.append((protocols, query_str))

class QueryShodan:

  protocols = []
  query_str = ''

  def __init__(self):
    self.api = WebAPI(SHODAN_API_KEY)

  def query(self, query):
    try:
      self.results = self.api.search(query)
    except Exception, e:
      print 'Error: %s' % e
      exit(1)
    self._get_protocols()
    self.query_str = query

  def _get_protocols(self):
    for result in self.results['ports']:
      self.protocols.append(Protocol(result))      



qs = QueryShodan()
qs.query('SCALANCE')

for entry in qs.protocols:
  entry.display()
  print ''
