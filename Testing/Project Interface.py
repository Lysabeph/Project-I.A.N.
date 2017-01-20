import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf

import os

def get_resource_path(rel_path):
    dir_of_py_file = os.path.dirname(__file__)
    rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
    abs_path_to_resource = os.path.abspath(rel_path_to_resource)
    return abs_path_to_resource

class mywindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Configuration")
        self.set_icon_from_file(get_resource_path("dice3.png"))

        notebook = Gtk.Notebook()
        notebook.set_tab_pos(Gtk.PositionType(0))
        self.add(notebook)

        self.settings_image_dynamic = Gtk.Image()
        self.settings_image_dynamic.set_from_file("cog_dynamic_32x32.gif")
        self.settings_image_dynamic.set_pixel_size(16)
        self.settings_image_still = Gtk.Image()
        self.settings_image_still.set_from_file("cog_still_32x32.png")
        
        self.settings_button = Gtk.Button()
        self.settings_button.set_image(self.settings_image_still)
        self.settings_button.set_size_request(32,32)
        self.settings_button.connect("clicked", self.settings_button_clicked)

        hbox_mini = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        hbox_mini.pack_start(self.settings_button, False, True, 0)

        page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        page1.set_border_width(10)
        page1.pack_end(hbox_mini, False, True, 0)
        notebook.append_page(page1, Gtk.Label("Recommendations"))

        page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        page2.set_border_width(10)
        notebook.append_page(page2, Gtk.Label("Most Common"))

        page3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        page3.set_border_width(10)
        notebook.append_page(page3, Gtk.Label("Favourites"))

        page4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        page4.set_border_width(10)
        notebook.append_page(page4, Gtk.Label("Settings"))

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.NONE)
        stack.set_transition_duration(500)

        vbox_child = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        check_button = Gtk.CheckButton("Click me!")
        button1 = Gtk.Button(label="This is a button")
        vbox_child.pack_start(check_button, False, True, 0)
        vbox_child.pack_start(button1, False, True, 0)
        stack.add_titled(vbox_child, "box", "Simple View")
        
        label = Gtk.Label()
        label.set_markup("<big>A fancy label</big>")
        stack.add_titled(label, "label", "Advanced View")

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        apply_button = Gtk.Button(label="Apply Changes")
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        hbox.pack_start(stack_switcher, True, True, 0)
        hbox.pack_end(apply_button, True, True, 0)
        vbox.pack_start(stack, True, True, 0)
        vbox.pack_start(hbox, False, True, 0)

    def settings_button_clicked(self, button):
        self.settings_button.set_image(self.settings_image_dynamic)

window = mywindow()
window.set_default_size(1000, 500)
window.connect("delete-event", Gtk.main_quit)
window.show_all()

Gtk.main()
