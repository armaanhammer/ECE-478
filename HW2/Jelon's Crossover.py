import random

def main():
    p1 = [0,1,2,3,4,5,4,3,2,1] #Parent 1
    p2 = [0,1,2,3,4,5,5,5,5,5] #Parent 2

    p1,p2 = crossover(p1,p2)
    print "This is new list for parent 1 {}".format(p1);
    print "This is new list for parent 2 {}".format(p2);
    print "============================================";

    p1 = mutate_one_index(p1)
    print "This is new list for parent 1 {}".format(p1);
    print "============================================";
	
    p2 = mutate_mult_index(p2)
    print "============================================";
    print "This is new list for parent 2 {}".format(p2);

def crossover(parent1, parent2):
    c1 = []
    c2 = []
    size = len(parent1)
    index = random.randrange(0,size)
    temp1 = parent1[0:index]
    temp2 = parent1[index:size]
    c1 = temp2 + temp1
    temp1 = parent2[0:index]
    temp2 = parent2[index:size]
    c2 = temp2 + temp1
    return c1,c2

def mutate_one_index(parent):
    size = len(parent)
    index = random.randrange(0,size)
    mutate_value = random.randrange(0,5)
    parent[index] = mutate_value 
    return parent 

def mutate_mult_index(parent):
    size = len(parent)
    while True:
        index1 = random.randrange(0,size)
        index2 = random.randrange(0,size)
        if (index1 != index2):
           temp  = parent[index1]
           parent[index1] = parent[index2]
           parent[index2] = temp
           break
    
    return parent 

if __name__=="__main__":
    main()
