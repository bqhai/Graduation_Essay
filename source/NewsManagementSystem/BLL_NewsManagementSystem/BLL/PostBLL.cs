﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DAL_NewsManagementSystem.Models;
using DAL_NewsManagementSystem.DAL;
using Models_NewsManagementSystem.MappingClass;
using Models_NewsManagementSystem.Repository;
using BLL_NewsManagementSystem.Lib;
using DAL_NewsManagementSystem.JoinningTable;

namespace BLL_NewsManagementSystem.BLL
{
    public class PostBLL
    {
        private PostDAL _dalPost = new PostDAL();
        private EntityMapper<JPost, PostDTO> _mapToPostDto = new EntityMapper<JPost, PostDTO>();
        private EntityMapper<PostDTO, Post> _mapToPost = new EntityMapper<PostDTO, Post>();
        public PostBLL()
        {

        }
        public List<PostDTO> GetAllPost()
        {
            IEnumerable<JPost> posts = _dalPost.GetAllPost();
            List<PostDTO> postDTOs = new List<PostDTO>();
            foreach (var item in posts)
            {
                postDTOs.Add(_mapToPostDto.Translate(item));
            }
            return postDTOs;
        }
        public List<PostDTO> FilterPost(string newsLabelID, string sentimentLabelID)
        {
            if (newsLabelID.Equals("ALL", StringComparison.InvariantCultureIgnoreCase) && sentimentLabelID.Equals("ALL", StringComparison.InvariantCultureIgnoreCase))
            {
                return GetAllPost();
            }
            if (newsLabelID.Equals("ALL", StringComparison.InvariantCultureIgnoreCase))
            {
                return GetAllPost().Where(po => po.NewsLabelID == po.NewsLabelID && po.SentimentLabelID == sentimentLabelID).ToList();
            }
            else if (sentimentLabelID.Equals("ALL", StringComparison.InvariantCultureIgnoreCase))
            {
                return GetAllPost().Where(po => po.NewsLabelID == newsLabelID && po.SentimentLabelID == po.SentimentLabelID).ToList();
            }
            else
            {
                return GetAllPost().Where(po => po.NewsLabelID == newsLabelID && po.SentimentLabelID == sentimentLabelID).ToList();
            }
        }
        public List<PostDTO> SearchPost(string keyword, string searchOption)
        {
            if(searchOption.Equals("post", StringComparison.InvariantCultureIgnoreCase) || searchOption.Equals(string.Empty))
                return GetAllPost().Where(po => po.PostContent.IndexOf(keyword, StringComparison.CurrentCultureIgnoreCase) != -1).ToList();
            else
                return GetAllPost().Where(po => po.FacebookName.IndexOf(keyword, StringComparison.CurrentCultureIgnoreCase) != -1).ToList();
        }
        public List<PostDTO> GetListPostByFacebookID(string facebookID)
        {
            return GetAllPost().Where(po => po.FacebookID == facebookID).ToList();
        }
        public PostDTO GetPostByID(string postID)
        {
            return _mapToPostDto.Translate(_dalPost.GetPostByID(postID));
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
                _dalPost.AddNewPost(post);
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
                        Post post = _mapToPost.Translate(item);
                        _dalPost.UpdatePost(post);
                    }
                    else
                    {
                        Post post = _mapToPost.Translate(item);
                        post.PostID = AutoGenerate.PostID();
                        _dalPost.AddNewPost(post);
                    }
                }
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }
        public bool RemovePost(string postID)
        {
            try
            {
                _dalPost.RemovePost(postID);
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }
    }
}
