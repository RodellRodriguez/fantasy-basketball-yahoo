from requests_oauthlib import OAuth2Session
import json

class Authenticator():
	"""	A session container that authenticates with Yahoo's api using OAuth2 standard, downloads xml data,
	and parses the xml data

	Attributes:
		client_id: Given client id key from Yahoo's API
		client_secret: Given secret key from Yahoo's API
		redirect_uri: Redirect url after user authenticates with Yahoo. Yahoo accepts a value of "oob" meaning
			out of bounds if there is no url specified
		yahoo_oauth_url: Yahoo url to being OAuth2 process
		yahoo_oauth_get_token_url: Yahoo url to get and refresh access token
		initial_session: This first session will grab the first access token and refresh token
		client: This will be the main session that will be used to grab xml data. This session will use the tokens reveived
			from the initial session and will be able to automatically refresh the tokens for the lifetime of this program
		authorization_url: Url returned that will prompt user to authorize access for the session to continue in the OAuth2 process
		state: current state of the session after the user authorizes access
		auth_code: code given to the user that is used to grant the session token to complete OAuth2 process
		token: token given by OAuth2 which contains the Access Token and Refresh Token
	"""

	def __init__(self):
		# Loading a config file that contains my 2 API keys
		with open('config.json') as f:
			config = json.load(f)
		
		self.client_id = config['api_keys']['client_id']
		self.client_secret = config['api_keys']['client_secret']
		self.redirect_uri = 'oob'
		self.yahoo_oauth_url = 'https://api.login.yahoo.com/oauth2/request_auth'
		self.yahoo_oauth_get_token_url = 'https://api.login.yahoo.com/oauth2/get_token'
		self.initial_session = None
		self.client = None
		self.authorization_url = None
		self.state = None
		self.auth_code = None
		self.token = None

		self.authenticate()

	def authenticate(self):
		self.initial_session = OAuth2Session(self.client_id, redirect_uri=self.redirect_uri)
		self.authorization_url, self.state = self.initial_session.authorization_url(self.yahoo_oauth_url, 
			access_type='offline',prompt='select_account')

		print("Please got to this website to get the authentication code: {}".format(self.authorization_url))
		self.auth_code = input("Type the exact code given from the website. Then press enter.")
		self.token = self.initial_session.fetch_token(token_url=self.yahoo_oauth_get_token_url, 
			code=self.auth_code, client_secret=self.client_secret)

		# Use token to create an automatic refresh token that refreshes every time the access token expires
		# Every request sent to the Yahoo API the session will check if the current Access Token is expire or not
		extra = {
			'client_id' : self.client_id,
			'client_secret': self.client_secret,
		}
		self.client = OAuth2Session(self.client_id, token=self.token, auto_refresh_url=self.yahoo_oauth_get_token_url, 
			auto_refresh_kwargs=extra, token_updater=self.token_saver)

	def token_saver(self, token):
		self.initial_session.token = token


def main():
	test = Authenticator()
	r = test.client.get('https://fantasysports.yahooapis.com/fantasy/v2/game/nba')
	print(r.content)

if __name__ == "__main__":
	main()