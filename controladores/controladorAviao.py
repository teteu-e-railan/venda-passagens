from entidades.aviao import Aviao
from telas.telaAviao import TelaAviao

class ControladorAviao():
    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.tela_aviao = TelaAviao()
        self.__avioes: list[Aviao] = [] 
        