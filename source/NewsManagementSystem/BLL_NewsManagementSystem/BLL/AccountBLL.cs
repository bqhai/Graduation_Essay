using DAL_NewsManagementSystem.DAL;
using DAL_NewsManagementSystem.Models;
using Models_NewsManagementSystem.DTO;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BLL_NewsManagementSystem.BLL
{
    public class AccountBLL
    {
        private AccountDAL _dalAccount = new AccountDAL();
        public AccountBLL()
        {

        }
        public bool ProcessLogin(string username, string password)
        {           
            Account account = _dalAccount.GetAccount(username);
            if (account != null)
            {
                if (account.Password == password)
                {
                    return true;
                }
            }
            return false;
        }
    }
}
