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
        private EntityMapper<Post, PostDTO> _mapToPostDto = new EntityMapper<Post, PostDTO>();
        private EntityMapper<PostDTO, Post> _mapToAutoCrawledPost = new EntityMapper<PostDTO, Post>();
        public PostBLL()
        {

        }
        public bool AddNewOrUpdatePost (PostDTO postDto)
        {
            Post post = _mapToAutoCrawledPost.Translate(postDto);
            if (_dalPost.CheckExistPost(postDto.PostUrl))
            {
                _dalPost.UpdatePost(post);
            }
            else
            {
                post.PostID = AutoGenerate.PostID();
                post.SentimentLabelID = "NEG";
                _dalPost.AddNewPost(post);
            }
            return true;
            //try
            //{
            //    Post post = _mapToAutoCrawledPost.Translate(postDto);
            //    if (_dalPost.CheckExistPost(postDto.PostUrl))
            //    {
            //        _dalPost.UpdatePost(post);
            //    }
            //    else
            //    {
            //        post.PostID = AutoGenerate.PostID();
            //        post.SentimentLabelID = "NEG";
            //        _dalPost.AddNewPost(post);
            //    }            
            //    return true;
            //}
            //catch (Exception)
            //{
            //    return false;
            //}
        }

    }
}
