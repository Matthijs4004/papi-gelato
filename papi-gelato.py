
print("\nWelkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.\n")

hvl = ""

def stap_1():
    hvl = int(input("Hoeveel bolletjes wilt u? "))
    if hvl in range(1, 4):
        stap_2()
    elif hvl in range(4, 8):
        print("Dan krijgt u van mij een bakje met " + str(hvl) + " bolletjes\n")
        stap_2()
    elif hvl > 8:
        print("Sorry, zulke grote bakken hebben we niet")
        
    else:
        print("Sorry dat snap ik niet...")

def stap_2():
    houder = input("Wilt u deze " + str(hvl) +  " bolletje(s) in A) een hoorntje of B) een bakje? ")
    if houder == "A":
        stap_3("hoorntje")
    elif houder == "B":
        stap_3("bakje")
    else:
        print("Sorry dat snap ik niet...")
        return stap_2()

def stap_3(houder):
    nogmaals = input("Hier is uw " + houder + " met " + str(hvl) + " bolletje(s). Wilt u nog meer bestellen? (ja/nee) ")
    if nogmaals.lower().strip() == "ja":
        stap_1()
    elif nogmaals.lower().strip() == "nee":
        print("Bedankt en tot ziens!")
    else:
        print("Sorry dat snap ik niet...")

stap_1()