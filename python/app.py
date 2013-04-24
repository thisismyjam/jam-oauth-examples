import oauth2 as oauth
import web
import urlparse
import urllib

APP_KEY = ''
APP_SECRET = ''
MY_HOST = '' # e.g. localhost:8080

urls = (
    '/', 'Index',
    '/callback', 'Callback',
    '/make_api_call', 'MakeApiCall',
    )


app = web.application(urls, globals())

class Index:
    def GET(self):

        # setup
        consumer = oauth.Consumer(APP_KEY, APP_SECRET)
        client = oauth.Client(consumer)

        # get request token
        request_token_url = 'http://www.thisismyjam.com/oauth/request_token'
        response, content = client.request(request_token_url)
        request_token = dict(urlparse.parse_qsl(content))

        # redirect to login screen
        callback_url = 'http://%s/callback' % MY_HOST
        redirect_url = 'http://www.thisismyjam.com/oauth/authorize?oauth_token=%s&oauth_callback=%s' % (
            request_token['oauth_token'], urllib.quote_plus(callback_url))

        return web.seeother(redirect_url)

class Callback:
    def GET(self):

        if 'oauth_token' not in web.input():
            return 'Failed to authorise app'

        # setup
        consumer = oauth.Consumer(APP_KEY, APP_SECRET)
        token = oauth.Token(web.input()['oauth_token'], web.input()['oauth_token_secret'])
        token.set_verifier(web.input()['oauth_verifier'])
        client = oauth.Client(consumer, token)

        # exchange request token for access token
        access_token_url = 'http://www.thisismyjam.com/oauth/access_token'
        response, content = client.request(access_token_url, 'POST')
        access_token = dict(urlparse.parse_qsl(content))

        # in a real app you would probably store the access token in db here

        return access_token

if __name__ == '__main__':
    app.run()
