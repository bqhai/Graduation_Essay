<?php
if(isset($_POST["ProductVersionID"]))
{
	$id = $_POST["ProductVersionID"];
$api_url ='http://cellphonesapi.somee.com/api/API_Product/GetProductVersionByID/'.$id;
// Read JSON file
$json_data = file_get_contents($api_url);

// Decode JSON data into PHP array
$response_data = json_decode($json_data);

// All user data exists in 'data' object
$user_data = $response_data;

// Cut long data into small & select only first 10 records
// Print data if need to debug
//print_r($user_data);

// Traverse array and display user data
  // echo "name: ".$user_data->ProductVersionID;
  // echo "name: ".$user_data->ProductVersionName;
  $output= '
  <h2>'.$user_data->ProductVersionID.'</h2>
  <p><label>'.$user_data->ProductVersionName.'</label></p>';

   echo $output;
}
?>


