from typing import Tuple


class Persona:

    def __init__(self, name: str, 
                surname: str, 
                data_di_nascita: str,
                genere: str) -> None:
        self.nome: str = name
        self.conome: str = surname
        self.data_di_nascita: str = data_di_nascita
        self.genere: str = genere

    def calcola_eta(self)->int:

        return 10



persona_1: Persona = Persona(name="Lollito",
                            surname="Chicano",
                            data_di_nascita="20/04/05",
                            genere="Maschio")

class Dipendente(Persona):

    def __init__(self,
                name: str, 
                surname: str,
                data_di_nascita: str,
                genere: str,
                ore_lavorate: int) -> None:
        super().__init__(name, surname, data_di_nascita, genere)

        self.ore_lavorate: int = ore_lavorate

class Professore(Dipendente):
    def  __init__(self,
                  name: str, 
                  surname: str, 
                  data_di_nascita: str, 
                  genere: str,
                  materia_insegnata: str,
                  ore_di_lezione: int ) -> None:
        super().__init__(name, surname, data_di_nascita, genere)

        self.materia_insegnata: str = materia_insegnata
        self.ore_di_lezione: int = ore_di_lezione

    print(persona_1.calcola_eta)

    def calcola_stipendio()->float:
        
        return 500.0

dipendente_1: Dipendente = Dipendente(name="Lollito",
                            surname="Chicano",
                            data_di_nascita="20/04/05",
                            genere="Maschio")



professore_1: Professore = Professore(name="Lollito",
                            surname="Chicano",
                            data_di_nascita="20/04/05",
                            genere="Maschio",
                            ore_lavorate= 4020,
                            materia_insegnata= "Erbologia",
                            ore_di_lezione= 420)

print(persona_1.calcola_eta())



print(dipendente_1.nome)

