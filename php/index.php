<?php

include 'config.php';

$oauth = new OAuth(APP_KEY, APP_SECRET);
$requestToken = $oauth->getRequestToken(
    'https://www.thisismyjam.com/oauth/request_token',
    'http://' . MY_HOST . '/callback.php');

header('Location: https://www.thisismyjam.com' . $requestToken['oauth_authorize_url'] .
       '?oauth_token=' . $requestToken['oauth_token']);
