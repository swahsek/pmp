





# PMS Revamp1.2.2.0 - Changes in API (NEW)



This document captures all the changes that have been made in the API
endpoints during the PMS Revamp Release 1.2.2.0. These changes include
addition of new endpoints, deprecation of a few endpoints and also some
other changes.

Partner Management Service:






Policy Management Service:

  ------------------------------------------------------------------------------------------------------------------
  **API Path**                                         **Method**   **Description**              **Changes done in
                                                                                                 release-1.2.2.0**
  ---------------------------------------------------- ------------ ---------------------------- -------------------
  /policies                                            GET          Service to get policies      No changes made in
                                                                                                 release 1.2.2.0

  /policies                                            POST         Service to create a new      Handled missing
                                                                    authentication, data         \'Empty Array and
                                                                    sharing, or credential       Empty String\'
                                                                    policy.                      Schema Validation

  /policies/{policyId}                                 GET          Service to retrieve the      No changes made in
                                                                    details of a specific policy release 1.2.2.0
                                                                    by its ID.                   

  /policies/{policyId}                                 PUT          Service to update policy     No changes made in
                                                                    details                      release 1.2.2.0

  /policies/{policyId}                                 PATCH        This endpoint deactivates a  Newly added in
                                                                    policy based on the Policy   release 1.2.2.0
                                                                    Id. It checks if any policy  
                                                                    requests are associated with 
                                                                    the policy: it can be        
                                                                    deactivated if there are no  
                                                                    requests or if there are     
                                                                    rejected requests. It cannot 
                                                                    be deactivated if there are  
                                                                    approved or pending          
                                                                    requests, returning error    
                                                                    codes PMS_POL_063 or         
                                                                    PMS_POL_064, respectively.   
                                                                    This endpoint is configured  
                                                                    for the **POLICYMANAGER** or 
                                                                    **PARTNER_ADMIN** roles.     

  /policies/{policyId}/group/{policygroupId}/publish   POST         Service to publish policy    No changes made in
                                                                                                 release 1.2.2.0

  /policies/active/group/{groupName}                   GET          Service to get active policy No changes made in
                                                                    details for policy group     release 1.2.2.0
                                                                    name                         

  /policies/group/{policygroupId}                      GET          Service to get policy group  No changes made in
                                                                                                 release 1.2.2.0

  /policies/group/{policyGroupId}                      PATCH        Service for Partner Admin    Newly added in
                                                                    users to deactivate a Policy release 1.2.2.0
                                                                    Group based on the Policy    
                                                                    Group Id. It is configured   
                                                                    for the **POLICYMANAGER** or 
                                                                    **PARTNER_ADMIN** roles.     

  /policies/group/new                                  POST         Service to create a new      No changes made in
                                                                    policy group                 release 1.2.2.0

  /policies/group/search                               POST         Service to search policy     No changes made in
                                                                    group                        release 1.2.2.0

  /policies/policy-groups                              GET          Service to retrieve details  Newly added in
                                                                    about all active Policy      release 1.2.2.0
                                                                    Groups                       

  /policies/v2                                         GET          Service to retrieve the list Newly added in
                                                                    of all Policies. It is       release 1.2.2.0
                                                                    configured for the           
                                                                    **POLICYMANAGER** or         
                                                                    **PARTNER_ADMIN** roles.     
  ------------------------------------------------------------------------------------------------------------------
