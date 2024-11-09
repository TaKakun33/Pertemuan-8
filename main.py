from list import *

def Rember1(X,L):
    if IsEmpty(L):
        return []
    else:
        if X == FirstElmt(L):
            return Tail(L)
        else:
            return Konso(FirstElmt(L),Rember1(X, Tail(L)))

def Rember2(X,L):
    if IsEmpty(L):
        return []
    else:
        if X == LastElmt(L):
            return Head(L)
        else:
            return Konsi(Rember2(X, Head(L)), LastElmt(L))
         
def MultiRember(X,L):
    if IsEmpty(L):
        return []
    else:
        if X == FirstElmt(L):
            return MultiRember(X,Tail(L))
        else:
            return Konso(FirstElmt(L),MultiRember(X, Tail(L))) 
        
def MakeSet1(L):
    if IsEmpty(L):
        return []
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSet1(Tail(L))
        else:
            return(Konso(FirstElmt(L),MakeSet1(Tail(L))))

def MakeSet2(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L),MakeSet2(MultiRember(FirstElmt(L),Tail(L))))
    
def KonsoSet(e,H):
    if IsMember(e,H):
        return H
    else:
        return Konso(e,H)

def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        if IsMember(FirstElmt(L),Tail(L)):
            return False
        else:
            return IsSet(Tail(L))
        
def IsSubset(H1,H2):
    if IsEmpty(H1):
        return True
    else:
        if IsMember(FirstElmt(H1),H2):
            return IsSubset(Tail(H1),H2)
        else:
            return False
            
def IsEqualSet1(H1,H2):
    return IsSubset(H1,H2) and IsSubset(H2,H1)
    
def IsEqualSet2(H1,H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return True
    elif IsEmpty(H1) and not IsEmpty(H2):
        return False
    elif not IsEmpty(H1) and IsEmpty(H2):
        return False
    else:
        return FirstElmt(H1) == FirstElmt(H2) and IsEqualSet2(Tail(H1),Tail(H2))
    

    
def  IsIntersect(H1,H2):
    if IsEmpty(H1) or IsEmpty(H2):
        return False
    else:
        return IsMember(FirstElmt(H1),H2) or IsIntersect(Tail(H1),H2)
    
def MakeIntersect1(H1,H2):
    if IsEmpty(H1):
        return []
    else:
        if IsMember(FirstElmt(H1),H2):
            return Konso(FirstElmt(H1),MakeIntersect1(Tail(H1),H2))
        else:
            return MakeIntersect1(Tail(H1),H2)
    
def MakeIntersect2(H1,H2):
    if IsEmpty(H2):
        return []
    else:
        if IsMember(FirstElmt(H2),H1):
            return Konso(FirstElmt(H2),MakeIntersect2(H1,Tail(H2)))
        else:
            return MakeIntersect2(H1,Tail(H2))
    
def MakeUnion1(H1,H2):
    if IsEmpty(H1):
        return H2
    else:
        if not IsMember(FirstElmt(H1),H2):
            return Konso(FirstElmt(H1),MakeUnion1(Tail(H1),H2))
        else:
            return MakeUnion1(Tail(H1),H2)
    
def MakeUnion2(H1,H2):
    if IsEmpty(H2):
        return H1
    else:
        if not IsMember(FirstElmt(H2),H1):
            return Konso(FirstElmt(H2),MakeUnion2(H1,Tail(H2)))
        else:
            return MakeUnion2(H1,Tail(H2))
        
def  NBIntersect(H1,H2):
    if IsEmpty(H1):
        return 0
    else:
        if IsMember(FirstElmt(H1),H2):
            return 1 + NBIntersect(Tail(H1),H2)
        else:
            return NBIntersect(Tail(H1),H2)
        
def NBUnion(H1,H2):
    if IsEmpty(H1):
        return NbElmt(H2) 
    else:
        if not IsMember(FirstElmt(H1),H2):
            return 1 + NBUnion(Tail(H1),H2)
        else:
            return NBUnion(Tail(H1),H2)

    
    
print(Rember1(4,[1,2,3,4,5,4,7]))
print(Rember2(4,[1,2,3,4,5,4,7]))
print(MultiRember(4,[1,2,3,4,5,4,7]))
print(MakeSet1([1,1,2,4,5,3,6,7,3,3]))
print(MakeSet2([1,1,2,4,5,3,6,7,3,3]))
print(KonsoSet(3,[1,2,4,5]))
print(KonsoSet(3,[1,2,3,4,5]))
print(IsSet([1,2,3,4,5,6,3,32,32,4,5,2]))
print(IsSubset([1,2,0],[1,2,3,4,5]))
print(IsEqualSet1([1,2,3],[1,2,3,4]))
print(IsEqualSet2([1,2,3],[1,2,3]))
print(IsIntersect([1,2,3],[4,5,6,1,2]))
print(MakeIntersect1([0,1,2,3,4,5],[4,5,6,1,2]))
print(MakeIntersect2([0,1,2,3,4,5],[4,5,6,1,2]))
print(MakeUnion1([0,1,2,3,4,5],[4,5,6,1,2]))
print(MakeUnion2([0,1,2,3,4,5],[4,5,6,1,2]))

print(NBIntersect([0,1,2,3,4,5],[4,5,6,1,2]))
print(NBUnion([0,1,2,3,4,5],[4,5,6,1,2]))