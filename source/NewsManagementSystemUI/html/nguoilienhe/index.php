<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
      <title>VCCI - Thông tin Người Liên Hệ</title>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
      <script src="https://kit.fontawesome.com/5e87b6033a.js" crossorigin="anonymous"></script>
      <!-- Global stylesheets -->
      <link href="https://fonts.googleapis.com/css?family=Roboto:400,300,100,500,700,900" rel="stylesheet" type="text/css">
      <link href="../assets/css/icons/icomoon/styles.css" rel="stylesheet" type="text/css">
      <link href="../assets/css/bootstrap.css" rel="stylesheet" type="text/css">
      <link href="../assets/css/core.css" rel="stylesheet" type="text/css">
      <link href="../assets/css/components.css" rel="stylesheet" type="text/css">
      <link href="../assets/css/colors.css" rel="stylesheet" type="text/css">
      <link href="../assets/css/style.css" rel="stylesheet" type="text/css">
      <link href="../assets/css/iconUNIX.css" rel="stylesheet" type="text/css">
      <!-- /global stylesheets -->
      <!-- Core JS files -->
      <script type="text/javascript" src="../assets/js/plugins/loaders/pace.min.js"></script>
      <script type="text/javascript" src="../assets/js/core/libraries/jquery.min.js"></script>
      <script type="text/javascript" src="../assets/js/core/libraries/bootstrap.min.js"></script>
      <script type="text/javascript" src="../assets/js/plugins/loaders/blockui.min.js"></script>
      <!-- /core JS files -->
      <!-- Theme JS files -->
      <script type="text/javascript" src="../assets/js/plugins/forms/styling/switchery.min.js"></script>
      <script type="text/javascript" src="../assets/js/plugins/forms/styling/uniform.min.js"></script>
      <script type="text/javascript" src="../assets/js/plugins/forms/selects/bootstrap_multiselect.js"></script>
      <script type="text/javascript" src="../assets/js/plugins/ui/moment/moment.min.js"></script>
      <script type="text/javascript" src="../assets/js/plugins/pickers/daterangepicker.js"></script>
      <script type="text/javascript" src="../assets/js/plugins/forms/selects/bootstrap_select.min.js"></script>
      <script type="text/javascript" src="../assets/js/plugins/tables/footable/footable.min.js"></script>
      <script type="text/javascript" src="../assets/js/core/app.js"></script>
      <script type="text/javascript" src="../assets/js/pages/form_bootstrap_select.js"></script>
      <script type="text/javascript" src="../assets/js/pages/components_modals.js"></script>
      <!-- /theme JS files -->
   </head>
   <body class="sidebar-xs sidebar-secondary-hidden">
      <!-- Navigation bar -->
      <?php include "../common/navigationBar.php" ?>
      <!-- /Navigation bar -->
      <!-- Page container -->
      <div class="page-container">
         <!-- Page content -->
         <div class="page-content">
            <!-- Menu -->
            <?php include "../common/menu.php" ?>
            <!-- /Menu -->
            <!-- Left sidebar -->
          
            <!-- /Left sidebar -->
            <!-- Main content -->
            <div class="content-wrapper">
               <!-- page header -->
               <?php include "../common/pageHeader.php" ?>
               <div class="page-header page-header-default">
                  <div class="page-header-content">
                     <div class="page-title">
                        <div class="row" style="padding-bottom:8px">
                           <div class="col-md-4">
                              <h2>
                              <i class="icon-arrow-left52 position-left font-size-100"></i> <span class="text-semibold" id="content" >Danh sách</span></h4>
                           </div>
                           <div class="col-md-4 col-xs-8">
                              <div class="no-margin">
                                 <!--  <div class="btn-group">
                                    <button href="javascript:void(0)" id='btn_export_data' data-url-parameter='' title='Export Data' class="btn btn-primary btn-export-data">
                                        <i class="icon-book"></i>
                                        <div class="menu">Show Data</div>
                                    </button>
                                    </div> -->
                              </div>
                           </div>
                           <div class="col-ms-6 col-lg-offset-9">
                              <div class="no-margin pull-right">
                                 <div class="btn-group">
                                 </div>
                                 <div class="btn-group">
                                    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal">Add New Data</button>
                                 </div>
                                 <div class="btn-group">
                                    <a href="export.php"><button type="button" class="btn btn-primary">Export Data</button></a>
                                 </div>
                              </div>
                           </div>
                        </div>
                        <!-- <button class="btn btn-primary pull-right btn-sm"  type="button">Cancel</button> -->
                     </div>
                  </div>
                  <div id="mess" role="alert"></div>
               </div>
               <!-- /page header -->
               <!-- Content area -->
               <div class="content">
                  <!-- change Page -->
                  <div id="contents">
                     <!-- Filter -->
                     <div class="modal fade" id="modal_filter_content">
                        <div class="modal-dialog modal-lg">
                           <div class="modal-content">
                              <div class="modal-header bg-primary-800">
                                 <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                 <span aria-hidden="true">×</span></button>
                                 <h4 class="modal-title"><i class='glyphicon glyphicon-filter'></i> Advanced Sort
                                    &amp; Filter
                                 </h4>
                              </div>
                              <!-- form filter -->
                              <div class="modal-body">
                                 <div class="form-group">
                                    <div class='row-filter-combo row'>
                                       <div class="col-sm-2">
                                          <strong>Candidate Id</strong>
                                       </div>
                                       <div class='col-sm-3'>
                                          <select name='' data-type='text' class="filter-combo form-control">
                                             <option value=''>** Select Operator Type</option>
                                             <option value='like'>LIKE</option>
                                             <option value='not like'>NOT LIKE</option>
                                             <option typeallow='all' value='='>=(Equal to)</option>
                                             <option typeallow='all' value='!='>!= (Not Equal to)</option>
                                             <option typeallow='all' value='in'>IN</option>
                                             <option typeallow='all' value='not in'>NOT IN</option>
                                             <option value='empty'>Empty ( or Null)</option>
                                          </select>
                                       </div>
                                       <div class='col-sm-5'>
                                          <input type='text' class='filter-value form-control' style="display:block" disabled name='' value=''>
                                          <div class='row between-group' style="display:none">
                                             <div class='col-sm-6'>
                                                <div class='input-group '>
                                                   <span class="input-group-addon">from:</span>
                                                   <input disabled type='text' class='filter-value-between form-control timepicker' readonly placeholder='Candidate Id from' name='' value=''>
                                                </div>
                                             </div>
                                          </div>
                                       </div>
                                       <div class='col-sm-2'>
                                          <select class='form-control' name=''>
                                             <option value=''>** Sorting</option>
                                             <option value='asc'>ASCENDING</option>
                                             <option value='desc'>DESCENDING</option>
                                          </select>
                                       </div>
                                    </div>
                                 </div>
                              </div>
                              <div class="modal-footer bg-gray">
                                 <button type="button" class="btn btn-xs btn-primary bg-primary-800 btn-labeled"><b><i class="icon-floppy-disk"></i></b> Lưu</button>
                                 <button type="button" class="btn btn-xs btn-labeled" data-dismiss="modal"><b><i class="glyphicon glyphicon-off"></i></b> Thoát</button>
                              </div>
                              <!-- /form filter -->
                           </div>
                           <!-- /.modal-content -->
                        </div>
                        <!-- /.modal-dialog -->
                     </div>
                     <div class="modal fade" id="modal_multi_content">
                        <div class="modal-dialog modal-lg">
                           <div class="modal-content">
                              <div class="modal-header bg-primary-800">
                                 <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                 <span aria-hidden="true">×</span></button>
                                 <h4 class="modal-title"><i class='glyphicon glyphicon-filter'></i> Chức năng
                                    nâng cao
                                 </h4>
                              </div>
                              <!-- form sort & filter -->
                              <div class="modal-body">
                                 <div class="form-group">
                                    <div class='row-filter-combo row'>
                                       <div class="col-sm-2">
                                          <strong>Candidate Id</strong>
                                       </div>
                                       <div class='col-sm-3'>
                                          <select name='' data-type='text' class="filter-combo form-control">
                                             <option value=''>** Select Operator Type</option>
                                             <option value='like'>LIKE</option>
                                             <option value='not like'>NOT LIKE</option>
                                             <option typeallow='all' value='='>=(Equal to)</option>
                                             <option typeallow='all' value='!='>!= (Not Equal to)</option>
                                             <option typeallow='all' value='in'>IN</option>
                                             <option typeallow='all' value='not in'>NOT IN</option>
                                             <option value='empty'>Empty ( or Null)</option>
                                          </select>
                                       </div>
                                       <div class='col-sm-5'>
                                          <input type='text' class='filter-value form-control' style="display:block" disabled name='' value=''>
                                          <div class='row between-group' style="display:none">
                                             <div class='col-sm-6'>
                                                <div class='input-group '>
                                                   <span class="input-group-addon">from:</span>
                                                   <input disabled type='text' class='filter-value-between form-control timepicker' readonly placeholder='Candidate Id from' name='' value=''>
                                                </div>
                                             </div>
                                          </div>
                                       </div>
                                       <div class='col-sm-2'>
                                          <button type="button" class="btn btn-primary btn-sm dropdown-toggle"><i class="fas fa-plus"></i> Thêm
                                          cột</button>
                                       </div>
                                    </div>
                                 </div>
                              </div>
                              <div class="modal-footer bg-gray">
                                 <button type="button" class="btn btn-xs btn-primary bg-primary-800 btn-labeled"><b><i class="icon-floppy-disk"></i></b> Lọc</button>
                              </div>
                              <!-- /form sort & filter-->
                           </div>
                           <!-- /.modal-content -->
                        </div>
                        <!-- /.modal-dialog -->
                     </div>
                     <div class="row">
                        <div class="col-lg-12">
                           <!-- Basic panel controls -->
                           <div class="panel panel-white border-top-lg border-top-primary-800">
                              <table class="table table-togglable table-hover table-bordered table-striped">
                                 <thead style="font-size: 12px" class="grey-light">
                                    <tr>
                                       <!-- <th class="text-center" data-toggle="true">FacebookID</th> -->
                                       <th class="text-center" data-toggle="true">FacebookName</th>
                                       <th class="text-center" data-toggle="true">FacebookURL</th>
                                       <!-- <th class="text-center" data-toggle="true">FacebookTypeID</th> -->
                                       <th class="text-center" data-toggle="true">FacebookTypeName</th>
                                       <!-- <th class="text-center" data-toggle="true">Status</th>
                                       <th class="text-center" data-toggle="true">InBlackList</th> -->
                                       <th class="text-center"  style="width:5%">Hành Động</th>
                                    </tr>
                                 </thead>
                                 <tbody id="data">
                                    
                                 </tbody>
                              <?php
                                    ini_set('display_errors','On');
                                    error_reporting(E_ALL);
                                    
                                    // Include the pagination class
                                    include 'pagination.class.php';
                                    $api_url = 'http://www.kltn26.somee.com/api/Home/GetAllWatchList';
                                    $json_data = file_get_contents($api_url);
                                    $response_data = json_decode($json_data);
                                    
                                    $user_data = $response_data;
                                    foreach ($user_data as $user) {
                                    
                                    }
                                    
                                    // If we have an array with items
                                    if (count($user_data)) {
                                      // Create the pagination object
                                      $pagination = new pagination($user_data, (isset($_GET['page']) ? $_GET['page'] : 1),15);
                                      // Decide if the first and last links should show
                                      $pagination->setShowFirstAndLast(false);
                                      // You can overwrite the default seperator
                                      $pagination->setMainSeperator(' | ');
                                      // Parse through the pagination class
                                      $productPages = $pagination->getResults();
                                      // If we have items 
                                      if (count($productPages) != 0) {
                                        // Create the page numbers
                                        $pageNumbers = '<div class="numbers">'.$pagination->getLinks($_GET).'</div>';
                                    
                                        // Loop through all the items in the array
                                        foreach ($productPages as $productArray) {
                                          // Show the information about the item
                                          echo '<tr>'
                                          // .'<td>'.$productArray->FacebookID.'</td>'
                                          .'<td>'.$productArray->FacebookName.'</td>'
                                          .'<td>'.'<a target="_blank" href="'.$productArray->FacebookUrl.'">'.$productArray->FacebookUrl.'</a></td>'
                                          // .'<td>'.$productArray->FacebookTypeID.'</td>'
                                          .'<td>'.$productArray->FacebookTypeName.'</td>'
                                          // .'<td>'.$productArray->Status.'</td>'
                                          // .'<td>'.$productArray->InBlackList.'</td>'
                                          .'<td class="text-center" style="border-right: hidden;">'
                                          .'<a target="_blank" name="view" class="view" id="'.$productArray->FacebookID.'" >'.'<i class="icon-eye"></i>'.'</a>'
                                          .'<a target="_blank" name="view1" class="view1" id="'.$productArray->FacebookID.'">'.'<i class="icon-pencil7"></i>'.'</a>'
                                          // .'<a href="#" target="_blank">'.'<i class="glyphicon glyphicon-remove"></i>'.'</a>'
                                          .'</td>'
                                          .'</tr>';                                       
                                        }
                                      }
                                      echo $pageNumbers;
                                    }
                                    
                                    ?>
                              </table>
                           </div>
                           <!-- /basic panel controls -->
                        </div>
                     </div>
                  </div>
                  <!-- Footer -->
                  <?php include "../common/pageFooter.php" ?>
                  <!-- /footer -->
               </div>
               <!-- /content area -->
            </div>
            <!-- /Main content -->
            <!-- Right sidebar -->
            
            <!-- /Right sidebar -->
         </div>
         <!-- /page content -->
      </div>
   
      <!-- /page container -->
      <!-- <script>
         var ops = {
             'html': true,
             content: function() {
                 return $('#module-sc').html();
             }
         };
         
         $('#link-module-sc').popover(ops);
         $(".styled, .multiselect-container input").uniform({
             radioClass: 'choice'
         });
         
         if (Array.prototype.forEach) {
             var elems = Array.prototype.slice.call(document.querySelectorAll('.switchery'));
             elems.forEach(function(html) {
                 var switchery = new Switchery(html);
             });
         } else {
             var elems = document.querySelectorAll('.switchery');
             for (var i = 0; i < elems.length; i++) {
                 var switchery = new Switchery(elems[i]);
             }
         }
         
         
         $('.table-togglable').footable();
         </script> -->
      <!-- <script type="text/javascript">
         fetch("https://jsonplaceholder.typicode.com/todos").then(
                 res=>{
                     res.json().then(
                         data=>{
                             console.log(data);
                         })
                 }
             )
         </script> -->
      <!-- <script>
         $(document).ready(function(){
          $(function() {
              $('.btn-filter-data').click(function() {
                  $('#filter-data').modal('show');
              })
          
              $('.btn-export-data').click(function() {
                  $('#export-data').modal('show');
              })
          
              var toggle_advanced_report_boolean = 1;
              $(".toggle_advanced_report").click(function() {
          
                  if (toggle_advanced_report_boolean == 1) {
                      $("#advanced_export").slideDown();
                      $(this).html("<i class='fa fa-minus-square-o'></i> Show Advanced Export");
                      toggle_advanced_report_boolean = 0;
                  } else {
                      $("#advanced_export").slideUp();
                      $(this).html("<i class='fa fa-plus-square-o'></i> Show Advanced Export");
                      toggle_advanced_report_boolean = 1;
                  }
          
              })
          })
         </script> -->
      <!--  <script type="text/javascript" src="../assets/js/contract.js"></script> -->
      <style>
         a.hover {
         text-decoration: underline;
         }
         a.selected {
         font-weight: bold;
         text-decoration: underline;
         }
         .numbers {
         font-size: 14px;
         float: right;
         line-height: 20px;
         word-spacing: 4px;
         }
      </style>
   </body>

</html>
<div id="post_modal" class="modal fade">
   <div class="modal-dialog">
      <div class="modal-content">
         <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">&times;</button>
            <h4 class="modal-title">ListFacebook Details</h4>
         </div>
         <div class="modal-body" id="post_detail">
         </div>
         <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
         </div>
      </div>
   </div>
</div>

<div class="modal fade" id="myModal1" role="dialog">
    <div class="modal-dialog">
      <!-- Modal content-->
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
          <h4 class="modal-title">Edit ListFacebook</h4>
        </div>
        <div class="modal-body" id="edit_list">
           <!-- <form action="editlistfb.php" method="post" enctype="multipart/form-data">
         
               <label>FacebookName</label>
               <input  type="text"  class="form-control" id="FacebookID" name="FacebookID"  placeholder="FacebookID">
               <br />
               <label>Select Status</label>
                 <select name="Status" id="Status" class="form-control">
                  <option value="true">True</option>  
                  <option value="false">False</option>
                 </select>
                 <br /> 
               <label>Select InBlackList</label>
                 <select name="InBlackListInBlackList" id="InBlackList" class="form-control">
                  <option value="true">True</option>  
                  <option value="false">False</option>
                 </select>
                 <br /> 
               <div class="modal-footer">
                  <button type="submit" onclick="myFunction()" class="btn btn-xs btn-primary bg-primary-800 btn-labeled"><b><i class="icon-floppy-disk"></i></b> Lưu</button>
                  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
               </div>
            </form> -->
            <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
         </div>
        </div>
      </div>
      
    </div>
  </div>
<div class="modal fade" id="myModal" role="dialog">
   <div class="modal-dialog">
      <!-- Modal content-->
      <div class="modal-content">
         <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">&times;</button>
            <h4 class="modal-title">Insert ListFacebook</h4>
         </div>
         <div class="modal-body">
            <form action="listfb.php" method="post" enctype="multipart/form-data">
               <!-- <th scope="row"><b>FacebookID</b></th> -->
               <label>FacebookID</label>
               <input  type="text"  class="form-control" id="FacebookID" name="FacebookID"  placeholder="FacebookID">
               <br />
               <label>FacebookName</label>
               <input type="text" class="form-control"  id="FacebookName" name="FacebookName"  placeholder="FacebookName">
               <br />
               <label>FacebookUrl</label>
               <input  type="text" class="form-control"  id="FacebookUrl" name="FacebookUrl"  placeholder="FacebookUrl">
               <br />
               <label>FacebookTypeID</label>
               <input  type="text" class="form-control"  id="FacebookTypeID" name="FacebookTypeID"  placeholder="FacebookTypeID">
               <br />
               <div class="modal-footer">
                  <button type="submit" onclick="myFunction()" class="btn btn-xs btn-primary bg-primary-800 btn-labeled"><b><i class="icon-floppy-disk"></i></b> Lưu</button>
                  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
               </div>
            </form>
         </div>
      </div>
   </div>
</div>


<script>
   $(document).ready(function(){
    
    function fetch_post_data(FacebookID)
    {
     $.ajax({
      url:"pageName_export.php",
       method:"POST",
      data:{FacebookID:FacebookID},
      success:function(data)
      {
       $('#post_modal').modal('show');
       $('#post_detail').html(data);
      }
     });
    }
    $(document).on('click', '.view', function(){
     var FacebookID = $(this).attr("id");
     fetch_post_data(FacebookID);
    });
   });
</script>


<script>
   $(document).ready(function(){
    
    function fetch_post_data1(FacebookID)
    {
     $.ajax({
      url:"editlistfb.php",
       method:"POST",
      data:{FacebookID:FacebookID},
      success:function(data)
      {
       $('#myModal1').modal('show');
       $('#edit_list').html(data);
      }
     });
    }
    $(document).on('click', '.view1', function(){
     var FacebookID = $(this).attr("id");
     fetch_post_data1(FacebookID);
    });
   });
</script>



<!-- <script>
  $(function() {
        $.ajax({
        url: "http://www.kltn26.somee.com/api/Home/GetAllWatchList",
       method: "GET",
        dataType: "json",
        success: function(data) {
            var str = "";          
           for(var i= 0; i < data.jobsBreakdown.length; i++){

             str +='Job Title : '+data.jobsBreakdown[i].description+' and Related Trades <br> Percentage of Occupancies in Area : '+data.jobsBreakdown[i].percentage.toPrecision(2)+'% <br><br>';
           }
          $("body").html(str);
        }
        });
    });
</script> -->