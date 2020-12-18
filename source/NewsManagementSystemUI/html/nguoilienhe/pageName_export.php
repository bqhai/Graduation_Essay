<?php
if(isset($_POST["FacebookID"]))
{
	$id = $_POST["FacebookID"];
$api_url ='http://www.kltn26.somee.com/api/Home/GetWatchListItemByID/'.$id;
// Read JSON file
$json_data = file_get_contents($api_url);

// Decode JSON data into PHP array
$response_data = json_decode($json_data);

// All user data exists in 'data' object
$user_data = $response_data;
  $output= '
  <h2>FacebookID:' .$user_data->FacebookID.'</h2>
  <p><label>FacebookName: ' .$user_data->FacebookName.'</label></p>
  <p><label>FacebookURL: ' .$user_data->FacebookUrl.'</label></p>
  <p><label>FacebookTypeID: ' .$user_data->FacebookTypeID.'</label></p>
  <p><label>FacebookTypeName: ' .$user_data->FacebookTypeName.'</label></p>
  <p><label>Status: ' .$user_data->Status.'</label></p>
  <p><label>InBlackList: ' .$user_data->InBlackList.'</label></p>
  ';

	echo $output;
}
?>


