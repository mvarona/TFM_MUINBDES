<?php 

	if (isset($_POST['auth_token']) && ($_POST['auth_token'] == '8DUJdMxsRxlTCa5w6egi6mY9g6NWORTUDBuS1uig') && isset($_POST['item']) && isset($_POST['user']) && isset($_POST['rating']) && (($_POST['rating'] == 1) || ($_POST['rating'] == 0))) {
		
		$lineToSearch = $_POST['item'] . "," . $_POST['user'];
		$newLine = $_POST['item'] . "," . $_POST['user'] . "," . $_POST['rating'] . "\n";
		$reading = fopen('ratings.csv', 'r');
		$writing = fopen('ratings.csv.tmp', 'w');
		$replaced = false;

		while (!feof($reading)) {
			$line = fgets($reading);
			if (stristr($line, $lineToSearch)) {
				$line = $newLine;
				$replaced = true;
			}
			fputs($writing, $line);
		}
		
		if ($replaced) {
			rename('ratings.csv.tmp', 'ratings.csv');
		} else {
			fputs($writing, $newLine);
			rename('ratings.csv.tmp', 'ratings.csv');
			unlink('ratings.csv.tmp');
		}

		fclose($reading);
		fclose($writing);

		$result = [];
		$result["status"] = "Ok";

		print_r($result);
		fclose($ratings);
	} else {
		header("HTTP/1.1 401 Unauthorized");
	}

?>