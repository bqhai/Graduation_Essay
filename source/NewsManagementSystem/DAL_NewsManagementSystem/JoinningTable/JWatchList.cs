using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DAL_NewsManagementSystem.JoinningTable
{
    public class JWatchList
    {
        public string FacebookID { get; set; }
        public string FacebookName { get; set; }
        public string FacebookUrl { get; set; }
        public string FacebookTypeID { get; set; }
        public string FacebookTypeName { get; set; }
        public string Description { get; set; }
        public bool Status { get; set; }
    }
}
