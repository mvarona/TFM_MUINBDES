<?php 

	require("DotEnv.php");
	use DevCoder\DotEnv;
	(new DotEnv('.env'))->load();

	if (isset($_POST['auth_token']) && ($_POST['auth_token'] == $_ENV['RATE_MUNICIPALITY_SECRET']) && isset($_POST['item']) && isset($_POST['user']) && isset($_POST['rating']) && (($_POST['rating'] == 1) || ($_POST['rating'] == 0))) {
		
		$lineToSearch = $_POST['item'] . "," . $_POST['user'];
		$newLine = $_POST['item'] . "," . $_POST['user'] . "," . $_POST['rating'] . "\n";
		$reading = fopen('storage/ratings.csv', 'r');
		$writing = fopen('storage/ratings.csv.tmp', 'w');
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
			rename('storage/ratings.csv.tmp', 'storage/ratings.csv');
		} else {
			fputs($writing, $newLine);
			rename('storage/ratings.csv.tmp', 'storage/ratings.csv');
			unlink('storage/ratings.csv.tmp');
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