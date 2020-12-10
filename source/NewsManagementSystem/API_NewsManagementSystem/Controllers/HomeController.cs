using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using System.Web.Http.Results;
using BLL_NewsManagementSystem.BLL;
using Models_NewsManagementSystem.MappingClass;

namespace API_NewsManagementSystem.Controllers
{
    [RoutePrefix("api/Home")]
    public class HomeController : ApiController
    {
        private WatchListBLL _bllWatchList = new WatchListBLL();
        private PostBLL _bllPost = new PostBLL();

        [HttpGet]
        [Route("GetAllWatchList")]
        public JsonResult<List<WatchListDTO>> GetAllWatchList()
        {
            List<WatchListDTO> blackListDtos = _bllWatchList.GetAllWatchList();
            return Json(blackListDtos);
        }

        [HttpGet]
        [Route("CheckExistInWatchList/{facebookID}")]
        public JsonResult<bool> CheckExistInWatchList(string facebookID)
        {
            return Json(_bllWatchList.CheckExistInWatchList(facebookID));
        }

        [HttpPost]
        [Route("AddToWatchList")]
        public JsonResult<bool> AddToWatchList(WatchListDTO watchListDto)
        {
            return Json(_bllWatchList.AddToWatchList(watchListDto));
        }

        [HttpGet]
        [Route("CheckExistPost/{postUrl}")]
        public JsonResult<bool> CheckExistPost(string postUrl)
        {
            return Json(_bllPost.CheckExistPost(postUrl));
        }

        [HttpPost]
        [Route("AddNewPost")]
        public JsonResult<bool> AddNewPost(PostDTO postDto)
        {
            return Json(_bllPost.AddNewPost(postDto));
        }

        [HttpPost]
        [Route("UpdatePost")]
        public JsonResult<bool> UpdatePost(PostDTO postDto)
        {
            return Json(_bllPost.UpdatePost(postDto));
        }

        [HttpPost]
        [Route("AddNewOrUpdateListPost")]
        public JsonResult<bool> AddNewOrUpdateListPost(List<PostDTO> postDtos)
        {
            return Json(_bllPost.AddNewOrUpdateListPost(postDtos));
        }
    }
}
