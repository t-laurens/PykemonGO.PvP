import powerbank
import pokebank
from englobebanks import Donnee

class Simulation:

    def __init__(self,duree_simulation:int,defense_cible:int):
        self.pokeDonnee=[
            Donnee(pokebank.FLORAMANTIS,powerbank.FEUILLAGE,powerbank.LAME_FEUILLE),
            Donnee(pokebank.EMPIFLOR,powerbank.FEUILE_MAGIK,powerbank.LAME_FEUILLE),
            Donnee(pokebank.JOLIFLOR,powerbank.BALLE_GRAINE,powerbank.LAME_FEUILLE),
            Donnee(pokebank.JUNGKO,powerbank.BALLE_GRAINE,powerbank.LAME_FEUILLE),
            Donnee(pokebank.TENGALICE,powerbank.BALLE_GRAINE,powerbank.LAME_FEUILLE),
            Donnee(pokebank.TROPIUS,powerbank.LAME_DAIR,powerbank.LAME_FEUILLE),
            Donnee(pokebank.PHYLLALI,powerbank.BALLE_GRAINE,powerbank.LAME_FEUILLE),
            Donnee(pokebank.GALLAME,powerbank.COUPE_PSYCHO,powerbank.LAME_FEUILLE),
            Donnee(pokebank.MANTERNEL,powerbank.GRIFFE_OMBRE,powerbank.LAME_FEUILLE),
            Donnee(pokebank.VIRIDIUM,powerbank.DOUBLE_PIED,powerbank.LAME_FEUILLE),
            Donnee(pokebank.CHEVROUM,powerbank.FOUET_LIANE,powerbank.LAME_FEUILLE),
            Donnee(pokebank.KATAGAMI,powerbank.LAME_DAIR,powerbank.LAME_FEUILLE)
        ]
        self.simulation(duree_simulation,defense_cible)
        
    def simulation(self,duree_simulation:int,defense_cible:int):
        for p in self.pokeDonnee:
            p.alattaque(duree_simulation,defense_cible)
        self.pokeDonnee.sort(key=lambda e:e.potentiel)
        self.pokeDonnee.reverse()

    def affichage(self):
        for p in self.pokeDonnee:
            print(p.pokemon.nom," : ",p.potentiel)
