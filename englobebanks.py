from pokemon import Pokemon
from attaque import Attaque

class Donnee:

    def __init__(self,pokemon:Pokemon,att_r:Attaque,att_c:Attaque):
        self.pokemon=pokemon
        self.att_r=att_r
        self.att_c=att_c
        self.potentiel=0
        
    def alattaque(self,duree_simulation:int,defense_cible:int):
        # Fonction de calcul des dégâts théoriques en [duree] secondes
        ttl=0
        charge=0
        charge_requise=-(self.att_c.energie)
        type_r=self.att_r.type
        type_c=self.att_c.type
        mult_r=1.0
        if type_r==self.pokemon.type or type_r==self.pokemon.type2:
            mult_r=1.2
        mult_c=1.0
        if type_c==self.pokemon.type or type_c==self.pokemon.type2:
            mult_c=1.2
        i=0
        while i<duree_simulation:
            if charge>=charge_requise:
                charge-=charge_requise
                ttl+=int(0.5*self.att_c.dps*(self.pokemon.stat_moyenne/defense_cible)*mult_c)+1
            else:
                ttl+=int(0.5*self.att_r.dps*(self.pokemon.stat_moyenne/defense_cible)*mult_r)+1
                charge+=self.att_r.energie
            i+=1
        self.potentiel=ttl
        return ttl
    
# Dégâts = floor(0.5 × Puissance × (Attaque / Défense) × Modificateurs) + 1
# Stab : x1.2 ? x1.25 ? 
# Attaque/Défense = (base_stat + iv_stat) * CPMult
# CPMult est un décimal qui passe à peu près de 0.5 (Pokémon niveau 1) à 0.8 (Pokémon niveau 50)
