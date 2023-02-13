from ast import get_source_segment


def lepani(x:list,y:list):
    """Kirjeldus...
    :param list x: Inimeste järjend
    :param list y: Palgade järjend
    :rtyper:str
    """
    nimi=input("Kelle palk tahad leia?")
    while nimi not in x:
        nimi=input("Palun kirjuta õige nimi ")
    n=x.count(nimi)
    if n!=1:
      print(f"Siin on mõned inimesed es nimi on nimi")
      kopia=x.copy()
      for i in range(n):
          ind=kopia.index(nimi)
          kopia.remove(nimi)
          print(f"{i+1} {nimi} saab {y[ind]}")
    else:
        inde=x.index(nimi)
        print(f"{nimi} saab {y[ind]}")
        

        

def Kustuta(i:list,p:list,):
    kesk_palk=sum(p)/len(p)
    print(kesk_palk)
    v=int(input("Kellele palk 1- on suurem,2-on väiksem?"))
    if v==1:
        for palk in p:
            if palk>kesk_palk:
                ind=p.index(palk)
                p.remoe(palk)
                i.pop(ind)
    else:
        pass
    return i,p


def allaKeskmine(i.list,p:list):
    summPalk=sum(p)
    kesk= summ=sum(p)
    for j in range (0,len (p)-1):
        if kesk<p[j]:
        ind=p.imdex()
       