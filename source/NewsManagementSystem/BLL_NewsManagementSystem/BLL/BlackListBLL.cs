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
    public class BlackListBLL
    {
        private BlackListDAL _dalBlackList = new BlackListDAL();
        private EntityMapper<JBlackList, BlackListDTO>_mapToBlackListDto = new EntityMapper<JBlackList, BlackListDTO>();

        public BlackListBLL()
        {
        }
        public List<BlackListDTO> GetALlBlackList()
        {
            IEnumerable<JBlackList> blackLists = _dalBlackList.GetAllBlackList();
            List<BlackListDTO> blackListDtos = new List<BlackListDTO>();
            foreach (var item in blackLists)
            {
                blackListDtos.Add(_mapToBlackListDto.Translate(item));
            }
            return blackListDtos;
        }
    }
}
