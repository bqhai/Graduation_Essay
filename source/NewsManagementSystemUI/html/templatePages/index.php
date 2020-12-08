<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bão Công Nghệ - Hệ thống quản lý hội viên</title>

    <!-- Global stylesheets -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,300,100,500,700,900" rel="stylesheet"
        type="text/css">
    <link href="../assets/css/icons/icomoon/styles.css" rel="stylesheet" type="text/css">
    <link href="../assets/css/bootstrap.css" rel="stylesheet" type="text/css">
    <link href="../assets/css/core.css" rel="stylesheet" type="text/css">
    <link href="../assets/css/components.css" rel="stylesheet" type="text/css">
    <link href="../assets/css/colors.css" rel="stylesheet" type="text/css">
    <link href="../assets/css/style.css" rel="stylesheet" type="text/css">
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
    <?php include "../common/navigationBar.php"?>

    <!-- /Navigation bar -->


    <!-- Page container -->
    <div class="page-container">

        <!-- Page content -->
        <div class="page-content">



            <!-- Menu -->
            <?php include "../common/menu.php"?>
            <!-- /Menu -->

            <!-- Left sidebar -->
            <?php include "pageName_leftSideBar.php"?>
            <!-- /Left sidebar -->


            <!-- Main content -->
            <div class="content-wrapper">
                <!-- page header -->
                <?php include "../common/pageHeader.php"?>
                <div class="page-header page-header-default">
                    <div class="page-header-content">
                        <div class="page-title">

                            <div class="row" style="padding-bottom:8px">
                                <div class="col-md-4">
                                    <h2><i class="icon-arrow-left52 position-left font-size-100"></i> <span
                                            class="text-semibold" id="content">Danh sach goi lien he</span></h4>
                                </div>
                                <div class="col-md-4 col-xs-8">
                                    <div class="no-margin">
                                        <div class="btn-group">
                                            <button class="btn btn-primary" type="button"><div class="glyphicon"><i class="icon-book"></i></div>
                                                <div class="menu">Show Data</div>

                                            </button>
                                        </div>
                                        <div class="btn-group">
                                            <button href="javascript:void(0)" id='btn_export_data' data-url-parameter=''
                                                title='Export Data' class="btn btn-primary btn-export-data">
                                                <div class="glyphicon"><i class="fa fa-upload"></i></div>
                                                <div class="menu">Export Data</div>
                                            </button>
                                        </div>
                                        <div class="btn-group">
                                            <button class="btn btn-primary" type="button"><div class="glyphicon"><i
                                                    class="glyphicon glyphicon-print"></i></div>
                                                <div class="menu">Print</div>
                                            </button>
                                        </div>

                                    </div>
                                </div>
                                <div class="col-ms-6 col-lg-offset-9">
                                    <div class="no-margin pull-right">
                                        <div class="btn-group">
                                            <a href="goitaitrosukien_import.php" id='btn_export_data'
                                                data-url-parameter='' title='Export Data'
                                                class="btn btn-primary btn-export-data">
                                                <div class="glyphicon"><i class="fa fa-download"></i></div>
                                                <div class="menu">Import Data</div>
                                            </a>
                                        </div>
                                        <div class="btn-group">
                                            <a href="goitaitrosukien_add.php" type="button" class="btn btn-primary"
                                                data-popup="tooltip" data-placement="top" data-original-title="Thêm"><div class="glyphicon"><i
                                                    class="icon-add"></i></div>
                                                <div class="menu">Add New</div>
                                            </a>
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
                                                    <input type='text' class='filter-value form-control'
                                                        style="display:block" disabled name='' value=''>
                                                    <div class='row between-group' style="display:none">
                                                        <div class='col-sm-6'>
                                                            <div class='input-group '>
                                                                <span class="input-group-addon">from:</span>
                                                                <input disabled type='text'
                                                                    class='filter-value-between form-control timepicker'
                                                                    readonly placeholder='Candidate Id from' name=''
                                                                    value=''>
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
                                        <button type="button"
                                            class="btn btn-xs btn-primary bg-primary-800 btn-labeled"><b><i
                                                    class="icon-floppy-disk"></i></b> Lưu</button>
                                        <button type="button" class="btn btn-xs btn-labeled" data-dismiss="modal"><b><i
                                                    class="glyphicon glyphicon-off"></i></b> Thoát</button>
                                    </div>
                                    <!-- /form sort & filter-->
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
                                                    <input type='text' class='filter-value form-control'
                                                        style="display:block" disabled name='' value=''>
                                                    <div class='row between-group' style="display:none">
                                                        <div class='col-sm-6'>
                                                            <div class='input-group '>
                                                                <span class="input-group-addon">from:</span>
                                                                <input disabled type='text'
                                                                    class='filter-value-between form-control timepicker'
                                                                    readonly placeholder='Candidate Id from' name=''
                                                                    value=''>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>



                                                <div class='col-sm-2'>
                                                    <button type="button"
                                                        class="btn btn-xs btn-primary bg-primary btn-labeled"> \</button>
                                                </div>


                                            </div>
                                        </div>
                                    </div>
                                    <div class="modal-footer bg-gray">
                                        <button type="button"
                                            class="btn btn-xs btn-primary bg-primary-800 btn-labeled"><b><i
                                                    class="icon-floppy-disk"></i></b> Lọc</button>
                                    </div>
                                    <!-- /form sort & filter-->
                                </div>
                                <!-- /.modal-content -->
                            </div>
                            <!-- /.modal-dialog -->


                        </div>















                        <!--thanh chức năng-->
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
                                                <button type="button" class="btn btn-primary" data-popup="tooltip"
                                                    data-placement="top" data-original-title="Thêm" data-toggle="modal"
                                                    data-target="#modal_filter_content" style="width:auto;"><div class="glyphicon"><i
                                                        class="glyphicon glyphicon-cog"></i></div>
                                                    <div class="menu">Nâng cao</div>
                                                </button>
                                            </div>
                                            <div class="btn-group">
                                                <button type="button" class="btn btn-primary" data-popup="tooltip"
                                                    data-placement="top" data-original-title="Thêm" data-toggle="modal"
                                                    data-target="#modal_multi_content" style="width:auto;"><div class="glyphicon"><i
                                                        class="glyphicon glyphicon-filter"></i></div>
                                                    <div class="menu">Sort & Filter</div>
                                                </button>
                                            </div>
                                            <div class="btn-group">
                                                <input type="text" placeholder="Tìm kiếm"
                                                    class="form-control daterange-single">
                                            </div>
                                            <div class="btn-group">
                                                <button type="button" class="btn btn-primary" data-popup="tooltip"
                                                    data-placement="top" data-original-title="Thực hiện lọc"><i
                                                        class="glyphicon glyphicon-search"></i></button>
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
                            <div id="mess" role="alert"></div>


                        </div>
                        <!--thanh chức năng-->
                        <!-- /Filter -->

                        <!-- Main content -->
                        <div class="row">
                            <div class="col-lg-12">
                                <!-- Basic panel controls -->
                                <div class="panel panel-white border-top-lg border-top-primary-800">
                                    <table class="table table-togglable table-hover table-bordered table-striped">
                                        <thead class="grey-light">
                                            <tr>
                                                <th class="text-center" style="width:100px">Ngày tạo</th>
                                                <th class="text-center" data-toggle="true">Tên tổ chức</th>
                                                <th class="text-center" data-hide="phone">Mã đơn hàng</th>
                                                <th class="text-center">Phân hệ</th>
                                                <th class="text-center" data-hide="phone" style="width:10%">Ngày gia hạn
                                                </th>
                                                <th class="text-center" style="width:10%">Ngày hết hạn</th>
                                                <th class="text-center" style="width:10%">Tình trạng</th>
                                                <th class="text-center" style="width:5%">Hành động</th>

                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td class="text-center">26/09/2018 09:00</td>
                                                <td data-label="Tên tổ chức">MNCL Nguyễn Cư Trinh</td>
                                                <td data-label="Mã đơn hàng">SO-BCN-190729-1007-EPKA</td>
                                                <td data-label="PHân hệ">Ứng dụng SCFamily</td>
                                                <td class="text-center" data-label="Ngày gia hạn">24/09/2019</td>
                                                <td class="text-center" data-label="Ngày hết hạn">24/09/2020</td>
                                                <td data-label="Tình trạng">
                                                    <span class="label label-success"><i class="icon-checkmark4"></i>
                                                        Đang
                                                        sử dụng</span>
                                                </td>
                                                <td class="text-center">
                                                    <ul class="icons-list">
                                                        <li class="dropdown">
                                                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                                                                <i class="icon-menu9"></i>
                                                            </a>

                                                            <ul class="dropdown-menu dropdown-menu-right">
                                                                <li><a href="../templatePages/pageName_view.php"
                                                                        data-toggle="modal"><i
                                                                            class="icon-eye"></i>Xem</a></li>
                                                                <li><a href="../templatePages/pageName_edit.php"
                                                                        data-toggle="modal"><i class="icon-pencil7"></i>
                                                                        Chỉnh sửa</a></li>
                                                                <li><a href="#"><i
                                                                            class="glyphicon glyphicon-remove"></i>Hủy
                                                                        bỏ</a></li>
                                                            </ul>
                                                        </li>
                                                    </ul>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td class="text-center">24/09/2018 09:00</td>
                                                <td data-label="Tên tổ chức">MNCL Lê Thị Riêng</td>
                                                <td data-label="Mã đơn hàng">SO-BCN-190729-1007-EPKA</td>
                                                <td data-label="Phân hệ">Quản lý thu chi</td>
                                                <td class="text-center" data-label="Ngày gia hạn">24/09/2018</td>
                                                <td class="text-center" data-label="Ngày hết hạn">24/09/2019</td>
                                                <td data-label="Tình trạng">
                                                    <span class="label bg-orange"><i class="icon-battery-charging"></i>
                                                        Sắp
                                                        hết hạn</span>
                                                </td>
                                                <td class="text-center">
                                                    <ul class="icons-list">
                                                        <li class="dropdown">
                                                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                                                                <i class="icon-menu9"></i>
                                                            </a>

                                                            <ul class="dropdown-menu dropdown-menu-right">
                                                                <li><a href="#" data-toggle="modal"><i
                                                                            class="icon-eye"></i>Xem</a></li>
                                                                <li><a href="#" data-toggle="modal"><i
                                                                            class="icon-pencil7"></i> Chỉnh sửa</a></li>
                                                                <li><a href="#"><i
                                                                            class="glyphicon glyphicon-remove"></i>Hủy
                                                                        bỏ</a></li>
                                                            </ul>
                                                        </li>
                                                    </ul>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td class="text-center">24/09/2018 09:00</td>
                                                <td data-label="Tên tổ chức">MNCL Lê Thị Riêng</td>
                                                <td data-label="Mã đơn hàng">SO-BCN-190729-1007-EPKA</td>
                                                <td data-label="Phân hệ">Khẩu phần dinh dưỡng</td>
                                                <td class="text-center" data-label="Ngày gia hạn">24/09/2018</td>
                                                <td class="text-center" data-label="Ngày hết hạn">24/09/2019</td>
                                                <td data-label="Tình trạng">
                                                    <span class="label bg-orange"><i class="icon-battery-charging"></i>
                                                        Sắp
                                                        hết hạn</span>
                                                </td>
                                                <td class="text-center">
                                                    <ul class="icons-list">
                                                        <li class="dropdown">
                                                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                                                                <i class="icon-menu9"></i>
                                                            </a>

                                                            <ul class="dropdown-menu dropdown-menu-right">
                                                                <li><a href="#" data-toggle="modal"><i
                                                                            class="icon-eye"></i>Xem</a></li>
                                                                <li><a href="#" data-toggle="modal"><i
                                                                            class="icon-pencil7"></i> Chỉnh sửa</a></li>
                                                                <li><a href="#"><i
                                                                            class="glyphicon glyphicon-remove"></i>Hủy
                                                                        bỏ</a></li>
                                                            </ul>
                                                        </li>
                                                    </ul>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                <!-- /basic panel controls -->
                            </div>
                        </div>
                    </div>
                    <!-- /change Page -->


                    <!-- /Main content -->





                    <!-- Footer -->
                    <?php include "../common/pageFooter.php"?>
                    <!-- /footer -->

                </div>
                <!-- /content area -->

            </div>
            <!-- /Main content -->


            <!-- Right sidebar -->
            <?php include "pageName_rightSideBar.php"?>
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
     <script type="text/javascript" src="../assets/js/contract.js"></script>
</body>

</html>