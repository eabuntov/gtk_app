import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio

from main.controller.main_controller import MainController
from services.components.loading_dialog.view.loading_dialog_view import LoadingDialog


class MainView(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Скачать приложение")
        self.set_default_size(800, 600)
        # self.set_border_width(10)

        self.download_button = Gtk.Button(label="Загрузить из API")
        self.download_button.connect("clicked", self.on_download_button_clicked)

        self.file_button = Gtk.Button(label="Загрузить из файла")
        self.file_button.connect("clicked", self.on_file_button_clicked)

        self.list_box = Gtk.ListBox()
        self.list_box.set_selection_mode(Gtk.SelectionMode.NONE)

        self.grid = Gtk.Grid()
        self.grid.attach(self.download_button, 0, 0, 1, 1)
        self.grid.attach(self.file_button, 1, 0, 1, 1)
        self.grid.attach(self.list_box, 0, 2, 4, 1)
        self.add(self.grid)

    def on_download_button_clicked(self, widget):
        loading_dialog = LoadingDialog(self, "Загрузка из API...", MainController.load_from_api)
        response = loading_dialog.run()
        for line in loading_dialog.get_result():
            self.add_list_item(line)
        loading_dialog.destroy()
        self.show_all()

    def on_file_button_clicked(self, widget):
        loading_dialog = LoadingDialog(self, "Загрузка из файла...", MainController.load_from_file)
        loading_dialog.run()
        for line in loading_dialog.get_result():
            self.add_list_item(line)
        loading_dialog.destroy()
        self.show_all()

    def add_list_item(self, text):
        row = Gtk.ListBoxRow()
        label = Gtk.Label(label=text)
        row.add(label)
        self.list_box.add(row)

if __name__ == "__main__":
    win = MainView()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()