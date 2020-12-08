using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DAL_NewsManagementSystem.Models;
using DAL_NewsManagementSystem.JoinningTable;
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
                            FacebookTypeName = fbt.FacebookTypeName
                        };
            return query;
        }
        public bool CheckExistID(string facebookID)
        {
            WatchList watchList = _db.WatchLists.SingleOrDefault(b => b.FacebookID == facebookID);
            if(watchList != null)
            {
                return true;
            }
            return false;
        }
    }
}
