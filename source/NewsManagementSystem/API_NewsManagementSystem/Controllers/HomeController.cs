using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using System.Web.Http.Results;
using PagedList;
using BLL_NewsManagementSystem.BLL;
using Models_NewsManagementSystem.DTO;
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
            return Json(_bllWatchList.GetAllWatchList());
        }

        [HttpGet]
        [Route("FilterWatchList/{facebookTypeID}/{status}")]
        public JsonResult<List<WatchListDTO>> FilterWatchList(string facebookTypeID, string status)
        {
            return Json(_bllWatchList.FilterWatchList(facebookTypeID, status));
        }

        [HttpGet]
        [Route("SearchWatchList/{keyword}")]
        public JsonResult<List<WatchListDTO>> SearchWatchList(string keyword)
        {
            return Json(_bllWatchList.SearchWatchList(keyword));
        }

        [HttpGet]
        [Route("GetWatchListItemByID/{facebookID}")]
        public JsonResult<WatchListDTO> GetWatchListItemByID(string facebookID)
        {
            return Json(_bllWatchList.GetWatchListItemByID(facebookID));
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

        [HttpPut]
        [Route("UpdateToWatchList")]
        public JsonResult<bool> UpdateToWatchList(WatchListDTO watchListDto)
        {
            return Json(_bllWatchList.UpdateToWatchList(watchListDto));
        }

        [HttpPut]
        [Route("Unfollow/{facebookID}")]
        public JsonResult<bool> Unfollow(string facebookID)
        {
            return Json(_bllWatchList.Unfollow(facebookID));
        }

        [HttpPut]
        [Route("Follow/{facebookID}")]
        public JsonResult<bool> Follow(string facebookID)
        {
            return Json(_bllWatchList.Follow(facebookID));
        }

        [HttpGet]
        [Route("GetAllPost")]
        public JsonResult<List<PostDTO>> GetAllPost()
        {
            return Json(_bllPost.GetAllPost());
        }

        [HttpGet]
        [Route("GetPost/{pageIndex}/{pageSize}")]
        public JsonResult<IPagedList<PostDTO>> GetPost(int pageIndex, int pageSize)
        {
            return Json(_bllPost.GetAllPost().ToPagedList(pageIndex, pageSize));
        }

        [HttpPost]
        [Route("FilterPost")]
        public JsonResult<List<PostDTO>> FilterPost(FilterDTO filterDto)
        {
            return Json(_bllPost.FilterPost(filterDto));
        }

        [HttpGet]
        [Route("SearchPost/{keyword}/{searchOption}")]
        public JsonResult<List<PostDTO>> SearchPost(string keyword, string searchOption)
        {
            return Json(_bllPost.SearchPost(keyword, searchOption));
        }

        [HttpGet]
        [Route("GetListPostByFacebookID/{facebookID}")]
        public JsonResult<List<PostDTO>> GetListPostByFacebookID(string facebookID)
        {
            return Json(_bllPost.GetListPostByFacebookID(facebookID));
        }

        [HttpGet]
        [Route("GetPostByID/{postID}")]
        public JsonResult<PostDTO> GetPostByID(string postID)
        {
            return Json(_bllPost.GetPostByID(postID));
        }

        [HttpGet]
        [Route("CheckExistPost")]
        public JsonResult<bool> CheckExistPost(PostDTO postDto)
        {
            return Json(_bllPost.CheckExistPost(postDto.PostUrl));
        }

        [HttpPost]
        [Route("AddNewPost")]
        public JsonResult<bool> AddNewPost(PostDTO postDto)
        {
            return Json(_bllPost.AddNewPost(postDto));
        }

        [HttpPut]
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

        [HttpDelete]
        [Route("RemovePost/{postID}")]
        public JsonResult<bool> RemovePost(string postID)
        {
            return Json(_bllPost.RemovePost(postID));
        }

        //[HttpDelete]
        //[Route("RemovePost")]
        //public JsonResult<bool> RemovePost(string[] listPostID)
        //{
        //    return Json(_bllPost.RemovePost(listPostID));
        //}

        [HttpDelete]
        [Route("RemovePost")]
        public JsonResult<bool> RemovePost(IEnumerable<PostDTO> postDtos)
        {
            return Json(_bllPost.RemovePost(postDtos));
        }
    }
}
