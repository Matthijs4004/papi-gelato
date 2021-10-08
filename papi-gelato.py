
x = ("                          --------+")

print("\nWelkom bij Papi Gelato.\n")

def bon():
    print("\n----------[Papi Gelato]----------\n")
    print("Bolletjes   ",hvl," x €1,10   = €",1.10*hvl)
    if houder == "hoorntje":
        print("Hoorntjes    1 x €1,25    = € 1,25  ")
        print(x)
        print("Totaal                    = €",(hvl*1.10)+1,25)
    if houder == "bakje":
        print("Bakjes       1 x €0,75    = € 0,75  ")
        print(x)
        print("Totaal                    = €",(hvl*1.10)+0.75)




def stap_1():
    global hvl
    hvl = int(input("Hoeveel bolletjes wilt u? "))
    if hvl in range(1, 4):
        smaak_keuze()
    elif hvl in range(4, 8):
        print("Dan krijgt u van mij een bakje met " + str(hvl) + " bolletjes\n")
        smaak_keuze()
    elif hvl >= 8:
        print("Sorry, zulke grote bakken hebben we niet")   
    else:
        print("Sorry dat snap ik niet...")

def smaak_keuze():
    aantal = hvl
    for x in range(hvl):
        smaak = input("Welke smaak wilt u voor bolletje nummer " + str(aantal) + "? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
    if smaak.lower().strip() == "A" or "C" or "M" or "V":
        stap_2()
    else:
        print("Sorry dat snap ik niet...")
        return smaak_keuze()
    

def stap_2():
    global houder
    houder = input("Wilt u deze " + str(hvl) +  " bolletje(s) in A) een hoorntje of B) een bakje? ")
    if houder == "A":
        houder = "hoorntje"
        stap_3("hoorntje")
    elif houder == "B":
        houder = "bakje"
        stap_3("bakje")
    else:
        print("Sorry dat snap ik niet...")
        return stap_2()

def stap_3(houder):
    nogmaals = input("Hier is uw " + houder + " met " + str(hvl) + " bolletje(s). Wilt u nog meer bestellen? (ja/nee) ")
    if nogmaals.lower().strip() == "ja":
        stap_1()
    elif nogmaals.lower().strip() == "nee":
        bon()
        print("\nBedankt en tot ziens!")
    else:
        print("Sorry dat snap ik niet...")

stap_1()