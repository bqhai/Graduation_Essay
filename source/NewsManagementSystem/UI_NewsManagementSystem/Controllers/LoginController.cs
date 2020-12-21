using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using UI_NewsManagementSystem.Models;
using UI_NewsManagementSystem.Repository;

namespace UI_NewsManagementSystem.Controllers
{
    public class LoginController : Controller
    {
        private ApiService _apiService = new ApiService();
        // GET: Login
        public ActionResult Login()
        {
            return View();
        }
        public ActionResult ProcessLogin(Account account)
        {
            var response = _apiService.GetResponse("api/Login/ProcessLogin/" + account.Username + "/" + account.Password + "/");
            if (response.IsSuccessStatusCode)
            {

            }
        }
    }
}