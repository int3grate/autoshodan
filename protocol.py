class Protocol:
  port = 0
  count = 0
  banners = []

  def __init__(self, tuple):
    self.port = int(tuple['name'])
    self.count = int(tuple['count'])

  def add_banner(self, data):
    pass

  def display(self):
    print 'Port  : ' + str(self.port)
    print 'Count : ' + str(self.count)
