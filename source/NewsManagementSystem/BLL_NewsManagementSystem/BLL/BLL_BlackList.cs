using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DAL_NewsManagementSystem.Models;
using DAL_NewsManagementSystem.DAL;
using Models_NewsManagementSystem.MappingClass;
using Models_NewsManagementSystem.Repository;
using DAL_NewsManagementSystem.JoinningTable;

namespace BLL_NewsManagementSystem.BLL
{
    public class BLL_BlackList
    {
        private DAL_BlackList _dalBlackList = new DAL_BlackList();
        private EntityMapper<JBlackList, BlackListDto>_mapToBlackListDto = new EntityMapper<JBlackList, BlackListDto>();

        public BLL_BlackList()
        {
        }
        public List<BlackListDto> GetALlBlackList()
        {
            IEnumerable<JBlackList> blackLists = _dalBlackList.GetAllBlackList();
            List<BlackListDto> blackListDtos = new List<BlackListDto>();
            foreach (var item in blackLists)
            {
                blackListDtos.Add(_mapToBlackListDto.Translate(item));
            }
            return blackListDtos;
        }
    }
}
