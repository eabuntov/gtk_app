import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio

from main.controller.main_controller import MainController
from services.components.loading_dialog import LoadingDialog


class MainView(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Приложение для скачивания")
        self.set_default_size(800, 600)

        self.download_button = Gtk.Button(label="Загрузить из API")
        self.download_button.connect("clicked", self.on_download_button_clicked)

        self.file_button = Gtk.Button(label="Загрузить из файла")
        self.file_button.connect("clicked", self.on_file_button_clicked)

        self.list_box = Gtk.ListBox()
        self.list_box.set_selection_mode(Gtk.SelectionMode.NONE)

        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolled_window.set_hexpand(True)
        self.scrolled_window.set_vexpand(True)
        self.scrolled_window.add(self.list_box)

        self.grid = Gtk.Grid()
        self.grid.attach(self.download_button, 0, 0, 1, 1)
        self.grid.attach(self.file_button, 1, 0, 1, 1)
        self.grid.attach(self.scrolled_window, 0, 1, 2, 1)
        self.grid.set_row_homogeneous(False)
        self.grid.set_row_spacing(10)
        self.add(self.grid)

    def on_download_button_clicked(self, _):
        loading_dialog = LoadingDialog(self, "Загрузка из API...", MainController.load_from_api)
        loading_dialog.run()
        self.clear_list_box()
        for api_result in loading_dialog.get_result():
            for item in api_result:
                self.add_list_item(f"{item['name']} {item['price']}")
        loading_dialog.destroy()
        self.show_all()

    def on_file_button_clicked(self, _):
        loading_dialog = LoadingDialog(self, "Загрузка из файла...", MainController.load_from_file)
        loading_dialog.run()
        self.clear_list_box()
        for line in loading_dialog.get_result():
            self.add_list_item(line)
        loading_dialog.destroy()
        self.show_all()

    def add_list_item(self, text: str):
        row = Gtk.ListBoxRow()
        label = Gtk.Label(label=text)
        row.add(label)
        self.list_box.add(row)

    def clear_list_box(self):
        while row := self.list_box.get_row_at_index(0):
            self.list_box.remove(row)

if __name__ == "__main__":
    win = MainView()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
