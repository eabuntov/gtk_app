from main.app import MainApp
from gi.repository import Gtk

win = MainApp()
win.connect("destroy", Gtk.main_quit)
for i in range(100):
    win.add_list_item(f"Example string {i}")
win.show_all()
Gtk.main()
