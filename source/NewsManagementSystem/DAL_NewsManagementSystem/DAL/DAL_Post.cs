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
        public DAL_Post()
        {
            
        }
        public void AddNewPost(Post post)
        {
            using(var db = new NewsManagementSystemEntities())
            {
                post.FacebookID = "viettan";
                db.Posts.Add(post);
                db.SaveChanges();
            }
            
        }
    }
}
