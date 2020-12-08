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
                                            <a href="pageName_import.php" id='btn_export_data'
                                                data-url-parameter='' title='Export Data'
                                                class="btn btn-primary btn-export-data">
                                                <div class="glyphicon"><i class="fa fa-download"></i></div>
                                                <div class="menu">Import Data</div>
                                            </a>
                                        </div>
                                        <div class="btn-group">
                                            <a href="pageName_add.php" type="button" class="btn btn-primary"
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
                                    <!-- /form filter -->
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
                                        <div id='box_main' class="box box-primary">
                                            <div class="box-header with-border">
                                                <h3 class="box-title">Upload a File</h3>
                                                <div class="box-tools">

                                                </div>
                                            </div>


                                            <form method='post' id="form" enctype="multipart/form-data"
                                                action='http://crud.dev.digiprojects.top/admin/candidate/do-upload-import-data'>
                                                <input type="hidden" name="_token"
                                                    value="vpgyXiVT8HKXWgehQsnGz9zrQScnPJjJxcVnILG4">
                                                <div class="box-body">

                                                    <div class='callout callout-success'>
                                                        <h4>Welcome to Data Importer Tool</h4>
                                                        Before doing upload a file, its better to read this bellow
                                                        instructions : <br />
                                                        * File format should be : xls or xlsx or csv<br />
                                                        * If you have a big file data, we can't guarantee. So, please
                                                        split those files into
                                                        some parts of file (at least max 5 MB).<br />
                                                        * This tool is generate data automatically so, be carefull about
                                                        your table xls
                                                        structure. Please make sure correctly the table
                                                        structure.<br />
                                                        * Table structure : Line 1 is heading column , and next is the
                                                        data. (For example,
                                                        you can export any module you wish to XLS format)
                                                    </div>

                                                    <div class='form-group'>
                                                        <label>File XLS / CSV</label>
                                                        <input type='file' name='userfile' class='form-control'
                                                            required />
                                                        <div class='help-block'>File type supported only : XLS, XLSX,
                                                            CSV</div>
                                                    </div>
                                                </div><!-- /.box-body -->

                                                <div class="box-footer">
                                                    <div class='pull-right'>
                                                        <a href='#' class='btn btn-default'>Cancel</a>
                                                        <input type='submit' class='btn btn-primary' name='submit'
                                                            value='Upload' />
                                                    </div>
                                                </div><!-- /.box-footer-->
                                            </form>
                                        </div><!-- /.box -->
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