using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Models_NewsManagementSystem.MappingClass
{
    public class PostDto
    {
        public string PostID { get; set; }
        public string PostUrl { get; set; }
        public string UserUrl { get; set; }
        public string ProfileName { get; set; }
        public string PostContent { get; set; }
        public string Time { get; set; }
        public int TotalLikes { get; set; }
        public int TotalComment { get; set; }
        public int TotalShare { get; set; }
        public string FacebookID { get; set; }
        public string NewsLabelID { get; set; }
        public string SentimentLabelID { get; set; }

    }
}
