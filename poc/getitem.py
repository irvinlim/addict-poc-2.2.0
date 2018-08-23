from addict import Dict


class CustomDict(Dict):
	def __init__(self, value):
		super(CustomDict, self).__init__()

		# The problem is that I do not initialize self.my as a Dict(),
		# since I previously assumed that this would work.
		self.my.custom.value = value


class CustomDict2(Dict):
	def __init__(self, value, **kwargs):
		super(CustomDict2, self).__init__()
		self.my.custom.value = value


class CustomDict3(Dict):
	def __init__(self, value=None, **kwargs):
		super(CustomDict3, self).__init__()
		self.my.custom.value = value


# Try running any of the following lines on its own
# custom_dict = CustomDict('hello world')
# custom_dict2 = CustomDict2('hello world')
# custom_dict3 = CustomDict3('hello world')


# This also breaks when I try to access a non-existent attribute
class CustomDict4(Dict):
	def __init__(self, value, **kwargs):
		super(CustomDict4, self).__init__()
		self.value = value


custom_dict4 = CustomDict4(1)
assert not custom_dict4.missing_attr

# The correct fix would be to do:
assert 'missing_attr' not in custom_dict4
