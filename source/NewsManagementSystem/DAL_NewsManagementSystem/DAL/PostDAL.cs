﻿using DAL_NewsManagementSystem.Models;
using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DAL_NewsManagementSystem.DAL
{
    public class PostDAL
    {
        private NewsManagementSystemEntities _db = new NewsManagementSystemEntities();
        public PostDAL()
        {

        }
        public void AddNewPost(Post post)
        {
            _db.Posts.Add(post);
            _db.SaveChanges();
        }
        public void UpdatePost(Post post)
        {
            Post po = _db.Posts.SingleOrDefault(p => p.PostUrl == post.PostUrl);
            po.PostContent = post.PostContent;
            po.TotalLikes = post.TotalLikes;
            po.TotalComment = post.TotalComment;
            po.TotalShare = post.TotalShare;
            _db.SaveChanges();
        }
        public bool CheckExistPost(string postUrl)
        {
            Post po = _db.Posts.SingleOrDefault(p => p.PostUrl == postUrl);
            if(po != null)
            {
                return true;
            }
            return false;
        }
    }
}
