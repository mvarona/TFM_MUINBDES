<?php

	require("DotEnv.php");
	use DevCoder\DotEnv;
	(new DotEnv('.env'))->load();

	if (isset($_POST['auth_token']) && ($_POST['auth_token'] == $_ENV['READ_UPDATE_SUGGESTIONS_SECRET'])) {
		$ratings = file_get_contents('storage/ratings.csv');
		header('Content-type: text/csv');		
		echo $ratings;
	} else {
		header("HTTP/1.1 401 Unauthorized");
	}

?>