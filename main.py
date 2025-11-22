import functions as fn
fn.show_menu()

option = fn.show_menu()

if option == 1:
    fn.run_search()
    fn.search()
else:
    break

if option == 2:
    fn.edit_name()
else:
    break