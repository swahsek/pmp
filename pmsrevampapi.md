


+-----------+---------+---------------------------+-------------------+
| **API     | **M     | **Description**           | **Changes done in |
| Path**    | ethod** |                           | release 1.2.2.0** |
+===========+=========+===========================+===================+
| /oau      | GET     | This endpoint retrieves a | Newly added in    |
| th/client |         | list of all OAuth clients | release 1.2.2.0   |
|           |         | created by the Auth       |                   |
|           |         | Partners. It supports     |                   |
|           |         | pagination, sorting, and  |                   |
|           |         | and filtering based on    |                   |
|           |         | optional query            |                   |
|           |         | parameters. If the token  |                   |
|           |         | used to access this       |                   |
|           |         | endpoint, does not have   |                   |
|           |         | the PARTNER_ADMIN role,   |                   |
|           |         | then it will fetch all    |                   |
|           |         | the OAuth clients created |                   |
|           |         | by all the partners       |                   |
|           |         | associated with the       |                   |
|           |         | logged in user only. If   |                   |
|           |         | the token used to access  |                   |
|           |         | this endpoint, has        |                   |
|           |         | PARTNER_ADMIN role, then  |                   |
|           |         | it will fetch all the     |                   |
|           |         | OAuth clients created by  |                   |
|           |         | all the partners. It is   |                   |
|           |         | configured for            |                   |
|           |         | **PARTNER_ADMIN** and     |                   |
|           |         | **AUTH_PARTNER** roles.   |                   |
+-----------+---------+---------------------------+-------------------+
| /oau      | POST    | This endpoint is used for | 1.  Added         |
| th/client |         | creating OIDC Client.     |     validation to |
|           |         |                           |     check the     |
|           |         |                           |     partner id in |
|           |         |                           |     the request   |
|           |         |                           |     body belongs  |
|           |         |                           |     to the user   |
|           |         |                           |     who's token   |
|           |         |                           |     is being used |
|           |         |                           |     to access     |
|           |         |                           |     this          |
|           |         |                           |     endpoint.     |
|           |         |                           |     This will     |
|           |         |                           |     ensure that   |
|           |         |                           |     PMS user can  |
|           |         |                           |     create OIDC   |
|           |         |                           |     client only   |
|           |         |                           |     for the       |
|           |         |                           |     partner id    |
|           |         |                           |     which belongs |
|           |         |                           |     to the user.  |
|           |         |                           |     This          |
|           |         |                           |     validation is |
|           |         |                           |     skipped if    |
|           |         |                           |     the user's    |
|           |         |                           |     role is       |
|           |         |                           |     *             |
|           |         |                           | *PARTNER_ADMIN**. |
|           |         |                           |                   |
|           |         |                           | 2.  Added         |
|           |         |                           |     validation to |
|           |         |                           |     check if the  |
|           |         |                           |     **Partner     |
|           |         |                           |     ID** used in  |
|           |         |                           |     the request   |
|           |         |                           |     body is       |
|           |         |                           |     active. This  |
|           |         |                           |     will ensure   |
|           |         |                           |     that OIDC     |
|           |         |                           |     client cannot |
|           |         |                           |     be created    |
|           |         |                           |     for an        |
|           |         |                           |     inactive      |
|           |         |                           |     partner.      |
|           |         |                           |     ([MOSIP-3427  |
|           |         |                           | 6](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-34276)) |
|           |         |                           |                   |
|           |         |                           | 3.  If multiple   |
|           |         |                           |     policy        |
|           |         |                           |     requests were |
|           |         |                           |     created by    |
|           |         |                           |     the partner   |
|           |         |                           |     for a policy, |
|           |         |                           |     then while    |
|           |         |                           |     creating the  |
|           |         |                           |     OIDC client,  |
|           |         |                           |     this endpoint |
|           |         |                           |     was checking  |
|           |         |                           |     the status of |
|           |         |                           |     only the      |
|           |         |                           |     first policy  |
|           |         |                           |     request. So   |
|           |         |                           |     even if there |
|           |         |                           |     was an        |
|           |         |                           |     approved      |
|           |         |                           |     policy        |
|           |         |                           |     request, it   |
|           |         |                           |     was still     |
|           |         |                           |     throwing an   |
|           |         |                           |     error. Fixed  |
|           |         |                           |     this bug      |
|           |         |                           |     ([MOSIP-3459  |
|           |         |                           | 9](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-34599)) |
|           |         |                           |                   |
|           |         |                           | 4.  Improved JWK  |
|           |         |                           |     validation    |
|           |         |                           |     for the       |
|           |         |                           |     public key by |
|           |         |                           |     adding        |
|           |         |                           |     validation    |
|           |         |                           |     that n value  |
|           |         |                           |     (modulus      |
|           |         |                           |     value) of the |
|           |         |                           |     JWK must be   |
|           |         |                           |     unique        |
|           |         |                           |     ([MOSIP-3621  |
|           |         |                           | 9](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-36219)) |
|           |         |                           |                   |
|           |         |                           | 5.  Updated       |
|           |         |                           |     client name   |
|           |         |                           |     to be a JSON  |
|           |         |                           |     string to     |
|           |         |                           |     support       |
|           |         |                           |     client name   |
|           |         |                           |     language map  |
|           |         |                           |     ([            |
|           |         |                           | ES-836](https://m |
|           |         |                           | osip.atlassian.ne |
|           |         |                           | t/browse/ES-836)) |
+-----------+---------+---------------------------+-------------------+
| /oauth/   | GET     | This endpoint retrieves   | 1.  Added         |
| client/{c |         | the OIDC client details   |     validation to |
| lient_id} |         | by client id              |     check the     |
|           |         |                           |     partner id in |
|           |         |                           |     the request   |
|           |         |                           |     belongs to    |
|           |         |                           |     the user      |
|           |         |                           |     who's token   |
|           |         |                           |     is being used |
|           |         |                           |     to access     |
|           |         |                           |     this          |
|           |         |                           |     endpoint.     |
|           |         |                           |     This will     |
|           |         |                           |     ensure that   |
|           |         |                           |     PMS user can  |
|           |         |                           |     access OIDC   |
|           |         |                           |     client only   |
|           |         |                           |     for the       |
|           |         |                           |     partner id    |
|           |         |                           |     which belongs |
|           |         |                           |     to the user.  |
|           |         |                           |     This          |
|           |         |                           |     validation is |
|           |         |                           |     skipped if    |
|           |         |                           |     the user's    |
|           |         |                           |     role is       |
|           |         |                           |     *             |
|           |         |                           | *PARTNER_ADMIN**. |
+-----------+---------+---------------------------+-------------------+
| /oauth/   | PUT     | This endpoint is used for | 1.  Added         |
| client/{c |         | updating OIDC Client      |     validation to |
| lient_id} |         | based on client id        |     check the     |
|           |         |                           |     partner id in |
|           |         |                           |     the request   |
|           |         |                           |     body belongs  |
|           |         |                           |     to the user   |
|           |         |                           |     who's token   |
|           |         |                           |     is being used |
|           |         |                           |     to access     |
|           |         |                           |     this          |
|           |         |                           |     endpoint.     |
|           |         |                           |     This will     |
|           |         |                           |     ensure that   |
|           |         |                           |     PMS user can  |
|           |         |                           |     update OIDC   |
|           |         |                           |     client only   |
|           |         |                           |     for the       |
|           |         |                           |     partner id    |
|           |         |                           |     which belongs |
|           |         |                           |     to the user.  |
|           |         |                           |     This          |
|           |         |                           |     validation is |
|           |         |                           |     skipped if    |
|           |         |                           |     the user's    |
|           |         |                           |     role is       |
|           |         |                           |     *             |
|           |         |                           | *PARTNER_ADMIN**. |
|           |         |                           |                   |
|           |         |                           | 2.  Added         |
|           |         |                           |     validation to |
|           |         |                           |     check if the  |
|           |         |                           |     **Partner     |
|           |         |                           |     ID** used in  |
|           |         |                           |     the request   |
|           |         |                           |     body is       |
|           |         |                           |     active. This  |
|           |         |                           |     will ensure   |
|           |         |                           |     that OIDC     |
|           |         |                           |     client cannot |
|           |         |                           |     be updated    |
|           |         |                           |     for an        |
|           |         |                           |     inactive      |
|           |         |                           |     partner. This |
|           |         |                           |     validation is |
|           |         |                           |     skipped if    |
|           |         |                           |     the user's    |
|           |         |                           |     role is       |
|           |         |                           |                   |
|           |         |                           | **PARTNER_ADMIN** |
|           |         |                           |     and status in |
|           |         |                           |     the request   |
|           |         |                           |     is changed to |
|           |         |                           |     **INACTIVE**. |
|           |         |                           |     ([MOSIP-3427  |
|           |         |                           | 6](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-34276)) |
|           |         |                           |                   |
|           |         |                           | 3.  If the status |
|           |         |                           |     in the        |
|           |         |                           |     request is    |
|           |         |                           |     changed to    |
|           |         |                           |     **INACTIVE**, |
|           |         |                           |     only the      |
|           |         |                           |     status is     |
|           |         |                           |     updated in    |
|           |         |                           |     the database  |
|           |         |                           |     other fields  |
|           |         |                           |     remain        |
|           |         |                           |     unchanged.    |
|           |         |                           |     This will     |
|           |         |                           |     ensure that   |
|           |         |                           |     PUT endpoint  |
|           |         |                           |     can be used   |
|           |         |                           |     to deactivate |
|           |         |                           |     the OIDC      |
|           |         |                           |     client.       |
|           |         |                           |                   |
|           |         |                           | 4.  Added a       |
|           |         |                           |     bypass for a  |
|           |         |                           |     user with     |
|           |         |                           |                   |
|           |         |                           | **PARTNER_ADMIN** |
|           |         |                           |     role. If the  |
|           |         |                           |     user with     |
|           |         |                           |                   |
|           |         |                           | **PARTNER_ADMIN** |
|           |         |                           |     role is used  |
|           |         |                           |     to access     |
|           |         |                           |     this          |
|           |         |                           |     endpoint,     |
|           |         |                           |     then it will  |
|           |         |                           |     deactivate    |
|           |         |                           |     the OIDC      |
|           |         |                           |     client for    |
|           |         |                           |     any partner   |
|           |         |                           |     ID, even if   |
|           |         |                           |     the partner   |
|           |         |                           |     ID is         |
|           |         |                           |     deactivated.  |
|           |         |                           |                   |
|           |         |                           | 5.  Added a       |
|           |         |                           |     validation to |
|           |         |                           |     check if the  |
|           |         |                           |     OIDC client   |
|           |         |                           |     is already    |
|           |         |                           |     deactiv       |
|           |         |                           | ated.([MOSIP-3410 |
|           |         |                           | 8](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-34108)) |
|           |         |                           |                   |
|           |         |                           | 6.  Updated       |
|           |         |                           |     client name   |
|           |         |                           |     to be a JSON  |
|           |         |                           |     string to     |
|           |         |                           |     support       |
|           |         |                           |     client name   |
|           |         |                           |     language map  |
|           |         |                           |     ([            |
|           |         |                           | ES-836](https://m |
|           |         |                           | osip.atlassian.ne |
|           |         |                           | t/browse/ES-836)) |
+-----------+---------+---------------------------+-------------------+
| /dev      | GET     | This endpoint retrieves a | Newly added in    |
| icedetail |         | list of all the Devices   | release 1.2.2.0   |
|           |         | across all the Device     |                   |
|           |         | Providers in PMS. It      |                   |
|           |         | supports pagination,      |                   |
|           |         | sorting, and filtering.   |                   |
|           |         | It is configured for the  |                   |
|           |         | role **PARTNER_ADMIN**.   |                   |
+-----------+---------+---------------------------+-------------------+
| /dev      | PUT     | Service to update Device  | This endpoint has |
| icedetail |         | Detail                    | been deprecated   |
|           |         |                           | since the         |
|           |         |                           | release-1.2.2.0.  |
+-----------+---------+---------------------------+-------------------+
| /dev      | POST    | Service to save Device    | This endpoint has |
| icedetail |         | Detail                    | been deprecated   |
|           |         |                           | since the         |
|           |         |                           | release-1.2.2.0.  |
|           |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new POST          |
|           |         |                           | /secure           |
|           |         |                           | biometricinterfac |
|           |         |                           | e/{sbiId}/devices |
|           |         |                           | endpoint          |
|           |         |                           |                   |
|           |         |                           | This ensures that |
|           |         |                           | a device will     |
|           |         |                           | always be created |
|           |         |                           | for a SBI and not |
|           |         |                           | without one.      |
+-----------+---------+---------------------------+-------------------+
| /dev      | PATCH   | Service to approve/reject | This endpoint has |
| icedetail |         | Device Detail             | been deprecated   |
|           |         |                           | since the         |
|           |         |                           | release-1.2.2.0.  |
|           |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new POST          |
|           |         |                           | devicedet         |
|           |         |                           | ail/{id}/approval |
|           |         |                           | endpoint          |
+-----------+---------+---------------------------+-------------------+
| /devic    | PATCH   | This endpoint deactivates | Newly added in    |
| edetail/{ |         | a Device based on the     | release 1.2.2.0   |
| deviceId} |         | Device Id. It is          |                   |
|           |         | configured for the roles  |                   |
|           |         | **DEVICE_PROVIDER** or    |                   |
|           |         | **PARTNER_ADMIN**.        |                   |
+-----------+---------+---------------------------+-------------------+
| /devicede | POST    | This endpoint is for the  | Newly added in    |
| tail/{id} |         | Partner Admin user to     | release 1.2.2.0   |
| /approval |         | approve or reject a       |                   |
|           |         | Device and activate the   |                   |
|           |         | mapping between the       |                   |
|           |         | Device and the SBI. It is |                   |
|           |         | configured for the role   |                   |
|           |         | **PARTNER_ADMIN**         |                   |
+-----------+---------+---------------------------+-------------------+
| /dev      | POST    | Service to filter Device  | No changes made   |
| icedetail |         | Sub Types                 | in release        |
| /deviceSu |         |                           | 1.2.2.0           |
| bType/fil |         |                           |                   |
| tervalues |         |                           |                   |
+-----------+---------+---------------------------+-------------------+
| /         | POST    | Service to filter Device  | No changes made   |
| devicedet |         | Types                     | in release        |
| ail/devic |         |                           | 1.2.2.0           |
| eType/fil |         |                           |                   |
| tervalues |         |                           |                   |
+-----------+---------+---------------------------+-------------------+
| /dev      | POST    | Service to search Device  | No changes made   |
| icedetail |         | Types                     | in release        |
| /deviceTy |         |                           | 1.2.2.0           |
| pe/search |         |                           |                   |
+-----------+---------+---------------------------+-------------------+
| /deviced  | POST    | Service to filter Device  | This endpoint has |
| etail/fil |         | Detail                    | been deprecated   |
| tervalues |         |                           | since the         |
|           |         |                           | release-1.2.2.0.  |
|           |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new GET           |
|           |         |                           | /devicedetail     |
|           |         |                           | endpoint          |
+-----------+---------+---------------------------+-------------------+
| /d        | POST    | Service to search Device  | This endpoint has |
| evicedeta |         | Detail                    | been deprecated   |
| il/search |         |                           | since the         |
|           |         |                           | release-1.2.2.0.  |
|           |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new GET           |
|           |         |                           | /devicedetail     |
|           |         |                           | endpoint          |
+-----------+---------+---------------------------+-------------------+
| /ftpc     | GET     | This endpoint retrieves a | Newly added in    |
| hipdetail |         | list of all FTM Chip      | release 1.2.2.0   |
|           |         | details created by all    |                   |
|           |         | the FTM Providers         |                   |
|           |         | associated with the       |                   |
|           |         | logged in user. It is     |                   |
|           |         | configured for the roles  |                   |
|           |         | **FTM_PROVIDER** or       |                   |
|           |         | **PARTNER_ADMIN**.        |                   |
+-----------+---------+---------------------------+-------------------+
| /ftpc     | PUT     | Service to update ftp     | This endpoint has |
| hipdetail |         | chip detail               | been deprecated   |
|           |         |                           | since the         |
|           |         |                           | release-1.2.2.0   |
+-----------+---------+---------------------------+-------------------+
| /ftpc     | POST    | Service to save ftp chip  | 1.  Improved the  |
| hipdetail |         | detail                    |     validation    |
|           |         |                           |     check by      |
|           |         |                           |     trimming      |
|           |         |                           |     extra spaces  |
|           |         |                           |     in make and   |
|           |         |                           |     model to      |
|           |         |                           |     prevent       |
|           |         |                           |     duplicate     |
|           |         |                           |     entries.      |
|           |         |                           |     ([MOSIP-3578  |
|           |         |                           | 8](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-35788)) |
+-----------+---------+---------------------------+-------------------+
| /ftpc     | PATCH   | Service to approve/reject | No changes made   |
| hipdetail |         | ftp chip detail           | in release        |
|           |         |                           | 1.2.2.0           |
+-----------+---------+---------------------------+-------------------+
| /ftp      | PATCH   | This endpoint deactivates | Newly added in    |
| chipdetai |         | the ftp chip detail based | release 1.2.2.0   |
| l/{ftmId} |         | on the ftp chip detail    |                   |
|           |         | Id. It is configured for  |                   |
|           |         | the roles                 |                   |
|           |         | **FTM_PROVIDER** or       |                   |
|           |         | **PARTNER_ADMIN**.        |                   |
+-----------+---------+---------------------------+-------------------+
| /ft       | GET     | This endpoint fetches     | Newly added in    |
| pchipdeta |         | both the CA signed        | release 1.2.2.0   |
| il/{ftmId |         | certificate uploaded by   |                   |
| }/certifi |         | the FTM Chip Provider and |                   |
| cate-data |         | the MOSIP signed          |                   |
|           |         | certificate generated by  |                   |
|           |         | PMS. It is configured for |                   |
|           |         | the roles                 |                   |
|           |         | **FTM_PROVIDER** or       |                   |
|           |         | **PARTNER_ADMIN**.        |                   |
+-----------+---------+---------------------------+-------------------+
| /ftpchipd | GET     | Service to get            | 1.  Improved Key  |
| etail/get |         | certificate of ftp chip   |     Manager error |
| PartnerCe |         |                           |     handling, to  |
| rtificate |         |                           |     capture the   |
| /{ftpChip |         |                           |     correct error |
| DetailId} |         |                           |     code from Key |
|           |         |                           |     Manager and   |
|           |         |                           |     send it in    |
|           |         |                           |     the           |
|           |         |                           |     endpoint's    |
|           |         |                           |     response.     |
+-----------+---------+---------------------------+-------------------+
| /ft       | POST    | Service to search ftp     | 1.  This endpoint |
| pchipdeta |         | chip details              |     has been      |
| il/search |         |                           |     deprecated    |
|           |         |                           |     since the     |
|           |         |                           |                   |
|           |         |                           |  release-1.2.2.0. |
|           |         |                           |     It has been   |
|           |         |                           |     replaced by   |
|           |         |                           |     the new GET   |
|           |         |                           |                   |
|           |         |                           | /ftpchipdetail/v2 |
|           |         |                           |     endpoint.     |
+-----------+---------+---------------------------+-------------------+
| /ftpc     | POST    | Service to upload         | 1.  Added         |
| hipdetail |         | certificate of ftp chip   |     validation to |
| /uploadce |         |                           |     allow         |
| rtificate |         |                           |     certificate   |
|           |         |                           |     upload only   |
|           |         |                           |     if the FTM    |
|           |         |                           |     chip details  |
|           |         |                           |     certificate   |
|           |         |                           |     status is     |
|           |         |                           |     **APPROVED**  |
|           |         |                           |     or            |
|           |         |                           |     **P           |
|           |         |                           | ENDING_CERT_UPLOA |
|           |         |                           | D**.([MOSIP-36283 |
|           |         |                           | ](https://mosip.a |
|           |         |                           | tlassian.net/brow |
|           |         |                           | se/MOSIP-36283)). |
|           |         |                           |     So for        |
|           |         |                           |     Rejected or   |
|           |         |                           |     Deactivated   |
|           |         |                           |     FTM, a        |
|           |         |                           |     certificate   |
|           |         |                           |     cannot be     |
|           |         |                           |     uploaded.     |
|           |         |                           |                   |
|           |         |                           | 2.  Improved Key  |
|           |         |                           |     Manager error |
|           |         |                           |     handling, to  |
|           |         |                           |     capture the   |
|           |         |                           |     correct error |
|           |         |                           |     code from Key |
|           |         |                           |     Manager and   |
|           |         |                           |     send it in    |
|           |         |                           |     the           |
|           |         |                           |     endpoint's    |
|           |         |                           |     response.     |
|           |         |                           |                   |
|           |         |                           | 3.  Set isActive  |
|           |         |                           |     to false      |
|           |         |                           |     after         |
|           |         |                           |     certificate   |
|           |         |                           |     re-upload.    |
|           |         |                           |     This will     |
|           |         |                           |     ensure that   |
|           |         |                           |     after cert is |
|           |         |                           |     reuploaded,   |
|           |         |                           |     partner admin |
|           |         |                           |     will have to  |
|           |         |                           |     approve the   |
|           |         |                           |     FTM again.    |
|           |         |                           |     ([MOSIP-3628  |
|           |         |                           | 5](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-36285)) |
+-----------+---------+---------------------------+-------------------+
| /ftpchip  | GET     | This endpoint retrieves a | Newly added in    |
| detail/v2 |         | list of all FTM Chip      | release 1.2.2.0   |
|           |         | details created by all    |                   |
|           |         | the FTM Providers. Also   |                   |
|           |         | supports pagination,      |                   |
|           |         | sorting, and filtering.   |                   |
|           |         | It is configured for the  |                   |
|           |         | role **PARTNER_ADMIN**.   |                   |
+-----------+---------+---------------------------+-------------------+
| /admin    | GET     | This endpoint retrieves a | Newly added in    |
| -partners |         | list of all Partners.     | release 1.2.2.0   |
|           |         | Also supports pagination, |                   |
|           |         | sorting, and filtering.   |                   |
|           |         | It is configured for the  |                   |
|           |         | role **PARTNER_ADMIN**.   |                   |
+-----------+---------+---------------------------+-------------------+
| /admin-pa | GET     | This endpoint retrieves   | Newly added in    |
| rtners/{p |         | all the details of the    | release 1.2.2.0   |
| artnerId} |         | Partner based on Partner  |                   |
|           |         | Id. It is configured for  |                   |
|           |         | the role                  |                   |
|           |         | **PARTNER_ADMIN**.        |                   |
+-----------+---------+---------------------------+-------------------+
| /partner  | GET     | This endpoint retrieves a | Newly added in    |
| -api-keys |         | list of all the API keys  | release 1.2.2.0   |
|           |         | created by the Auth       |                   |
|           |         | Partners. Also supports   |                   |
|           |         | pagination, sorting, and  |                   |
|           |         | and filtering based on    |                   |
|           |         | optional query            |                   |
|           |         | parameters. If the token  |                   |
|           |         | used to access this       |                   |
|           |         | endpoint, does not have   |                   |
|           |         | the **PARTNER_ADMIN**     |                   |
|           |         | role, then it will fetch  |                   |
|           |         | all the API keys created  |                   |
|           |         | by all the partners       |                   |
|           |         | associated with the       |                   |
|           |         | logged in user only. If   |                   |
|           |         | the token used to access  |                   |
|           |         | this endpoint, has        |                   |
|           |         | **PARTNER_ADMIN** role,   |                   |
|           |         | then it will fetch all    |                   |
|           |         | the API keys created by   |                   |
|           |         | all the partners.         |                   |
+-----------+---------+---------------------------+-------------------+
| /partn    | GET     | This endpoint fetches     | Newly added in    |
| er-policy |         | list of all the policy    | release 1.2.2.0   |
| -requests |         | requests made by the      |                   |
|           |         | partners. Also supports   |                   |
|           |         | pagination, sorting, and  |                   |
|           |         | filtering based on        |                   |
|           |         | optional query            |                   |
|           |         | parameters. If the token  |                   |
|           |         | used to access this       |                   |
|           |         | endpoint, does not have   |                   |
|           |         | the **PARTNER_ADMIN**     |                   |
|           |         | role, then it will fetch  |                   |
|           |         | all the policy requests   |                   |
|           |         | made by all the partners  |                   |
|           |         | associated with the       |                   |
|           |         | logged in user only.If    |                   |
|           |         | the token used to access  |                   |
|           |         | this endpoint, has        |                   |
|           |         | **PARTNER_ADMIN** role,   |                   |
|           |         | then it will fetch all    |                   |
|           |         | the policy requests made  |                   |
|           |         | by all the partners.      |                   |
+-----------+---------+---------------------------+-------------------+
| /partners | GET     | Service to get partner    | 1.  This endpoint |
|           |         | details                   |     has been      |
|           |         |                           |     deprecated    |
|           |         |                           |     since the     |
|           |         |                           |                   |
|           |         |                           |  release-1.2.2.0. |
|           |         |                           |     It has been   |
|           |         |                           |     replaced by   |
|           |         |                           |     the new GET   |
|           |         |                           |     /partners/v3  |
|           |         |                           |     endpoint.     |
+-----------+---------+---------------------------+-------------------+
| /pa       | PATCH   | Service to                | 1.  Added a check |
| rtners/{p |         | activate/de-activate      |     to verify if  |
| artnerId} |         | partner                   |     the           |
|           |         |                           |     **partner**   |
|           |         |                           |     is already    |
|           |         |                           |     deactivated.  |
|           |         |                           |     If yes,       |
|           |         |                           |     partner       |
|           |         |                           |     cannot be     |
|           |         |                           |     deactivated   |
|           |         |                           |     again.        |
|           |         |                           |     ([MOSIP-3701  |
|           |         |                           | 7](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-37017)) |
+-----------+---------+---------------------------+-------------------+
| /         | GET     | Service to get policy for | No changes made   |
| partners/ |         | given API key             | in release        |
| {partnerI |         |                           | 1.2.2.0           |
| d}/apikey |         |                           |                   |
| /{apikey} |         |                           |                   |
+-----------+---------+---------------------------+-------------------+
| /         | PUT     | Service to update         | No changes made   |
| partners/ |         | policies against to API   | in release        |
| {partnerI |         | key                       | 1.2.2.0           |
| d}/apikey |         |                           |                   |
| /{apikey} |         |                           |                   |
| /policies |         |                           |                   |
+-----------+---------+---------------------------+-------------------+
| /partner  | PATCH   | Service to                | 1.  If the API    |
| s/{partne |         | activate/de-activate      |     key is        |
| rId}/poli |         | partner API key           |     already       |
| cy/{polic |         |                           |     deactivated,  |
| yId}/apik |         |                           |     it cannot be  |
| ey/status |         |                           |     deactivated   |
|           |         |                           |     a             |
|           |         |                           | gain.([MOSIP-3443 |
|           |         |                           | 0](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-34430)) |
|           |         |                           |                   |
|           |         |                           | 2.  Added a       |
|           |         |                           |     validation to |
|           |         |                           |     check if the  |
|           |         |                           |     **Partner     |
|           |         |                           |     ID** used in  |
|           |         |                           |     the request   |
|           |         |                           |     body is       |
|           |         |                           |     active. This  |
|           |         |                           |     will ensure   |
|           |         |                           |     that API      |
|           |         |                           |     cannot be     |
|           |         |                           |     deactivated   |
|           |         |                           |     if partner    |
|           |         |                           |     has been      |
|           |         |                           |     deactivated.  |
|           |         |                           |     This          |
|           |         |                           |     validation is |
|           |         |                           |     skipped if    |
|           |         |                           |     the user's    |
|           |         |                           |     role is       |
|           |         |                           |     *             |
|           |         |                           | *PARTNER_ADMIN**. |
|           |         |                           |     ([MOSIP-3443  |
|           |         |                           | 0](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-34430)) |
+-----------+---------+---------------------------+-------------------+
| /partne   | GET     | Service to get API key    | This endpoint has |
| rs/apikey |         | requests                  | been deprecated   |
|           |         |                           | since the         |
|           |         |                           | release-1.2.2.0.  |
|           |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new GET           |
|           |         |                           | /partne           |
|           |         |                           | r-policy-requests |
|           |         |                           | endpoint.         |
+-----------+---------+---------------------------+-------------------+
| /partne   | GET     | Service to get API key    | No changes made   |
| rs/apikey |         | request                   | in release        |
| /{apikey} |         |                           | 1.2.2.0           |
+-----------+---------+---------------------------+-------------------+
| /p        | PUT     | Service to approve/reject | No changes made   |
| artners/p |         | partner policy mapping    | in release        |
| olicy/{ma |         |                           | 1.2.2.0           |
| ppingkey} |         |                           |                   |
+-----------+---------+---------------------------+-------------------+
| /pa       | GET     | Service to get partner    | This endpoint has |
| rtners/v2 |         | details                   | been deprecated   |
|           |         |                           | since the         |
|           |         |                           | release-1.2.2.0.  |
|           |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new GET           |
|           |         |                           | /partners/v3      |
|           |         |                           | endpoint.         |
+-----------+---------+---------------------------+-------------------+
| /trust-   | GET     | This endpoint retrieves a | Newly added in    |
| chain-cer |         | list of all the Trust     | release 1.2.2.0   |
| tificates |         | Certificates uploaded by  |                   |
|           |         | the Partner Admin. Also   |                   |
|           |         | supports pagination,      |                   |
|           |         | sorting, and filtering.   |                   |
|           |         | It is configured for the  |                   |
|           |         | role **PARTNER_ADMIN**.   |                   |
+-----------+---------+---------------------------+-------------------+
| /tr       | GET     | This endpoint will        | Newly added in    |
| ust-chain |         | download p7b file for a   | release 1.2.2.0   |
| -certific |         | CA / Intermediate CA      |                   |
| ates/{cer |         | certificate along with    |                   |
| tificateI |         | the trust chain based on  |                   |
| d}/certif |         | Certificate Id. It is     |                   |
| icateFile |         | configured for the role   |                   |
|           |         | **PARTNER_ADMIN**.        |                   |
+-----------+---------+---------------------------+-------------------+
| /partners | POST    | partner self registration | No changes made   |
|           |         |                           | in release        |
|           |         |                           | 1.2.2.0           |
+-----------+---------+---------------------------+-------------------+
| /pa       | GET     | Service to get details of | Corrected the     |
| rtners/{p |         | partner                   | version in the    |
| artnerId} |         |                           | response body     |
+-----------+---------+---------------------------+-------------------+
| /pa       | PUT     | Service to update details |                   |
| rtners/{p |         | of partner                |                   |
| artnerId} |         |                           |                   |
+-----------+---------+---------------------------+-------------------+
| /partners | GET     | Service to get API key    | Corrected the     |
| /{partner |         | requests of partner       | version in the    |
| Id}/apike |         |                           | response body     |
| y/request |         |                           |                   |
+-----------+---------+---------------------------+-------------------+
| /partn    | GET     | Service to get partner    | 1.  Added         |
| ers/{part |         | certificate               |     validation to |
| nerId}/ce |         |                           |     check the     |
| rtificate |         |                           |     partner id in |
|           |         |                           |     the request   |
|           |         |                           |     belongs to    |
|           |         |                           |     the user      |
|           |         |                           |     who's token   |
|           |         |                           |     is being used |
|           |         |                           |     to access     |
|           |         |                           |     this          |
|           |         |                           |     endpoint.     |
|           |         |                           |     This will     |
|           |         |                           |     ensure that   |
|           |         |                           |     PMS user can  |
|           |         |                           |     access the    |
|           |         |                           |     certificate   |
|           |         |                           |     only for the  |
|           |         |                           |     partner id    |
|           |         |                           |     which belongs |
|           |         |                           |     to the user.  |
|           |         |                           |     This          |
|           |         |                           |     validation is |
|           |         |                           |     skipped if    |
|           |         |                           |     the user's    |
|           |         |                           |     role is       |
|           |         |                           |     *             |
|           |         |                           | *PARTNER_ADMIN**. |
|           |         |                           |                   |
|           |         |                           | 2.  Added a check |
|           |         |                           |     to verify if  |
|           |         |                           |     the partner   |
|           |         |                           |     id in the     |
|           |         |                           |     request       |
|           |         |                           |     exists in the |
|           |         |                           |     data          |
|           |         |                           | base.([MOSIP-3701 |
|           |         |                           | 7](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-37017)) |
|           |         |                           |                   |
|           |         |                           | 3.  Added         |
|           |         |                           |     validation to |
|           |         |                           |     check if the  |
|           |         |                           |     certificate   |
|           |         |                           |     has been      |
|           |         |                           |     uploaded      |
|           |         |                           |     previously.   |
+-----------+---------+---------------------------+-------------------+
| /p        | GET     | This endpoint retrieves   | Newly added in    |
| artners/{ |         | both the CA signed        | release 1.2.2.0   |
| partnerId |         | certificate uploaded by   |                   |
| }/certifi |         | the partner and the       |                   |
| cate-data |         | MOSIP-signed certificate  |                   |
|           |         | generated by PMS. It is   |                   |
|           |         | configured for role any   |                   |
|           |         | of the partner type or    |                   |
|           |         | **PARTNER_ADMIN**.        |                   |
+-----------+---------+---------------------------+-------------------+
| /         | PATCH   | To generate API Key for   | Added a check to  |
| partners/ |         | approved policies         | remove extra      |
| {partnerI |         |                           | spaces in the API |
| d}/genera |         |                           | key label before  |
| te/apikey |         |                           | saving to the     |
|           |         |                           | database,         |
|           |         |                           | preventing the    |
|           |         |                           | creation of       |
|           |         |                           | duplicate API key |
|           |         |                           | labels with extra |
|           |         |                           | sp                |
|           |         |                           | aces.([MOSIP-3578 |
|           |         |                           | 8](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-35788)) |
+-----------+---------+---------------------------+-------------------+
| /part     | POST    | To request for policy     | Updated error     |
| ners/{par |         | mapping                   | messages to       |
| tnerId}/p |         |                           | indicate if the   |
| olicy/map |         |                           | policy is already |
|           |         |                           | mapped and its    |
|           |         |                           | status is         |
|           |         |                           | **Approved** or   |
|           |         |                           | **In              |
|           |         |                           | Progre            |
|           |         |                           | ss**.([MOSIP-3380 |
|           |         |                           | 3](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-33803)) |
+-----------+---------+---------------------------+-------------------+
| /partn    | PUT     | Service to update the     | No changes made   |
| ers/{part |         | policy group for partner  | in release        |
| nerId}/po |         |                           | 1.2.2.0           |
| licygroup |         |                           |                   |
| /{policyg |         |                           |                   |
| roupName} |         |                           |                   |
+-----------+---------+---------------------------+-------------------+
| /         | POST    | Service to filter API key | This endpoint has |
| partners/ |         | requests                  | been deprecated   |
| apikey/re |         |                           | since the         |
| quest/fil |         |                           | release-1.2.2.0.  |
| tervalues |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new GET           |
|           |         |                           | /partne           |
|           |         |                           | r-policy-requests |
|           |         |                           | endpoint.         |
+-----------+---------+---------------------------+-------------------+
| /par      | POST    | Service to search API key | This endpoint has |
| tners/api |         | requests                  | been deprecated   |
| key/reque |         |                           | since the         |
| st/search |         |                           | release-1.2.2.0.  |
|           |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new GET           |
|           |         |                           | /partne           |
|           |         |                           | r-policy-requests |
|           |         |                           | endpoint.         |
+-----------+---------+---------------------------+-------------------+
| /part     | POST    | Service to search API key | This endpoint has |
| ners/apik |         |                           | been deprecated   |
| ey/search |         |                           | since the         |
|           |         |                           | release-1.2.2.0.  |
|           |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new GET           |
|           |         |                           | /partner-api-keys |
|           |         |                           | endpoint.         |
+-----------+---------+---------------------------+-------------------+
| /par      | POST    | Service to upload ca      | No changes made   |
| tners/cer |         | certificate               | in release        |
| tificate/ |         |                           | 1.2.2.0           |
| ca/upload |         |                           |                   |
+-----------+---------+---------------------------+-------------------+
| /         | POST    | Service to upload partner | 1.  Added a       |
| partners/ |         | certificate               |     validation to |
| certifica |         |                           |     check if the  |
| te/upload |         |                           |     **Partner     |
|           |         |                           |     ID** used in  |
|           |         |                           |     the request   |
|           |         |                           |     body is       |
|           |         |                           |     active. This  |
|           |         |                           |     will ensure   |
|           |         |                           |     that          |
|           |         |                           |     certificate   |
|           |         |                           |     cannot be     |
|           |         |                           |     uploaded if   |
|           |         |                           |     partner has   |
|           |         |                           |     been          |
|           |         |                           |     deactivated.  |
|           |         |                           |     ([MOSIP-3449  |
|           |         |                           | 8](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-34498)) |
|           |         |                           |                   |
|           |         |                           | 2.  If domain is  |
|           |         |                           |     **FTM**, do   |
|           |         |                           |     not call the  |
|           |         |                           |     uploadOther   |
|           |         |                           | DomainCertificate |
|           |         |                           |     endpoint of   |
|           |         |                           |     KeyMan        |
|           |         |                           | ager.([MOSIP-3579 |
|           |         |                           | 7](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-35797)) |
+-----------+---------+---------------------------+-------------------+
| /par      | PUT     | Service to verify partner | No changes made   |
| tners/ema |         | email                     | in release        |
| il/verify |         |                           | 1.2.2.0           |
+-----------+---------+---------------------------+-------------------+
| /par      | POST    | Service to filter partner | This endpoint has |
| tners/fil |         | details                   | been deprecated   |
| tervalues |         |                           | since the         |
|           |         |                           | release-1.2.2.0.  |
|           |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new GET           |
|           |         |                           | /partners/v3      |
|           |         |                           | endpoint.         |
+-----------+---------+---------------------------+-------------------+
| /p        | GET     | This endpoint retrieves a | Newly added in    |
| artners/p |         | list of all Partner       | release 1.2.2.0   |
| artner-ce |         | Certicates uploaded by    |                   |
| rtificate |         | the logged in user        |                   |
| s-details |         |                           |                   |
+-----------+---------+---------------------------+-------------------+
| /         | POST    | Service to search partner | No changes made   |
| partners/ |         | types                     | in release        |
| partnerTy |         |                           | 1.2.2.0           |
| pe/search |         |                           |                   |
+-----------+---------+---------------------------+-------------------+
| partne    | POST    | Service to search partner | This endpoint has |
| rs/search |         | details                   | been deprecated   |
|           |         |                           | since the         |
|           |         |                           | release-1.2.2.0.  |
|           |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new GET           |
|           |         |                           | /partners/v3      |
|           |         |                           | endpoint.         |
+-----------+---------+---------------------------+-------------------+
| pa        | POST    | Registers partner details | No changes made   |
| rtners/v2 |         |                           | in release        |
|           |         |                           | 1.2.2.0           |
+-----------+---------+---------------------------+-------------------+
| partn     | PUT     | Service to update details | No changes made   |
| ers/v2/{p |         | of partner                | in release        |
| artnerId} |         |                           | 1.2.2.0           |
+-----------+---------+---------------------------+-------------------+
| pa        | GET     | This endpoint retrieves a | Newly added in    |
| rtners/v3 |         | list of Partners          | release 1.2.2.0   |
|           |         | associated with the       |                   |
|           |         | logged in user, based on  |                   |
|           |         | the query parameters. It  |                   |
|           |         | is configured for role    |                   |
|           |         | any of the partner type   |                   |
|           |         | or **PARTNER_ADMIN**.     |                   |
+-----------+---------+---------------------------+-------------------+
| /roles    | GET     | Service to get required   | No changes made   |
|           |         | roles                     | in release        |
|           |         |                           | 1.2.2.0           |
+-----------+---------+---------------------------+-------------------+
| /secure   | GET     | This endpoint retrieves a | Newly added in    |
| biometric |         | list of all SBIs created  | release 1.2.2.0   |
| interface |         | by the Device Providers.  |                   |
|           |         | Also supports pagination, |                   |
|           |         | sorting, and and          |                   |
|           |         | filtering based on        |                   |
|           |         | optional query            |                   |
|           |         | parameters. If the token  |                   |
|           |         | used to access this       |                   |
|           |         | endpoint, does not have   |                   |
|           |         | the **PARTNER_ADMIN**     |                   |
|           |         | role, then it will fetch  |                   |
|           |         | all SBIs created by all   |                   |
|           |         | the partners associated   |                   |
|           |         | with the logged in user   |                   |
|           |         | only. If the token used   |                   |
|           |         | to access this endpoint,  |                   |
|           |         | has **PARTNER_ADMIN**     |                   |
|           |         | role, then it will fetch  |                   |
|           |         | all the SBIs created by   |                   |
|           |         | all the partners.         |                   |
+-----------+---------+---------------------------+-------------------+
| /secure   | PUT     | Service to update         | This endpoint has |
| biometric |         | SecureBiometricInterface  | been deprecated   |
| interface |         |                           | since the         |
|           |         |                           | release-1.2.2.0   |
+-----------+---------+---------------------------+-------------------+
| /secure   | POST    | Service to save           | Added a check to  |
| biometric |         | SecureBiometricInterface  | remove extra      |
| interface |         | details                   | spaces in the SBI |
|           |         |                           | version before    |
|           |         |                           | saving to the     |
|           |         |                           | database,         |
|           |         |                           | preventing the    |
|           |         |                           | creation of       |
|           |         |                           | duplicate SBI     |
|           |         |                           | versions with     |
|           |         |                           | extra             |
|           |         |                           | sp                |
|           |         |                           | aces.([MOSIP-3578 |
|           |         |                           | 8](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-35788)) |
+-----------+---------+---------------------------+-------------------+
| /secure   | PATCH   | Service to approve/reject | Added separate    |
| biometric |         | SecureBiometricInterface  | error codes for   |
| interface |         |                           | cases when SBI is |
|           |         |                           | already           |
|           |         |                           | **approved** or   |
|           |         |                           | **reject          |
|           |         |                           | ed**.([MOSIP-3897 |
|           |         |                           | 3](https://mosip. |
|           |         |                           | atlassian.net/bro |
|           |         |                           | wse/MOSIP-38973)) |
+-----------+---------+---------------------------+-------------------+
| /secur    | PATCH   | This endpoint deactivates | Newly added in    |
| ebiometri |         | an SBI along with         | release 1.2.2.0   |
| cinterfac |         | associated Devices. It is |                   |
| e/{sbiId} |         | configured for the roles  |                   |
|           |         | **DEVICE_PROVIDER** or    |                   |
|           |         | **PARTNER_ADMIN**.        |                   |
+-----------+---------+---------------------------+-------------------+
| /secu     | GET     | This endpoint fetches the | Newly added in    |
| rebiometr |         | list of Devices           | release 1.2.2.0   |
| icinterfa |         | associated with a given   |                   |
| ce/{sbiId |         | SBI Id. It is configured  |                   |
| }/devices |         | for the roles             |                   |
|           |         | **DEVICE_PROVIDER** or    |                   |
|           |         | **PARTNER_ADMIN**.        |                   |
+-----------+---------+---------------------------+-------------------+
| /secu     | POST    | This endpoint adds a new  | Newly added in    |
| rebiometr |         | Device and creates an     | release 1.2.2.0   |
| icinterfa |         | inactive mapping between  |                   |
| ce/{sbiId |         | the device and the given  |                   |
| }/devices |         | SBI. It is configured for |                   |
|           |         | the roles                 |                   |
|           |         | **DEVICE_PROVIDER** or    |                   |
|           |         | **PARTNER_ADMIN**.        |                   |
+-----------+---------+---------------------------+-------------------+
| /secure   | PUT     | Service to map device     | This endpoint has |
| biometric |         | details with sbi          | been deprecated   |
| interface |         |                           | since the         |
| /devicede |         |                           | release-1.2.2.0.  |
| tails/map |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new POST          |
|           |         |                           | /secure           |
|           |         |                           | biometricinterfac |
|           |         |                           | e/{sbiId}/devices |
|           |         |                           | endpoint.         |
+-----------+---------+---------------------------+-------------------+
| /secu     | PUT     | Service to remove mapped  | This endpoint has |
| rebiometr |         | device details with sbi   | been deprecated   |
| icinterfa |         |                           | since the         |
| ce/device |         |                           | release-1.2.2.0.  |
| details/m |         |                           |                   |
| ap/remove |         |                           |                   |
+-----------+---------+---------------------------+-------------------+
| /secu     | POST    | Service to search mapped  | This endpoint has |
| rebiometr |         | device details and        | been deprecated   |
| icinterfa |         | SecureBiometricInterface  | since the         |
| ce/device |         | details                   | release-1.2.2.0.  |
| details/m |         |                           | It has been       |
| ap/search |         |                           | replaced by the   |
|           |         |                           | new GET           |
|           |         |                           | /secure           |
|           |         |                           | biometricinterfac |
|           |         |                           | e/{sbiId}/devices |
|           |         |                           | endpoint.         |
+-----------+---------+---------------------------+-------------------+
| /s        | POST    | Service to filter SBI\'s  | This endpoint has |
| ecurebiom |         |                           | been deprecated   |
| etricinte |         |                           | since the         |
| rface/fil |         |                           | release-1.2.2.0.  |
| tervalues |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new GET           |
|           |         |                           | /secureb          |
|           |         |                           | iometricinterface |
|           |         |                           | endpoint.         |
+-----------+---------+---------------------------+-------------------+
| /secu     | POST    | Service to search         | This endpoint has |
| rebiometr |         | SecureBiometricInterface  | been deprecated   |
| icinterfa |         | details                   | since the         |
| ce/search |         |                           | release-1.2.2.0.  |
|           |         |                           | It has been       |
|           |         |                           | replaced by the   |
|           |         |                           | new GET           |
|           |         |                           | /secureb          |
|           |         |                           | iometricinterface |
|           |         |                           | endpoint.         |
+-----------+---------+---------------------------+-------------------+
| /syst     | GET     | This endpoint fetches the | Newly added in    |
| em-config |         | configurations for PMS    | release 1.2.2.0   |
|           |         | and sends them to the UI. |                   |
|           |         | No roles are required for |                   |
|           |         | access.                   |                   |
+-----------+---------+---------------------------+-------------------+
| /users    | POST    | Service to register user  | No changes made   |
|           |         |                           | in release        |
|           |         |                           | 1.2.2.0           |
+-----------+---------+---------------------------+-------------------+
| /         | GET     | This endpoint fetches the | Newly added in    |
| users/use |         | user\'s consent related   | release 1.2.2.0   |
| r-consent |         | to the data captured by   |                   |
|           |         | PMS. The consent is       |                   |
|           |         | requested only once after |                   |
|           |         | the user\'s first login,  |                   |
|           |         | and won\'t be asked again |                   |
|           |         | if already given. It is   |                   |
|           |         | configured for all        |                   |
|           |         | Partner Type roles.       |                   |
+-----------+---------+---------------------------+-------------------+
| /         | POST    | This endpoint saves the   | Newly added in    |
| users/use |         | user\'s consent related   | release 1.2.2.0   |
| r-consent |         | to data captured by the   |                   |
|           |         | PMS portal, which is      |                   |
|           |         | requested only once after |                   |
|           |         | the user\'s first login.  |                   |
|           |         | Once provided, the        |                   |
|           |         | consent will not be asked |                   |
|           |         | again. It is configured   |                   |
|           |         | for all Partner Type      |                   |
|           |         | roles.                    |                   |
+-----------+---------+---------------------------+-------------------+

