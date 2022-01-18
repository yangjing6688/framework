StartTest(function(t) {
    t.chain(
        {
            action: "click",
            target: "#leftNavToolbar button[text=Network] => .x-btn-inner-extr-nav-toolbar-button-small"
        },
        {
            action: "rightclick",
            target: "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel deviceGrid[title=Devices] tableview => .x-grid-cell:nth-of-type(3) .x-grid-cell-inner"
        },
        {
            waitFor: 2000
        },
        {
            action: "click",
            target: "menu(true):root(21) menuitem[text=Configuration\/Firmware] => .x-menu-item-text"
        },
        {
            action: "moveCursorTo",
            target: "menu(true):root(21) #deviceGridMenu #ext-259 => .x-menu-item-link"
        },
        {
            action: "click",
            target: "menu(true):root(21) #deviceGridMenu #ext-261 => .x-menu-item-text"
        },
        {
            wait_for_load_mask: ["loadmask[msg=Retrieving firmware information from ExtremeNetworks.com...]", "[0]"]
        },
        {
            action: "click",
            target: "firmwareReleasesWindow[title=Current Firmware Releases] button[text=OK] => .x-btn-inner-blue-small"
        }
    )
})