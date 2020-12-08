<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>VCCI - Thông tin Người Liên Hệ</title>
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
            <?php include "nguoilienhe_leftSideBar.php" ?>
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
                                    <h2><i class="icon-arrow-left52 position-left font-size-100"></i> <span class="text-semibold" id="content" >Danh sách</span></h4>
                                </div>
                                <div class="col-md-4 col-xs-8">
                                    <div class="no-margin">
                                        <!-- <div class="btn-group">
                                            <button class="btn btn-primary" type="button"><i class="icon-book"></i>
                                                <div class="menu">Show Data</div>

                                            </button>
                                        </div>
                                        <div class="btn-group">
                                            <button href="javascript:void(0)" id='btn_export_data' data-url-parameter='' title='Export Data' class="btn btn-primary btn-export-data">
                                                <i class="fa fa-upload"></i>
                                                <div class="menu">Export Data</div>
                                            </button>
                                        </div>
                                        <div class="btn-group">
                                            <button class="btn btn-primary" type="button"><i class="glyphicon glyphicon-print"></i>
                                                <div class="menu">Print</div>
                                            </button>
                                        </div> -->

                                    </div>
                                </div>
                                <div class="col-ms-6 col-lg-offset-9">
                                    <div class="no-margin pull-right">
                                        <div class="btn-group">
                                        <!-- <a href="nguoilienhe_import.php" type="button" class="btn btn-primary"
                                                data-popup="tooltip" data-placement="top">
                                                <div class="glyphicon"><i class="fa fa-download"></i></div>
                                                <div class="menu">Import Data</div>
                                            </a> -->
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
                                            &amp; Filter</h4>
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
                                            nâng cao</h4>
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

                        <div class="page-header page-header-default">
                            <div class="page-header-content">
                                <div class="page-title">

                                    <div class="row" style="padding-bottom:8px">
                                        <div class="col-md-5 col-xs-7" style="height: 38px;">
                                            <div class="btn-group" id="select">
                                                <select class="bootstrap-select" style="width: auto;" data-width="100%">
                                                    <option value="1" selected="selected">Hành động</option>
                                                    <option value="2">Xóa hàng chọn</option>

                                                </select>
                                            </div>

                                        </div>

                                        <div class="col-ms-6 pull-right">
                                            <div class="btn-group">
                                                <button type="button" class="btn btn-primary" data-popup="tooltip" data-placement="top" data-original-title="" data-toggle="modal" data-target="#modal_filter_content" style="width:auto;"><i class="glyphicon glyphicon-cog"></i>
                                                    <div class="menu">Nâng cao</div>
                                                </button>
                                            </div>
                                            <div class="btn-group">
                                                <button type="button" class="btn btn-primary" data-popup="tooltip" data-placement="top" data-original-title="" data-toggle="modal" data-target="#modal_multi_content" style="width:auto;"><i class="glyphicon glyphicon-filter"></i>
                                                    <div class="menu">Sort & Filter</div>
                                                </button>
                                            </div>
                                            <div class="btn-group">
                                                <input type="text" placeholder="Tìm kiếm" class="form-control daterange-single">
                                            </div>
                                            <div class="btn-group">
                                                <button type="button" class="btn btn-primary" data-popup="tooltip" data-placement="top" data-original-title=""><i class="glyphicon glyphicon-search"></i></button>
                                            </div>
                                            <div class="btn-group" id="downdrop">
                                                <select class="bootstrap-select" style="width: auto;" data-width="100%">
                                                    <option value="1" selected="selected">10</option>
                                                    <option value="2">20</option>
                                                    <option value="3">30</option>
                                                </select>
                                            </div>
                                        </div>
                                    </div>



                                    <!-- <button class="btn btn-primary pull-right btn-sm"  type="button">Cancel</button> -->
                                </div>

                            </div>
                            <!--                   <div id="mess" role="alert"></div> -->


                        </div>
                        <!-- /Filter -->

                        <!-- Main content -->
                        <div class="row">
                            <div class="col-lg-12">
                                <!-- Basic panel controls -->
                                <div class="panel panel-white border-top-lg border-top-primary-800">
                                    <table class="table table-togglable table-hover table-bordered table-striped">
                                        <thead class="grey-light">
                                            <tr>
                                                <!-- <th class="text-center" style="width:3%">STT</th> -->
                                                <th class="text-center" data-toggle="true">FacebookID</th>
                                                <th class="text-center" data-toggle="true">Facebook Name</th>
                                                <!-- <th class="text-center" data-toggle="true">Facebook URL</th>
                                                <th class="text-center" data-toggle="true">FacebookTypeID</th>
                                                
                                                <th class="text-center"  style="width:5%">Hành Động</th> -->

                                            </tr>
                                        </thead>
                                        <tbody id="data">

                                        </tbody>
                                    </table>
                                     <script type="text/javascript">
                            fetch("http://cellphonesapi.somee.com/api/API_Product/GetAllProductVersion").then(
                res=>{
                    res.json().then(
                        data=>{
                            console.log(data);
                            if(data.length>0)
                            {
                              var temp ="";
                              data.forEach((u)=>{
                                temp +="<tr>";
                                temp +="<td>"+u.ProductVersionID+"</td>";
                                temp +="<td>"+u.ProductVersionName+"</td>";
                              })
                             document.getElementById("data").innerHTML=temp;
                            }
                        })
                }
            )
 </script>
                                </div>
                                <!-- /basic panel controls -->
                            </div>
                        </div>
                    </div>
                    <!-- /change Page -->


                    <!-- /Main content -->





                    <!-- Footer -->
                    <?php include "../common/pageFooter.php" ?>
                    <!-- /footer -->

                </div>
                <!-- /content area -->

            </div>
            <!-- /Main content -->


            <!-- Right sidebar -->
            <?php include "nguoilienhe_rightSideBar.php" ?>
            <!-- /Right sidebar -->

        </div>
        <!-- /page content -->

    </div>
    <!-- /page container -->
    <script>
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

        // Switchery
        // ------------------------------

        // Initialize multiple switches
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

        // Initialize responsive functionality
        $('.table-togglable').footable();
    </script>
    <script type="text/javascript">
        fetch("https://jsonplaceholder.typicode.com/todos").then(
                res=>{
                    res.json().then(
                        data=>{
                            console.log(data);
                        })
                }
            )
    </script>
    <script>
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
    </script>
    <script>

    </script>
    <script type="text/javascript" src="../assets/js/contract.js"></script>
</body>

</html>