using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DAL_NewsManagementSystem.Models;
using DAL_NewsManagementSystem.DAL;
using Models_NewsManagementSystem.MappingClass;
using Models_NewsManagementSystem.Repository;
using BLL_NewsManagementSystem.Lib;

namespace BLL_NewsManagementSystem.BLL
{
    public class PostBLL
    {
        private PostDAL _dalPost = new PostDAL();
        private WatchListDAL _dalWatchList = new WatchListDAL();
        private EntityMapper<Post, PostDTO> _mapToPostDto = new EntityMapper<Post, PostDTO>();
        private EntityMapper<PostDTO, Post> _mapToPost = new EntityMapper<PostDTO, Post>();
        public PostBLL()
        {

        }
        public bool CheckExistPost(string postUrl)
        {
            return _dalPost.CheckExistPost(postUrl);
        }
        public bool AddNewPost(PostDTO postDto)
        {
            try
            {
                Post post = _mapToPost.Translate(postDto);
                post.PostID = AutoGenerate.PostID();
                if (_dalWatchList.CheckExistInWatchList(postDto.FacebookID))
                {              
                    _dalPost.AddNewPost(post);
                }
                else
                {
                    WatchList watchList = new WatchList()
                    {
                        FacebookID = postDto.FacebookID,
                        FacebookName = postDto.ProfileName,
                        FacebookUrl = postDto.UserUrl,
                        FacebookTypeID = postDto.FacebookTypeID
                    };
                    _dalWatchList.AddToWatchList(watchList);
                    _dalPost.AddNewPost(post);
                }
               
                return true;
            }
            catch (Exception)
            {
                return false;
            }
            
        }
        public bool UpdatePost(PostDTO postDto)
        {
            try
            {
                Post post = _mapToPost.Translate(postDto);
                _dalPost.UpdatePost(post);
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }
        public bool AddNewOrUpdateListPost(List<PostDTO> postDtos)
        {
            //step 1: check ID exits in Post -> then update / add new
            //step 2: if add new -> check FacebookID exits in WatchList -> if not then add facebookID before add post           
            try
            {               
                foreach (var item in postDtos)
                {
                    if (CheckExistPost(item.PostUrl))
                    {
                        UpdatePost(item);
                    }
                    else
                    {
                        item.PostID = AutoGenerate.PostID();
                        item.SentimentLabelID = "NEG";
                        AddNewPost(item);
                    }
                }                
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }

    }
}
