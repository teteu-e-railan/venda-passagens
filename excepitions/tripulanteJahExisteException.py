class TripulanteJahExisteException(Exception):
    def __init__(self):
        super().__init__("Tripulante já existe!")
