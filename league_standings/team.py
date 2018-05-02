from pprint import pprint

class Team():
	""" This class will store the parsed XML data from Yahoo API for each team in the league.
	The intention is then to write to the database stored in each Team class instantiation
		
	Attributes:

		stats: {
			'week_number': {
				'each stat'
			}
		}
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