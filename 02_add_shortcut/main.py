import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio, GLib


APPID = 'com.github.taniyoshima.pyt_gtk4_headerbar'


@Gtk.Template(filename=os.path.dirname(__file__) + '/ui_file.ui')
class Gtk4TestTest(Gtk.ApplicationWindow):

    __gtype_name__ = "window"

    menubutton = Gtk.Template.Child()
    menu = Gtk.Template.Child()

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

        action = Gio.SimpleAction.new("button", None)
        action.connect("activate", self.on_button_clicked)
        self.add_action(action)

        lbl_variant = GLib.Variant.new_string("Button1")
        action = Gio.SimpleAction.new_stateful(
            "button1", lbl_variant.get_type(), lbl_variant)
        action.connect("change-state", self.on_button1_clicked)
        self.add_action(action)

        action = Gio.SimpleAction.new_stateful(
            "button3", None, GLib.Variant.new_boolean(False))
        action.connect("change-state", self.on_button3_clicked)
        self.add_action(action)

        popover = Gtk.PopoverMenu.new_from_model(self.menu)
        self.menubutton.set_popover(popover)

    def on_button_clicked(self, action, param):
        print('button selected')

    def on_button1_clicked(self, action, param):
        action.set_state(param)
        print(param.get_string())

    def on_button3_clicked(self, action, param):
        action.set_state(param)
        if param.get_boolean():
            print('hello')
        else:
            print('hi')



class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        window = Gtk4TestTest(self)
        window.present()


def main():
    app = Gtk4TestApp()
    app.run()


if __name__ == '__main__':
    main()
