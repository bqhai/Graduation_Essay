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
        private EntityMapper<AutoCrawledPost, PostDTO> _mapToPostDto = new EntityMapper<AutoCrawledPost, PostDTO>();
        private EntityMapper<PostDTO, AutoCrawledPost> _mapToAutoCrawledPost = new EntityMapper<PostDTO, AutoCrawledPost>();
        public PostBLL()
        {

        }
        public bool AddNewOrUpdatePost (PostDTO postDto)
        {           
            try
            {
                AutoCrawledPost post = _mapToAutoCrawledPost.Translate(postDto);
                if (_dalPost.CheckExistAutoCrawledPost(postDto.PostUrl))
                {
                    _dalPost.UpdateAutoCrawledPost(post);
                }
                else
                {
                    post.PostID = AutoGenerate.PostID();
                    post.SentimentLabelID = "NEG";
                    _dalPost.AddNewAutoCrawledPost(post);
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
