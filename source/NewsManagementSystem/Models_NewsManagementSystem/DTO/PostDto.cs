using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Models_NewsManagementSystem.MappingClass
{
    public class PostDTO
    {
        public string PostID { get; set; }
        public string PostUrl { get; set; }
        public string UserUrl { get; set; }
        public string PostContent { get; set; }
        public string Image { get; set; }
        public string UploadTime { get; set; }
        public Nullable<int> TotalLikes { get; set; }
        public Nullable<int> TotalComment { get; set; }
        public Nullable<int> TotalShare { get; set; }
        public string FacebookID { get; set; }
        public string NewsLabelID { get; set; }
        public string SentimentLabelID { get; set; }
        public string FacebookName { get; set; }
        public string NewsLabelName { get; set; }
        public string SentimentLabelName { get; set; }

    }
}
