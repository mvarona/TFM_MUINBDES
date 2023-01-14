<?php

	require("DotEnv.php");
	use DevCoder\DotEnv;
	(new DotEnv('.env'))->load();

	if (isset($_POST['auth_token']) && ($_POST['auth_token'] == $_ENV['GET_USER_SUGGESTIONS_SECRET'])) {
		$reading = file_get_contents('storage/suggestions.json');
		header('Content-type: application/json');		
		echo $reading;
	} else {
		header("HTTP/1.1 401 Unauthorized");
	}

?>