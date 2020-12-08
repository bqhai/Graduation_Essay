using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AutoMapper;
using DAL_NewsManagementSystem.JoinningTable;
using DAL_NewsManagementSystem.Models;
using Models_NewsManagementSystem.MappingClass;

namespace Models_NewsManagementSystem.Repository
{
    public class EntityMapper<TSource, TDestination> where TSource:class where TDestination:class
    {
        public EntityMapper()
        {
            Mapper.CreateMap<JBlackList, BlackListDTO>();
            Mapper.CreateMap<BlackListDTO, JBlackList>();

            Mapper.CreateMap<Post, PostDTO>();
            Mapper.CreateMap<PostDTO, Post>();
        }
        public TDestination Translate(TSource obj)
        {
            return Mapper.Map<TDestination>(obj);
        }
    }
}
