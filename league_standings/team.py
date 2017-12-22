from pprint import pprint

class Team():
	""" This class will store the parsed XML data from Yahoo API for each team in the league.
	The intention is then to write to the database stored in each Team class instantiation
		
	Attributes:

		stats: a dictionary of dictionaries. Outer dictionary corresponds to the week and then the innter dictionary will contain all
			of the stat types e.g stats['1']['FG%'] returns the FG% value for week 1.
			We cannot do a list of dictionaries and use each index to correspond to the week number
			Because in the future I wont be parsing values from week 1. I can start from week 5,10,12 etc.

	"""

	def __init__(self, team_id):
		self.id = team_id
		self.name = None
		self.stats = {}


	def print_stats(self):
		print("Team Name: {}\nTeam ID: {}\n".format(self.name,self.id))
		pprint(self.stats)


def main():
	pass

if __name__ == "__main__":
	main()