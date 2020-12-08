<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>VCCI - Thêm mới Người Liên Hệ</title>
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
                                    <h2><i class="icon-arrow-left52 position-left font-size-100"></i> <span class="text-semibold" id="content">Thêm người liên hệ</span></h4>
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
                                        <h4 class="modal-title"><i class='glyphicon glyphicon-filter'></i> Lọc</h4>
                                    </div>
                                    <!-- form filter -->
                                    <div class="modal-body">
                                        <div class="btn-group" id="downdrop">
                                            <select class="bootstrap-select" style="width: auto;" data-width="100%">
                                                <option value="1" selected="selected">10</option>
                                                <option value="2">20</option>
                                                <option value="3">30</option>
                                                <option value="4">All</option>
                                            </select>
                                        </div>
                                        <table id="fixed-table1"
                                            class="table table-togglable table-hover table-bordered table-striped"
                                            width="100%" border="0" cellspacing="0" cellpadding="0"
                                            style="margin-top: 10px;">
                                            <thead class="modal-header bg-primary-800" style="font-size: large;">
                                                <tr>
                                                    <th style="width:5%;"></th>
                                                    <th class="text-center" style="width: 10%;">MST</th>
                                                    <th class="text-center">Tên công ty</th>
                                                    <th class="text-center">Tỉnh/Thành</th>
                                                    <th class="text-center" style="width: 13%;">Điện thoại</th>
                                                </tr>
                                            </thead>
                                            <thead class="tsc_fixed_tables _scrolling _thead" style="color: #666;">
                                                <tr>
                                                    <th style="width: 5%;"></th>
                                                    <th class="text-center"><input placeholder="Filler MST"
                                                            class="form-control text-center"
                                                            style="margin: 0 auto; width: 70%;height: 30px;"></th>
                                                    <th><input placeholder="Filler Tỉnh/Thành"
                                                            class="form-control text-center"
                                                            style="margin: 0 auto; width: 70%;height: 30px;"></th>
                                                    <th><input placeholder="Filler Tỉnh/Thành"
                                                            class="form-control text-center"
                                                            style="margin: 0 auto; width: 70%;height: 30px;"></th>
                                                    <th><input placeholder="Filler SDT" class="form-control text-center"
                                                            style="margin: 0 auto; width: 70%;height: 30px;"></th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>CTCP DƯỢC HẬU GIANG</td>
                                                    <td>TP. HỒ CHÍ MINH</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>CTCP DƯỢC HẬU GIANG - CN SÓC TRĂNG</td>
                                                    <td>TP. HÀ NỘI</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>CTCP DƯỢC HẬU GIANG - CN NHÀ MÁY DƯỢC PHẨM DHG TẠI HẬU GIANG
                                                    </td>
                                                    <td>TP. HÀ NỘI</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>VPĐD CTY TNHH TƯ VẤN ĐẦU TƯ XÂY DỰNG CÔNG TRÌNH ĐÔ THỊ HẬU GIANG
                                                        - CN CẦN THƠ</td>
                                                    <td>TỈNH QUẢNG NINH</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>CTY TNHH ĐẦU TƯ BẤT ĐỘNG SẢN VIVALAND GROUP</td>
                                                    <td>TỈNH BÀ RỊA - VŨNG TÀU</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>CTCP DƯỢC HẬU GIANG - CN NHÀ MÁY DƯỢC PHẨM DHG TẠI HẬU GIANG
                                                    </td>
                                                    <td>TỈNH BÀ RỊA - VŨNG TÀU</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>CTCP DƯỢC HẬU GIANG - CN NHÀ MÁY DƯỢC PHẨM DHG TẠI HẬU GIANG
                                                    </td>
                                                    <td>TỈNH BÀ RỊA - VŨNG TÀU</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>CTCP DƯỢC HẬU GIANG - CN NHÀ MÁY DƯỢC PHẨM DHG TẠI HẬU GIANG
                                                    </td>
                                                    <td>TỈNH BÀ RỊA - VŨNG TÀU</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>CTCP DƯỢC HẬU GIANG - CN NHÀ MÁY DƯỢC PHẨM DHG TẠI HẬU GIANG
                                                    </td>
                                                    <td>TỈNH BÀ RỊA - VŨNG TÀU</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>CTCP DƯỢC HẬU GIANG - CN NHÀ MÁY DƯỢC PHẨM DHG TẠI HẬU GIANG
                                                    </td>
                                                    <td>TỈNH BÀ RỊA - VŨNG TÀU</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>CTCP DƯỢC HẬU GIANG - CN NHÀ MÁY DƯỢC PHẨM DHG TẠI HẬU GIANG
                                                    </td>
                                                    <td>TỈNH BÀ RỊA - VŨNG TÀU</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>CTCP DƯỢC HẬU GIANG - CN NHÀ MÁY DƯỢC PHẨM DHG TẠI HẬU GIANG
                                                    </td>
                                                    <td>TỈNH BÀ RỊA - VŨNG TÀU</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>CTCP DƯỢC HẬU GIANG - CN NHÀ MÁY DƯỢC PHẨM DHG TẠI HẬU GIANG
                                                    </td>
                                                    <td>TỈNH BÀ RỊA - VŨNG TÀU</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                                <tr>
                                                    <td class="text-center"><input type="radio" name="rad" id="Radio0"
                                                            checked="checked" data-waschecked="true"
                                                            style="margin: 0 auto;" /></td>
                                                    <td>1231231231</td>
                                                    <td>CTCP DƯỢC HẬU GIANG - CN NHÀ MÁY DƯỢC PHẨM DHG TẠI HẬU GIANG
                                                    </td>
                                                    <td>TỈNH BÀ RỊA - VŨNG TÀU</td>
                                                    <td>028 6682 5781</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                        <div class="content-group-lg pt-20 text-center">
                                            <ul class="pagination">
                                                <li class="disabled"><a href="#"><i
                                                            class="icon-arrow-small-left"></i></a></li>
                                                <li class="active"><a href="#">1</a></li>
                                                <li><a href="#">2</a></li>
                                                <li><a href="#">3</a></li>
                                                <li><a href="#">4</a></li>
                                                <li><a href="#">5</a></li>
                                                <li><a href="#"><i class="icon-arrow-small-right"></i></a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="modal-footer bg-gray">
                                        <button type="button"
                                            class="btn btn-xs btn-primary bg-primary-800 btn-labeled"><b><i
                                                    class="icon-sort"></i></b> Lọc</button>
                                        <button type="button" class="btn btn-xs btn-labeled" data-dismiss="modal"><b><i
                                                    class="glyphicon glyphicon-off"></i></b> Thoát</button>
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
                        <!--thanh chuc nang  -->

                        <!-- /Filter -->

                        <!-- Main content -->
                        <div class="row">
                            <div class="col-lg-12">
                                <!-- Basic panel controls -->
                                <div class="panel panel-white border-top-lg border-top-primary-800">
                                    <table class="table table-togglable table-hover table-bordered table-striped">
                                        <div class="modal-content">
                                            <div class="modal-header bg-primary-800">

                                                <h4 class="modal-title">Thêm người liên hệ</h4>
                                            </div>
                                            <table class="table">

                                                <tbody>
                                                    <tr>
                                                        <th style="width:15%" scope="row"><b>Danh xưng</b></th>
                                                        <td>
                                                            <select width: 50% class="bootstrap-select" data-width="50%">
                                                                <option value="0">Chọn danh xưng</option>
                                                                <option value="1" >Anh</option>
                                                                <option value="2">Chị</option>
                                                            </select>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"><b>Họ Và Tên</b></th>
                                                        <td>
                                                            <input style="width:50%" type="text"  class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Người Liên Hệ">
                                                        </td>

                                                    </tr>
                                                    <tr>
                                                        <th scope="row"><b>Chức Danh</b></th>
                                                        <td>
                                                            <select class="bootstrap-select" data-width="50%">
                                                                <option value="0">Chọn chức danh</option>
                                                                <option value="1">Sales admin</option>
                                                                <option value="2" >Giám đốc</option>
                                                                <option value="3">Phó phòng Tín dụng - Đầu tư</option>
                                                                <option value="4">Giám đốc chi nhánh</option>
                                                                <option value="5">Giám đốc</option>
                                                            </select>
                                                        </td>

                                                    </tr>

                                                    <tr>
                                                        <th scope="row"><b>Phòng Ban</b></th>
                                                        <td>

                                                            <select class="bootstrap-select" data-width="50%">
                                                                <option value="0">Chọn phòng ban</option>
                                                                <option value="1">Phòng kinh doanh</option>
                                                                <option value="2" >Tín dụng - Đầu tư
                                                                </option>
                                                            </select>

                                                        </td>

                                                    </tr>
                                                    <tr>
                                                        <th scope="row"><b>Điện Thoại</b></th>
                                                        <td>
                                                            <input style="width:50%" type="text" class="form-control"  id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Nhập Điện Thoại">
                                                        </td>
                                                    </tr>

                                                    <tr>
                                                        <th scope="row"><b>Email</b></th>
                                                        <td>
                                                            <input style="width:50%" type="email" class="form-control"  id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Nhập Địa Chỉ Email">
                                                        </td>
                                                    </tr>

                                                    <tr>
                                                        <th scope="row"><b>Ngày Sinh</b></th>
                                                        <td>
                                                            <input style="width:50%" class="form-control" type="date" data-width="50%" value="11/1092020">
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"><b>Địa chỉ</b></th>
                                                        <td>
                                                            <!-- <input style="width:50%" type="text"
                                                                value="Tổ 4"
                                                                class="form-control" id="exampleInputEmail1"
                                                                aria-describedby="emailHelp" placeholder="Nhập Địa Chỉ"> -->
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row">Số nhà</th>
                                                        <td>
                                                            <input style="width:50%" type="text"  class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Nhập số nhà">
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row">Đường</th>
                                                        <td>
                                                            <input style="width:50%" type="text"  class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Nhập đường">
                                                        </td>
                                                    </tr>

                                                    <tr>
                                                        <th scope="row">Xã/Phường</th>
                                                        <td>
                                                            <input style="width:50%" type="text"  class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Nhập xã phường">
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row">Quận/Huyện</th>
                                                        <td>
                                                            <input style="width:50%" type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Nhập quận/huyện">
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row">Tỉnh / Thành Phố</th>
                                                        <td>
                                                            <input style="width:50%" type="text"  class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Nhập tỉnh/thành phố">
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row">Quốc gia</th>
                                                        <td>
                                                            <input style="width:50%" type="text"  class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Nhập quốc gia">
                                                        </td>
                                                    </tr>

                                                    <tr>
                                                        <th scope="row"><b>Doanh nghiệp</b></th>
                                                        <td>
                                                            <div class="input-group"  style="width: 50%;">
                                                                <input type="text" readonly="false" class="form-control"
                                                                    value="Chọn doanh nghiệp">
                                                                <span data-popup="tooltip" data-placement="top"
                                                                    data-toggle="modal"
                                                                    data-target="#modal_filter_content"
                                                                    class="input-group-addon"><i class="icon-sort">
                                                                    </i></span>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"><b>Nhân Viên Chăm Sóc</b></th>
                                                        <td>
                                                            <select class="bootstrap-select" data-width="50%">
                                                                <option value="0">Chọn Nhân Viên Chăm Sóc
                                                                </option>
                                                                <option value="1">Nguyễn Văn B
                                                                </option>
                                                                <option value="2" >MNCL Lê Thị Riêng
                                                                </option>

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
            element.innerHTML = "Thêm Thành Công !";
        }
    </script>
    <script type="text/javascript" src="../assets/js/contract.js"></script>
</body>

</html>