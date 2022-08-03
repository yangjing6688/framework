# extauto.xiqse.flows.license package

## extauto.xiqse.flows.license.XIQSE_LicenseAgreement module


### _class_ extauto.xiqse.flows.license.XIQSE_LicenseAgreement.XIQSE_LicenseAgreement()
Bases: `LicenseAgreementWebElements`


#### xiqse_accept_license_agreement()
> 
> * This keyword selects the “I accept the License Agreement” checkbox.


> * Keyword Usage

> > 
> > * `XIQSE Accept License Agreement`


* **Returns**

    1 if action successful, else -1



#### xiqse_accept_license_agreement_and_click_next()
> 
> * This keyword selects the “I accept the License Agreement” checkbox and clicks Next.


> * Keyword Usage

> > 
> > * `XIQSE Accept License Agreement and Click Next`


* **Returns**

    1 if action successful, else -1



#### xiqse_confirm_accept_license_agreement_checkbox_deselected()
> 
> * This keyword confirms the checkbox to select the license agreement is deselected.


> * Keyword Usage

> > 
> > * `XIQSE Confirm Accept License Agreement Checkbox Deselected`


* **Returns**

    1 if action successful, else -1



#### xiqse_confirm_accept_license_agreement_checkbox_selected()
> 
> * This keyword confirms the checkbox to select the license agreement is selected.


> * Keyword Usage

> > 
> > * `XIQSE Confirm Accept License Agreement Checkbox Selected`


* **Returns**

    1 if action successful, else -1



#### xiqse_confirm_license_agreement_next_button_disabled()
> 
> * This keyword confirms the Next button is disabled.


> * Keyword Usage

> > 
> > * `XIQSE Confirm License Agreement Next Button Disabled`


* **Returns**

    1 if action successful, else -1



#### xiqse_confirm_license_agreement_next_button_enabled()
> 
> * This keyword confirms the Next button is enabled.


> * Keyword Usage

> > 
> > * `XIQSE Confirm License Agreement Next Button Enabled`


* **Returns**

    1 if action successful, else -1



#### xiqse_confirm_license_agreement_page_displayed()
> 
> * This keyword confirms the License Agreement page is being displayed.


> * Keyword Usage

> > 
> > * `XIQSE Confirm License Agreement Page Displayed`


* **Returns**

    1 if action successful, else -1



#### xiqse_decline_license_agreement()
> 
> * This keyword deselects the “I accept the License Agreement” checkbox.


> * Keyword Usage

> > 
> > * `XIQSE Decline License Agreement`


* **Returns**

    1 if action successful, else -1


## extauto.xiqse.flows.license.XIQSE_LicenseDeployment module


### _class_ extauto.xiqse.flows.license.XIQSE_LicenseDeployment.XIQSE_LicenseDeployment()
Bases: `LicenseDeploymentWebElements`


#### xiqse_confirm_license_deployment_airgap_radio_selected()
> 
> * This keyword confirms the Airgap radio button is selected.


> * Keyword Usage

> > 
> > * `XIQSE Confirm Airgap Radio Selected`


* **Returns**

    1 if action successful, else -1



#### xiqse_confirm_license_deployment_onboard_radio_selected()
> 
> * This keyword confirms the Onboard to ExtremeCloud IQ radio button is selected.


> * Keyword Usage

> > 
> > * `XIQSE Confirm Onboard Radio Selected`


* **Returns**

    1 if action successful, else -1



#### xiqse_confirm_license_deployment_page_displayed()
> 
> * This keyword confirms the License Deployment page is being displayed.


> * Keyword Usage

> > 
> > * `XIQSE Confirm License Deployment Page Displayed`


* **Returns**

    1 if page properly displayed, else -1



#### xiqse_is_license_deployment_page_displayed()
> 
> * This keyword checks if the License Deployment page is being displayed.


> * Keyword Usage

> > 
> > * `XIQSE Is License Deployment Page Displayed`


* **Returns**

    1 if page is displayed, else -1



#### xiqse_license_deployment_click_next()
> 
> * This keyword clicks the Next button on the license deployment page.


> * Keyword Usage

> > 
> > * `XIQSE License Deployment Click Next`


* **Returns**

    1 if action successful, else -1



#### xiqse_license_deployment_select_airgap_radio()
> 
> * This keyword selects the Airgap radio button on the license deployment page.


> * Keyword Usage

> > 
> > * `XIQSE License Deployment Select Airgap Radio`


* **Returns**

    1 if action successful, else -1



#### xiqse_license_deployment_select_onboard_radio()
> 
> * This keyword selects the Onboard radio button on the license deployment page.


> * Keyword Usage

> > 
> > * `XIQSE License Deployment Select Onboard Radio`


* **Returns**

    1 if action successful, else -1


## extauto.xiqse.flows.license.XIQSE_LicenseOnboard module


### _class_ extauto.xiqse.flows.license.XIQSE_LicenseOnboard.XIQSE_LicenseOnboard()
Bases: `LicenseOnboardWebElements`


#### get_xiqse_serial_number_from_onboard_page()
> 
> * This keyword returns the XIQ-SE serial number listed on the Advanced section of the Welcome/Onboard page.


> * Keyword Usage

> > 
> > * `Get XIQSE Serial Number from Onboard Page`


* **Returns**

    XIQ-SE serial number, if found;  else, -1



#### get_xiqse_serial_number_label_value_from_onboard_page()
> 
> * This keyword returns the XIQ-SE serial number, found on the Welcome/Onboard page.


> * It is assumed the Welcome/Onboard page is displayed and the Advanced section is expanded.


> * Keyword Usage

> > 
> > * `Get XIQSE Serial Number Label Value from Onboard Page`


* **Returns**

    XIQ-SE serial number, if found;  else, empty string



#### xiqse_confirm_onboard_page_displayed()
> 
> * This keyword confirms the Onboard to ExtremeCloud IQ page is being displayed.


> * Keyword Usage

> > 
> > * `XIQSE Confirm Onboard Page Displayed`


* **Returns**

    1 if action successful, else -1



#### xiqse_onboard_to_xiq(email, pwd)
> 
> * This keyword enters the email and password and clicks the Onboard button on the Onboard to XIQ page.


> * It is assumed the Onboard to ExtremeCloud IQ page is displayed.


> * NOTE: this keyword does not check that the onboard itself was successful.


> * Keyword Usage

> > 
> > * `XIQSE Onboard to XIQ`


* **Parameters**

    
    * **email** – value to enter in the Email field


    * **pwd** – value to enter in the Password field



* **Returns**

    1 if action successful, else -1
