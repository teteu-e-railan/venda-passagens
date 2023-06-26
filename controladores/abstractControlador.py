from telas.abstractFrame import AbstractFrame


class AbstractController:
    """Classe abstrata para controladores que possuem uma tela."""

    STATE_INITIALIZED = 0
    STATE_CONFIGURED = 1
    STATE_STARTED = 2
    STATE_STOPPED = -1

    VIEW_CLASS = AbstractFrame

    def __init__(self, parent, view=None):
        self.__parent = parent
        self.__view = view

        self.__state = self.STATE_INITIALIZED

    @property
    def state(self):
        return self.__state

    @property
    def parent_view(self):
        return self.__parent.root

    @property
    def view(self):
        return self.__view

    def is_initialized(self):
        return self.state == self.STATE_INITIALIZED

    def is_configured(self):
        return self.state == self.STATE_CONFIGURED

    def is_running(self):
        return self.state == self.STATE_STARTED

    def is_stopped(self):
        return self.state == self.STATE_STOPPED

    def init_config(self):
        self.__init_config()
        self._state = self.STATE_CONFIGURED

        return self

    def __init_config(self):
        """Método de configuracao para preparar o controlador e a tela.

        Deve ser chamado antes de mostrar a tela ou iniciar o controlador.
        """
        if not self.view:
            self.carrega_tela()

        self.view.prepare()

        return self

    def start(self):
        if not self.is_configured():
            self.init_config()

        self._state = self.STATE_STARTED
        return self._start()

    def _start(self):
        """Inicializa o controlador e abre a tela"""
        self.view.show()

    def stop(self):
        """Para o controlador e fecha a tela"""
        self._state = self.STATE_STOPPED
        return self._stop()

    def _stop(self):
        if not self.view.is_closed():
            self.view.close()

    def carrega_tela(self):
        """Retorna a instancia da classe associada ao controlador em VIEW_CLASS"""
        self._view = self.VIEW_CLASS(self.parent_view, self)
        return self.view


class AbstractControllerSet(AbstractController):
    """
    Classe abstrata para controladores que
    possuem uma tela e outros controladores associados.
    """

    def __init__(self, parent, view):
        super().__init__(parent, view)

        self.__controladores = {}

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
