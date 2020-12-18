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
<!-- <form action="editlistfb.php" method="post" enctype="multipart/form-data">
               
               <label>FacebookName</label>
               <input  type="text"  class="form-control" id="FacebookID" name="FacebookID" value="'.$user_data->FacebookName.'" placeholder="FacebookID">
               <br />
               <label>Select Status</label>
                 <select name="Status" id="Status" class="form-control">
                            
                            <?php
                            if($user_data->Status==1){
                                ?>
                            <option selected value="1">True</option>
                            <option value="0">False</option>
                            <?php
                            }
                            else{
                                ?>
                            <option selected value="0">False</option>
                            <option value="1">True</option>
                            <?php
                            }
                            ?>
                            
                        </select>
                 <br /> 
               <label>Select InBlackList</label>
                 <select name="InBlackListInBlackList" id="InBlackList" class="form-control">
                  <option value="'.$user_data->InBlackList.'">'.$user_data->InBlackList.'</option>  
                  
                 </select>
                 <br /> 
               <div class="modal-footer">
                  <button type="submit" onclick="myFunction()" class="btn btn-xs btn-primary bg-primary-800 btn-labeled"><b><i class="icon-floppy-disk"></i></b> Lưu</button>
                  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
               </div>
            </form> -->

