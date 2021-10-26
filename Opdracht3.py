import sys
print('Hallo, vandaag ga jij je aanmelden voor een helden avontuur, we gaan een aantal vragen stellen om te kijken of je geschikt bent!\n')
Leeftijd = int(input('Hoeveel jaar ben je?\n---> '))
Beschikbaarheid = int(input('Hoeveel uren per week bent u beschikbaar?\n---> '))
Positief = int(input('Tussen 1-10 hoe positief bent u over het leven?\n---> '))
Doorzettend = int(input('Tussen 1-10 hoe doorzettend bent u in het leven?\n--->'))
if Leeftijd >= 16 and Beschikbaarheid >= 12 and Positief >= 7 and Doorzettend >= 6:
    Vraag1 = int(input('Hoeveel kilo kunt u benchen?\n---> '))
    Vraag2 = int(input('Hoevaak uren train je per week?\n--->'))
    Vraag3 = int(input('Tussen 1-10 hoe goed zijn uw ogen?\n---> '))
    Vraag4 = int(input('Wat voor cijfers haalde u gemiddeld op school 1-10?\n---> '))
    Vraag5 = int(input('Hoevaak bouwt u in uw vrije tijd per week in uren?\n---> '))
    Vraag6 = int(input('Tussen 1-10 hoe handig bent u met materialen?\n---> '))
    Vraag7 = int(input('Tussen 1-10 hoeveel kennis heeft u met eten?\n---> '))
    Vraag8 = int(input('Tussen 1-10 hoeveel kennis heeft u met drinken?\n---> '))
    Vraag9 = int(input('Tussen 1-10 hoeveel kennis heeft u met genezen?\n---> '))
    Vraag10 = int(input('Tussen 1-10 hoeveel kennis heeft u met beschermen?\n---> '))

    if Vraag1 >= 80 and Vraag2 >= 6:
        print('Gefeliciteerd je kunt een beer worden')
    if Vraag3 >= 6 and Vraag4 >= 6:
        print('Gefeliciteerd je kunt een vos worden')
    if Vraag5 >= 4 and Vraag6 >= 6:
        print('Gefeliciteerd je kunt een bever worden')
    if Vraag7 >= 6 and Vraag8 >= 6 and Vraag9 >= 6 and Vraag10 >= 6:
        print('Gefeliciteerd je kunt een uil worden')

else:
    print('Helaas! Je bent niet geschikt voor deze baan.')
    exit()

