class Individual:
    counter = 0
    genotypes = ("AA","Ai","BB","Bi","AB","ii")
    def __init__(self, genotype, name = None ,agglutinogens = None,agglutinins = None, blood_type = None):
        
        self.__name = name
        self.__genotype = genotype
        self.__genotype1 = genotype[0]
        self.__genotype2 = genotype[1]
        self.__agglutinogens = agglutinogens
        self.__agglutinins = agglutinins
        self.__blood_type =  blood_type

        Individual.counter += 1
        
        if genotype not in self.genotypes: 
            raise TypeError("Invalid genotype")
        
        if name == None:
            self.__name = 'Indiv'+str(Individual.counter)
        #tiposanguineo
        if self.__genotype1 == self.__genotype2:
            self.__blood_type = str(self.__genotype1)
            if self.__blood_type == 'i':
                self.__blood_type = 'O'
        elif self.__genotype1 != self.__genotype2 and self.__genotype2 == 'i':
            self.__blood_type = str(self.__genotype1)
        elif self.__genotype1 != self.__genotype2 and self.__genotype1 == 'i':
            self.__blood_type = str(self.__genotype2)
        elif self.__genotype1 == 'A' and self.__genotype2 == 'B':
            self.__blood_type = str(self.__genotype)
        elif self.__genotype2 == 'A' and self.__genotype1 == 'B':
            self.__blood_type = str(self.__genotype)
        #aglutinogenio
        if self.__blood_type == 'O':
             self.__agglutinogens == None
        else:
            self.__agglutinogens = self.__blood_type
        #aglutinina
        if self.__blood_type == 'B':
            self.__agglutinins = 'A'
        if self.__blood_type == 'A':
            self.__agglutinins = 'B'
        if self.__blood_type == 'O':
            self.__agglutinins = 'A, B'
        if self.__blood_type == 'AB':
            self.__agglutinins = 'None'
    def name(self):
        return self.__name 
    name = property(name)
    
    def genotype(self):
        return self.__genotype
    genotype = property(genotype)
    
    def blood_type(self):
        return self.__blood_type
    blood_type = property(blood_type)
      
    def agglutinogens(self):
        return self.__agglutinogens
    agglutinogens = property(agglutinogens)
       
    def agglutinins(self):
        return self.__agglutinins
    agglutinins = property(agglutinins)
     
    def offsprings_genotypes(self, indivi2):
        a = list()
        C = list()
        for i1 in self.genotype:
            for i2 in indivi2.genotype:
                    a.append(i1+i2) 
        for i in a:
            i1 = i[0]
            i2 = i[1]
            if i1 == "i":
                i = i[1]+i[0]
            if i1 == "B" and i2 == "A":
                i = i[1]+i[0]
            if i not in C:
                C.append(i)
        return C

    def offsprings_blood_types(self, indivi2):
        a = list()
        b = list()
        c = list()
        for  i1 in self.genotype:
            for i2 in indivi2.genotype:
                a.append(i1+i2)
        for i in a:
            if i not in b:
                i1 = i[0]
                i2 = i[1]
                if i1 == i2 and i != "ii":
                    b.append(i1)
                elif i == "ii":
                    b.append("o")
                elif i1 != i2 and i2 == "i":
                    b.append(i1)
                elif i1 != i2 and i1 == "i":
                    b.append(i2)
                elif i1 == "A" and i2 == "B":
                    b.append(i)
                elif i2 == "A" and i1 == "B":
                    b.append("AB")

        for i in b:
            if i not in c:
                c.append(i)
        return c
    
    def can_donate(self, indivi2):
        if self.agglutinogens == None and indivi2.agglutinins == None:
            return True
        if self.agglutinogens == None:
            return True
        if len(self.agglutinogens) > 1:
            if indivi2.agglutinins == None:
                return True
            else:
                return False
        for i1 in self.agglutinogens:
            if indivi2.agglutinins == None:
                return True
            if len(indivi2.agglutinins) > 1:
                return False
            for i2 in indivi2.agglutinins:
                if i1 != i2:
                    return True
                else:
                    return False

    def can_receive(self, indivi2):
        if self.agglutinins == None and indivi2.agglutinogens == None:
            return True
        if self.agglutinins == None:
            return True
        if len(self.agglutinins) > 1:
            if indivi2.agglutinogens == None:
                return True
            else:
                return False
        for i1 in self.agglutinins:
            if indivi2.agglutinogens == None:
                return True
            if len(indivi2.agglutinogens) > 1:
                return False
            for i2 in indivi2.agglutinogens:
                if i1 != i2:
                    return True
                else:
                    return False
    def __str__(self):
        return(("Genotype:%s\nName:%s") % (self.name, self.genotype))
