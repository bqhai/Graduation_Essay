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
        private static Random random = new Random();
        public static string PostID()
        {
            Thread.Sleep(5);
            return DateTime.Now.ToString("ddMMyyyyHHmmss") + RandomString(6);
        }
        public static string RandomString(int length)
        {
            const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            return new string(Enumerable.Repeat(chars, length)
              .Select(s => s[random.Next(s.Length)]).ToArray());
        }
    }
}
