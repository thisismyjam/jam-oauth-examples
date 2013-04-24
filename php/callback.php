<?php

session_start();

include 'config.php';

if(!isset($_GET['oauth_token']))
    die('Failed to connect');

$oauth = new OAuth(APP_KEY, APP_SECRET);
$oauth->setToken($_GET['oauth_token'], $_GET['oauth_token_secret']);

$accessToken = $oauth->getAccessToken('https://www.thisismyjam.com/oauth/access_token');

var_dump($accessToken);