﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
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
                var resultLogin = response.Content.ReadAsAsync<bool>().Result;
                if (resultLogin)
                {
                    return RedirectToAction("Index", "Home");
                }
                else
                {
                    TempData["DangerMessage"] = Message.AuthenticateFail();
                    return Redirect(this.Request.UrlReferrer.ToString());
                }
            }
            TempData["DangerMessage"] = Message.ConnectFail();
            return Redirect(this.Request.UrlReferrer.ToString());
        }
    }
}