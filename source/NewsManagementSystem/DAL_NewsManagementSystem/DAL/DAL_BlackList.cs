using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DAL_NewsManagementSystem.Models;

namespace DAL_NewsManagementSystem.DAL
{
    public class DAL_BlackList
    {
        NewsManagementSystemEntities db = new NewsManagementSystemEntities();
        public DAL_BlackList()
        {
            db.Configuration.ProxyCreationEnabled = false;
        }
        
    }
}
