//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace DAL_NewsManagementSystem.Models
{
    using System;
    using System.Collections.Generic;
    
    public partial class WatchList
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors")]
        public WatchList()
        {
            this.Posts = new HashSet<Post>();
        }
    
        public string FacebookID { get; set; }
        public string FacebookName { get; set; }
        public string FacebookUrl { get; set; }
        public string FacebookTypeID { get; set; }
        public bool Status { get; set; }
        public bool InBlackList { get; set; }
    
        public virtual FacebookType FacebookType { get; set; }
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<Post> Posts { get; set; }
    }
}
