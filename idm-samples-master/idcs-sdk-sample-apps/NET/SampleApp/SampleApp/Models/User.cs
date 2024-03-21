﻿/*
 *  Copyright (c) 2000, 2021, Oracle and/or its affiliates.
 *
 *   Licensed under the Universal Permissive License v 1.0 as shown at
 *   http://oss.oracle.com/licenses/upl.
 */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using IDCSClient;

namespace SampleApp.Models
{
    public class User
    {
        public string DisplayName { get; set; }
        public string IdDomain { get; set; }
        public string UserID { get; set; }
        public string Issuer { get; set; }
        public string Token { get; set; }
        public List<Group> Groups { get; set; }
        public List<AppRole> AppRoles { get; set; }
    }
}