using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DAL_NewsManagementSystem.Models;
using DAL_NewsManagementSystem.DAL;
using Models_NewsManagementSystem.MappingClass;
using Models_NewsManagementSystem.Repository;

namespace BLL_NewsManagementSystem.BLL
{
    public class BLL_Post
    {
        private DAL_Post _dalPost = new DAL_Post();
        private EntityMapper<Post, PostDto> _mapToPostDto = new EntityMapper<Post, PostDto>();
        private EntityMapper<PostDto, Post> _mapToPost = new EntityMapper<PostDto, Post>();
        public BLL_Post()
        {

        }
        public bool AddNewPost(PostDto postDto)
        {
            try
            {
                Post post = _mapToPost.Translate(postDto);
                _dalPost.AddNewPost(post);
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }

    }
}
