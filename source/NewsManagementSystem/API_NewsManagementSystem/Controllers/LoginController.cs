using BLL_NewsManagementSystem.BLL;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

namespace API_NewsManagementSystem.Controllers
{
    [RoutePrefix("api/Login")]
    public class LoginController : ApiController
    {
        private AccountBLL _bllAccount = new AccountBLL();
        [HttpGet]
        [Route("ProcessLogin/{username}/{password}")]
        public bool ProcessLogin(string username, string password)
        {
            return _bllAccount.ProcessLogin(username, password);
        }
    }
}
