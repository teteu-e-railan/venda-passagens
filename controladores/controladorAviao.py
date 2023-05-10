from entidades.aviao import Aviao
from telas.telaAviao import TelaAviao

class ControladorAviao():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_aviao = TelaAviao()
        self.__avioes: list[Aviao] = [] 
        
    def buscar_aviao_por_modelo(self, modelo):
        for aviao in self.__avioes:
            if(aviao.modelo == modelo):
                return aviao
        return None
    
    def incluir_aviao(self):
        dados_aviao = self.__tela_aviao.pega_dados_aviao()
        if(dados_aviao is not None):
            try:
                for aviao in self.__avioes:
                    if(aviao.modelo == dados_aviao["modelo"]):
                        raise Exception
                novo_aviao = Aviao(dados_aviao["modelo"], dados_aviao["fileiras"], dados_aviao["assentos_por_fileira"])
                self.__avioes.append(novo_aviao)
            except Exception: 
                pass
    
    def alterar_aviao(self, modelo):
        aviao = self.buscar_aviao_por_modelo(modelo)
        if aviao is None:
            self.__tela_aviao.mostra_mensagem("Avião não encontrado!!!")
        else:
            dados_aviao = self.__tela_aviao.pega_dados_aviao()
            aviao.modelo = dados_aviao["modelo"]
            aviao.fileiras = dados_aviao["fileiras"]
            aviao.assentos_por_fileira = dados_aviao["assentos_por_fileira"]
            