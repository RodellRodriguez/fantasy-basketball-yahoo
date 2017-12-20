import xml.etree.ElementTree as ET
from pprint import pprint

class Parser():
	def __init__(self):
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


	def parse_stats(self, response, team):
		pprint(response.text)
		print("Hello this team id is {}".format(team.id))

	def check_team_id(self, response):
		pass

	# MAKE SURE THE STATS ARE CONVERTED TO FLOAT OR INTS
	def update_stats(self, team):
		pass

	def create_week_entry(self, team, week):
		pass

	def update_name(self, team):
		pass

	def insert_stat(self, team):
		pass

	def parse_week_calendar(self, response):
		pass


def main():
	pass

if __name__ == "__main__":
	main()