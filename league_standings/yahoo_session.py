from authentication import Authenticator
from downloader import Downloader
from parser import Parser 
from team import Team


class YahooSession():
	"""	A session container that encapsulates: authenticating with Yahoo's API using OAuth2 standard, downloading xml data with Yahoo's API,
	and parsing the xml data

	Attributes:
		num_of_teams: Number of teams competing in the league
		oauth: An Authenticator object that authenticates this program with Yahoo's API and contains the token and session necessary to use Yahoo's API indefinitely
		client: A session object that points to oauth's session object bult from the authentication module. This variable is used just to reference oauth's session object easier for the user
		league_id: Your Yahoo Fantasy league id. Can find the value through looking at the last digits of the URL of your Yahoo Fantasy league
		league_key: The format of a league key is: {sport abbreviation}.{l}.{league_id}
	"""

	def __init__(self, num_of_teams):
		# Immediately launches OAuth2 protocol
		self.num_of_teams = num_of_teams
		self.oauth = Authenticator()
		self.client = self.oauth.client
		self.league_id = '160754'
		self.league_key = 'nba.l.' + self.league_id
		self.downloader = Downloader(self.client, self.league_key)
		self.parser = Parser()

		# Each team data will be stored in the same index in the array as its id number
		self.all_teams = [None]
		for id in range(1, num_of_teams+1): 
			self.all_teams.append(Team(id))


	def get_all_team_stats(self, start_week_number, end_week_number):
		for week in range(start_week_number, end_week_number+1):
			for team_id, team in enumerate(self.all_teams[1:], 1):
				response = self.downloader.get_stats(team_id, week)
				self.parser.parse_stats(response, team, week)


def main():
	num_of_teams = 8
	test = YahooSession(num_of_teams)
	test.get_all_team_stats(1,3)
	test.all_teams[7].print_stats()
	test.all_teams[8].print_stats()

if __name__ == "__main__":
	main()
