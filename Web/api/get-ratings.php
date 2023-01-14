<?php 

	if (isset($_POST['auth_token']) && ($_POST['auth_token'] == 'GKdaAFdQivtnEP74nxer3zsvdNrE67dJsAv2Ea0l')) {
		$reading = file_get_contents('storage/ratings.csv');
		header('Content-type: text/csv');		
		echo $reading;
	} else {
		header("HTTP/1.1 401 Unauthorized");
	}

?>