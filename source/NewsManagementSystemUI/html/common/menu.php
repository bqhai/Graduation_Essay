<div class="sidebar sidebar-main">
    <div class="sidebar-content">
        <!-- Module name -->
        <!-- <div class="sidebar-user">
        <div class="category-content">
            <div class="media">
                <a href="#" class="media-left" data-popup="tooltip" data-placement="right"
                    data-original-title="PHÂN HỆ QUẢN LÝ NHÂN SỰ">
                    <img src="../assets/images/settings.svg" title="Quản lý nhân sự" alt="EP" />
                </a>
                <div class="media-body">
                    <span class="media-heading text-size-mini text-muted">Phân hệ quản lý </span>
                    <div class="text-semibold ">
                        Thiết lập hệ thống
                    </div>
                </div>

                <div class="media-right media-middle">
                    <ul class="icons-list">
                        <li>
                            <a href="#"><i class="icon-cog3"></i></a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        </div> -->
        <!-- /Module name -->


        <!-- Main navigation -->
        <div class="sidebar-category sidebar-category-visible">
            <div class="category-content no-padding">
                <ul class="navigation navigation-main navigation-accordion">

                    <!-- Main -->

                    <li>
                        <a href="#"><img id="myimg" src='../assets/images/eduplan.svg' style="height: 32px;" />
                            <span>CHĂM SÓC HỘI VIÊN</span></a>

                    </li>
                    <li class="navigation-header"><span>Danh sách các tính năng</span> <i class="icon-menu" title=""
                            data-original-title="Các tính năng"></i>
                    </li>



                    <!-- Dash Board -->
                    <li>
                        <a href="#"><img src="../assets/images/icons/ic/finance.svg" style="width: 32px;" />
                            <span>DASH BOARD</span></a>
                        <ul>
                            <li><a href="../dashboard/index.php" class="tieu_de"><i
                                        class="fas fa-tachometer-alt"></i>DASH BOARD</a></li>
                        </ul>
                    </li>
                    <!-- Danh nghiệp & hội viên -->
                    <li>
                        <a href="#"><img src="../assets/images/icons/sys/school.svg" style="width: 32px;" />
                            <span>Quản Lý</span></a>
                        <ul>

                            <!-- <li><a href="#"><i class="fas fa-archway"></i>Doanh nghiệp</i></a>
                                <ul>
                                    <a href="../doanhnghiep/index.php" class="tieu_de"><i
                                            class="far fa-list-alt"></i>Danh sách
                                        Doanh nghiệp</a>
                                    <a href="../doanhnghiep/doanhnghiep_add.php" class="tieu_de"><i
                                            class="fas fa-plus"></i>Thêm
                                        mới</a>
                                </ul>
                            </li> -->
                            <li><!-- <a href="../hoivien/index.php" class="tieu_de"><i class="fas fa-user-friends"></i>Hội Viên</a> -->
                            <li><a href="#"><i class="fas fa-user-friends"></i>ListFacebook</a>
                                <ul>
                                    <a id="1" onClick="GFG_click(this.id)" href="../nguoilienhe/index.php"
                                        class="tieu_de"><i class="far fa-list-alt"></i>Danh sách
                                        Faccbook</a>
                                    <a id="1" onClick="GFG_click(this.id)" href="../nguoilienhe/nguoilienhe_add.php"
                                        class="tieu_de"><i class="fas fa-plus"></i>Thêm mới</a>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <!-- Chăm sóc hội viên -->
                   <!--  <li>
                        <a href="#"><img src="../assets/images/icons/sys/users.svg" style="width: 32px;" />
                            <span>CHĂM SÓC HỘI VIÊN</span></a>
                        <ul>
                            <li><a href="#"><i class="far fa-calendar-alt"></i>Lịch nhăc nhở</a>
                                <ul>
                                    <a id="2" onClick="GFG_click(this.id)" href="../lichnhacnho/index.php"
                                        class="tieu_de"><i class="far fa-list-alt"></i>Danh sách việc làm</a>
                                    <a id="2" onClick="GFG_click(this.id)" href="../lichnhacnho/lichnhacnho_add.php"
                                        class="tieu_de"><i class="fas fa-plus"></i>Tạo mới</a>
                                </ul>
                            </li>
                            <li><a href="#"><i class="far fa-bell"></i>Thông báo hội viên</a>
                                <ul>
                                    <a href="../thongbaohoivien/index.php" class="tieu_de"><i
                                            class="far fa-bell"></i>Thông báo tới doanh nghiệp</a>
                                    <a href="../thongbaohoivien/thongbaohoivien_add.php" class="tieu_de"><i
                                            class="fas fa-plus"></i>Tạo mới</a>
                                </ul>
                            </li>
                            <li><a href="#"><i class="fas fa-boxes"></i>Mẫu công việc cần làm</a>
                                <ul>
                                    <a href="../maucongvieccanlam/index.php" class="tieu_de"><i
                                            class="far fa-list-alt"></i>Danh sách các hạng mục</a>
                                    <a href="../maucongvieccanlam/maucongvieccanlam_add.php" class="tieu_de"><i
                                            class="fas fa-plus"></i>Thêm mới</a>
                                </ul>

                            </li>
                            <li><a href="#"><i class="fas fa-chart-line"></i>Hoạt Động hội viên</a>
                                <ul>
                                  <a href="../lichsudongphihoivien/index.php" class="tieu_de"><i class="fas fa-history"></i>Lịch
                                            sử đóng phí hội viên</a>
                                   <a href="../lichsuthamgiasukien/index.php"class="tieu_de"><i class="fas fa-history"></i>Lịch
                                            sử tham gia sự kiện</a>
                                   <a href="../lichsutaitrosukien/index.php"class="tieu_de"><i class="fas fa-history"></i>Lịch
                                            sử tài trợ sự kiện</a>
                                   <a href="../lichsuchamsochoivien/index.php"class="tieu_de"><i class="fas fa-history"></i>Lịch
                                            sử chăm sóc hội viên</a>
                                </ul>

                            </li>
                        </ul>
                    </li> -->
                    <!-- Sự kiện -->
                 <!--    <li>
                        <a href="#"><img src="../assets/images/icons/sys/voucher_1332606.svg" style="width: 32px;" />
                            <span>SỰ KIỆN</span></a>
                        <ul>
                            <li><a href="#"><i class="fas fa-gift"></i></i>Sự kiện</a>
                                <ul>
                                    <a href="../event/index.php" class="tieu_de"><i class="far fa-list-alt"></i></i>Danh
                                        sách sự
                                        kiện</a>
                                    <a href="../event/event_add.php" class="tieu_de"><i class="fas fa-plus"></i>Thêm
                                        mới</a>
                                </ul>
                            </li>

                            <li><a href="#"><i class="fas fa-hand-holding-heart"></i>Gói tài trợ sự kiện</a>
                                <ul>
                                    <a href="../goitaitrosukien/index.php" class="tieu_de"><i
                                            class="far fa-list-alt"></i>Danh sách
                                        gói tài trợ</a>
                                    <a href="../goitaitrosukien/goitaitrosukien_add.php" class="tieu_de"><i
                                            class="fas fa-plus"></i>Thêm mới</a>
                                </ul>
                            </li>
                        </ul>
                    </li> -->
                    <!-- Báo cáo thông kê -->
                   <!--  <li>
                        <a href="#"><img src="../assets/images/icons/ic/finance.svg" style="width: 32px;" />
                            <span>BÁO CÁO & THỐNG KÊ</span></a>
                        <ul>
                            <li><a href="../baocaotonghophoivien/index.php" class="tieu_de"><i class="fas fa-book-open"></i>Báo cáo tổng hợp</a></li>
                            <li><a href="#" class="tieu_de"><i class="fas fa-book-open"></i>Tình hình đóng Hội Phí</a>
                            </li>
                            <li><a href="#" class="tieu_de"><i class="fas fa-book-open"></i>Báo cáo hoạt động chăm sóc
                                    Hội viên</a></li>
                            <li><a href="#" class="tieu_de"><i class="fas fa-book-open"></i>Tình hình tổ chức & tham dự
                                    Sự kiện</a></li>
                            <li><a href="#" class="tieu_de"><i class="fas fa-book-open"></i>Báo cáo tính hình gửi Email
                                    Marketing</a>
                            </li>
                        </ul>
                    </li> -->
                    <!-- Danh mục -->
                   <!--  <li>
                        <a href="#"><img src="../assets/images/icons/ep/files.svg" style="width: 32px;" />
                            <span>DANH MỤC</span></a>
                        <ul>
                            <li><a href="#"><i class="fas fa-briefcase"></i>Ngành nghề</a>
                                <ul>
                                    <a href="../nganhnghe/index.php" class="tieu_de"><i class="far fa-list-alt"></i>Danh
                                        sách nghành nghề</a>
                                    <a href="../nganhnghe/nganhnghe_add.php" class="tieu_de"><i
                                            class="fas fa-plus"></i>Thêm mới</a>
                                </ul>
                            </li>
                            <li><a href="#"><i class="far fa-money-bill-alt"></i> Gói phí hội viên</a>
                                <ul>
                                    <a href="../goiphihoivien/index.php" class="tieu_de"><i
                                            class="far fa-list-alt"></i>Danh sách gói hội viên</a>
                                    <a href="../goiphihoivien/goiphihoivien_add.php" class="tieu_de"><i
                                            class="fas fa-plus"></i>Thêm mới</a>
                                </ul>
                            </li>
                        </ul>
                    </li> -->
                    <!-- quản trị hệ thống -->
                   <!--  <li>
                        <a href="#"><img src="../assets/images/icons/sys/help.svg" style="width: 32px;" />
                            <span>QUẢN TRỊ HỆ THỐNG</span></a>
                        <ul>
                            <li><a href="#"><i class=" fas fa-user"></i>Tài khoản</a>
                                <ul>
                                    <a href="#" class="tieu_de"><i class="far fa-list-alt"></i>Danh sách tài khoản</a>
                                    <a href="#" class="tieu_de"><i class="fas fa-plus"></i>Thêm mới</a>
                                </ul>
                            </li>
                        </ul>
                    </li> -->
                    <a href="../doanhnghiep/doanhnghiep_view.php" class="tieu_de" hidden="true"></a>
                    <a href="../doanhnghiep/doanhnghiep_edit.php" class="tieu_de" hidden="true"></a>
                    <a href="../doanhnghiep/doanhnghiep_import.php" class="tieu_de" hidden="true"></a>
                    <a href="../event/event_edit.php" class="tieu_de" hidden="true"></a>
                    <a href="../event/event_view.php" class="tieu_de" hidden="true"></a>
                    <a href="../event/event_import.php" class="tieu_de" hidden="true"></a>
                    <a href="../goiphihoivien/goiphihoivien_edit.php" class="tieu_de" hidden="true"></a>
                    <a href="../goiphihoivien/goiphihoivien_view.php" class="tieu_de" hidden="true"></a>
                    <a href="../goiphihoivien/goiphihoivien_import.php" class="tieu_de" hidden="true"></a>
                    <a href="../goitaitrosukien/goitaitrosukien_edit.php" class="tieu_de" hidden="true"></a>
                    <a href="../goitaitrosukien/goitaitrosukien_view.php" class="tieu_de" hidden="true"></a>
                    <a href="../goitaitrosukien/goitaitrosukien_import.php" class="tieu_de" hidden="true"></a>
                    <!-- <a href="../hoivien/hoivien_edit.php" class="tieu_de" hidden="true"></a>
                    <a href="../hoivien/hoivien_view.php" class="tieu_de" hidden="true"></a>
                    <a href="../hoivien/hoivien_import.php" class="tieu_de" hidden="true"></a> -->
                    <a href="../lichnhacnho/lichnhacnho_edit.php" class="tieu_de" hidden="true"></a>
                    <a href="../lichnhacnho/lichnhacnho_view.php" class="tieu_de" hidden="true"></a>
                    <a href="../lichnhacnho/lichnhacnho_import.php" class="tieu_de" hidden="true"></a>
                    <a href="../lichsudongphihoivien/lichsudongphihoivien_import.php" class="tieu_de" hidden="true"></a>
                    <a href="../lichsudongphihoivien/lichsudongphihoivien_chuathanhtoan.php" class="tieu_de" hidden="true"></a>
                    <a href="../lichsudongphihoivien/lichsudongphihoivien_dathanhtoan.php" class="tieu_de" hidden="true"></a>
                    <a href="../lichsudongphihoivien/lichsudongphihoivien_add.php" class="tieu_de" hidden="true"></a>
                    <a href="../lichsutaitrosukien/lichsutaitrosukien_import.php" class="tieu_de" hidden="true"></a>
                    <a href="../lichsutaitrosukien/lichsutaitrosukien_add.php" class="tieu_de" hidden="true"></a>
                    <a href="../lichsuthamgiasukien/lichsuthamgiasukien_import.php" class="tieu_de" hidden="true"></a>
                    <a href="../lichsuthamgiasukien/lichsuthamgiasukien_add.php" class="tieu_de" hidden="true"></a>
                    <a href="../maucongvieccanlam/maucongvieccanlam_view.php" class="tieu_de" hidden="true"></a>
                    <a href="../maucongvieccanlam/maucongvieccanlam_edit.php" class="tieu_de" hidden="true"></a>
                    <a href="../maucongvieccanlam/maucongvieccanlam_import.php" class="tieu_de" hidden="true"></a>
                    <a href="../nganhnghe/nganhnghe_view.php" class="tieu_de" hidden="true"></a>
                    <a href="../nganhnghe/nganhnghe_edit.php" class="tieu_de" hidden="true"></a>
                    <a href="../nganhnghe/nganhnghe_import.php" class="tieu_de" hidden="true"></a>
                    <a href="../nguoilienhe/nguoilienhe_view.php" class="tieu_de" hidden="true"></a>
                    <a href="../nguoilienhe/nguoilienhe_edit.php" class="tieu_de" hidden="true"></a>
                    <a href="../nguoilienhe/nguoilienhe_import.php" class="tieu_de" hidden="true"></a>
                    <a href="../thongbaohoivien/thongbaohoivien_view.php" class="tieu_de" hidden="true"></a>
                    <a href="../thongbaohoivien/thongbaohoivien_edit.php" class="tieu_de" hidden="true"></a>
                    <a href="../thongbaohoivien/thongbaohoivien_import.php" class="tieu_de" hidden="true"></a>
                    <a href="../baocaotonghophoivien/baocaotonghophoivien_add.php" class="tieu_de" hidden="true"></a>
                    <a href="../baocaotonghophoivien/baocaotonghophoivien_import.php" class="tieu_de" hidden="true"></a>
                    <!-- <li>
                        <a href="../NguoiLienHe/"><img src="../assets/images/icons/sys/users.svg" style="width: 32px;" />
                            <span>NGƯỜI LIÊN HỆ</span></a>
                         <ul>
                            <li><a href="sys_taikhoannguoidung.php">Danh sách tài khoản</a></li>
                            <li><a href="sys_vaitronguoidung.php">Vai trò người dùng</a></li>
                            <li><a href="sys_capquyensudung.php">Cấp quyền sử dụng</a></li>
                        </ul> 
                    </li> 
                    <li>
                        <a href="../GoiTaiTroSuKien/"><img src="../assets/images/icons/admin/parcel.svg"
                                style="width: 32px;" />
                            <span>GÓI TÀI TRỢ</span></a>
                        <ul>
                            <li><a href="sys_sanpham.php">Sản phẩm</a></li>
                            <li><a href="sys_loaisanpham.php">Loại sản phẩm</a></li>
                            <li><a href="sys_thuonghieu.php">Thương hiệu</a></li>
                            <li><a href="sys_donvitinh.php">Đơn vị tính</a></li>
                        </ul>
                    </li>


                     <li>
                        <a href="#"><img src="../assets/images/icons/sys/invoice.svg" style="width: 32px;" />
                            <span>BÁN HÀNG</span></a>
                        <ul>
                            <li><a href="sys_taodonbanhang.php">Tạo đơn bán hàng</a></li>
                            <li><a href="sys_danhsachbanhang.php">Danh sách bán hàng</a></li>
                        </ul>
                    </li>
                    <li>
                        <a href="#"><img src="../assets/images/icons/ic/finance.svg" style="width: 32px;" />
                            <span>THU - CHI</span></a>
                        <ul>
                            <li><a href="sys_phieuthuchi.php">Phiếu thu chi</a></li>
                            <li><a href="sys_soquythuchi.php">Sổ quỹ thu chi</a></li>
                            <li><a href="sys_hangmucthuchi.php">Hạng mục thu chi</a></li>
                            <li><a href="sys_taikhoannganhang.php">Tài khoản ngân hàng</a></li>
                        </ul>
                    </li>
                    <li>
                        <a href="#"><img src="../assets/images/icons/sys/big-license.svg" style="width: 32px;" />
                            <span>BẢN QUYỀN PHẦN MỀM</span></a>
                        <ul>
                            <li><a href="sys_capbanquyen.php">Cấp bản quyền</a></li>
                            <li class="active" id="banQuyenPhanMem"><a href="sys_banquyenphanmem.php">Danh
                                    sách bản quyền</a>
                            </li>
                            <li id="banQuyenSapHetHan"><a href="sys_banquyensaphethan.php">Bản quyền sắp hết
                                    hạn</a></li>
                        </ul>
                    </li>
                    
                    <li>
                        <a href="sys_yeucauhotro.php"><img src="../assets/images/icons/sys/help.svg"
                                style="width: 32px;" />
                            <span>YÊU CẦU HỖ TRỢ</span></a>
                    </li>
                    <li>
                        <a href="sys_lienhegopy.php"><img src="../assets/images/icons/web/mail.svg"
                                style="width: 32px;" />
                            <span>LIÊN HỆ GÓP Ý</span></a>
                    </li>
                    <li>
                        <a href="#"><img src="../assets/images/icons/sys/bell.svg" style="width: 32px;" />
                            <span>THÔNG BÁO</span></a>
                        <ul>
                            <li><a href="sys_thongbao.php">Thông báo</a></li>
                            <li><a href="sys_loaithongbao.php">Loại thông báo</a></li>
                        </ul>
                    </li>
                 

                   
                    <li class="navigation-header"><span>Thiết lập SC</span> <i class="icon-menu" title=""
                            data-original-title="Thiết lập SC"></i></li>
                    <li>
                        <a href="#"><img src="../assets/images/icons/sys/healthy-food_2210818.svg"
                                style="width: 32px;" />
                            <span>THIẾT LẬP DINH DƯỠNG</span></a>
                        <ul>
                            <li><a href="fk_donvitinh.php">Đơn vị tính</a></li>
                            <li><a href="fk_baobi.php">Bao bì</a></li>
                            <li><a href="fk_thucpham.php">Thực phẩm</a></li>
                        </ul>
                    </li>
                    <li>
                        <a href="#"><img src="../assets/images/icons/ep/files.svg" style="width: 32px;" />
                            <span>THIẾT LẬP KẾ HOẠCH GIÁO DỤC</span></a>
                        <ul>
                            <li><a href="ep_khochude.php">Kho chủ đề/sự kiện</a></li>
                            <li><a href="ep_khogiaoangiangday.php">Thư viện bài giảng</a></li>
                            <li><a href="ep_thuvienhinhanh.php">Thư viện hình ảnh</a></li>
                            <li><a href="ep_thuvienvideo.php">Thư viện video</a></li>
                            <li><a href="ep_khobaihatmamnon.php">Thư viện bài hát</a></li>
                            <li class="navigation-divider"></li>
                            <li><a href="ep_vanbanhuongdan.php.php">Văn bản hướng dẫn</a></li>
                            <li><a href="ep_loaivanbanhuongdan.php">Loại văn bản hướng dẫn</a></li>
                            <li class="navigation-divider"></li>
                            <li><a href="ep_chedosinhhoat.php">Chế độ sinh hoạt từng tỉnh</a></li>
                            <li><a href="ep_muctieugiaoduc.php">Mục tiêu giáo dục</a></li>
                        </ul>
                    </li> -->
                    <!-- /sc-->

                </ul>
            </div>
        </div>
        <!-- /main navigation -->

    </div>
</div>