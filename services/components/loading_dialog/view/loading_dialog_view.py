from typing import Callable
from gi.repository import Gtk


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

