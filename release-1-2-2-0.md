# Release : 1.2.2.0

**Release Name**: Partner Management System Revamp

**Release Number**: v1.2.2.0

**Release Date**: 28th Feb, 2025

### Overview

We are excited to announce the launch of the **new and improved Partner
Management System (PMS) portal**, now live with an upgraded UI and
enhanced capabilities!

The new version **1.2.2.0** is a full feature release , serving as a
continuation of the earlier developer preview (**1.3.0-dp.1**). This
release brings:\
✅ **Technology stack upgrade** for improved performance and security.\
✅ Expanded system capabilities with **diverse partner types** and
**admin** roles.\
✅ **New functionalities** tailored for a seamless experience.

✅ **Feature enhancements** to streamline partner management.\
✅ **Improved usability & user experience** for better navigation and
efficiency.

This release officially launches **PMS version 1.2.2.0**, focusing on
the implementation of **Device Provider** and **FTM Chip Provider**
partner types, along with an enhanced **Partner Admin/Policy Manager
workflow** in the new UI.

This version of PMS is designed to run on 1.2.0.1 version of MOSIP
platform.

The **key features** of **[Device Provider]{.underline}** are:

-   **Partner Certificate:**

    -   **Upload and Re-upload:** Easily upload or re-upload Certificate
        Authority (CA) signed Partner Certificate.

    -   **Download:** Download CA signed Partner Certificate and
        corresponding MOSIP Signed Certificate.

-   **Device Provider Services:**

    -   **SBI - Device Creation:** Add SBI, Add Devices associated to an
        SBI. SBI/ Device submissions will go to Partner Admin for
        approval.

    -   **Deactivate:** SBI, deactivate mapped devices

    -   **View** SBI and its associated devices

The **key features** of **[FTM Chip Provider]{.underline}** are:

-   **Partner Certificate:**

    -   **Upload and Re-upload:** Easily upload or re-upload Certificate
        Authority (CA) signed Partner Certificate.

    -   **Download:** Download CA signed Partner Certificate and
        corresponding MOSIP Signed Certificate.

-   **FTM Chip Services:**

    -   **FTM Chip details:** Add FTM details, deactivate FTM details.

    -   **FTM Chip Certificate:** Upload, Re- upload and download
        certificate.

The **key features** of **[Partner Admin]{.underline}** are:

a\) [Admin dashboard-]{.underline}

-   Displays the cards for Certificate Trust Store, Partners, Policies,
    Parter Policy-Linking, SBI-Device, FTM Chip, Authentications
    Services.

-   Displays the entier splay pending requests count for Parter
    Policy-Linking, SBI-Device, FTM Chip

b\) [Certificate Trust Store-]{.underline}

-   **Upload** Certificate

-   **Download** Original Certificate

-   **Tabular view**

-   **View** Uploaded Certificate details

-   

c\) [Partners]{.underline}

-   **Tabular view**

-   **View** Partner details

-   **Deactivate** partner

-   **Download** Original & MOSIP Signed Certificate

d\) [Policies]{.underline}

-   Create [**[Policy
    Group]{.underline}**](file:////wiki/spaces/PMS/pages/1348665691/Overview+RELOOK)

-   Create
    [**[Policy]{.underline}**](file:////wiki/spaces/PMS/pages/1348665691/Overview+RELOOK)

    -   [Authentication
        Policy](file:////wiki/spaces/PMS/pages/1348665691/Overview+RELOOK)

    -   [Datashare
        Policy](file:////wiki/spaces/PMS/pages/1348665691/Overview+RELOOK)

-   **Clone Policy** in different Policy Group

-   **Publish** Policy in draft status

-   **Edit** Policy in draft status

-   **Tabular View**

-   **View** individual details

-   **Deactivate** Policy Group (if no active policy is linked)

-   **Deactivate** Policy (if no active partner policy mappings)

e[) Partner Policy Linking]{.underline}

-   **Approve/ Reject**

-   **Tabular View**

-   **View** individual details

f\) [Authentication Services]{.underline}

-   OIDC Client:

    -   **Tabular View**

    -   **View** individual details

    -   **Deactivate**

> API Key:

-   **Tabular View**

-   **View** individual details

-   **Deactivate**

g\) [SBI-Device]{.underline}

 SBI:

-   **Approve/ Reject**

-   **Tabular View**

-   **View** individual details

-   **Deactivate** (if no active devices present)

Device:

-   **Approve/ Reject**

-   **Tabular View**

-   **View** individual details

-   **Deactivate**

h\) [FTM Chip]{.underline}

-   **Approve/ Reject**

-   **Tabular View**

-   **View** individual details

-   **Deactivate**

<!-- -->

-   **Browser Support:**

    -   Complete support on **Chrome, Firefox, Edge and Safari** ensures
        a seamless user experience across these popular browsers.

-   **Language Support:**

    -   Multi Language is supported with support for resource bundles in
        3 languages (Eng, Ara, Fra). More resource bundles can be easily
        added by following the following documentation [New Language
        Support](file:////wiki/spaces/PMS/pages/1606254602/New+Language+Support)

    -   

    -   

-   **Compatibility:**

    -   Optimized for standard browser sizes (laptop/desktop/tablet/
        extra large screens) with responsive UI design for
        laptop/desktop views.

For detailed description of the above features, refer to [Feature
Documentation](https://docs.mosip.io/1.2.0/modules/partner-management-services/pms-revamp/functional-overview/auth-partner/features).

To know more about the upcoming features planned as part of PMS Revamp
for this year, please check out [Roadmap
2025](https://docs.mosip.io/1.2.0/roadmap/roadmap-2025#inji-stack-1).

### **Known Issues**

Below is the list of key [[known
issues]{.underline}](https://mosip.atlassian.net/issues/?filter=12233):

+--------+-------------------------------------------------------------+
| **Jira | **Issue Description**                                       |
| I      |                                                             |
| ssue** |                                                             |
+========+=============================================================+
|        |                                                             |
+--------+-------------------------------------------------------------+
| [      | Partner domain dropdown items (AUTH/ DEVICE/ FTM) are in    |
| MOSIP- | English and do not support multi-language.                  |
| 38890] |                                                             |
| (https |                                                             |
| ://mos |                                                             |
| ip.atl |                                                             |
| assian |                                                             |
| .net/b |                                                             |
| rowse/ |                                                             |
| MOSIP- |                                                             |
| 38890) |                                                             |
+--------+-------------------------------------------------------------+
| [      | On deactivating an API key from one browser , the status    |
| MOSIP- | still remains \'Activated\' on viewing the same API Key     |
| 34427] | details in another browser.                                 |
| (https |                                                             |
| ://mos | This is occurring due to caching. Hence user is expected to |
| ip.atl | reload the tabular page of API Keys to see the latest       |
| assian | status in View API Key screen.                              |
| .net/b |                                                             |
| rowse/ |                                                             |
| MOSIP- |                                                             |
| 34427) |                                                             |
+--------+-------------------------------------------------------------+
| [      | Length validation of OIDC Client name is not functioning as |
| MOSIP- | expected for lengthy names within the given range. This has |
| 34109] | a dependency with eSignet, where the column size needs to   |
| (https | be increased.                                               |
| ://mos |                                                             |
| ip.atl | Its suggested that meaningful and reasonable length be      |
| assian | utilised for OIDC Client name.                              |
| .net/b |                                                             |
| rowse/ |                                                             |
| MOSIP- |                                                             |
| 34109) |                                                             |
+--------+-------------------------------------------------------------+
| [      | Unable to select policy group in tablet and mac devices.    |
| MOSIP- |                                                             |
| 39623] | This issue is found when more than 3000 Policy Groups are   |
| (https | getting loaded into the Dropdown for selection. As a        |
| ://mos | workaround, suggested to keep the create policy groups less |
| ip.atl | than 3000.                                                  |
| assian |                                                             |
| .net/b |                                                             |
| rowse/ |                                                             |
| MOSIP- |                                                             |
| 39623) |                                                             |
+--------+-------------------------------------------------------------+
| [      | In UI, both PARTNER_ADMIN and POLICYMANAGER roles are       |
| MOSIP- | necessary to access Policy features. But in API, either of  |
| 38393] | the two roles are sufficient to perform any policy related  |
| (https | functionalities.                                            |
| ://mos |                                                             |
| ip.atl |                                                             |
| assian |                                                             |
| .net/b |                                                             |
| rowse/ |                                                             |
| MOSIP- |                                                             |
| 38393) |                                                             |
+--------+-------------------------------------------------------------+
| [      | An error is thrown when public key in JWK format is         |
| MOSIP- | entered, due to which unable to submit the details. This is |
| 35085] | faced only in Safari browser of Macbook.                    |
| (https |                                                             |
| ://mos | As a workaround, the create OIDC Client functionality can   |
| ip.atl | be performed across Chrome/ Firefox/ Edge/ Safari in        |
| assian | Windows OS or Chrome/ Firefox/ Edge in mac OS, until this   |
| .net/b | is resolved.                                                |
| rowse/ |                                                             |
| MOSIP- |                                                             |
| 35085) |                                                             |
+--------+-------------------------------------------------------------+
| [      | Add Installation scripts for each module-wise apitest.      |
| MOSIP- |                                                             |
| 35421] |                                                             |
| (https |                                                             |
| ://mos |                                                             |
| ip.atl |                                                             |
| assian |                                                             |
| .net/b |                                                             |
| rowse/ |                                                             |
| MOSIP- |                                                             |
| 35421) |                                                             |
+--------+-------------------------------------------------------------+

For more details on all the known issues, please refer
[here](https://mosip.atlassian.net/issues/?filter=12233&jql=project%20%3D%20MOSIP%20AND%20%22Epic%20Link%22%20%3D%20MOSIP-32075%20and%20labels%3Dknown_issue%20and%20%22Severity%5BDropdown%5D%22%20in%20%28Blocker%2C%20critical%2C%20major%2C%20minor%29%20and%20status%20not%20in%20%28Closed%29).

### **Repositories Released**

  ------------------------------------------------------------------------
  **Repository Released**                **Branch name**      **Tags**
  -------------------------------------- -------------------- ------------
  partner-management-services            release-1.2.2.x      v1.2.2.0

  partner-management-portal              release-1.2.2.x      v1.2.2.0

                                                              

                                                              
  ------------------------------------------------------------------------

### Compatible Modules

The following table outlines the tested and certified compatibility of
PMS 1.2.2.0 with other modules.

  -----------------------------------------------------------------------------------------------------------------
  **Module/ Repo**                                **Tags**
  ----------------------------------------------- -----------------------------------------------------------------
  **Key Manager**                                 v1.3.0-beta.2

  **auth manager**                                1.2.0.1

  **artifactory**                                 1.2.0.2

  IDA                                             1.2.1.0

  **eSignet**                                     1.4.1

  **Reg Proc**                                    [v1.2.0.1](https://github.com/mosip/registration/tree/v1.2.0.1)

  **kernel notification service**                 1.2.0.1

  **Audit manager**                               1.2.0.1

  **ID Repo**                                     1.2.1.0

  **datashare**                                   [v1.2.0.1](https://github.com/mosip/durian/tree/v1.2.0.1)

  **Keycloak**                                    [v1.2.0.1](https://github.com/mosip/keycloak/tree/v1.2.0.1)

  **mosip config**                                1.1.2

  config-server                                   1.1.2

  **Websub**                                      1.2.0.1
  -----------------------------------------------------------------------------------------------------------------

### Services

For code and implementation of Partner Management Services, refer
[here](https://github.com/mosip/partner-management-services/tree/release-1.2.2.x).

### Partner Management Portal UI

For code and implementation of Partner Management Portal (revamp) ,
refer
[here](https://github.com/mosip/partner-management-portal/tree/release-1.2.2.x).

To get started with the new interface of Partner Management Portal,
refer to the [Partner Management Portal End User
Guide](https://docs.mosip.io/1.2.0/modules/partner-management-services/pms-revamp/functional-overview).

### Build and Deploy

To access the build and read through the deployment instructions, refer
to the [Partner Management Services Deployment
Guide](https://docs.mosip.io/1.2.0/modules/partner-management-services/pms-revamp/technical-overview/build-and-development-guide).

**Note**: The deployment script for the PMS module-wise test rig will be
addressed in the next release. Meanwhile, users who wish to run
automation tests can refer to the
[[documentation]{.underline}](https://github.com/mosip/mosip-infra/tree/v1.2.0.2/deployment/v3/testrig)
and deploy using the image mosipid/apitest-pms:1.2.2.0 .

### Configurations

For details related to partner management services revamp
configurations, refer to the [PMS Revamp Configuration
Guide](https://docs.mosip.io/1.2.0/modules/partner-management-services/pms-revamp/technical-overview/pms-configuration-guide)

### **Collab Guide**

To assist you with accessing PMS on Collab environment ,refer to
**[[\<collab_updated_doc\>]{.underline}](https://docs.mosip.io/1.2.0/collab-getting-started-guide/collab-pmp-guide)
// this section will be updated soon!!**

### Developers Guide

For a detailed description of Partner Management System, code, design,
and setup steps, refer to:

1.  [UI Developer's
    Guide](https://docs.mosip.io/1.2.0/modules/partner-management-services/pms-revamp/technical-overview/ui-developers-guide)

2.  [Backend Developer's
    Guide](https://docs.mosip.io/1.2.0/modules/partner-management-services/pms-revamp/technical-overview/backend-developers-guide)

### API

Refer [API
Documentation](https://mosip.stoplight.io/docs/partner-management-portal-revamp).

**Note:** Please refer to this
[document](file:////wiki/spaces/PMS/pages/1577451541/PMS+Revamp1.2.2.0+-+Changes+in+API+NEW)
which captures all the changes that have been made in the existing API
endpoints during the PMS Revamp Release 1.2.2.0. These changes include
addition of new endpoints, deprecation of a few endpoints and also some
other changes.

### Test Report

For details on the test results, refer
[here](https://github.com/mosip/test-management/tree/master/PMS%20Revamp/1.2.2.0).

## Other Documentation

-   [Technology
    Stack](https://docs.mosip.io/1.2.0/modules/partner-management-services/pms-revamp/technical-overview/technology-stack)

-   [Browsers
    Supported](https://docs.mosip.io/1.2.0/modules/partner-management-services/pms-revamp/technical-overview/browsers-supported)
