using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace UI_NewsManagementSystem.Models
{
    public class Filter
    {
        public string NewsLabelID { get; set; }
        public string SentimentLabelID { get; set; }
        public Nullable<System.DateTime> StartDate { get; set; }
        public Nullable<System.DateTime> EndDate { get; set; }
    }
}