using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace UI_NewsManagementSystem.Repository
{
    public class Message
    {
        public static string ConnectFail()
        {
            return "Kết nối server thất bại";
        }
        public static string AuthenticateFail()
        {
            return "Tài khoản hoặc mật khẩu không chính xác";
        }
    }
}