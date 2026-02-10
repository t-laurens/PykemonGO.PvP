from poketype import Type
class Pokemon:

    def __init__(self,nom:str,stats:list,type:Type,type2:Type|None=None):
        self.nom=nom
        assert(len(stats)==3),"Exception détectée : le Pokémon "+self.nom+" n'a pas 3 statistiques"
        self.stat_moyenne = sum(stats)/len(stats)
        self.type=type
        self.type2=type2
