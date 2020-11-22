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
        BLL_BlackList bllBlackList = new BLL_BlackList();
        BLL_Post bllPost = new BLL_Post();

        [HttpGet]
        [Route("GetAllBlackList")]
        public JsonResult<List<BlackListDto>> GetAllBlackList()
        {
            List<BlackListDto> blackListDtos = bllBlackList.GetALlBlackList();
            return Json(blackListDtos);        
        }
        [HttpPost]
        [Route("GetAllBlackList")]
        public JsonResult<bool> AddNewPost(PostDto postDto)
        {
            bool result = bllPost.AddNewPost(postDto);
            return Json(result);
        }
    }
}
