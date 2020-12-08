<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>VCCI - Thông tin các hoạt động chăm sóc hội viên</title>
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
                                    <h2><i class="icon-arrow-left52 position-left font-size-100"></i> <span class="text-semibold" id="content">Chỉnh sửa các hoạt động chăm sóc hội
                                            viên</span></h4>
                                </div>
                                <div class="col-md-4 col-xs-8">
                                    <div class="no-margin">


                                    </div>
                                </div>
                                <div class="col-ms-6 col-lg-offset-9">
                                    <div class="no-margin pull-right">

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

                    <!-- modal_add_content -->

                    <!-- /modal_add_content -->
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


                        <!-- /Filter -->

                        <!-- Main content -->
                        <div class="row">
                            <div class="col-lg-12">
                                <!-- Basic panel controls -->
                                <div class="panel panel-white border-top-lg border-top-primary-800">
                                    <table class="table table-togglable table-hover table-bordered table-striped">
                                        <div class="modal-content">
                                            <div class="modal-header bg-primary-800">

                                                <h4 class="modal-title">Chỉnh sửa các hoạt động chăm sóc hội viên</h4>
                                            </div>
                                            <table class="table">

                                                <tbody>
                                                    <tr>
                                                        <th scope="row"><b>Chủ Đề</b></th>
                                                        <td>
                                                            <input value="2019.Q2_Lịch đào tạo gửi CEO: Trung tâm MEET_Kính gửi Chương trình Đào tạo Doanh nghiệp Q2.2019." style="width: 50%" type="text" class="form-control"
                                                                id="exampleInputEmail1" aria-describedby="emailHelp"
                                                                placeholder="Chủ Đề">
                                                        </td>

                                                    </tr>    
                                                    <tr>
                                                        <th scope="row"><b>Tình trạng</b></th>
                                                        <td>
                                                            <select class="bootstrap-select" data-width="50%">
                                                                <option value="1">Đã Gửi</option>
                                                                <option value="2">Đang Gửi</option>
                                                                <option value="3">Chưa Gửi</option>
                                                            </select>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"><b>Liên hệ</b></th>
                                                        <td>
                                                            <select class="bootstrap-select" data-width="50%">
                                                                <option value="1">Anh Đặng Đình Mạnh</option>
                                                                <option value="2">Chị Anh Đặng Đình</option>
                                                            </select>
                                                        </td>

                                                    </tr>
                                                    <tr>
                                                        <th scope="row"><b>Người chỉ định</b></th>
                                                        <td>
                                                            <select class="bootstrap-select" data-width="50%">
                                                                <option value="1" selected="selected">Phan Bảo</option>
                                                                <option value="2">Phạm Phượng</option>
                                                            </select>
                                                            
                                                        </td>
                                                    </tr>
                                                    
                                                                                   
                                                    
                                                </tbody>
                                            </table>

                                            <div class="modal-footer bg-gray">
                                                <button type="button" onclick="myFunction()" class="btn btn-xs btn-primary bg-primary-800 btn-labeled"><b><i class="icon-floppy-disk"></i></b> Lưu</button>
                                                <button type="button" class="btn btn-xs btn-labeled" data-dismiss="modal"><b><i class="glyphicon glyphicon-off"></i></b>
                                                    Thoát</button>
                                            </div>
                                        </div>
                                    </table>
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
        function myFunction() {
            var element = document.getElementById("mess");
            element.classList.add("alert", "alert-warning");
            element.innerHTML = "Sửa Thành Công !";
        }
    </script>
    <script type="text/javascript" src="../assets/js/contract.js"></script>
</body>

</html>