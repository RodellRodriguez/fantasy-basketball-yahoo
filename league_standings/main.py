from requests_oauthlib import OAuth2Session

client_id = 'insert client id'
client_secret = 'insert secret key'
redirect_uri = 'oob'

yahoo_oauth_url = 'https://api.login.yahoo.com/oauth2/request_auth'
yahoo_oauth_get_token_url = 'https://api.login.yahoo.com/oauth2/get_token'

league_id = '160754'
league_key = '375.l.160754'



oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
authorization_url, state = oauth.authorization_url(yahoo_oauth_url,
	access_type='offline',prompt='select_account')

