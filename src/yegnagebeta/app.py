import toga
from toga.style import Pack
from toga.style.pack import COLUMN

class YegnaGebeta(toga.App):

    def startup(self):

        webview = toga.WebView(
            url="https://test.mychurch.com.et/yegna_gebeta",
            style=Pack(flex=1)
        )

        box = toga.Box(style=Pack(direction=COLUMN, flex=1))
        box.add(webview)

        self.main_window = toga.MainWindow(title="Yegna Gebeta")
        self.main_window.content = box
        self.main_window.show()

def main():
    return YegnaGebeta()