from authentication import Authenticator
from team_data import Team

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




def main():
	test = YahooSession()
	r = test.client.get('https://fantasysports.yahooapis.com/fantasy/v2/game/nba/')
	print(r.content)

if __name__ == "__main__":
	main()