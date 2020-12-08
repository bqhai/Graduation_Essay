<?php
$api_url = 'http://cellphonesapi.somee.com/api/API_Product/GetAllProductVersion';
$json_data = file_get_contents($api_url);
$response_data = json_decode($json_data);
$user_data = $response_data;
// $user_data = array_slice($user_data, 0, 9);
$html='<table><tr><td>Name</td><td>City</td></tr>';
foreach ($user_data as $user) {
  $html.='<tr><td>'.$user->ProductVersionID.'</td><td>'.$user->ProductVersionName.'</td></tr>';
}
$html.='</table>';
header('Content-Type:application/xls');
header('Content-Disposition:attachment;filename=report.xls');
echo $html;
?>