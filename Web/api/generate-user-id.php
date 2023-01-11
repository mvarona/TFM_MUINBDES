<?php 

	function generateRandomString($length = 30) {
		$characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
		$charactersLength = strlen($characters);
		$randomString = '';
		for ($i = 0; $i < $length; $i++) {
			$randomString .= $characters[rand(0, $charactersLength - 1)];
		}
		return $randomString;
	}

	function generateNewId() {
		$newId = generateRandomString();
		$newId = substr($newId, 0, 4) . "-" . substr($newId, 4);
		$newId = substr($newId, 0, 8) . "-" . substr($newId, 8);
		return $newId;
	}

	if (isset($_POST['auth_token']) && ($_POST['auth_token'] == '8DUJdMxsRxlTCa5w6egi6mY9g6NWORTUDBuS1uig')){
		$users = fopen("storage/users.csv","a+");
		$ids = array();
		$i = 0;
		while ($id = fgetcsv($users)[0]) {
			if ($i != 0) {
				array_push($ids, $id);
			}
			$i += 1;
		}

		$newId = generateNewId();

		while (in_array($newId, $ids)) {
			$newId = generateNewId();
		}

		$unixTimestamp = time();

		$newUser = $newId . "," . $unixTimestamp . "\n";

		fwrite($users, $newUser);
		print_r($newId);
		fclose($users);
	} else {
		header("HTTP/1.1 401 Unauthorized");
	}


?>