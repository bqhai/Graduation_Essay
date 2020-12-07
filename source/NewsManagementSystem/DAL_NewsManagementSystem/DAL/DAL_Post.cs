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
        public void AddNewPost(AutoCrawledPost post)
        {
            _db.AutoCrawledPosts.Add(post);
            _db.SaveChanges();
        }
        public void UpdatePost(AutoCrawledPost post)
        {
            AutoCrawledPost po = _db.AutoCrawledPosts.SingleOrDefault(p => p.PostUrl == post.PostUrl);
            po.PostContent = post.PostContent;
            po.TotalLikes = post.TotalLikes;
            po.TotalComment = post.TotalComment;
            po.TotalShare = post.TotalShare;
            _db.SaveChanges();
        }
        public bool CheckExistPost(string postUrl)
        {
            AutoCrawledPost po = _db.AutoCrawledPosts.SingleOrDefault(p => p.PostUrl == postUrl);
            if(po != null)
            {
                return true;
            }
            return false;
        }
    }
}
