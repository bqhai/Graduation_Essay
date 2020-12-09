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
        [HttpPost]
        [Route("AddToWatchList")]
        public JsonResult<bool> AddToWatchList(WatchListDTO watchListDto)
        {
            return Json(_bllWatchList.AddToWatchList(watchListDto));
        }
        [HttpPost]
        [Route("AddNewOrUpdateListPost")]
        public JsonResult<bool> AddNewOrUpdateListPost(List<PostDTO> postDtos)
        {
            foreach (var item in postDtos)
            {
                bool result = _bllPost.AddNewOrUpdatePost(item);
                if (!result)
                {
                    return Json(false);
                }
            }
            return Json(true);       
        }
    }
}
