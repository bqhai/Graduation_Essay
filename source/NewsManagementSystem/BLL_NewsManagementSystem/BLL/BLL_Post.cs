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
        DAL_Post dalPost = new DAL_Post();
        EntityMapper<Post, PostDto> mapToPostDto = new EntityMapper<Post, PostDto>();
        EntityMapper<PostDto, Post> mapToPost = new EntityMapper<PostDto, Post>();
        public BLL_Post()
        {

        }
        public bool AddNewPost(PostDto postDto)
        {
            try
            {
                Post post = mapToPost.Translate(postDto);
                dalPost.AddNewPost(post);
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }

    }
}
