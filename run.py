from main.app import MainApp
from gi.repository import Gtk

win = MainApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
