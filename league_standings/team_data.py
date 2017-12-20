from downloader import Downloader

class Team():
	""" This class will store the parsed XML data from Yahoo API for each team in the league.
	The intention is then to write to the database stored in each Team class instantiation
		
	Attributes:

	"""

	def __init__(self, team_id):
		self.id = team_id
		self.name = None
		self.stats = [None]
		self.stats_mapping  = {
			'5':'FG%',
			'8':'FT%',
			'10':'3PTM',
			'12':'PTS',
			'15':'REB',
			'16':'AST',
			'17':'ST',
			'18':'BLK',
			'19':'TO',
		}

	def parse_stats(self, response):
		pass

	def parse_week_calendar(self, response):
		pass



def main():
	pass

if __name__ == "__main__":
	main()