from addict import Dict


class BaseStrategy(Dict):
	name = None

	def __init__(self):
		super(BaseStrategy, self).__init__()

		# This line breaks because the class variable
		# name is the same as the instance variable name.
		self.name = self.__class__.name


class ExampleStrategy(BaseStrategy):
	name = 'EXAMPLE'


example = ExampleStrategy()
