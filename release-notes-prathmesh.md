# Release : 1.2.2.0

**Release Name**: Partner Management System Revamp

**Release Number**: v1.2.2.0

**Release Date**: 28th Feb, 2025

# Overview

We are excited to announce the launch of the **new Partner Management
Portal** which is a complete/comprehensive/full release and brings
significant improvement over the earlier one 1.3.0-dp.1. Now out, this
also brings good sum / substantial upgrades to the UX and the UI which
now has enhanced capabilities!

-   The new version **1.2.2.0** is a full feature release, serving as a
    continuation of the earlier developer preview (**1.3.0-dp.1**).

-   This release brings **Technology stack upgrade** for improved
    performance and security.

-   This release brings expanded system capabilities to **various
    Partner Types and Admin Roles** which now includes Partner-1,
    Partner-1, Partner-1.

-   **New functionalities** now spans not only a particular part of the
    PMP but it is ground up improvement that we pulled off on every
    section being released this time.

-   **Feature enhancements** comes to majority of features which existed
    and certainly the new ones and this helps you streamline partner
    management like never before.

-   **Improved usability & user experience** for better navigation and
    efficiency. UX and UI has been worked upon ground up, The user flow
    has now been structured and it is easy and quick to get familiar
    with the interface helping users identify a logical/consistent
    pattern in usage.

This release officially launches **PMS version 1.2.2.0**, focusing on
the implementation of **Device Provider** and **FTM Chip Provider**
partner types along with an enhanced **Partner Admin/Policy Manager
workflow** in the new UI.

This version of PMS is designed to run on 1.2.0.1 version of MOSIP
platform.

The comprehensive release of PMS 1.2.2.0 encompasses improvements done
on almost all the aspects/components of the PMS and which includes
following:

-   PMS for Partner User

-   PMS for Partner Admin

## PMS for Partner User

The current release has focused on the feature enhancement for Device
Provider and FTM Chip Provider which is in addition to the
'Authentication Partner' which we worked upon with last release.

### The key features of Device Provider

-   **Partner Certificate:**

    -   **Upload and Re-upload:** Easily upload or re-upload Certificate
        Authority (CA) signed Partner Certificate.

    -   **Download:** Download CA signed Partner Certificate and
        corresponding MOSIP Signed Certificate.

-   **Device Provider Services:**

    -   **SBI - Device Creation:** Add SBI, Add Devices associated to an
        SBI. SBI / Device submissions will go to Partner Admin for
        approval.

    -   **Deactivate:** Deactivate SBI or Deactivate mapped devices

    -   **View** SBI and its associated devices

### The key features of FTM Chip Provider

-   **Partner Certificate:**

    -   **Upload and Re-upload:** Easily upload or re-upload Certificate
        Authority (CA) signed Partner Certificate.

    -   **Download:** Download CA signed Partner Certificate and
        corresponding MOSIP Signed Certificate.

-   **FTM Chip Services:**

    -   **FTM Chip details:** Add FTM details, deactivate FTM details.

    -   **FTM Chip Certificate:** Upload, Re-upload or download
        certificate.

## PMS for Partner Admin

Partner Admin has gone under a whole sum overhaul and here we enlist
what all is transformed.

### Admin dashboard

The release brings a refreshed new user experience to the Admin
dashboard which now has structured the high level functionalities with
help of cards and which are ordered logically on the dashboard.

-   The dashboard displays the cards for **Certificate Trust Store**,
    **Partners, Policies**, **Parter Policy-Linking**, **SBI-Device**,
    **FTM Chip** and **Authentications Services**.

-   It also displays pending requests count for Partner Policy-Linking,
    SBI-Device and FTM Chip.

### Certificate Trust Store

Upload, Download or View (List View and Detailed view) of Certificates.

### Partners

Download (Original & MOSIP Signed Certificate), Deactivate Partner or
View (List and Detailed View)

### Policies

You can use this section for Policy Group and Policy related operations
enlisted here:

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

-   **View**

    -   **List View**

    -   **Detail View**

-   **Deactivate** Policy Group (if no active policy is linked)

-   **Deactivate** Policy (if no active partner policy mappings)

### Partner Policy Linking

Approve / Reject or View (List View and Details View)

### Authentication Services

OIDC Client: View (List and Details View) or Deactivate

API Key: View (List and Details View) or Deactivate

### SBI-Device

SBI: View (List and Details View), **Approve / Reject** or
**Deactivate** (if no active devices present)

Device: View (List and Details View), **Approve / Reject** or
**Deactivate** (if no active devices present)

### FTM Chip 

View (List and Details View), **Approve / Reject** or **Deactivate** (if
no active devices in FTM Chip present).

## Browser Support

-   Complete support on **Chrome, Firefox, Edge and Safari** ensures a
    seamless user experience across all these popular browsers.

## Language Support

-   Multiple language is supported with support for resource bundles in
    3 languages (English, Arabic, French). More resource bundles can be
    easily added by following the documentation, '[New Language
    Support](file:////wiki/spaces/PMS/pages/1606254602/New+Language+Support)'.

## Compatibility

-   Responsive UI design for laptop/desktop views, Optimized for
    standard browser sizes (laptop/desktop/tablet/larger screens).

For a comprehensive and detailed description of all the features, 'refer
to [Feature
Documentation](https://docs.mosip.io/1.2.0/modules/partner-management-services/pms-revamp/functional-overview/auth-partner/features)'.

To know more about the upcoming features planned as part of PMS Revamp
for this year, please check out [Roadmap
2025](https://docs.mosip.io/1.2.0/roadmap/roadmap-2025#inji-stack-1).

## Known Issues

Below is the list of key [[known
issues]{.underline}](https://mosip.atlassian.net/issues/?filter=12233):

+-----------------+----------------------------------------------------+
| **Jira Issue**  | **Issue Description**                              |
+=================+====================================================+
| [               | Partner domain dropdown items (AUTH/ DEVICE/ FTM)  |
| MOSIP-38890](ht | are in English and do not support multi-language.  |
| tps://mosip.atl |                                                    |
| assian.net/brow |                                                    |
| se/MOSIP-38890) |                                                    |
+-----------------+----------------------------------------------------+
| [               | On deactivating an API key from one browser , the  |
| MOSIP-34427](ht | status still remains \'Activated\' on viewing the  |
| tps://mosip.atl | same API Key details in another browser.           |
| assian.net/brow |                                                    |
| se/MOSIP-34427) | This is occurring due to caching. Hence user is    |
|                 | expected to reload the tabular page of API Keys to |
|                 | see the latest status in View API Key screen.      |
+-----------------+----------------------------------------------------+
| [               | Length validation of OIDC Client name is not       |
| MOSIP-34109](ht | functioning as expected for lengthy names within   |
| tps://mosip.atl | the given range. This has a dependency with        |
| assian.net/brow | eSignet, where the column size needs to be         |
| se/MOSIP-34109) | increased.                                         |
|                 |                                                    |
|                 | Its suggested that meaningful and reasonable       |
|                 | length be utilised for OIDC Client name.           |
+-----------------+----------------------------------------------------+
| [               | Unable to select policy group in tablet and mac    |
| MOSIP-39623](ht | devices.                                           |
| tps://mosip.atl |                                                    |
| assian.net/brow | This issue is found when more than 3000 Policy     |
| se/MOSIP-39623) | Groups are getting loaded into the Dropdown for    |
|                 | selection. As a workaround, suggested to keep the  |
|                 | create policy groups less than 3000.               |
+-----------------+----------------------------------------------------+
| [               | In UI, both PARTNER_ADMIN and POLICYMANAGER roles  |
| MOSIP-38393](ht | are necessary to access Policy features. But in    |
| tps://mosip.atl | API, either of the two roles are sufficient to     |
| assian.net/brow | perform any policy related functionalities.        |
| se/MOSIP-38393) |                                                    |
+-----------------+----------------------------------------------------+
| [               | An error is thrown when public key in JWK format   |
| MOSIP-35085](ht | is entered, due to which unable to submit the      |
| tps://mosip.atl | details. This is faced only in Safari browser of   |
| assian.net/brow | Macbook.                                           |
| se/MOSIP-35085) |                                                    |
|                 | As a workaround, the create OIDC Client            |
|                 | functionality can be performed across Chrome/      |
|                 | Firefox/ Edge/ Safari in Windows OS or Chrome/     |
|                 | Firefox/ Edge in mac OS, until this is resolved.   |
+-----------------+----------------------------------------------------+
| [               | Add Installation scripts for each module-wise      |
| MOSIP-35421](ht | apitest.                                           |
| tps://mosip.atl |                                                    |
| assian.net/brow |                                                    |
| se/MOSIP-35421) |                                                    |
+-----------------+----------------------------------------------------+

For more details on all the known issues, please refer
[here](https://mosip.atlassian.net/issues/?filter=12233&jql=project%20%3D%20MOSIP%20AND%20%22Epic%20Link%22%20%3D%20MOSIP-32075%20and%20labels%3Dknown_issue%20and%20%22Severity%5BDropdown%5D%22%20in%20%28Blocker%2C%20critical%2C%20major%2C%20minor%29%20and%20status%20not%20in%20%28Closed%29).

## Repositories Released

  --------------------------------------------------------------------------
  **Repository Released**       **Branch name**   **Tags**
  ----------------------------- ----------------- --------------------------
  partner-management-services   release-1.2.2.x   v1.2.2.0

  partner-management-portal     release-1.2.2.x   v1.2.2.0
  --------------------------------------------------------------------------

## Compatible Modules

The following table outlines the tested and certified compatibility of
PMS 1.2.2.0 with other modules.

  ---------------------------------------------------------------------------------------------------------------------------
  Modules / Repository                              Tags
  ------------------------------------------------- -------------------------------------------------------------------------
  Key Manager                                       [v1.3.0-beta.2](https://github.com/mosip/keymanager/tree/v1.3.0-beta.2)

  auth manager                                      [1.2.0.1](https://github.com/mosip/mosip-openid-bridge)

  artifactory                                       [1.2.0.2](https://github.com/mosip/artifactory-ref-impl/tree/v1.2.0.2)

  IDA                                               [1.2.1.0](https://github.com/mosip/id-authentication/tree/v1.2.1.0)

  eSignet                                           [1.4.1](https://github.com/mosip/esignet/tree/v1.4.1)

  Reg Proc                                          [1.2.0.1](https://github.com/mosip/registration/tree/v1.2.0.1)

  Notifier (Kernel)                                 [1.2.0.1](https://github.com/mosip/commons/tree/v1.2.0.1/kernel)

  Audit manager                                     [1.2.0.1](https://github.com/mosip/audit-manager/tree/v1.2.0.1)

  ID Repo                                           [1.2.1.0](https://github.com/mosip/id-repository/tree/v1.2.1.0)

  datashare                                         [1.2.0.1](https://github.com/mosip/durian/tree/v1.2.0.1)

  Keycloak                                          [1.2.0.1](https://github.com/mosip/keycloak/tree/v1.2.0.1)

  config-server                                     [v1.1.2](https://github.com/mosip/mosip-config/tree/v1.1.2)

  Websub                                            [1.2.0.1](https://github.com/mosip/websub/tree/v1.2.0.1)
  ---------------------------------------------------------------------------------------------------------------------------

## Documentation

+-------------------+--------------------------------------------------+
| Documentation     | Description                                      |
+===================+==================================================+
| Services          | For code and implementation of Partner           |
|                   | Management Services, refer                       |
|                   | [here](https://github.com/mosip/pa               |
|                   | rtner-management-services/tree/release-1.2.2.x). |
+-------------------+--------------------------------------------------+
| Partner           | To get started with the new interface of Partner |
| Management Portal | Management Portal, refer to the [Partner         |
| End User Guide    | Management Portal End User                       |
|                   | Guide]                                           |
|                   | (https://docs.mosip.io/1.2.0/modules/partner-man |
|                   | agement-services/pms-revamp/functional-overview) |
+-------------------+--------------------------------------------------+
| **Build and       | To access the build and read through the         |
| Deploy**          | deployment instructions, refer to the [Partner   |
|                   | Management Services Deployment                   |
|                   | Guide](https://docs.mosip.io/1.2.0               |
|                   | /modules/partner-management-services/pms-revamp/ |
|                   | technical-overview/build-and-development-guide). |
|                   |                                                  |
|                   | **Note**: The deployment script for the PMS      |
|                   | module-wise test rig will be addressed in the    |
|                   | next release. Meanwhile, users who wish to run   |
|                   | automation tests can refer to the                |
|                   | [[docum                                          |
|                   | entation]{.underline}](https://github.com/mosip/ |
|                   | mosip-infra/tree/v1.2.0.2/deployment/v3/testrig) |
|                   | and deploy using the image                       |
|                   | mosipid/apitest-pms:1.2.2.0 .                    |
|                   |                                                  |
|                   | For details related to partner management        |
|                   | services revamp configurations, refer to the     |
|                   | [PMS Revamp Configuration                        |
|                   | Guide](https://docs.mosip.io/                    |
|                   | 1.2.0/modules/partner-management-services/pms-re |
|                   | vamp/technical-overview/pms-configuration-guide) |
+-------------------+--------------------------------------------------+
| **                | For details related to partner management        |
| Configurations**: | services revamp configurations, refer to the     |
|                   | [PMS Revamp Configuration                        |
|                   | Guide](https://docs.mosip.io/                    |
|                   | 1.2.0/modules/partner-management-services/pms-re |
|                   | vamp/technical-overview/pms-configuration-guide) |
+-------------------+--------------------------------------------------+
| **Collab Guide**: | To assist you with accessing PMS on Collab       |
|                   | environment ,refer to                            |
|                   | **[[\<collab_updated_                            |
|                   | doc\>]{.underline}](https://docs.mosip.io/1.2.0/ |
|                   | collab-getting-started-guide/collab-pmp-guide)// |
|                   | this section will be updated soon!!**            |
+-------------------+--------------------------------------------------+
| **Developers      | For a detailed description of Partner Management |
| Guide**           | System, code, design, and setup steps, refer     |
|                   | to:UI Developer's Guide                          |
|                   |                                                  |
|                   | \- [UI Developer's                               |
|                   | Guide](https://docs.mosip                        |
|                   | .io/1.2.0/modules/partner-management-services/pm |
|                   | s-revamp/technical-overview/ui-developers-guide) |
|                   |                                                  |
|                   | \- [Backend Developer's                          |
|                   | Guide](https://docs.mosip.io/1                   |
|                   | .2.0/modules/partner-management-services/pms-rev |
|                   | amp/technical-overview/backend-developers-guide) |
|                   |                                                  |
|                   | \- API: Refer [API                               |
|                   | Documentation](https://mosip.sto                 |
|                   | plight.io/docs/partner-management-portal-revamp) |
|                   |                                                  |
|                   | Note: Please refer to this document which        |
|                   | captures all the changes that have been made in  |
|                   | the existing API endpoints during the PMS Revamp |
|                   | Release 1.2.2.0. These changes include addition  |
|                   | of new endpoints, deprecation of a few endpoints |
|                   | and also some other changes.                     |
+-------------------+--------------------------------------------------+
| **Test Report**:  | For details on the test results, refer here.     |
+-------------------+--------------------------------------------------+

## 
