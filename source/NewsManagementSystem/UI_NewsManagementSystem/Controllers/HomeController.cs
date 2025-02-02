﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Web;
using System.Web.Mvc;
using UI_NewsManagementSystem.Models;
using UI_NewsManagementSystem.Repository;
using PagedList;
using System.Web.UI.WebControls;
using System.IO;
using System.Web.UI;
using System.Text;

namespace UI_NewsManagementSystem.Controllers
{
    public class HomeController : Controller
    {
        private ApiService _apiService = new ApiService();
        public ActionResult SetPageSize(int pageSize)
        {
            HttpCookie cookie = new HttpCookie("PageSize", pageSize.ToString());
            cookie.Expires.AddDays(7);
            Response.Cookies.Add(cookie);
            return Redirect(Request.UrlReferrer.ToString());
        }
        private int GetPageSize()
        {
            HttpCookie cookie = Request.Cookies["PageSize"];
            if (cookie == null)
            {
                return 11;
            }
            else
            {
                return Convert.ToInt32(cookie.Value);
            }
        }
        public ActionResult Index()
        {
            if (Session["Account"] == null)
                return RedirectToAction("Login", "Account");
            return View();
        }

        #region WatchList
        private List<WatchList> GetWatchList()
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
            if(Session["Account"] == null)
                return RedirectToAction("Login", "Account");
            var watchList = GetWatchList().Where(wl => wl.Status == true).ToList();
            if (watchList != null)
            {
                ViewBag.Count = watchList.Count;
                ViewBag.Status = true;
                ViewBag.State = "All";
                return View(watchList.Where(wl => wl.Status == true).ToPagedList(pageIndex, pageSize));
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return RedirectToAction("Index", "Home");
        }
        public ActionResult FilterWatchList(string facebookTypeID, string status, int pageIndex = 1, int pageSize = 11)
        {
            if (Session["Account"] == null)
                return RedirectToAction("Login", "Account");
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
            if (Session["Account"] == null)
                return RedirectToAction("Login", "Account");
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
        private string GetIdFromUrl(string url)
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
        private int CheckExistInWatchList(string facebookUrl)
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
            if (Session["Account"] == null)
                return RedirectToAction("Login", "Account");
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
            if (Session["Account"] == null)
                return RedirectToAction("Login", "Account");
            var response = _apiService.PostResponse("api/Home/UpdateToWatchList", watchList);
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
        private List<Post> GetAllPost()
        {
            var response = _apiService.GetResponse("api/Home/GetAllPost");
            if (response.IsSuccessStatusCode)
            {
                 return response.Content.ReadAsAsync<List<Post>>().Result;               
            }
            return null;
        }
        public ActionResult Post(int pageIndex = 1)
        {
            if (Session["Account"] == null)
                return RedirectToAction("Login", "Account");
            var listPost = GetAllPost();
            var pageSize = GetPageSize();
            if (listPost != null)
            {
                ViewBag.Count = listPost.Count;
                ViewBag.State = "All";
                ViewBag.PageSize = pageSize;
                Session["Post"] = listPost.ToPagedList(pageIndex, pageSize);
                return View(listPost.ToPagedList(pageIndex, pageSize));
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return RedirectToAction("Index", "Home");
        }
        public ActionResult FilterPost(string newsLabelID, string sentimentLabelID, Nullable<DateTime> startDate, Nullable<DateTime> endDate,  int pageIndex = 1)
        {
            if (Session["Account"] == null)
                return RedirectToAction("Login", "Account");
            Models.Filter filter = new Models.Filter
            {
                NewsLabelID = newsLabelID,
                SentimentLabelID = sentimentLabelID,
                StartDate = startDate,
                EndDate = endDate
            };
            var response = _apiService.GetResponse("api/Home/FilterPost/", filter);
            var pageSize = GetPageSize();
            if (response.IsSuccessStatusCode)
            {
                var result = response.Content.ReadAsAsync<List<Post>>().Result;
                ViewBag.Count = result.Count;
                ViewBag.NewsLabelID = newsLabelID;
                ViewBag.SentimentLabelID = sentimentLabelID;
                ViewBag.StartDate = startDate;
                ViewBag.EndDate = endDate;
                ViewBag.State = "Filter";
                ViewBag.PageSize = pageSize;
                Session["Post"] = result.ToPagedList(pageIndex, pageSize);
                return View("~/Views/Home/Post.cshtml", result.ToPagedList(pageIndex, pageSize));
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return RedirectToAction("Index", "Home");
        }
        public ActionResult SearchPost(string keyword, string searchOption, int pageIndex = 1)
        {
            if (Session["Account"] == null)
                return RedirectToAction("Login", "Account");
            var response = _apiService.GetResponse("api/Home/SearchPost/" + keyword + "/" + searchOption + "/");
            var pageSize = GetPageSize();
            if (response.IsSuccessStatusCode)
            {
                var result = response.Content.ReadAsAsync<List<Post>>().Result;
                ViewBag.Count = result.Count;
                ViewBag.Keyword = keyword;
                ViewBag.SearchOption = searchOption;
                ViewBag.State = "Search";
                ViewBag.PageSize = pageSize;
                Session["Post"] = result.ToPagedList(pageIndex, pageSize);
                return View("~/Views/Home/Post.cshtml", result.ToPagedList(pageIndex, pageSize));
            }
            TempData["DangerMessage"] = Message.ConnectFailed();
            return RedirectToAction("Index", "Home");
        }
        public ActionResult ExcelExport()
        {
            var gv = new GridView();
            gv.DataSource = Session["Post"];
            gv.DataBind();
            Response.ClearContent();
            Response.Buffer = true;
            Response.AddHeader("content-disposition", "attachment; filename=DanhSachBaiViet.xls");
            Response.ContentType = "application/ms-excel";
            Response.Charset = "";
            StringWriter objStringWriter = new StringWriter();
            HtmlTextWriter objHtmlTextWriter = new HtmlTextWriter(objStringWriter);
            gv.RenderControl(objHtmlTextWriter);
            Response.Write(objStringWriter.ToString());
            Response.Flush();
            Response.End();
            return Redirect(Request.UrlReferrer.ToString());
        }
        public ActionResult CsvExport()
        {
            var sb = new StringBuilder();
            var listPost = (Session["Post"] as IPagedList<Post>);           
            sb.AppendFormat("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}", 
                "ID bài viết", 
                "URL bài viết", 
                "URL người đăng", 
                "Nội dung", 
                "URL hình ảnh", 
                "Thời gian đăng", 
                "Thời gian thu thập",
                "Like",
                "Comment",
                "Share",
                "Nơi thu thập",
                "URL Nơi thu thập",
                "Nhãn bài viết",
                "Mức độ",
                Environment.NewLine);
            foreach (var item in listPost)
            {
                sb.AppendFormat("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}", 
                    item.PostID,
                    item.PostUrl,
                    item.UserUrl,
                    item.PostContent,
                    item.Image,
                    item.UploadTime,
                    item.CrawledTime,
                    item.TotalLikes,
                    item.TotalComment,
                    item.TotalShare,
                    item.FacebookName,
                    item.FacebookUrl,
                    item.NewsLabelName,
                    item.SentimentLabelName,
                    Environment.NewLine);
            }
            var response = System.Web.HttpContext.Current.Response;
            response.BufferOutput = true;
            response.Clear();
            response.ClearHeaders();
            response.ContentEncoding = Encoding.UTF8;
            response.AddHeader("content-disposition", "attachment;filename=DanhSachBaiViet.csv");
            response.ContentType = "text/plain";
            response.Write(sb.ToString());
            response.End();
            return Redirect(Request.UrlReferrer.ToString());
        }
        #endregion

        #region Analysis
        private List<Post> GetListPostByFacebookID(string facebookID)
        {
            var response = _apiService.GetResponse("api/Home/GetListPostByFacebookID/" + facebookID + "/");
            if (response.IsSuccessStatusCode)
            {
                return response.Content.ReadAsAsync<List<Post>>().Result;
            }
            return null;
        }
        public ActionResult Analysis(string facebookID)
        {
            if (Session["Account"] == null)
                return RedirectToAction("Login", "Account");
            var watchlist = GetWatchList();
            var listPost = GetAllPost();
            Analysis analysis = new Analysis()
            {
                NumberOfWatchList = watchlist.Count,
                NumberOfPost = listPost.Count,
                NumberOfPositivePost = listPost.Where(po => po.SentimentLabelID == "POS").ToList().Count,
                NumberOfNegativePost = listPost.Where(po => po.SentimentLabelID == "NEG").ToList().Count
            };
            if (facebookID != null)
            {
                var listPostByID = GetListPostByFacebookID(facebookID);
                if (listPostByID.Count > 0)
                {
                    ViewBag.ListPost = listPostByID;
                    ViewBag.TopInteractive = listPostByID.OrderByDescending(po => po.TotalLikes + po.TotalComment + po.TotalShare).Take(8).ToList();
                    ViewBag.FacebookName = listPostByID.Select(po => po.FacebookName).Take(1).ToList()[0];
                }                  
                else
                    TempData["WarningMessage"] = "Đối tượng này chưa có dữ liệu";
            }                          
            return View(analysis);
        }
        #endregion
    }
}