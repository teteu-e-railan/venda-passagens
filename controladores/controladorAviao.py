from entidades.aviao import Aviao


class ControladorAviao(Aviao):
    def __init__(self, modelo: str, fileiras: int, assentos_por_fileira: int):
        super().__init__(modelo, fileiras, assentos_por_fileira)
        self.__avioes: list[Aviao] = []

    
    # verificar se o avião ja existe dentro da lista
    def incluir_aviao(self):
        aviao = Aviao(self.__modelo, self.__fileiras, self.__assentos_por_fileira)
        self.__avioes.append(aviao)
        return aviao

    # verificar se o avião existe dentro da lista e assim sim deletar
    def deletar_aviao(self):
        aviao = Aviao(self.__modelo, self.__fileiras, self.__assentos_por_fileira)
        self.__avioes.remove(aviao)
        return aviao
    