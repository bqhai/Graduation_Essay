// $(document).on('click', '.sidebar-opposite-fix', function() {
//     var cog = document.getElementsByClassName("menu");
//     for (var i = 0; i < cog.length; i++) {
//         if (cog[i].style.display == "none")
//             cog[i].style.display = "block";
//         else
//             cog[i].style.display = "none";
//     }
//     $(document).on('click', '.sidebar-secondary-hide', function() {
//         var cog = document.getElementsByClassName("menu");
//         for (var i = 0; i < cog.length; i++) {
//             if (cog[i].style.display == "none")
//                 cog[i].style.display = "block";
//             else
//                 cog[i].style.display = "none";
//         }
//     });
// });



// $(document).on('click', '.sidebar-secondary-hide', function() {
//     var cog = document.getElementsByClassName("menu");
//     for (var i = 0; i < cog.length; i++) {
//         if (cog[i].style.display == "none")
//             cog[i].style.display = "block";
//         else
//             cog[i].style.display = "none";
//     }
//     $(document).on('click', '.sidebar-opposite-fix', function() {
//         var cog = document.getElementsByClassName("menu");
//         for (var i = 0; i < cog.length; i++) {
//             if (cog[i].style.display == "none")
//                 cog[i].style.display = "block";
//             else
//                 cog[i].style.display = "none";
//         }
//     });
// });

// function change() {
//     var img = document.getElementsById('myimg');
//     img.src = "../assets/images/pupil.svg";
// }

// // function menu
//  var menu=[
//      "Dash board",                              
//      "Danh sách doanh nghiệp",                  
//      "Thêm mới doanh nghiệp",                   
//      "Hội viên",                                
//      "Danh sách người liên hệ",                 
//      "Thêm mới người liên hệ",                  
//      "Danh sách việc làm",                      
//      "Thêm mới việc làm",                       
//      "Thông báo tới doanh nghiệp",              
//      "Tạo mới thông báo hội viên",              
//      "Danh sách các hạng mục",                  
//      "Thêm mới mẫu việc cần làm",               
//      "Lịch sử đóng phí hội viên",               
//      "Lịch sử tham gia sự kiện",                
//      "Lịch sử tài trợ sự kiện",                 
//      "Lịch sử chăm sóc hội viên",               
//      "Danh sách sự kiện",                       
//      "Thêm mới sự kiện",                        
//      "Danh sách gói tài trợ",                   
//      "Thêm mới gói tài trợ",                    
//      "Báo cáo tổng hợp",                        
//      "Tình hình đóng hội phí",                  
//      "Báo cáo hoạt động CSHV",                  
//      "Tình hình TCSK & TGSK",                   
//      "Báo cáo tình hình gửi mail Marketing",    
//      "Danh sách ngành nghề",                    
//      "Thêm mới ngành nghề",                     
//      "Danh sách gói phí hội viên",              
//      "Thêm mới gói phí hội viên",               
//      "Danh sách tài khoản",                            
//      "Thêm mới tài khoản",    
//      "Chi tiết doanh nghiệp",  
//      "Sửa doanh nghiệp",
//      "Nhập file dữ liệu doanh nghiệp",  
//      "Sửa sự kiện",
//      "Chi tiết sự kiện",
//      "Nhập file dữ liệu sự kiện",
//      "Sửa gói phí hội viên",
//      "Chi tiết gói phí hội viên",
//      "Nhập file dữ liệu gói phí hội viên", 
//      "Sửa gói tài trợ",
//      "Chi tiết gói tài trợ",
//      "Nhập file dữ liệu gói tài trợ",
//      "Sửa việc làm",
//      "Chi tiết việc làm",
//      "Nhập file dữ liệu việc làm",
//      "Nhập file dữ liệu LSĐPHV",
//      "Lịch sử đóng phí hội viên (chưa thanh toán)",
//      "Lịch sử đóng phí hội viên (đã thanh toán)",
//      "Thêm mới lịch sử đóng phí hội viên",
//      "Nhập file dữ liệu LSTTSK",
//      "Thêm mới LSTTSK",
//      "Nhập file dữ liệu LSTGSK",
//      "Thêm mới LSTGSK",
//      "Chi tiết mẫu việc cần làm",
//      "Sửa mẫu việc cần làm",
//      "Nhập file dữ liệu mẫu việc cần làm", 
//      "Chi tiết ngành nghề",
//      "Sửa ngành nghề",
//      "Nhập file dữ liệu ngành nghề", 
//      "Chi tiết người liên hệ",
//      "Sửa người liên hệ",
//      "Nhập file dữ liệu người liên hệ", 
//      "Chi tiết thông báo",
//      "Sửa thông báo",
//      "Nhập file dữ liệu thông báo", 
//      "Thêm mới báo cáo THHV",
//      "Nhập file dữ liệu BCTHHV",   
//  ];

// //  var tenphanhe = [
// //     "Dash board",
// //     "Doanh nghiệp & hội viên",
// //     "Chăm sóc hội viên",
// //     "Sự kiện",
// //     "Báo cáo & thống kê",
// //     "Danh mục",
// //     "Quản trị hệ thống",

// //    ];

// // var tendoituong = [
// //     "Dash board",
// //     "Doanh nghiệp",
// //     "Hội viên",
// //     "Người liên hệ",
// //     "Lịch nhắc nhở",
// //     "Thông báo hội viên",
// //     "Mẫu công việc cần làm",
// //     "Hoạt động hội viên",
// //     "Sự kiện",
// //     "Gói tài trợ sự kiện",
// //     "Báo cáo tổng hợp",                        
// //     "Tình hình đóng hội phí",                  
// //     "Báo cáo hoạt động CSHV",                  
// //     "Tình hình TCSK & TGSK",                   
// //     "Báo cáo tình hình gui mail Marketing",
// //     "Ngành nghề",
// //     "Gói phí hội viên",
// //     "Tài khoản"
// // ];




// // $(window).resize(function(){
// //     var width = $(window).width();
// //     console.log(width);
// //     if(width < 900){
// //         var cog=document.getElementsByClassName("glyphicon");
// //         var menu=document.getElementsByClassName("menu");
// //         // console.log(cog);
// //         for(var i=0; i < cog.length;i++){
// //            if(cog[i].style.display=="block" && menu[i].style.display=="block" ){
// //                cog[i].style.display="none";

// //            }
// //         }        
// //     }
// //     if(width > 600 && width < 1024){
// //         var cog=document.getElementsByClassName("menu");
// //         for(var i=0; i < cog.length;i++){
// //            if(cog[i].style.display=="none"){
// //                cog[i].style.display="block";

// //            }
// //         }        
// //     }
// //     if(width <= 623){
// //         var menu = document.getElementsByClassName("menu");
// //         for(var j=0;j< menu.length;j++){
// //             if(menu[j].style.display=="block"){
// //                 menu[j].style.display="none";
// //             }
// //         }
// //     }
// // });


// // as2D= new Array(); 
// //  as2D[0]= new Array("Dash board");
// //  as2D[1]= new Array("Doanh nghiệp","Thêm mới doanh nghiệp","Hội viên","Danh sách người liên hệ","Thêm mới người liên hệ");
// //  as2D[2]= new Array("Danh sách việc cần làm","Thêm mới việc cần làm","Thông báo tới doanh nghiệp","Tạo mới thông báo hội viên","Danh sách các hạng mục","Thêm mới mẫu việc cần làm","Lịch sử đóng phí hội viên", "Lịch sử tham gia sự kiện","Lịch sử tài trợ sự kiện","Lịch sử chăm sóc hội viên");
// //  as2D[3]= new Array("Danh sách sự kiện","Thêm mới sự kiện","Danh sách gói tài trợ","Thêm mới gói tài trợ");
// //  as2D[4]= new Array("Báo cáo tổng hợp","Tình hình đóng hội phí", "Báo cáo hoạt động CSHV","Tình hình TCSK & TGSK","Báo cáo tình hình gui mail Marketing", );
// //  as2D[5]= new Array("Danh sách ngành nghề","Thêm mới ngành nghề","Danh sách gói phí hội viên","Thêm mới gói phí hội viên");
// //  as2D[6]= new Array("Danh sách tài khoản","Thêm mới tài khoản");


// //  as3D=new Array();
// //  as3D[0]= new Array("Dash board");
// //  as3D[1]= new Array("Doanh nghiệp","Hội viên", "Người liên hệ");
// //  as3D[2]= new Array("Lịch nhắc nhở", "Thông báo hội viên","Mẫu công việc cần làm","Hoạt động hội viên");
// //  as3D[3]= new Array("Sự kiện","Gói tài trợ sự kiện");
// //  as3D[4]= new Array("Báo cáo tổng hợp", "Tình hình đóng hội phí", "Báo cáo hoạt động CSHV","Tình hình TCSK & TGSK","Báo cáo tình hình gui mail Marketing",);
// //  as3D[5]= new Array("Ngành nghề gói phí hội viên");
// //  as3D[6]= new Array("Tài khoản");

// //  as4D=new Array();
// //  as4D[0]= new Array("Dash board");
// //  as4D[1]= new Array("Doanh nghiệp","Thêm mới doanh nghiệp");
// //  as4D[2]= new Array("Hội viên");
// //  as4D[3]= new Array("Danh sách người liên hệ","Thêm mới người liên hệ");
// //  as4D[4]= new Array("Danh sách việc cần làm","Thêm mới việc cần làm");
// //  as4D[5]= new Array("Thông báo tới doanh nghiệp","Tạo mới thông báo hội viên");
// //  as4D[6]= new Array("Danh sách các hạng mục","Thêm mới mẫu việc cần làm");
// //  as4D[7]= new Array("Lịch sử đóng phí hội viên", "Lịch sử tham gia sự kiện","Lịch sử tài trợ sự kiện","Lịch sử chăm sóc hội viên");
// //  as4D[8]= new Array("Danh sách sự kiện","Thêm mới sự kiện");
// //  as4D[9]= new Array("Danh sách gói tài trợ","Thêm mới gói tài trợ");
// //  as4D[10]= new Array("Báo cáo tổng hợp");
// //  as4D[11]= new Array("Tình hình đóng hội phí");
// //  as4D[12]= new Array("Báo cáo hoạt động CSHV");
// //  as4D[13]= new Array("Tình hình TCSK & TGSK");
// //  as4D[14]= new Array("Báo cáo tình hình gui mail Marketing");
// //  as4D[15]= new Array("Ngành nghề");
// //  as4D[16]= new Array("Gói phí hội viên");
// //  as4D[17]= new Array("Danh sách tài khoản","Thêm mới tài khoản");










// // // ////////////////////////////////////////////////////////////////////////



// //  $(document).ready(function(){
// //     var url=location.pathname;
// //     var title=document.getElementsByClassName("tieu_de");
// //     var flag =0;
// //     var flag1=0;
// //     if (performance.navigation.type != 1) {// kiem tra xem co chuyen trang ko
// //         console.log("chuyen trang");
// //         console.log("tong title class tieu_de: "+title.length);
// //        for(var i=0;i<as2D.length;i++)
// //        { 
// //            if(flag == 1)
// //            { 
// //                break;
// //            }

// //            for(var j=0;j<as2D[i].length;j++)
// //            {
// //                 for(var t =0;t<title.length;t++){

// //                     var strURL=url.substring(url.lastIndexOf('html'));// link cua URL
// //                     var strURL_=strURL.replace('html','..');// xu ly chuoi bang cach thay the html => .
// //                     if(strURL_==title[t].getAttribute('href') && menu[t]==as2D[i][j])
// //                     {
// //                         document.getElementById("content").innerHTML=menu[t];
// //                         document.getElementById("tenphanhe").innerHTML=tenphanhe[i];
// //                         // console.log(taendoituong.length);
// //                         // for(var t=0;t<as3D[i].length;t++)
// //                         // {

// //                         //    for(var k=0;k<tendoituong.length;k++)
// //                         //    {

// //                         //        for(var h=0;h<as4D.length;h++)
// //                         //        {
// //                         //            for(var g=0;g<as4D[h].length;g++)
// //                         //            {
// //                         //                if(as4D[h][g]==menu[t])
// //                         //                {
// //                         //                    document.getElementsByClassName("ten_doi_tuong")[0].innerHTML=tendoituong[h];
// //                         //                    document.getElementsByClassName("ten_doi_tuong")[1].innerHTML=tendoituong[h];
// //                         //                     flag1 =1;
// //                         //                     break;
// //                         //                }
// //                         //            }
// //                         //        }
// //                         //    }
// //                         // }
// //                         flag =1;
// //                       break;
// //                     }

// //                 } 
// //            } 
// //        }

// //     } else {
// //         console.log("co nhan refesh trang web");

// //     }
// // });


// var array = [];
// array.push(
//     {
//         phanhe: "Dash board",
//         mang: [{
//             title: "Dash board",
//             arr: ["Dash board"]
//         }],
//     }, 
//     {
//         phanhe: "Doanh nghiệp & hội viên",
//         mang: [{
//                 title: "Doanh nghiệp",
//                 arr: [
//                     "Danh sách doanh nghiệp",
//                     "Thêm mới doanh nghiệp",
//                     "Chi tiết doanh nghiệp",
//                     "Sửa doanh nghiệp",
//                     "Nhập file dữ liệu doanh nghiệp",     
//                 ],
//             },
//             {
//                 title: "Hội viên",
//                 arr: ["Hội viên"],
//             },
//             {
//                 title: "Người liên hệ",
//                 arr: [
//                     "Danh sách người liên hệ",
//                     "Thêm mới người liên hệ",
//                     "Chi tiết người liên hệ",
//                     "Sửa người liên hệ",
//                     "Nhập file dữ liệu người liên hệ", 
//                 ],
//             }
//         ],

//     },
//     {
//         phanhe: "Chăm sóc hội viên",
//         mang: [{
//                 title: "Lịch nhắc nhở",
//                 arr: [
//                     "Danh sách việc làm",
//                     "Thêm mới việc làm",
//                     "Sửa việc làm",
//                     "Chi tiết việc làm",
//                     "Nhập file dữ liệu việc làm", 
//                 ],
//             },
//             {
//                 title: "Thông báo hội viên",
//                 arr: [
//                     "Thông báo tới doanh nghiệp",
//                     "Tạo mới thông báo hội viên",
//                     "Chi tiết thông báo",
//                     "Sửa thông báo",
//                     "Nhập file dữ liệu thông báo", 
//                 ],
//             },
//             {
//                 title: "Mẫu công việc cần làm",
//                 arr: [
//                     "Danh sách các hạng mục",
//                     "Thêm mới mẫu việc cần làm",
//                     "Chi tiết mẫu việc cần làm",
//                     "Nhập file dữ liệu mẫu việc cần làm", 
//                     "Sửa mẫu việc cần làm",
//                 ],
//             },
//             {
//                 title: "Hoạt động hội viên",
//                 arr: [
//                     "Lịch sử đóng phí hội viên",
//                     "Nhập file dữ liệu LSĐPHV",
//                     "Lịch sử đóng phí hội viên (chưa thanh toán)",
//                     "Lịch sử đóng phí hội viên (đã thanh toán)",
//                     "Thêm mới lịch sử đóng phí hội viên",
//                     "Lịch sử tham gia sự kiện",
//                     "Nhập file dữ liệu LSTGSK",
//                     "Thêm mới LSTGSK",
//                     "Lịch sử tài trợ sự kiện",
//                     "Thêm mới LSTTSK",
//                     "Nhập file dữ liệu LSTTSK",
//                     "Lịch sử chăm sóc hội viên"
//                 ],
//             }
//         ],

//     },
//     {
//         phanhe: "Sự kiện",
//         mang: [{
//                 title: "Sự kiện",
//                 arr: [
//                     "Danh sách sự kiện",
//                     "Thêm mới sự kiện",
//                     "Chi tiết sự kiện",
//                     "Sửa sự kiện",
//                     "Nhập file dữ liệu sự kiện",
//                 ],
//             },
//             {
//                 title: "Gói tài trợ sự kiện",
//                 arr: [
//                     "Danh sách gói tài trợ",
//                     "Thêm mới gói tài trợ",
//                     "Sửa gói tài trợ",
//                     "Chi tiết gói tài trợ",
//                     "Nhập file dữ liệu gói tài trợ",  
//                 ],
//             }
//         ],

//     },
//     {
//         phanhe: "Báo cáo & thống kê",
//         mang: [{
//                 title: "Báo cáo tổng hợp",
//                 arr: [
//                     "Báo cáo tổng hợp",
//                     "Thêm mới báo cáo THHV",
//                     "Nhập file dữ liệu BCTHHV",
//                 ],
//             },
//             {
//                 title: "Tình hình đóng hội phí",
//                 arr: ["Tình hình đóng hội phí"],
//             },
//             {
//                 title: "Báo cáo hoạt động CSHV",
//                 arr: ["Báo cáo hoạt động CSHV"],
//             },
//             {
//                 title: "Tình hình TCSK & TGSK",
//                 arr: ["Tình hình TCSK & TGSK"],
//             },
//             {
//                 title: "Báo cáo tình hình gửi mail Marketing",
//                 arr: ["Báo cáo tình hình gửi mail Marketing"],
//             },
//         ],

//     },
//     {
//         phanhe: "Danh mục",
//         mang: [{
//                 title: "Ngành nghề",
//                 arr: [
//                     "Danh sách ngành nghề",
//                     "Thêm mới ngành nghề",
//                     "Chi tiết ngành nghề",
//                     "Sửa ngành nghề",
//                     "Nhập file dữ liệu ngành nghề", 
//                 ],
//             },
//             {
//                 title: "Gói phí hội viên",
//                 arr: [
//                     "Danh sách gói phí hội viên",
//                     "Thêm mới gói phí hội viên",
//                     "Sửa gói phí hội viên",
//                     "Chi gói phí hội viên",
//                     "Nhập file dữ liệu gói phí hội viên", 
//                 ],
//             }
//         ],

//     },
//     {
//         phanhe: "Quản trị hệ thống",
//         mang: [{
//                 title: "Tài khoản",
//                 arr: [
//                     "Danh sách tài khoản",
//                     "Thêm mới tài khoản"
//                 ],
//             },
//         ],

//     },


// );
// // console.log(array);
// $(document).ready(function() {
//     var url = location.pathname;
//     var title = document.getElementsByClassName("tieu_de");
//     var flag=0;
//     if (performance.navigation.type != 1) {
//         for (var t = 0; t < title.length; t++) {
//         var strURL = url.substring(url.lastIndexOf('html')); // link cua URL
//         var strURL_ = strURL.replace('html', '..'); // xu ly chuoi bang cach thay the html => .
//         var a=title[t].getAttribute('href');
//         console.log(title.length);
//         console.log(t);
//         console.log(a);
//         if (strURL_ == a) 
//             {
//                 for(var i=0;i<array.length;i++)
//                 { 
//                     if(flag==1){
//                         break;
//                     }
//                     for(var k=0;k<array[i].mang.length;k++)
//                     {
//                         for(var h=0;h<array[i].mang[k].arr.length;h++)
//                         {
//                             if(array[i].mang[k].arr[h]==menu[t])
//                             {
//                                 document.getElementById("content").innerHTML=menu[t];
//                                 document.getElementById("tenphanhe").innerHTML=array[i].phanhe;
//                                 document.getElementsByClassName("ten_doi_tuong")[0].innerHTML=array[i].mang[k].title;
//                                 document.getElementsByClassName("ten_doi_tuong")[1].innerHTML=array[i].mang[k].title;                           
//                                 flag=1;
//                             }
//                         }
//                     }
//                 }
//             }
//         }
//         // console.log(array[1].mang[2].arr[1]);
//     } else {
//         var title = document.getElementsByClassName("tieu_de");
//         console.log("co nhan refesh");
//         console.log(title.length);
        
//     }
// });
// // $(function(){
// //     $('input[name="rad"]').click(function(){
// //     var $radio = $(this);
    
// //     // if this was previously checked
// //     if ($radio.data('waschecked') == true)
// //     {
// //     $radio.prop('checked', false);
// //     $radio.data('waschecked', false);
// //     }
// //     else
// //     $radio.data('waschecked', true);
    
// //     // remove was checked from other radios
// //     $radio.siblings('input[name="rad"]').data('waschecked', false);
// //     });
// //     });