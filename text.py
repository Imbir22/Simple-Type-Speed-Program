import random

polish = 'Dojeżdżaczy Ściągnęły słowa laskę światłość zwykł' \
         'palcem' \
         'Dworu biję bezprzykładną Iżby smycz pokrewieństwem marszałkowską Brał osoby najwymowniejsza jeden rosciągnionemi Zgody Światłość wraz piwa nami Podkomorzanki Jego Podkomorzynie książeczkę przy Ogara domek cichu mamę Zwano Grał dziwo Stał znał zimny skrzypiące Zamku orzę pistoletów rozzuchwali jaką prawidłach ścieszkami Niezwyczajnéj Był tylu Ojca gaju nieszczęście szczęśliwsza swą rostrzygnijcie roskrzyżował Gors. Miny rany moim Mój gospodarskiéj zacietrzewiony Też rozmaitością. ' \
         'Chlubi drzeć Szanowany porcelany Wielkiego spoczynek stopą Korsak Rossyj Siedzi' \
         'Przywoławszy jakie wódz Panna druki chude przeszłości Mickiewiczów zapowiedział' \
         'Żołniersczyzny najpiękniejszym spory Kościuszkowskie Żeby każe Może tonem Kusym największa czemu zlewa astry Skoro niém nową Póty urządzenie spójrzała Wystrzeliliśmy garnie Dojeżdżaczowi pokrewieństwem Ciszę grobie bezprzykładną pieprz pijani spokojniejszych' \
         'Nowy nierostrzygniony echo Kościuszkowskie wiem Niesiołowskiemu Już inne psem najpiękniejszym lecz żołniersczyzny Przyciągnąć pary łez roskrzyżował najstraszniéj rano piwa gdym ubóstwiałbym' \
         'Owiec wtém góry Kościuszkowskie wicin cichu gród nierostrzygniony Choć żołniersczyzny ' \
         'Najpiękniejszym żołniersczyzny nierostrzygniony zboża wesoł Kościuszkowskie ' \
         'Niesiołowskiemu płoty kiedym Ciocia'

english = 'Projecting surrounded literature yet delightful alteration but bed men Open are from long why cold. If must snug by upon sang loud left As me do preference entreaties compliment motionless ye literature Day behaviour explained law remainder Produce can cousins account you pasture. Peculiar delicate an pleasant provided do perceive ' \
          'Extremely we promotion remainder eagerness enjoyment an Ham her demands removal brought minuter raising invited gay Contented consisted continual curiosity contained get sex Forth child dried in in aware do You had met they song how feel lain evil near. Small she avoid six yet table china And bed make say been then dine mrs To household rapturous fulfilled attempted on so'\
          'She suspicion dejection saw instantly Well deny may real one told yet saw hard dear Bed chief house rapid right the Set noisy one state tears which No girl oh part must fact high my he Simplicity in excellence melancholy as remarkably discovered Own partiality motionless was old excellence she inquietude contrasted Sister giving so wicket cousin of an he rather marked Of on game part body rich Adapted mr savings venture it or comfort affixed friends'

english_text = english.lower().split()
polish_text = polish.lower().split()


def word_choice(words):
    text = []
    for n in range(1, 101):
        i = random.randint(1, 100)
        text.append(words[i])
    return text

