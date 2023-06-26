from customtkinter import CTkFrame


class BaseFrame:
    """Classe usada para compartilhar as funcionalidades basicas de todos os frames"""

    FONT_FAMILY = "Arial"
    FONT_SMALL = (FONT_FAMILY, 8)
    FONT_NORMAL = (FONT_FAMILY, 10)
    FONT_LARGE = (FONT_FAMILY, 14)
    FONT_HUGE = (FONT_FAMILY, 16)

    @staticmethod
    def configurar_grid(frame: CTkFrame, sticky="nsew", **kwargs):
        frame.grid(sticky=sticky, **kwargs)

    @staticmethod
    def configurar_coluna(frame: CTkFrame, indexes, weight=1, **kwargs):
        if not isinstance(indexes, (tuple, list)):
            indexes = [indexes]

        kwargs["weight"] = weight

        for index in indexes:
            frame.grid_columnconfigure(index, **kwargs)

    @staticmethod
    def configurar_linha(frame, indexes, weight=1, **kwargs):
        if not isinstance(indexes, (tuple, list)):
            indexes = [indexes]

        kwargs["weight"] = weight

        for index in indexes:
            frame.grid_rowconfigure(index, **kwargs)


class AbstractFrame(CTkFrame, BaseFrame):
    """Tela abstrata que implementa algumas funcionalidades basicas"""

    STATE_INITIALIZED = 0
    STATE_CONFIGURED = 1
    STATE_SHOWING = 2
    STATE_HIDDEN = 3
    STATE_CLOSED = -1

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, master=parent)
        self.__view_state = self.STATE_INITIALIZED
        self.__parent = parent
        self.__controller = controller
        self.__widgets = {}

    def __del__(self):
        self.close()

    @property
    def view_state(self):
        return self.__view_state

    @property
    def parent(self):
        """Retorna o "Pai" do widget"""
        return self.__parent

    @property
    def root(self):
        """Retorna a tela base"""
        if isinstance(self.parent, AbstractFrame):
            return self.parent.root

        return self.parent

    @property
    def controlador_app(self):
        """Retorna o controler do App"""
        result = self.controller.parent
        if not isinstance(result, Application):
            result = result.application

        return result

    @property
    def controller(self):
        return self.__controller

    @property
    def widgets(self):
        return self.__widgets

    def is_initialized(self):
        return self.view_state == self.STATE_INITIALIZED

    def is_configured(self):
        return self.view_state == self.STATE_CONFIGURED

    def is_showing(self):
        return self.view_state == self.STATE_SHOWING

    def is_hidden(self):
        return self.view_state == self.STATE_HIDDEN

    def is_closed(self):
        return self.view_state == self.STATE_CLOSED

    def init_components(self):
        self.__init_components()
        self._view_state = self.STATE_CONFIGURED

        return self

    def __init_components(self):
        """Método de configuracao para preparar os componentes da tela."""
        raise NotImplementedError

    def show(self):
        if self.view_state < self.STATE_CONFIGURED:
            self.init_components()

        self._view_state = self.STATE_SHOWING
        self.__show()

    def __show(self):
        """Mostra a tela"""
        self.tkraise()

    def hide(self):
        self._view_state = self.STATE_HIDDEN
        self.__hide()

    def __hide(self):
        """Oculta a tela"""
        self.grid_remove()

    def close(self):
        self._view_state = self.STATE_CLOSED
        return self.__close()

    def __close(self):
        raise NotImplementedError

    def has_widget(self, name):
        return name in self.widgets.keys()

    def add_widget(self, name, widget):
        if self.has_widget(name):
            raise KeyError("Widget name already registered to this view")

        self.widgets[name] = widget
        return widget

    def get_widget(self, name):
        if not self.has_widget(name):
            raise KeyError("Widget name not registered to this view")

        return self.widgets[name]

    def remove_widget(self, name):
        if not self.has_widget(name):
            raise KeyError("Widget name not registered to this view")

        self.widgets.pop(name)
        return not self.has_widget(name)


class AbstractFrameSet(AbstractFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.__frames: dict[str, AbstractFrame] = {}

    @property
    def frames(self):
        return self.__frames

    def get_view(self, key: str):
        if key not in self.frames:
            raise KeyError(f"Frame {key} não registrado!")

        return self.frames[key]

    def add_frame(self, key: str, frame):
        if key in self.frames:
            raise KeyError(f"Frame {key} já existe!")

        self.frames[key] = frame

    def show_frame(self, key: str):
        self.get_view(key).show()

    def hide_frame(self, key: str):
        self.get_view(key).hide()

    def hide_frames(self):
        for key in self.frames:
            self.hide_frame(key)
