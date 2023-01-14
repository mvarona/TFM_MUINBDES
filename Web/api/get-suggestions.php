<?php 

	if (isset($_POST['auth_token']) && ($_POST['auth_token'] == 'vgV1cqgaCR44AbPSm8aC0FlEwPt4CsdSBHSrfD1b')) {
		$reading = file_get_contents('storage/suggestions.json');
		header('Content-type: application/json');		
		echo $reading;
	} else {
		header("HTTP/1.1 401 Unauthorized");
	}

?>