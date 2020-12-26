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
        public List<WatchList> GetWatchList()
        {
            var response = _apiService.GetResponse("api/Home/GetAllWatchList");
            if (response.IsSuccessStatusCode)
            {
                return response.Content.ReadAsAsync<List<WatchList>>().Result;
            }
            return null;
        }
        public List<WatchList> GetFilterWatchList(string facebookTypeID, string status)
        {
            var response = _apiService.GetResponse("api/Home/FilterWatchList/" + facebookTypeID + "/" + status + "/");
            if (response.IsSuccessStatusCode)
            {
                return response.Content.ReadAsAsync<List<WatchList>>().Result;
            }
            return null;
        }
        public ActionResult WatchList(int pageIndex = 1, int pageSize = 11)
        {
            var watchList = GetWatchList();
            if (watchList != null)
            {
                ViewBag.Count = watchList.Count;
                ViewBag.State = "All";
                return View(watchList.ToPagedList(pageIndex, pageSize));
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return RedirectToAction("Index", "Home");
        }
        public ActionResult FilterWatchList(string facebookTypeID, string status, int pageIndex = 1, int pageSize = 11)
        {
            var watchList = GetFilterWatchList(facebookTypeID, status);
            if (watchList != null)
            {
                ViewBag.Count = watchList.Count;
                ViewBag.FacebookTypeID = facebookTypeID;
                ViewBag.Status = status;
                ViewBag.State = "Filter";
                return View("~/Views/Home/WatchList.cshtml", watchList.ToPagedList(pageIndex, pageSize));
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return RedirectToAction("Index", "Home");
        }
        public ActionResult SearchWatchList(string keyword, int pageIndex = 1, int pageSize = 11)
        {
            var response = _apiService.GetResponse("api/Home/SearchWatchList/" + keyword + "/");
            if (response.IsSuccessStatusCode)
            {
                var result = response.Content.ReadAsAsync<List<WatchList>>().Result;
                ViewBag.Count = result.Count;
                ViewBag.Keyword = keyword;
                ViewBag.State = "Search";
                return View("~/Views/Home/WatchList.cshtml", result.ToPagedList(pageIndex, pageSize));
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
        public int CheckExistInWatchList(string facebookUrl)
        {
            string facebookID = GetIdFromUrl(facebookUrl);
            var response = _apiService.GetResponse("api/Home/CheckExistInWatchList/" + facebookID + "/");
            if (response.IsSuccessStatusCode)
            {
                if (response.Content.ReadAsAsync<bool>().Result) //true: exits -- false: ok we can add now
                    return 1;
                else
                    return -1;
            }
            return 404;
        }
        public ActionResult AddToWatchList(WatchList watchList)
        {
            int check = CheckExistInWatchList(watchList.FacebookUrl);
            if (check == 1)
            {
                TempData["WarningMessage"] = "Link facebook đã tồn tại";
                return RedirectToAction("WatchList", "Home");
            }
            else if (check == 404)
            {
                TempData["WarningMessage"] = "Link facebook không được chưa ký tự đặc biệt";
                return RedirectToAction("WatchList", "Home");
            }
            watchList.FacebookID = GetIdFromUrl(watchList.FacebookUrl);
            var response = _apiService.PostResponse("api/Home/AddToWatchList", watchList);
            if (response.IsSuccessStatusCode)
            {
                var result = response.Content.ReadAsAsync<bool>().Result;
                if (result)
                {
                    TempData["SuccessMessage"] = Message.AddItemSuccessful();
                    return RedirectToAction("WatchList", "Home");
                }
                TempData["DangerMessage"] = Message.AddItemFaled();
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return RedirectToAction("WatchList", "Home");
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
                    return RedirectToAction("WatchList", "Home");
                }
                TempData["DangerMessage"] = Message.UpdateItemFaled();
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return RedirectToAction("WatchList", "Home");
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
                ViewBag.State = "All";
                return View(result.ToPagedList(pageIndex, pageSize));
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return RedirectToAction("Index", "Home");
        }
        public ActionResult FilterPost(string newsLabelID, string sentimentLabelID, int pageIndex = 1, int pageSize = 11)
        {
            var response = _apiService.GetResponse("api/Home/FilterPost/" + newsLabelID + "/" + sentimentLabelID + "/");
            if (response.IsSuccessStatusCode)
            {
                var result = response.Content.ReadAsAsync<List<Post>>().Result;
                ViewBag.Count = result.Count;
                ViewBag.NewsLabelID = newsLabelID;
                ViewBag.SentimentLabelID = sentimentLabelID;
                ViewBag.State = "Filter";
                return View("~/Views/Home/Post.cshtml", result.ToPagedList(pageIndex, pageSize));
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return RedirectToAction("Index", "Home");
        }
        public ActionResult SearchPost(string keyword, int pageIndex = 1, int pageSize = 11)
        {
            var response = _apiService.GetResponse("api/Home/SearchPost/" + keyword + "/");
            if (response.IsSuccessStatusCode)
            {
                var result = response.Content.ReadAsAsync<List<Post>>().Result;
                ViewBag.Count = result.Count;
                ViewBag.Keyword = keyword;
                ViewBag.State = "Search";
                return View("~/Views/Home/Post.cshtml", result.ToPagedList(pageIndex, pageSize));
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return RedirectToAction("Index", "Home");
        }
        #endregion
    }
}