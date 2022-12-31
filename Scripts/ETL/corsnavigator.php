<?php  

	header('Access-Control-Allow-Origin: *');
	header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
	
	print_r(file_get_contents($_POST['url']));
?>