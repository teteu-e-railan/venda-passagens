from customtkinter import CTk


class App:
    def __init__(self):
        self.__root = CTk()
        self.__controladores = {}

    @property
    def root(self):
        return self.__root

    @property
    def controladores(self):
        return self.__controladores

    def get_controlador(self, key: str):
        if key not in self.controladores:
            raise KeyError(f"Controlador {key} não registrado!")

        return self.controladores[key]

    def add_controlador(self, key: str, controlador):
        if key in self.controladores:
            raise KeyError(f"Controlador {key} já existe!")

        self.controladores[key] = controlador

    def init_config(self):
        self._init_config()
        self.__is_configured = True

        return self

    def _init_config(self):
        """Configura a aplicaçao e carrega pelo menos um controlador"""
        raise NotImplementedError

    def run(self):
        self.init_config()
        self.start()
        self._execute()

    def _execute(self):
        """Executa o loop principal"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            pass

    def start(self):
        if not self.__is_configured:
            self.init_config()

        self._start()

    def _start(self):
        raise NotImplementedError

    def stop(self):
        self.root.quit()
