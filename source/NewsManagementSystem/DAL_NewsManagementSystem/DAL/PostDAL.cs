using DAL_NewsManagementSystem.JoinningTable;
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
        public IEnumerable<JPost> GetAllPost()
        {
            var query = from po in _db.Posts
                        join wl in _db.WatchLists on po.FacebookID equals wl.FacebookID
                        join nlb in _db.NewsLabels on po.NewsLabelID equals nlb.NewsLabelID
                        join slb in _db.SentimentLabels on po.SentimentLabelID equals slb.SentimentLabelID
                        select new JPost
                        {
                            PostID = po.PostID,
                            PostUrl = po.PostUrl,
                            UserUrl = po.UserUrl,
                            PostContent = po.PostContent,
                            Image = po.Image,
                            UploadTime = po.UploadTime,
                            TotalLikes = po.TotalLikes,
                            TotalComment = po.TotalComment,
                            TotalShare = po.TotalShare,
                            FacebookID = po.FacebookID,
                            FacebookName = wl.FacebookName,
                            NewsLabelID = po.NewsLabelID,
                            NewsLabelName = nlb.NewsLabelName,
                            SentimentLabelID = po.SentimentLabelID,
                            SentimentLabelName = slb.SentimentLabelName
                        };
            return query;
        }
        public void AddNewPost(Post post)
        {
            _db.Posts.Add(post);
            _db.SaveChanges();
        }
        public void UpdatePost(Post post)
        {
            Post po = _db.Posts.SingleOrDefault(p => p.PostUrl == post.PostUrl);
            po.UserUrl = post.UserUrl;
            po.PostContent = post.PostContent;
            po.Image = post.Image;
            po.TotalLikes = post.TotalLikes;
            po.TotalComment = post.TotalComment;
            po.TotalShare = post.TotalShare;
            po.NewsLabelID = post.NewsLabelID;
            po.SentimentLabelID = post.SentimentLabelID;
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
        public void RemovePost(string postID)
        {
            Post post = _db.Posts.SingleOrDefault(p => p.PostID == postID);
            _db.Posts.Remove(post);
            _db.SaveChanges();
        }
    }
}
