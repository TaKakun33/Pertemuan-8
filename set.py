# Nama File: set.py
# Deskripsi: berisi type dan operasi set yang menggunakan list
# Pembuat: Akmal Kafli Anan
# Tanggal: 10 November 2024

#DEFINISI DAN SPESIFIKASI TYPE
#Set adalah sebuah list dengan syarat setiap elemen harus unik Semua konstruktor, selektor, dan operasi yang telah didefinisikan untuk list juga berlaku pada set

from list import *

#DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN 
# Rember: elemen, list -> list 
#   {Rember(x,L) menghapus sebuah elemen x dari list L 
# Jika x ada di list L, maka elemen L berkurang 1. Jika x tidak ada di list L maka L tetap danList kosong tetap menjadi list kosong.}

# MultiRember: elemen, list -> list 
#   {MultiRember(x,L) menghapus semua kemunculan elemen x dari list L.  
# List baru yang dihasilkan tidak lagi memiliki elemen x dan List kosong tetap menjadi list kosong.}

# Realisasi
def RemberV1(X,L):
    if IsEmpty(L):
        return []
    else:
        if X == FirstElmt(L):
            return Tail(L)
        else:
            return Konso(FirstElmt(L),RemberV1(X, Tail(L)))

def RemberV2(X,L):
    if IsEmpty(L):
        return []
    else:
        if X == LastElmt(L):
            return Head(L)
        else:
            return Konsi(RemberV2(X, Head(L)), LastElmt(L))
        
def MultiRember(X,L):
    if IsEmpty(L):
        return []
    else:
        if X == FirstElmt(L):
            return MultiRember(X,Tail(L))
        else:
            return Konso(FirstElmt(L),MultiRember(X, Tail(L))) 
        
#DEFINISI DAN SPESIKASI KONSTRUKTOR SET DARI LIST 
# MakeSet: list -> set  
#   {MakeSet(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali dan list kosong tetap menjadi himpunan kosong.}

# Realisasi
def MakeSetV1(L):
    if IsEmpty(L):
        return []
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSetV1(Tail(L))
        else:
            return(Konso(FirstElmt(L),MakeSetV1(Tail(L))))

def MakeSetV2(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L),MakeSetV2(MultiRember(FirstElmt(L),Tail(L))))
    
#DEFINISI DAN SPESIKASI KONSTRUKTOR SET  
# KonsoSet: elemen,set -> set  
#   {konsoSet(e,H) menambahkan sebuah elemen e sebagai elemen pertama set H dengan syarat e belum ada di dalam himpunan H }

# Realisasi
def KonsoSet(e,H):
    if IsMember(e,H):
        return H
    else:
        return Konso(e,H)
#DEFINISI DAN SPESIFIKASI PREDIKAT 
# IsSet: list -> boolean 
#   {IsSet(L) mengembalikan true jika L adalah sebuah set.}

# IsSubset: 2 set -> boolean 
#   {IsSubset(H1,H2) mengembalikan true jika H1 merupakan subset dari H2.}
 
# IsEqualSet: 2 set -> boolean 
#   {IsEqualSet(H1,H2} benar jika H1 adalah set yang sama dengan H2.}
 
# IsIntersect: 2 set -> boolean 
#   {IsIntersect(H1,H2) benar jika H1 beririsan dengan H2.}

# Realisasi
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
            
def IsEqualSetV1(H1,H2):
    return IsSubset(H1,H2) and IsSubset(H2,H1)
    
def IsEqualSetV2(H1,H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return True
    elif IsEmpty(H1) and not IsEmpty(H2):
        return False
    elif not IsEmpty(H1) and IsEmpty(H2):
        return False
    else:
        return FirstElmt(H1) == FirstElmt(H2) and IsEqualSetV2(Tail(H1),Tail(H2))
    
def  IsIntersect(H1,H2):
    if IsEmpty(H1) or IsEmpty(H2):
        return False
    else:
        return IsMember(FirstElmt(H1),H2) or IsIntersect(Tail(H1),H2)
    
#DEFINISI DAN SPESIFIKASI OPERASI TERHADAP HIMPUNAN 
# MakeIntersect: 2 set -> set 
#   {MakeIntersect(H1,H2) menghasilkan set baru yang merupakan hasil irisan antara H1 dan H2.}
 
# MakeUnion: 2 set -> set 
#   {MakeUnion(H1,H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2}
 
# NBIntersect: 2 set -> integer 
#   {NBIntersect(H1,H2) menghasilkan jumlah elemen yang beririsan pada H1 dan H2 tanpa memanfaatkan fungsi MakeIntersect(H1,H2).}
 
# NBUnion: 2 set -> integer 
#   {NBUnion(H1,H2) menghasilkan jumlah elemen hasil gabungan antara H1 dan H2 tanpa memanfaatkan fungsi MakeUnion(H1,H2).}

# Realisasi 
def MakeIntersectV1(H1,H2):
    if IsEmpty(H1):
        return []
    else:
        if IsMember(FirstElmt(H1),H2):
            return Konso(FirstElmt(H1),MakeIntersectV1(Tail(H1),H2))
        else:
            return MakeIntersectV1(Tail(H1),H2)
    
def MakeIntersectV2(H1,H2):
    if IsEmpty(H2):
        return []
    else:
        if IsMember(FirstElmt(H2),H1):
            return Konso(FirstElmt(H2),MakeIntersectV2(H1,Tail(H2)))
        else:
            return MakeIntersectV2(H1,Tail(H2))
    
def MakeUnionV1(H1,H2):
    if IsEmpty(H1):
        return H2
    else:
        if not IsMember(FirstElmt(H1),H2):
            return Konso(FirstElmt(H1),MakeUnionV1(Tail(H1),H2))
        else:
            return MakeUnionV1(Tail(H1),H2)
    
def MakeUnionV2(H1,H2):
    if IsEmpty(H2):
        return H1
    else:
        if not IsMember(FirstElmt(H2),H1):
            return Konso(FirstElmt(H2),MakeUnionV2(H1,Tail(H2)))
        else:
            return MakeUnionV2(H1,Tail(H2))
        
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

    
# Aplikasi
print(RemberV1(4,[1,2,3,4,5,4,7]))
print(RemberV2(4,[1,2,3,4,5,4,7]))

print(MultiRember(4,[1,2,3,4,5,4,7]))

print(MakeSetV1([1,1,2,4,5,3,6,7,3,3]))
print(MakeSetV2([1,1,2,4,5,3,6,7,3,3]))

print(KonsoSet(3,[1,2,4,5]))
print(KonsoSet(3,[1,2,3,4,5]))

print(IsSet([1,2,3,4,5,6,3,32,32,4,5,2]))
print(IsSubset([1,2,0],[1,2,3,4,5]))
print(IsEqualSetV1([1,2,3],[1,2,3,4]))
print(IsEqualSetV2([1,2,3],[1,2,3]))
print(IsIntersect([1,2,3],[4,5,6,1,2]))

print(MakeIntersectV1([0,1,2,3,4,5],[4,5,6,1,2]))
print(MakeIntersectV2([0,1,2,3,4,5],[4,5,6,1,2]))

print(MakeUnionV1([0,1,2,3,4,5],[4,5,6,1,2]))
print(MakeUnionV2([0,1,2,3,4,5],[4,5,6,1,2]))

print(NBIntersect([0,1,2,3,4,5],[4,5,6,1,2]))
print(NBUnion([0,1,2,3,4,5],[4,5,6,1,2]))