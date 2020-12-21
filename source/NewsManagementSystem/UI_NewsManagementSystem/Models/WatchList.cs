using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace UI_NewsManagementSystem.Models
{
    public class WatchList
    {
        public string FacebookID { get; set; }
        public string FacebookName { get; set; }
        public string FacebookUrl { get; set; }
        public string FacebookTypeID { get; set; }
        public string FacebookTypeName { get; set; }
        public bool Status { get; set; }
        public bool InBlackList { get; set; }
    }
}
