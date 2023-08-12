import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio

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

        self.grid = Gtk.Grid()
        self.grid.attach(self.download_button, 0, 0, 1, 1)
        self.grid.attach(self.file_button, 1, 0, 1, 1)
        self.grid.attach(self.list_box, 0, 1, 2, 1)
        self.add(self.grid)

    def on_download_button_clicked(self, widget):
        loading_dialog = LoadingDialog(self, "Загрузка из API...")
        response = loading_dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Загрузка из API...")
        loading_dialog.destroy()

    def on_file_button_clicked(self, widget):
        loading_dialog = LoadingDialog(self, "Загрузка из файла...")
        response = loading_dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Загрузка из файла...")
        loading_dialog.destroy()

    def add_list_item(self, text):
        row = Gtk.ListBoxRow()
        label = Gtk.Label(label=text)
        row.add(label)
        self.list_box.add(row)

class LoadingDialog(Gtk.Dialog):
    def __init__(self, parent, title: str):
        Gtk.Dialog.__init__(self, title, parent, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        box = self.get_content_area()
        spinner = Gtk.Spinner()
        box.pack_start(spinner, True, True, 0)
        spinner.start()

        self.show_all()

if __name__ == "__main__":
    win = MainApp()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
