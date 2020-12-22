using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace UI_NewsManagementSystem.Repository
{
    public class Message
    {
        public static string ConnectFailed()
        {
            return "Kết nối server thất bại";
        }
        public static string AuthenticateFailed()
        {
            return "Tài khoản hoặc mật khẩu không chính xác";
        }
        public static string AddItemSuccessful()
        {
            return "Thêm thành công";
        }
        public static string AddItemFaled()
        {
            return "Thêm thất bại, có lỗi xảy ra phía server";
        }
        public static string UpdateItemSuccessful()
        {
            return "Cập nhật thành công";
        }
        public static string UpdateItemFaled()
        {
            return "Cập nhật thất bại, có lỗi xảy ra phía server";
        }
    }
}