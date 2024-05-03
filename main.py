import panel as pn
from model import Person

p = Person()
p.region = "Moscow"

button = pn.widgets.Button(name="Click me", icon="caret-right", button_type="primary")
button_output = pn.widgets.Button(
    name="Click me", icon="caret-right", button_type="primary"
)
output = pn.widgets.TextInput(name="Write me")
input = pn.widgets.TextInput(name="Write me", value=p.region)

components = pn.Column(pn.Row(button, input), pn.Row(button_output, output))


def handle_click(event):
    p.region = input.value


def output_click(event):
    output.value = p.region


button_output.on_click(output_click)
button.on_click(handle_click)
components.servable()
