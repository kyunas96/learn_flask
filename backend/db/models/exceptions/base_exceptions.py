class InvalidFilterParameters(Exception):
  def __init__(self, message):
    self.message = message
  def __str__(self):
    if len(self.message) == 1:
      return f"{self.__class__}: {self.message}"
    else:
      return f"{self.__class__}: {','.join(self.message)}"