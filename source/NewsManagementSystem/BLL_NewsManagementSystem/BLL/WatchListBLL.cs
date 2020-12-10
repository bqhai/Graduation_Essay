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
    public class WatchListBLL
    {
        private WatchListDAL _dalWatchList = new WatchListDAL();
        private EntityMapper<JWatchList, WatchListDTO>_mapToWatchListDto = new EntityMapper<JWatchList, WatchListDTO>();
        private EntityMapper<WatchListDTO, WatchList> _mapToWatchList = new EntityMapper<WatchListDTO, WatchList>();
        public WatchListBLL()
        {
        }
        public List<WatchListDTO> GetAllWatchList()
        {
            IEnumerable<JWatchList> watchLists = _dalWatchList.GetAllWatchList();
            List<WatchListDTO> watchListDtos = new List<WatchListDTO>();
            foreach (var item in watchLists)
            {
                watchListDtos.Add(_mapToWatchListDto.Translate(item));
            }
            return watchListDtos;
        }
        public bool CheckExistInWatchList(string facebookID)
        {
            return _dalWatchList.CheckExistInWatchList(facebookID);
        }
        public bool AddToWatchList(WatchListDTO watchListDto)
        {
            try
            {
                WatchList watchList = _mapToWatchList.Translate(watchListDto);
                _dalWatchList.AddToWatchList(watchList);
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }
    }
}
