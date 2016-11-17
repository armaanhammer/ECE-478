import random

def main():
    p1 = [0,1,2,3,4,5,4,3,2,1] #Parent 1
    p2 = [8,8,8,8,8,6,6,6,6,6] #Parent 2
    
    p1,p2 = crossover(p1,p2)
    
    print "This is new list for parent 1 {}".format(p1);
    print "This is new list for parent 2 {}".format(p2);

def crossover(parent1, parent2):
    c1 = []
    c2 = []
    size = len(parent1)
    index1 = random.randint(1, size - 1)
    print index1
    index2 = random.randint(1, size - 1)
    print index2
    if index1 > index2:
        index1 = index2
        index2 = index1
    temp1 = parent1[0:index1]
    temp2 = parent2[index1:index2]
    temp3 = parent1[index2:size]
    c1 = temp1 + temp2 + temp3
    temp1 = parent2[0:index1]
    temp2 = parent1[index1:index2]
    temp3 = parent2[index2:size]
    c2 = temp1 + temp2 + temp3
    return c1,c2

if __name__=="__main__":
    main()
