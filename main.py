from app import App
from controladores.controladorSistema import ControladorSistema


class AppSistema(App):
    def _init_config(self):
        self.add_controlador("main", ControladorSistema(self))

    @property
    def main(self):
        return self.get_controlador("main")

    def _start(self):
        self.main.start()


if __name__ == "__main__":
    AppSistema().run()
