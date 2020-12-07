using DAL_NewsManagementSystem.Models;
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
        public void AddNewAutoCrawledPost(AutoCrawledPost acPost)
        {
            _db.AutoCrawledPosts.Add(acPost);
            _db.SaveChanges();
        }
        public void UpdateAutoCrawledPost(AutoCrawledPost acPost)
        {
            AutoCrawledPost acp = _db.AutoCrawledPosts.SingleOrDefault(p => p.PostUrl == acPost.PostUrl);
            acp.PostContent = acPost.PostContent;
            acp.TotalLikes = acPost.TotalLikes;
            acp.TotalComment = acPost.TotalComment;
            acp.TotalShare = acPost.TotalShare;
            _db.SaveChanges();
        }
        public bool CheckExistAutoCrawledPost(string postUrl)
        {
            AutoCrawledPost acp = _db.AutoCrawledPosts.SingleOrDefault(p => p.PostUrl == postUrl);
            if(acp != null)
            {
                return true;
            }
            return false;
        }
    }
}
