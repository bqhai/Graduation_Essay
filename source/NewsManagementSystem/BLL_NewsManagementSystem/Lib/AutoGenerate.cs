using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BLL_NewsManagementSystem.Lib
{
    public static class AutoGenerate
    {
        public static string ID(string headID, string lastID)
        {
            string ID = headID;
            if (lastID == null)
            {
                ID += "100000";
            }
            else
            {
                int k = Convert.ToInt32(lastID.Substring(8, 6));
                k++;
                ID += k.ToString();
            }
            return ID;
        }
        public static string PostID()
        {
            return DateTime.Now.ToString("ddMMyyyyHHmmssffffff");
        }
    }
}
