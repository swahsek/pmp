# User Guide

## PMS Admin (Partner Admin)

**Partner Management Portal (PMP) is used by both; PMS Admin and Partner
User.**

-   Partner Administrator: Partner Admin
-   Partners: Partner User

<!-- -->

-   [**Partner User** - 'Authentication Partners' can use the new
    interface to perform all the activities mentioned under
    '**[Authentication Partner
    Workflow](end-user-guide.md#authentication-partner-workflow)'**]{.mark}
-   [**Partner Admin** - Partner Admin still will have to user the older
    'Partner Admin Interface to perform all the activities explained
    under'[**What all activities does a 'Partner Admin' perform for
    Authentication
    Partner?**](end-user-guide.md#what-all-activities-does-a-partner-admin-perform-for-authentication-partner)'.
    {% endhint %}]{.mark}

## What all activities does a 'Partner Admin' perform for Authentication Partner?

Being a 'Partner Admin' you can perform following 3 activities to
complete the end to end functionality pertaining to Authentication
partner.

It should be noted that all these activities that you can perform as an
admin you will still have to use the older 'Partner Admin Interface' as
of now untill we complete its revamp which is already underway on a war
footing.

-   Upload Root CA and Sub CA Certificates
-   Create Policy Group and Policy
-   Approve/Reject Policy

### Upload Root CA and Sub CA

Only after you 'Upload Root CA and Sub CA Certificates (From Older PMP
Interface)' that a Partner will then be able to 'Upload CA signed
Partner Certificate.

> As a process of Partner onboarding onto PMP after successful
> registration, Partner is required to **Upload CA signed Partner
> Certificate** on behalf of their organisation which would be used to
> build a trust store in MOSIP to cryptographically validate that they
> are from a trusted organisation to perform authentication of citizens.
> Also this certificate is used to encrypt the response shared in e-KYC.

{% hint style="warning" %} **Important:**

You will have to use older Partner Admin interface, Yes! you read it
correct! before a Partner will be able to '**Upload 'CA Signed
Certificate**' it is prerequisite that the '**Partner Admin**' must
upload the **Root CA** and **Sub CA** certificates and this you can do
from '**Older PMP Interface'**. {% endhint %}

#### [To Upload Root CA and Sub CA Certificates]{.mark}

1.  [In 'Certificate Trust Store' click on 'Upload Trust
    Certificate'.]{.mark}
2.  [Select the Partner Domain- AUTH in Upload Trust Certificate
    page.]{.mark}
3.  [Choose the **Root CA Certificate** to upload (only files with
    extensions as .cer or .pem).]{.mark}
4.  [Click Submit.]{.mark}
5.  [Similarly, sub/intermediate CA certificate should be uploaded by
    following the above steps (1-4).]{.mark}

<figure>
<img src="/Users/keshavsingh/Office/pmp/half/media/image1.png"
style="width:6.49183in;height:2.88954in" />
<figcaption><p>image</p></figcaption>
</figure>

### [Creating Policy Group and Policy]{.mark}

[As Partner Admin you are required to '**Create Policy Group**' and
'**Create Policy(s)**' which a 'Partner' will be able to select while
self-registering on PMP.]{.mark}

[As an admin you will also have privilege to '**Approve Policy
Request**' when a Partner selects a Policy and it comes to you for
approval, You can read more about this
[**here**](end-user-guide.md#approve-policy-request).]{.mark}

#### [Create Policy group]{.mark}

-   [Login as Partner Admin into the PMS portal (Older PMP
    Interface).]{.mark}

-   [All the policy groups created so far by Partner Admin/ Policy
    Manager are displayed on 'List of Policy Groups' page.]{.mark}

![](/Users/keshavsingh/Office/pmp/half/media/temp-auth-partner-image2.png){width="6.84375in"
height="3.007179571303587in"}

-   [On clicking the 'Create Policy Group' option on the top right of
    the screen, we can create a Policy Group by providing suitable name
    and description that is self explanatory for partners, who would be
    selecting them during Partner Policy Request to create API Key/ OIDC
    Client etc.]{.mark}

![](/Users/keshavsingh/Office/pmp/half/media/image3.png){width="6.347222222222222in"
height="2.7604779090113736in"}

-   [On click of Submit, a success message appears.]{.mark}

![](/Users/keshavsingh/Office/pmp/half/media/image4.png){width="6.096946631671041in"
height="2.6821139545056867in"}

#### [Create Auth policy]{.mark}

[Once you 'Create Policy' you will also be required to activate it and
then it will reflect when a Partner wants to select a policy. You can
also change the status of **Policy Group** ( Deactivate) or edit it
using the Action menu as shown below.]{.mark}

1.  [On clicking Authentication Policy tab, List of all previously
    created Authentication Policies are displayed.]{.mark}

[On clicking Authentication Policy tab, List of all previously created
Authentication Policies are displayed.]{.mark}

![](/Users/keshavsingh/Office/pmp/half/media/image5.png){width="6.184027777777778in"
height="2.8616535433070864in"}

[On clicking 'Create Authentication Policy' button, Partner Admin/
Policy manager is navigated to Create Authentication Policy page where
details such as policy group, policy name, description etc will have to
be entered]{.mark}

[Note: Only active policy groups are available in the policy group
dropdown.]{.mark}

[click on the upload button to upload policy data . Only json files are
allowed for upload.]{.mark}

![](/Users/keshavsingh/Office/pmp/half/media/image6.png){width="5.868055555555555in"
height="2.546596675415573in"}

[On clicking on Save as Draft, following success message appears
.]{.mark}

![](/Users/keshavsingh/Office/pmp/half/media/image7.png){width="6.15625in"
height="2.724448818897638in"}

[On clicking 'Go Back', admin is navigated back to tabular view where
the policy is saved as 'draft' status.]{.mark}

[To **publish policy** which is currently in draft status, click on
'publish' option in action menu. A popup window appears seeking for
confirmation to publish.]{.mark}

![](/Users/keshavsingh/Office/pmp/half/media/image8.png){width="6.326388888888889in"
height="2.744536307961505in"}

[On clicking Publish, a success message appears . Click on close to
close the window.]{.mark}

![](/Users/keshavsingh/Office/pmp/half/media/image9.png){width="6.003472222222222in"
height="2.5937117235345584in"}

[The given policy changes to 'Activated' status after being published.
Once activated, the admin cannot edit the policy, hence the option is
disabled.]{.mark}

[Approve Policy Request]{.mark}

[When a Partner have chosen a 'Policy Group' and the 'Policy', an
approval request will come to you and you can approve or reject a
'**Policy Request**' using '**Request Policy**' screen.]{.mark}

[When a Partner have chosen a 'Policy Group' and the 'Policy' an
approval request will come to you and you can approve or reject a
'**Policy Request**' using '**Request Policy**' screen.]{.mark}

-   [Click on **Partner Policy Linking** in the admin dashboard.]{.mark}
-   [Select the policy mapping that needs an approval.The options
    provided for policy linking requests in 'Pending for Approval' are
    to Approve/ Reject. Also an option to view the policy request
    details is also provided.]{.mark}

![](/Users/keshavsingh/Office/pmp/half/media/image10.png){width="6.861111111111111in"
height="2.987739501312336in"}

[On clicking the Approve/ Reject option, the window appears - and
partner admin can click on either Approve or Reject to take appropriate
action]{.mark}

![](/Users/keshavsingh/Office/pmp/half/media/image11.png){width="6.399305555555555in"
height="2.811311242344707in"}

[The status- Approved / Rejected gets updated in the tabular
view.]{.mark}

![](/Users/keshavsingh/Office/pmp/half/media/image12.png){width="6.46875in"
height="2.8723359580052494in"}
