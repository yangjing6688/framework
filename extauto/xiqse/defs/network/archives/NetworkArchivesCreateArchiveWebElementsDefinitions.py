

class NetworkArchivesCreateArchiveWebElementsDefinitions:

    create_cancel_button = \
        {
            'DESC': 'Cancel button for the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//span[text()="Cancel"]/ancestor::a',
            
        }

    create_next_button = \
        {
            'DESC': 'Next button for the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//span[contains(text(), "Next")]/ancestor::a',
            
        }

    create_previous_button = \
        {
            'DESC': 'Previous button for the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//span[contains(text(), "Previous")]/ancestor::a',
            
        }

    create_finish_button = \
        {
            'DESC': 'Finish button for the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//span[text()="Finish"]/ancestor::a',
            
        }

    create_name_field = \
        {
            'DESC': 'Name field in the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//input[@name="archiveName"]',
            
        }

    create_description_field = \
        {
            'DESC': 'Description field in the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//textarea[@name="archiveMemo"]',
            
        }

    create_max_versions_max_radio = \
        {
            'DESC': 'Maximum # of Versions radio button for the Max Versions field in the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//label[text()="Maximum # of Versions"]',
            
        }

    create_max_versions_unlimited_radio = \
        {
            'DESC': 'Unlimited radio button for the Max Versions field in the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//label[text()="Unlimited"]',
            
        }

    create_max_versions_value = \
        {
            'DESC': 'Value for the Maximum # of Versions field in the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//input[@name="archiveMaxVersions"]',
            
        }

    create_type_config_checkbox = \
        {
            'DESC': 'Archive Configuration Data checkbox for the Archive Type field in the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//input[@name="archiveIsConfig"]',
            
        }

    create_type_capacity_checkbox = \
        {
            'DESC': 'Archive Capacity Planning Data checkbox for the Archive Type field in the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//input[@name="archiveIsCapacity"]',
            
        }

    create_frequency_dropdown = \
        {
            'DESC': 'Frequency Dropdown in the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//input[@name="archiveSaveFrequency"]',
            
        }

    create_run_compliance_checkbox = \
        {
            'DESC': 'Run Compliance checkbox for the Compliance field in the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//input[@name="govEnabled"]',
            
        }

    create_regime_dropdown = \
        {
            'DESC': 'Regime Dropdown for the Compliance field in the Create Archive dialog',
            'XPATH': '//div[contains(@id, "archiveWizardWindow")]//input[@name="govRegimeId"]',
            
        }

    create_regime_dropdown_items = \
        {
            'DESC': 'Regime Dropdown Items for the Compliance field in the Create Archive dialog',
            'XPATH': '//div[contains(@class, "x-boundlist-list-ct")]//li',
            
        }

    create_select_device_expand_node = \
        {
            'DESC': 'Expander icon for the Select Devices tree node specified by element_name in the Create Archive dialog',
            'XPATH': '//div[contains(@id, "deviceSelectionTree")]//span[contains(text(), "${element_name}")]' +
                     '/preceding-sibling::div[contains(@class, "x-tree-expander")]',
            
        }

    create_select_device_node = \
        {
            'DESC': 'Select Devices tree node for the device specified by element_name in the Create Archive dialog',
            'XPATH': '//div[contains(@id, "deviceSelectionTree")]//span[text()="${element_name}"]',
            
        }
