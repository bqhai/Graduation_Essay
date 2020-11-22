using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AutoMapper;
using DAL_NewsManagementSystem.Models;

namespace Models_NewsManagementSystem.Repository
{
    public class EntityMapper<TSource, TDestination> where TSource:class where TDestination:class
    {
        public EntityMapper()
        {
            
        }
        public TDestination Translate(TSource obj)
        {
            return Mapper.Map<TDestination>(obj);
        }
    }
}
