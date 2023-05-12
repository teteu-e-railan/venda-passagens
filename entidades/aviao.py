class Aviao:
    def __init__(
        self,
        modelo: str,
        fileiras: int,
        assentos_por_fileira: int,
    ):
        self.__modelo = modelo
        self.__fileiras = fileiras
        self.__assentos_por_fileira = assentos_por_fileira
        self.__assentos_total = assentos_por_fileira * fileiras

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, novo_modelo: str):
        self.__modelo = novo_modelo

    @property
    def fileiras(self):
        return self.__fileiras

    @fileiras.setter
    def fileiras(self, nova_fileiras: int):
        self.__fileiras = nova_fileiras
        self.__assentos_total = self.assentos_por_fileira * self.fileiras

    @property
    def assentos_por_fileira(self):
        return self.__assentos_por_fileira

    @assentos_por_fileira.setter
    def assentos_por_fileira(self, nova_assentos_por_fileira: int):
        self.__assentos_por_fileira = nova_assentos_por_fileira
        self.__assentos_total = self.assentos_por_fileira * self.fileiras

    @property
    def assentos_total(self):
        return self.__assentos_total
