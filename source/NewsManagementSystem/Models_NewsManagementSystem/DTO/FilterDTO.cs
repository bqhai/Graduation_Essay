using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Models_NewsManagementSystem.DTO
{
    public class FilterDTO
    {
        public string NewsLabelID { get; set; }
        public string SentimentLabelID { get; set; }
        public Nullable<System.DateTime> StartDate { get; set; }
        public Nullable<System.DateTime> EndDate { get; set; }
    }
}
