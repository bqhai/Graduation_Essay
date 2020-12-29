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
        public List<WatchListDTO> FilterWatchList(string facebookTypeID, string status)
        {
            bool st;
            if (status == "true")
                st = true;
            else
                st = false;
            if (facebookTypeID == "ALL" && status == "ALL")
            {
                return GetAllWatchList();
            }
            if (facebookTypeID == "ALL")
            {
                return GetAllWatchList().Where(wl => wl.FacebookTypeID == wl.FacebookTypeID && wl.Status == st).ToList();
            }
            else if (status == "ALL")
            {
                return GetAllWatchList().Where(wl => wl.FacebookTypeID == facebookTypeID && wl.Status == wl.Status).ToList();
            }
            else
            {
                return GetAllWatchList().Where(wl => wl.FacebookTypeID == facebookTypeID && wl.Status == st).ToList();
            }
        }
        public List<WatchListDTO> SearchWatchList(string keyword)
        {
            return GetAllWatchList().Where(wl => wl.FacebookName.IndexOf(keyword, StringComparison.CurrentCultureIgnoreCase) != -1).ToList();
        }
        public WatchListDTO GetWatchListItemByID(string facebookID)
        {
            JWatchList jWatchList = _dalWatchList.GetWatchListItemByID(facebookID);
            return _mapToWatchListDto.Translate(jWatchList);
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
                watchList.Status = true;
                _dalWatchList.AddToWatchList(watchList);
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }
        public bool UpdateToWatchList(WatchListDTO watchListDto)
        {
            try
            {
                WatchList watchList = _mapToWatchList.Translate(watchListDto);
                _dalWatchList.UpdateToWatchList(watchList);
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }
        public bool Unfollow(string facebookID)
        {
            try
            {
                _dalWatchList.Unfollow(facebookID);
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }
    }
}
