class Aviao:
    def __init__(self,codigo: str, modelo: str, fileiras: int, assentos_por_fileira: int):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__fileiras = fileiras
        self.__assentos_por_fileira = assentos_por_fileira
        self.__assentos_total = assentos_por_fileira * fileiras


    '''adicionei a propiedade CODIGO parar ser mais facil de encontar o avião na hora de alterar
    os dados, vamos utilizar o codigo apra ser o localizador dele dentro da lista.
    '''
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

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

    @property
    def assentos_por_fileira(self):
        return self.__assentos_por_fileira
    
    @assentos_por_fileira.setter
    def assentos_por_fileira(self, nova_assentos_por_fileira: int):
        self.__assentos_por_fileira = nova_assentos_por_fileira

    @property
    def assentos_total(self):
        return self.__assentos_total
    