<?php 

	if (isset($_POST['auth_token']) && ($_POST['auth_token'] == 'GKdaAFdQivtnEP74nxer3zsvdNrE67dJsAv2Ea0l') && isset($_POST['suggestions'])) {
		$f = fopen('storage/suggestions.json', 'w+');
		$suggestions = $_POST['suggestions'];
		fwrite($f, $suggestions);
		fclose($f);
		
	} else {
		header("HTTP/1.1 401 Unauthorized");
	}

?>