Class('EmcUtils', {
    isa         : Siesta.Test.ExtJS,

    methods : {
		find_component_index : function(target, args, key, val, exact_match) {
			// Function Args:
			// [target] - The target for the component query.
			// [args] - The args that should be passed at the end of the component query.
			// [key] - The key within the component to search for.
			// [val] - The value the key should have configured.
			//
			// This function searches through a given component and returns the index if the element is found
			// in the component and -1 if it is not.
			var table = this.execute_cq_by_string(target, args);

			if (exact_match === "True") {
			    exact_match = true;
			}
			else {
			    exact_match = false;
			}

			if (table) {
			    // https://docs.sencha.com/extjs/6.2.0/modern/Ext.data.Store.html#method-find
				return table.store.find(key, val, undefined, undefined, undefined, exact_match);
			}
			return -1;
		},

		find_menu_index : function(target, args, text, exact_match) {
			// Function Args:
			// [target] - The target for the component query.
			// [args] - The args that should be passed at the end of the component query.
			// [text] - The text assigned to the menu item.
			//
			// This function will search through a menus items to determine the index of a given item.
			// If the text is not found -1 is returned.
			var num_items = this.execute_cq_by_string(target, args + ".menu.items.items.length");

			if (num_items > 0) {
				for (i = 0; i < num_items; i++) {
					var item_name = this.execute_cq_by_string(target, args + ".menu.items.items[" + i.toString() + "].text");
					if (exact_match === "True") {
						if (item_name === text) {
							return i;
						}
					}
					else {
						if (item_name.indexOf(text) === 0) {
							return i;
						}
					}
				}
				return -1;
			}
			else {
				return -1;
			}
		},

		//
		// Helper methods
		//
		execute_cq_by_string : function(target, args) {
			return eval("this.global.Ext.ComponentQuery.query('" + target + "')" + args + ";");
		}
	}
})
