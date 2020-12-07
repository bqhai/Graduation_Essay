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
        private BlackListBLL _bllBlackList = new BlackListBLL();
        private BLL_Post _bllPost = new BLL_Post();

        [HttpGet]
        [Route("GetAllBlackList")]
        public JsonResult<List<BlackListDto>> GetAllBlackList()
        {
            List<BlackListDto> blackListDtos = _bllBlackList.GetALlBlackList();
            return Json(blackListDtos);        
        }
        [HttpPost]
        [Route("AddNewOrUpdateListPost")]
        public JsonResult<bool> AddNewOrUpdateListPost(List<PostDto> postDtos)
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
