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
        public ActionResult WatchList(int pageIndex = 1, int pageSize = 11)
        {
            var response = _apiService.GetResponse("api/Home/GetAllWatchList");
            if (response.IsSuccessStatusCode)
            {
                var result = response.Content.ReadAsAsync<List<WatchList>>().Result;
                ViewBag.Count = result.Count;
                return View(result.ToPagedList(pageIndex, pageSize));
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return RedirectToAction("Index", "Home");
        }
        public string GetIdFromUrl(string url)
        {
            var arr = url.Split('/');
            if (arr[arr.Length - 1] == string.Empty)
            {
                return arr[arr.Length - 2];
            }
            else
            {
                return arr[arr.Length - 1];
            }
        }
        public bool CheckExistInWatchList(string facebookUrl)
        {
            string facebookID = GetIdFromUrl(facebookUrl);
            var response = _apiService.GetResponse("api/Home/CheckExistInWatchList/" + facebookID + "/");
            return response.Content.ReadAsAsync<bool>().Result; //true: exits -- false: ok we can add now
        }
        public ActionResult AddToWatchList(WatchList watchList)
        {
            if (CheckExistInWatchList(watchList.FacebookUrl))
            {
                TempData["WarningMessage"] = "Link facebook đã tồn tại";
                return Redirect(Request.UrlReferrer.ToString());
            }
            watchList.FacebookID = GetIdFromUrl(watchList.FacebookUrl);
            var response = _apiService.PostResponse("api/Home/AddToWatchList", watchList);
            if (response.IsSuccessStatusCode)
            {
                var result = response.Content.ReadAsAsync<bool>().Result;
                if (result)
                {
                    TempData["SuccessMessage"] = Message.AddItemSuccessful();
                    return Redirect(Request.UrlReferrer.ToString());
                }
                TempData["DangerMessage"] = Message.AddItemFaled();
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return Redirect(Request.UrlReferrer.ToString());
        }
        public ActionResult UpdateToWatchList(WatchList watchList)
        {
            var response = _apiService.PutResponse("api/Home/UpdateToWatchList", watchList);
            if (response.IsSuccessStatusCode)
            {
                var result = response.Content.ReadAsAsync<bool>().Result;
                if (result)
                {
                    TempData["SuccessMessage"] = Message.UpdateItemSuccessful();
                    return Redirect(Request.UrlReferrer.ToString());
                }
                TempData["DangerMessage"] = Message.UpdateItemFaled();
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return Redirect(Request.UrlReferrer.ToString());
        }
        #endregion

        #region Post
        public ActionResult Post(int pageIndex = 1, int pageSize = 11)
        {
            var response = _apiService.GetResponse("api/Home/GetAllPost");
            if (response.IsSuccessStatusCode)
            {
                var result = response.Content.ReadAsAsync<List<Post>>().Result;
                ViewBag.Count = result.Count;
                return View(result.ToPagedList(pageIndex, pageSize));
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return RedirectToAction("Index", "Home");
        }
        #endregion
    }
}