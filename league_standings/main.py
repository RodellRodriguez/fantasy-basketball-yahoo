from requests_oauthlib import OAuth2Session
import json

def main():
	with open('config.json') as f:
		config = json.load(f)

	client_id = config['api_keys']['client_id']
	client_secret = config['api_keys']['client_secret']
	redirect_uri = 'oob'

	yahoo_oauth_url = 'https://api.login.yahoo.com/oauth2/request_auth'
	yahoo_oauth_get_token_url = 'https://api.login.yahoo.com/oauth2/get_token'

	league_id = '160754'
	league_key = 'nba.l.' + league_id



	oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
	authorization_url, state = oauth.authorization_url(yahoo_oauth_url,
		access_type='offline',prompt='select_account')

	print("Please got to this website to get the authentication code: {}".format(authorization_url))
	auth_code = input("Type the exact code given from the website. Then press enter.")

	token = oauth.fetch_token(token_url=yahoo_oauth_get_token_url,
		code=auth_code,client_secret=client_secret)

	extra = {
		'client_id' : client_id,
		'client_secret': client_secret,
	    }

	def token_saver(token):
		oauth.token = token


	client = OAuth2Session(client_id, token=token, auto_refresh_url=yahoo_oauth_get_token_url,
		auto_refresh_kwargs=extra, token_updater=token_saver
	   )

	base_yahoo_endpoint = 'https://fantasysports.yahooapis.com/fantasy/v2/'

	r = client.get(base_yahoo_endpoint + 'game/nba/')

	stat_category = {
		'FG%': 5,
		'FT%': 8,
		'3PTM': 10,
		'PTS': 12,
		'REB': 15,
		'AST': 16,
		'ST': 17,
		'BLK': 18,
		'TO': 19,
	}
	print(r.content)
	print('Im Done!')



if __name__== "__main__":
	main()