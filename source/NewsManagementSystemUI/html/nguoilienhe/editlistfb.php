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
if(($user_data->Status)==1)
{
	$kq1 = 'true';
	$kq2 = 'false';
}
else
{
	$kq1 = 'false';
	$kq2 = 'true';
}

if(($kq1)=='true')
{
	$test1 ='Đang theo dõi';
	$test2 ='Bỏ theo dõi';
}
else
{
	$test1 ='Bỏ theo dõi';
	$test2 ='Đang theo dõi';
}

if(($user_data->InBlackList)==1)
{
	$kqq1 = 'true';
	$kqq2 = 'false';
}
else
{
	$kqq1 = 'false';
	$kqq2 = 'true';
}
if(($kqq1)=='true')
{
	$test11 ='Đang theo dõi';
	$test22 ='Bỏ theo dõi';
}
else
{
	$test11 ='Bỏ theo dõi';
	$test22 ='Đang theo dõi';
}
if( empty($_POST["InBlackList"]) )
 { 
 	echo "Checkbox was left unchecked."; 
}
else
 { 
 	echo "Checkbox was checked.";
  }

  $output= '
  <form action="editfinal.php" method="post" enctype="multipart/form-data">
               <label>FacebookID</label>
               <input  type="text" readonly="true" class="form-control" id="FacebookID" name="FacebookID" value="'.$user_data->FacebookID.'" placeholder="FacebookID">
               <br />
               <label>FacebookName</label>
               <input  type="text"  class="form-control" id="FacebookName" name="FacebookName" value="'.$user_data->FacebookName.'" placeholder="FacebookID">
               <br />
               <label>Select Status</label>
               <br /> 
               
    <label class="radio-inline">
      <input type="radio" name="Status" id="Status" value="'.$kq1.'" checked>'.$test1.'
    </label>
    <label class="radio-inline">
    <input type="radio" name="Status" id="Status" value="'.$kq2.'">'.$test2.'
    </label>
			<br /> 
			<br /> 
               <label>Select InBlackList</label>
               <br /> 
                 
                 <label class="radio-inline">
      <input type="radio" name="InBlackList" id="InBlackList" value="'.$kqq1.'" checked>'.$test11.'
    </label>
    <label class="radio-inline">
    <input type="radio" name="InBlackList" id="InBlackList" value="'.$kqq2.'">'.$test22.'
    </label>
                 <br /> 
                 <br /> 
               <div class="modal-footer">
                  <button type="submit" onclick="myFunction()" class="btn btn-xs btn-primary bg-primary-800 btn-labeled"><b><i class="icon-floppy-disk"></i></b> Lưu</button>
                  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
               </div>
            </form>
 ';
echo $output;

}
?>
<!-- <h2>FacebookID:' .$user_data->FacebookID.'</h2>
<p><label>FacebookName: ' .$user_data->FacebookName.'</label></p>
  <p><label>FacebookURL: ' .$user_data->FacebookUrl.'</label></p>
  <p><label>FacebookTypeID: ' .$user_data->FacebookTypeID.'</label></p>
  <p><label>FacebookTypeName: ' .$user_data->FacebookTypeName.'</label></p>
  <p><label>Status: ' .$user_data->Status.'</label></p>
  <p><label>InBlackList: ' .$user_data->InBlackList.'</label></p>
  <select name="InBlackList" id="InBlackList" class="form-control">
                  <option selected  value="'.$kqq1.'">'.$kqq1.'</option>
                  <option  value="'.$kqq2.'">'.$kqq2.'</option>
                  
                 </select>
                 <label class="checkbox-inline">
                 <input type="checkbox" checked name="InBlackList" id="InBlackList" value="'.$kqq1.'">Theo Dõi
                 </label> -->


