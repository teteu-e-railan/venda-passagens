class PassageiroJahExisteException(Exception):
    def __init__(self):
        super().__init__("Passageiro já existe!")
