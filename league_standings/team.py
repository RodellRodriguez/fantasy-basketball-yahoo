class Team():
	""" This class will store the parsed XML data from Yahoo API for each team in the league.
	The intention is then to write to the database stored in each Team class instantiation
		
	Attributes:

	"""

	def __init__(self, team_id):
		self.id = team_id
		self.name = None
		self.stats = {}


def main():
	pass

if __name__ == "__main__":
	main()