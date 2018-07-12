def stableMatching(n, menPreferences, womenPreferences):

    unmarriedMen = list(range(n))
    manSpouse = [None] * n                      

    womanSpouse = [None] * n                      

    nextManChoice = [0] * n                       
    while unmarriedMen:
        he = unmarriedMen[0]                      
        hisPreferences = menPreferences[he]       
        she = hisPreferences[nextManChoice[he]] 
        herPreferences = womenPreferences[she]
        currentHusband = womanSpouse[she]         
        if currentHusband != None:
          if herPreferences.index(he) < herPreferences.index(currentHusband):
            manSpouse[he] = she
            womanSpouse[she] = he
            unmarriedMen.remove(he)
            unmarriedMen.append(currentHusband)
            nextManChoice[currentHusband] = (nextManChoice[currentHusband] + 1 ) % n
          else:
            nextManChoice[he] = (nextManChoice[he] + 1 ) % n
        else:
          manSpouse[he] = she
          womanSpouse[she] = he
          unmarriedMen.remove(he)   
    return manSpouse
    
# You might want to test your implementation on the following two tests:
assert(stableMatching(1, [ [0] ], [ [0] ]) == [0])

assert(stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ]) == [0, 1])
assert(stableMatching(2, [ [0,1], [0,1] ], [ [1,0], [0,1] ]) == [1, 0])
