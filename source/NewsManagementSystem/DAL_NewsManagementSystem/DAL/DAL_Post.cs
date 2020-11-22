using DAL_NewsManagementSystem.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DAL_NewsManagementSystem.DAL
{
    public class DAL_Post
    {
        NewsManagementSystemEntities db = new NewsManagementSystemEntities();
        public DAL_Post()
        {
            db.Configuration.ProxyCreationEnabled = false;
        }
        public void AddNewPost(Post post)
        {
            post.FacebookID = "viettan";
            post.NewsLabelID = "CT";
            db.Posts.Add(post);
            db.SaveChanges();
        }
    }
}
