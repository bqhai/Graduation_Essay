using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace BLL_NewsManagementSystem.Lib
{
    public static class AutoGenerate
    {
        public static string PostID()
        {
            Thread.Sleep(5);
            return DateTime.Now.ToString("ddMMyyyyHHmmssfffff");
        }
    }
}
