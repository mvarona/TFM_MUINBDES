<?php

	require("DotEnv.php");
	use DevCoder\DotEnv;
	(new DotEnv('.env'))->load();

	if (isset($_POST['auth_token']) && ($_POST['auth_token'] == $_ENV['READ_UPDATE_SUGGESTIONS_SECRET']) && isset($_POST['suggestions'])) {
		$f = fopen('storage/suggestions.json', 'w+');
		$suggestions = $_POST['suggestions'];
		fwrite($f, $suggestions);
		fclose($f);
		
	} else {
		header("HTTP/1.1 401 Unauthorized");
	}

?>