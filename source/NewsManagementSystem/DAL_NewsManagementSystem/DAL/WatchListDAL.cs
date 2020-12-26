using DAL_NewsManagementSystem.JoinningTable;
using DAL_NewsManagementSystem.Models;
using System.Collections.Generic;
using System.Linq;
namespace DAL_NewsManagementSystem.DAL
{
    public class WatchListDAL
    {
        private NewsManagementSystemEntities _db = new NewsManagementSystemEntities();
        public WatchListDAL()
        {

        }
        public IEnumerable<JWatchList> GetAllWatchList()
        {
            var query = from wl in _db.WatchLists
                        join fbt in _db.FacebookTypes on wl.FacebookTypeID equals fbt.FacebookTypeID
                        select new JWatchList
                        {
                            FacebookID = wl.FacebookID,
                            FacebookName = wl.FacebookName,
                            FacebookUrl = wl.FacebookUrl,
                            FacebookTypeID = wl.FacebookTypeID,
                            FacebookTypeName = fbt.FacebookTypeName,
                            Status = wl.Status
                        };
            return query;
        }
        public JWatchList GetWatchListItemByID(string facebookID)
        {
            var query = (from wl in _db.WatchLists
                        join fbt in _db.FacebookTypes on wl.FacebookTypeID equals fbt.FacebookTypeID
                        where wl.FacebookID == facebookID
                        select new JWatchList
                        {
                            FacebookID = wl.FacebookID,
                            FacebookName = wl.FacebookName,
                            FacebookUrl = wl.FacebookUrl,
                            FacebookTypeID = wl.FacebookTypeID,
                            FacebookTypeName = fbt.FacebookTypeName,
                            Status = wl.Status
                        }).SingleOrDefault();
            return query;
        }
        public bool CheckExistInWatchList(string facebookID)
        {
            WatchList watchList = _db.WatchLists.SingleOrDefault(wl => wl.FacebookID == facebookID);
            if(watchList != null)
            {
                return true;
            }
            return false;
        }
        public void AddToWatchList(WatchList watchList)
        {
            _db.WatchLists.Add(watchList);
            _db.SaveChanges();
        }
        public void UpdateToWatchList(WatchList watchList)
        {
            WatchList wl = _db.WatchLists.SingleOrDefault(w => w.FacebookID == watchList.FacebookID);
            wl.FacebookName = watchList.FacebookName;
            wl.FacebookTypeID = watchList.FacebookTypeID;
            wl.Status = watchList.Status;
            _db.SaveChanges();
        }
    }
}
