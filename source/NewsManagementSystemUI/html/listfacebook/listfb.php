<?php
// $FacebookID = $_POST['FacebookID'];
$FacebookName = $_POST['FacebookName'];
$FacebookUrl = $_POST['FacebookUrl'];
$FacebookTypeID = $_POST['FacebookTypeID'];
$link = $FacebookUrl;
$string = chop($link,'/');
$last_Word_start = strrpos($string, '/') + 1;
$last_Word = substr($string, $last_Word_start);
$FacebookID = $last_Word;

$url = 'http://www.kltn26.somee.com/api/Home/CheckExistInWatchList/'.$FacebookID;

// curl initiate
$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $url);

// SET Method as a POST

// Pass user data in POST command
curl_setopt($ch, CURLOPT_RETURNTRANSFER,true);
// print_r (curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Execute curl and assign returned data
$response  = curl_exec($ch);

// Close curl
curl_close($ch);

// See response if data is posted successfully or any error
// print_r ($response);
if($response=='true'){
	 echo "<script>alert('Đã tồn tại URL này'); 
	 window.location = './index.php';</script>";
	
}else{
  $data = array('FacebookID'=>"${FacebookID}",'FacebookUrl'=>"${FacebookUrl}", 'FacebookName' =>"${FacebookName}",'FacebookTypeID' =>"${FacebookTypeID}");

// Data should be passed as json format
$data_json = json_encode($data);

// API URL to send data
$url = 'http://www.kltn26.somee.com/api/Home/AddToWatchList';

// curl initiate
$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $url);

curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));

// SET Method as a POST
curl_setopt($ch, CURLOPT_POST, 1);

// Pass user data in POST command
curl_setopt($ch, CURLOPT_POSTFIELDS,$data_json);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Execute curl and assign returned data
$response  = curl_exec($ch);

// Close curl
curl_close($ch);

// See response if data is posted successfully or any error
// print_r ($response);
echo "<script>alert('Thêm dữ liệu thành công'); 
	 window.location = './index.php';</script>";
}



?>