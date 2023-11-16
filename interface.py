from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import (
    Button,
    Footer,
    Input,
    Header,
    Label,
    RadioButton,
    RadioSet,
    TabbedContent,
    TabPane,
)


class Interface(App[None]):
    CSS_PATH = "radio_set.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(
            yield RadioSet(id="type"):
                yield Label("Type:")
                yield RadioButton("Merchandise")
                yield RadioButton("Services")

            with RadioSet(id="frequency"):
                yield Label("Frequency:")
                yield RadioButton("Annual")
                yield RadioButton("Monthly")

            with RadioSet(id="classification"):
                yield Label("Classification:")
                yield RadioButton("HS")
                yield RadioButton("SITC")
                yield RadioButton("BEC")

            with RadioSet(id="flow"):
                yield Label("Flow:")
                yield RadioButton("Imports")
                yield RadioButton("Exports")
                id="radio"
        )

        with TabbedContent():
            with TabPane("Classification"):
                with Horizontal():
                    yield Label("HS Classification")
                    yield Input(placeholder="01-97")
            with TabPane("Time Period"):
                with Horizontal():
                    yield Label("Time Period")
                    yield Input(placeholder="1994")
            with TabPane("Reporting Country"):
                with Horizontal():
                    yield Label("Reporting Country")
                    yield Input(placeholder="156 - China")
            with TabPane("Partner Country"):
                with Horizontal():
                    yield Label("Partner Country")
                    yield Input(placeholder="156 - China")
            with TabPane("2nd Partner Country"):
                with Horizontal():
                    yield Label("2nd Partner Country")
                    yield Input(placeholder="156 - China")

        Button("Default")

        yield Footer()

    def on_mount(self) -> None:
        self.title = "UN COMTRADE DATA DOWNLOADER"


if __name__ == "__main__":
    app = Interface()
    app.run()
