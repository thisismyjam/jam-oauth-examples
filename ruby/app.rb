require "rubygems"
require "sinatra"
require "oauth"
require "oauth/consumer"
require "pp"

APP_KEY = ''
APP_SECRET = ''
MY_HOST = '' # e.g. localhost:4567

# setup
before do
  session[:oauth] ||= {}  
  @consumer ||=OAuth::Consumer.new APP_KEY, APP_SECRET, {
    :site => 'http://www.thisismyjam.com'
  }
end

get "/" do

  # get request token
  callback_url = 'http://' + MY_HOST + '/callback'
  @request_token = @consumer.get_request_token(:oauth_callback => callback_url)

  # redirect to login screen
  redirect @request_token.authorize_url
end

get "/callback" do

  # exchange authorised request token for access token
  @request_token = OAuth::RequestToken.new(@consumer, params[:oauth_token], params[:oauth_token_secret])
  @access_token = @request_token.get_access_token :oauth_verifier => params[:oauth_verifier]

  return PP.pp(@access_token.params, '')
end
