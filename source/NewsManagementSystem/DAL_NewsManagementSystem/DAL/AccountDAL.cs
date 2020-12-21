using DAL_NewsManagementSystem.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DAL_NewsManagementSystem.DAL
{
    public class AccountDAL
    {
        private NewsManagementSystemEntities _db = new NewsManagementSystemEntities();
        public AccountDAL()
        {

        }
        public Account GetAccount(string username)
        {
            return _db.Accounts.SingleOrDefault(acc => acc.Username == username);
        }
    }
}
