import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class mywindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Configuration")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(500)

        checkbutton = Gtk.CheckButton("Click me!")
        stack.add_titled(checkbutton, "check", "Simple View")
        
        label = Gtk.Label()
        label.set_markup("<big>A fancy label</big>")
        stack.add_titled(label, "label", "Advanced View")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)

window = mywindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()

Gtk.main()
