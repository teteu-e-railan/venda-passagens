class AviaoJahExisteException(Exception):
    def __init__(self):
        super().__init__("Avião já existe!")
