using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DAL_NewsManagementSystem.Models;
using DAL_NewsManagementSystem.JoinningTable;
namespace DAL_NewsManagementSystem.DAL
{
    public class DAL_BlackList
    {
        NewsManagementSystemEntities db = new NewsManagementSystemEntities();
        public DAL_BlackList()
        {
            db.Configuration.ProxyCreationEnabled = false;
        }
        public IEnumerable<JBlackList> GetAllBlackList()
        {
            var query = from bll in db.BlackLists
                        join fbt in db.FacebookTypes on bll.FacebookTypeID equals fbt.FacebookTypeID
                        select new JBlackList
                        {
                            FacebookID = bll.FacebookID,
                            FacebookName = bll.FacebookName,
                            FacebookUrl = bll.FacebookUrl,
                            FacebookTypeID = bll.FacebookTypeID,
                            FacebookTypeName = fbt.FacebookTypeName
                        };
            return query;
        }
    }
}
