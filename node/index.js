// See https://github.com/ciaranj/node-oauth
// This example gets you as far as getting a request tokemn, but you'll need to handle your own redirect/server etc
var config = require('./config');
var sys = require('sys');
var OAuth = require('oauth').OAuth;


var oa = new OAuth(
    'http://www.thisismyjam.com/oauth/request_token',
    'http://www.thisismyjam.com/oauth/access_token',
    config.APP_KEY,
    config.APP_SECRET,
    '1.0',
    'http://' + config.MY_HOST + '/callback',
    'HMAC-SHA1'
);

oa.getOAuthRequestToken(function(error, oauth_token, oauth_token_secret, results) {
    if (error) {
        console.log('error: ' + JSON.stringify(error));
    } else {
        console.log('oauth_token: ' + oauth_token);
        console.log('oauth_token_secret: ' + oauth_token_secret);
        console.log('requestoken results: ' + sys.inspect(results));
        console.log('Request token received. Now requesting access token');

        // At this point you'll want your server to point to here:
        console.log('Please go to http://www.thisismyjam.com/oauth/authorize?oauth_token=' + oauth_token);

        // Then return to this kind of function:
        // oa.getOAuthAccessToken(oauth_token, oauth_token_secret, function(error, data) {
        //     console.log(sys.inspect(data));
        // });
    }
});