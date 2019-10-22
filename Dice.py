import random as rn
class Die:
    
    def __init__(self, sides, probabilities = None):
        self.sides = sides
        self.probabilities = probabilities
        self.value = 1
  
    
    def roll(self):
        if(self.probabilities == None):
            self.value = rn.randint(1,self.sides + 1)
        else:
            self.setProbabilities()
            

    def negative_probabilities(self):
        for x in self.probabilities:
            if(isinstance(x, int)):
                pass
            else:
                raise Exception("only integer values allowed")
        

    def greater_than(self):
        for x in self.probabilities:
            if(x >= 0):
                pass
            else:
                 raise Exception("probability sum must be greater than 0") 
      

    def integer_values(self):
        for x in self.probabilities:
             if(sum(self.probabilities) > 1):
                pass
             else:
                raise Exception("negative probabilities not allowed")

    def setProbabilities(self):
        weight = []
        self.integer_values()
        self.greater_than()
        self.negative_probabilities()
        for i in range(1,self.sides+1): 
            weight.append(str(i))
        new = [weight * self.probabilities for weight,self.probabilities in zip(weight,self.probabilities)]
        weight_list = [b for i in new for b in i]
        self.value = rn.choice(weight_list)

        
class DiceFactory():
    
    def __init__(self,sides):
        self.sides = sides
        
        
    def make_die(self):
        
        self.value = rn.randrange(1, self.sides+1)
        print(self.value)
        
        return Die(self.sides)


        
class DiceFactory():
    
    def __init__(self,sides):
        self.sides = sides
        
        
    def make_die(self):
        
        self.value = rn.randrange(1, self.sides+1)
        print(self.value)
        
        return Die(self.sides)


die6 = Die(6)
die6.roll()
print(die6.value)

die20 = Die(20)
die20.roll()
print(die20.value)

Die_6 = Die(6,[1,1,1,2,2,-2])
Die_6.roll()
print(Die_6.value)

factory20 = DiceFactory(20)
die20 = factory20.make_die()
anotherDie20 = factory20.make_die()