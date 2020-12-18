<?php


// User data to send using HTTP PUT method in curl
// $data = array('name'=>'New Robin User','salary'=>'62000', 'age' => '34');

// // Data should be passed as json format
// $data_json = json_encode($data);

// // API URL to update data with employee id
// $url = 'http://dummy.restapiexample.com/api/v1/update/10';

// // curl initiate
// $ch = curl_init();

// curl_setopt($ch, CURLOPT_URL, $url);

// curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json','Content-Length: ' . strlen($data_json)));

// // SET Method as a PUT
// curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');

// // Pass user data in POST command
// curl_setopt($ch, CURLOPT_POSTFIELDS,$data_json);

// curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// // Execute curl and assign returned data
// $response  = curl_exec($ch);

// // Close curl
// curl_close($ch);

// // See response if data is posted successfully or any error
// print_r ($response);

?>