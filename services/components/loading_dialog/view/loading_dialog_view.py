import threading
from typing import Callable
from gi.repository import Gtk
from gi.repository import GObject


class LoadingDialog(Gtk.Dialog):
    def __init__(self, parent, title: str, load_func: Callable):
        Gtk.Dialog.__init__(self, title, parent, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        box = self.get_content_area()
        self.spinner = Gtk.Spinner()
        box.pack_start(self.spinner, True, True, 0)
        self.spinner.start()
        self.result = ""
        self.show_all()
        self.load_func = load_func
        self.work_thread = threading.Thread(target=self.run_thread)
        self.work_thread.start()
        self.running = True
        pass

    def run_thread(self):
        self.result = self.load_func()
        GObject.idle_add(self.stop_progress)

    def stop_progress(self):
        self.spinner.stop()
        self.work_thread.join()
        self.destroy()

    def get_result(self):
        return self.result

