using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Web;
using System.Web.Mvc;
using UI_NewsManagementSystem.Models;
using UI_NewsManagementSystem.Repository;
using PagedList;

namespace UI_NewsManagementSystem.Controllers
{
    public class HomeController : Controller
    {
        private ApiService _apiService = new ApiService();
        public ActionResult Index()
        {
            return View();
        }
        #region WatchList
        public ActionResult WatchList(int pageIndex = 1, int pageSize = 13)
        {
            var response = _apiService.GetResponse("api/Home/GetAllWatchList");
            if (response.IsSuccessStatusCode)
            {
                var result = response.Content.ReadAsAsync<List<WatchList>>().Result;
                return View(result.ToPagedList(pageIndex, pageSize));
            }
            return RedirectToAction("Index", "Home");
        }
        #endregion
    }
}