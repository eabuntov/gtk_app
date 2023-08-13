from main import MainView
from gi.repository import Gtk

win = MainView()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
