from typing import Callable

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio


def csv_reader():
    for row in open("test_assignment/База для тестового.csv", "r"):
        parsed = row.split(',')
        yield f"{parsed[1]} {parsed[3]}"


def load_from_file() -> list:
    return [row for row in csv_reader()]


def load_from_api() -> list:
    return [f"Example string {i}" for i in range(100)]


class MainApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Скачать приложение")
        self.set_default_size(800, 600)
        self.set_border_width(10)

        self.download_button = Gtk.Button(label="Загрузить из API")
        self.download_button.connect("clicked", self.on_download_button_clicked)

        self.file_button = Gtk.Button(label="Загрузить из файла")
        self.file_button.connect("clicked", self.on_file_button_clicked)

        self.list_box = Gtk.ListBox()
        self.list_box.set_selection_mode(Gtk.SelectionMode.NONE)

        self.grid = Gtk.Grid(expand=True)
        self.grid.attach(self.download_button, 0, 0, 1, 1)
        self.grid.attach(self.file_button, 1, 0, 1, 1)
        self.grid.attach(self.list_box, 0, 2, 4, 1)
        self.add(self.grid)

    def on_download_button_clicked(self, widget):
        loading_dialog = LoadingDialog(self, "Загрузка из API...", load_from_api)
        response = loading_dialog.run()
        for line in loading_dialog.get_result():
            self.add_list_item(line)
        loading_dialog.destroy()
        self.show_all()

    def on_file_button_clicked(self, widget):
        loading_dialog = LoadingDialog(self, "Загрузка из файла...", load_from_file)
        response = loading_dialog.run()
        for line in loading_dialog.get_result():
            self.add_list_item(line)
        loading_dialog.destroy()
        self.show_all()

    def add_list_item(self, text):
        row = Gtk.ListBoxRow()
        label = Gtk.Label(label=text)
        row.add(label)
        self.list_box.add(row)


class LoadingDialog(Gtk.Dialog):
    def __init__(self, parent, title: str, load_func: Callable):
        Gtk.Dialog.__init__(self, title, parent, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                                     Gtk.STOCK_OK, Gtk.ResponseType.OK))

        box = self.get_content_area()
        spinner = Gtk.Spinner()
        box.pack_start(spinner, True, True, 0)
        spinner.start()
        self.result = ""
        # self.connect("response", self.on_response)
        self.show_all()
        self.result = load_func()
        pass

    def get_result(self):
        return self.result


if __name__ == "__main__":
    win = MainApp()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
