using DAL_NewsManagementSystem.Models;
using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DAL_NewsManagementSystem.DAL
{
    public class DAL_Post
    {
        private NewsManagementSystemEntities _db = new NewsManagementSystemEntities();
        public DAL_Post()
        {

        }
        public void AddNewPost(Post post)
        {
            post.FacebookID = "viettan";
            _db.Posts.Add(post);
            _db.SaveChanges();
        }
    }
}
