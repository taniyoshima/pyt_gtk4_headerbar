import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio


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

        action = Gio.SimpleAction.new("button1", None)
        action.connect("activate", self.on_button1_clicked)
        self.add_action(action)

        action = Gio.SimpleAction.new("button2", None)
        action.connect("activate", self.on_button2_clicked)
        self.add_action(action)

        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.on_about_clicked)
        self.add_action(action)

        popover = Gtk.PopoverMenu.new_from_model(self.menu)
        self.menubutton.set_popover(popover)

    def on_button_clicked(self, action, param):
        print('button selected')

    def on_button1_clicked(self, action, param):
        print('button1 selected')

    def on_button2_clicked(self, action, param):
        print('button2 selected')

    def on_about_clicked(self, action, param):
        print('about selected')


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
