import os
import random
import pickle
#import tkinter as tk
#from tkinter import font as tkfont
import ctypes
import sys
import time
from threading import Timer
minigames=[]
for x in range(15):
    minigames.append(0)
currentRoom = 1
currentFloor = "parter"
Ekwipunek = []
parter = {
1 : { "name" : "Hol",
"prawo" : 2,
"lewo" : 5,
"tyl" : 3,
"prosto":4,
"Opis":"Duży hol prowadzący w różnych kierunkach, ze schodami po środku oraz włazem do piwnicy",},
2 : { "name" : "Kuchnia",
"lewo" : 1,
"Opis":"Pokój przypominający stołówkę, ze stojącą w rogu lodówką",},
3 : { "name" : "Weranda",
"prosto" : 1,
"Opis":"Weranda z widokiem na kwiaty"},
4 : { "name" : "Łazienki",
"tyl" : 1,
"Opis": "Duże pomieszczenie z wieloma lustrami i pisuarami. Przeglądasz się w lustrze... no piękny/a jesteś, już wystarczy" },
5 : {"name" : "Medical",
"prawo" : 1,
"Opis": "Może lepiej jednak stąd wyjść zanim wróci ta straszna Pani?"}
}
pietro = {
1 : { "name" : "Balkonowy Hol",
"prawo" : 2,
"tyl" : 3,
"Opis":"Z piętra widzisz cały parterowy hol"},
2 : { "name" : "Sypialnia",
"lewo":1,
"prosto" : 5,
"Opis":"Bogata sypialnia z wygodnym łóżkiem i pojemną szafą. Może warto sprawdzić co się w niej kryje?"},
3 : { "name" : "Mała_Łazienka",
"prosto" : 1,
"Opis":"Klozet jest zapchany papierem... fuj."},
4 : { "name" : "Duży pokój",
"Opis":"Wygląda jak bióro jakiegoś złola",},
5 : {"name" : "Taras_widokowy",
"tyl" : 2,
"Opis": "Nawet nie próbuj skakać. Nie przeżyjesz."}
}
piwnica = {
1 : { "name" : "Duży_zimny_pokój",
"prawo" : 2,
"prosto" : 4 ,
"Opis":"Duży betonowy pokój. Wszechobecny chłód i ciemność, którą tłamsi nikły blask pochodni. Wrrrr..."},
2 : { "name" : "Spooky_bedroom",
"lewo" : 1,
"tyl" : 3,
"Opis":"Dlaczego ktoś chciałby spać w strasznej piwnicy?"},
3 : { "name" : "Podmogły pokój",
"prosto" : 2,
"Opis":"Gratulacje! Udało ci się pobrudzić sobie buty."},
4 : { "name" : "Pokój z grajkiem",
"tyl" : 1,
"Opis":"Wchodząc słyszysz dobrze znajome ci dźwięki..."},
}
def font_changes():
    LF_FACESIZE = 32
    STD_OUTPUT_HANDLE = -11

    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong),
                    ("nFont", ctypes.c_ulong),
                    ("dwFontSize", COORD),
                    ("FontFamily", ctypes.c_uint),
                    ("FontWeight", ctypes.c_uint),
                    ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    font.nFont = 12
    font.dwFontSize.X = 20
    font.dwFontSize.Y = 34
    font.FontFamily = 54
    font.FontWeight = 400
    font.FaceName = "Courier New"

    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
            handle, ctypes.c_long(False), ctypes.pointer(font))
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
Sprawdzenie ="Oke"
postac = {
    "Imie":"",
    "Nazwisko":"",
    "styl_magii": "",
    "poziom": 1,
}
statystyki={}
slownik_komend = ("menu - powrót do menu","leave - powrót do menu", "quit - wyjście z gry","ekwipunek - podgląd ekwipunku" "help - spis komend", "statystyki - podgląd nabytych statystyk", "postac - podgląd informacji o naszej postaci (imię, nazwisko, profesja magii, HP, obrona)")
#aktualna_plansza = "0"
game_active = False
warunek = ""
temp=""
decyzje = {
    "drzwi": "",
}



def centering(text):
    txt = text

    x = txt.center(20)

    print(x)
def prolog():
    clear_screen()
    print("Delikatne stukanie. Miarowe tik-tak, tik-tak, tik-tak przywodzące na myśl klekotkę wbudowaną w stary, drewniany zegar. Pamiętasz ten dźwięk? Wsłuchiwałeś się w niego przez całe dzieciństwo; leżąc na miękkiej kanapie, z głową opartą o kolana babci, czując delikatne, kobiece palce sunące przez gąszcz ciemnych włosów. Tykanie cię uspokaja. Otaczająca cię ciemność staje się prostsza do zniesienia, bardziej zrozumiała, bezpieczna. Czujesz, jak z sekundy na sekundę twoje serce zaczyna powracać do naturalnego rytmu. Niczym włączany po dłuższym czasie komputer, testujesz sprawność systemu, po kolei uruchamiając każdy zmysł.")
    print("W głuchej ciszy coraz głośniej rozbrzmiewa kilka dźwięków; miarowe tykanie schodzi na boczny tor, zastąpione dziwacznym skrzypieniem przestarzałych drzwi.")
    print("Powieki wreszcie się unoszą, ciężkie i wciąż zmęczone, a w otaczającym cię mroku dostrzegasz jedynie majaczące w oddali cztery plamy. Jeszcze nie odróżniasz ich kolorów.")
    print("")
    print("")
    temp = input("Naciśnij ENTER, aby kontynuować\n")
    if temp != "":
        Podstawowe_komendy(temp)

    clear_screen()
    print("Czujesz dreszcz przebiegający wzdłuż kręgosłupa, mrowienie we wszystkich kończynach, tępy ból w skroni. Wiesz, że coś jest nie tak: nie potrafisz określić, gdzie dokładnie się znajdujesz i nie wiesz nawet, w jakim stanie. Góra łączy się z dołem, prawo i lewo wyglądają tak samo, nie dostrzegasz podłoża, po którym stąpasz.")
    print("Robisz kilka kroków w stronę rozmazanych świateł, wreszcie potrafiąc określić ich kontury. Słuch cię nie zawiódł: im bliżej się znajdujesz, tym wyraźniej widzisz, że pośrodku niczego, między ciemnością łączącą jedną pustkę z drugą, znajduje się czworo drzwi.")
    print("")
    print("")
    print(f"{bcolors.FAIL}CZERWONE{bcolors.ENDC} przyciągają cię ciepłem. Kuszą obietnicą niebezpieczeństwa i wspaniałych przygód.")
    print("")
    print(f"{bcolors.OKCYAN}NIEBIESKIE{bcolors.ENDC} przywodzą na myśl spokojne niebo: błękitne, wolne od chmur, z wymalowanym jasną kredką, gorącym słońcem.")
    print("")
    print(f"{bcolors.OKGREEN}ZIELONE{bcolors.ENDC} kojarzą ci się z łąką, na której odpoczywałeś w dzieciństwie. Czujesz w ustach smak świeżych truskawek.")
    print("")
    print(f"{bcolors.WARNING}ŻÓŁTE{bcolors.ENDC} światło miga, zmienia kolory, ewoluuje. Jego natura przypomina żywy organizm, dobiegające z rozchylonych drzwi uderzenia powietrza koją twoje nozdrza zapachem świeżych ziół.")
    print("")
    print(f"{bcolors.HEADER}Które wybierzesz?{bcolors.ENDC}")
    print(f"[1]{bcolors.FAIL}CZERWONE{bcolors.ENDC}")
    print(f"[2]{bcolors.OKBLUE}NIEBIESKIE{bcolors.ENDC}")
    print(f"[3]{bcolors.OKGREEN}ZIELONE{bcolors.ENDC}")
    print(f"[4]{bcolors.WARNING}ŻÓŁTE{bcolors.ENDC}")
    print("")
    while True:
        terminal = input()
        Podstawowe_komendy(terminal)

        if terminal == "1":
            declare_statystyki(terminal)
            decyzje["drzwi"] = "Czerwone"
            postac["styl_magii"] = "Bojowa"
            print(decyzje["drzwi"])
            break
        elif terminal == "2":
            declare_statystyki(terminal)
            decyzje["drzwi"]="Niebieskie"
            postac["styl_magii"] = "Uzdrawiania"
            print(decyzje["drzwi"])
            break
        elif terminal == "3":
            declare_statystyki(terminal)
            decyzje["drzwi"] = "Zielone"
            postac["styl_magii"] = "Fizyczna"
            print(decyzje["drzwi"])
            break
        elif terminal == "4":
            declare_statystyki(terminal)
            decyzje["drzwi"] = "Żółte"
            postac["styl_magii"] = "Mentalna"
            print(decyzje["drzwi"])
            break
        elif terminal == "":
            continue
        else:
            print("")
            print("Wybierz numer odpowiadający drzwiom")
            continue

def declare_statystyki(magia):

    if magia == "1":
        statystyki["hp"] = 111
        statystyki["atak"] = 6
        statystyki["obrona"] = 1
    elif magia =="2":
        statystyki["hp"] = 222
        statystyki["atak"] = 9
        statystyki["obrona"] = 2
    elif magia == "3":
        statystyki["hp"] = 333
        statystyki["atak"] = 12
        statystyki["obrona"] = 3
    elif magia == "4":
        statystyki["hp"] = 444
        statystyki["atak"] = 15
        statystyki["obrona"] = 4


    print(type(statystyki))
    print(statystyki)


def Load_game():
    print("loaded")

def Quit_game():
    print("exited")
    # exit()

def Podstawowe_komendy(terminal):
    if terminal.lower() == "menu" or terminal.lower() == "leave":
        Show_menu()
        return 0
       # sys.modules[__name__].__dict__.clear()
    elif terminal.lower() == "help" or terminal.lower() == "pomoc":
        for x in range(len(slownik_komend)):
            print(slownik_komend[x])

    elif terminal.lower() == "statystyki":
        print(statystyki)
    elif terminal.lower() == "ekwipunek":
        print(Ekwipunek)
    elif terminal.lower() == "postac":
        for key in postac.keys():
            print("{key} - {odnosc}".format(key=key, odnosc=postac[key]))

    else:
        return 0

def New_game():
    clear_screen()
    global game_active
    game_active = True
    prolog()
    Tworzenie_postaci()
    plansza1()
    plansza2()
    plansza3()
    Game()

def Save():
    print()

def Tworzenie_postaci():
    clear_screen()
    if decyzje["drzwi"] == "Czerwone":
        print("Jeszcze nigdy nie czułeś się tak silny. Gorąca krew wrze w twoich żyłach, skóra twardnieje niczym ciężka zbroja, w dłoni czujesz lodowaty chłód metalu. Bierzesz zamach i uderzasz powietrze; powstała energia odpycha cię na kilka metrów. Starając się złapać równowagę, chwytasz za leżącą na ziemi tarczę. Idealnie wyważona, świetnie układa się w twojej dłoni i już wiesz, że została stworzona specjalnie dla ciebie.")
        print("Czy raczej... to ty ją stworzyłeś. Z otaczającej cię magii, z dzikiego zewu wydzierającego się z twojego gardła. Czujesz, że ty i broń jesteście jednością. Klinga przypomina przedłużenie twojego ramienia - używasz jej z taką łatwością, z jaką przychodzi ci każdy oddech.")
        print("W jednej chwili dociera do ciebie, że coś się zmieniło. Nie jesteś już tym samym chłopcem, który opierał głowę o miękkie kolana babci.")
        print("Jesteś silny. Niezwyciężony.")
        print("Jesteś...")
        print("")
        print("Kim właściwie jesteś?")


    elif decyzje["drzwi"] == "Niebieskie":
        print("Ucisk, który do tej pory rozsadzał twoje skronie, w jednej chwili rozpływa się jak za dotknięciem magicznej różdżki. Płuca napełniają się czystym powietrzem, wszystkie dysproporcje w ciele znikają, skóra zaczyna przypominać miękki jedwab. Czujesz się zdrowy, silny, po raz pierwszy od dawna - naprawdę szczęśliwy.")
        print("Rozpoznajesz w powietrzu zapachy, których nigdy wcześniej nie czułeś i od razu łączysz je z ich właściwościami.")
        print("Imbir - pozwala ci się skupić. Na chwilę wygłuszyć bodźce, które uderzają w ciebie ze wszystkich stron.")
        print("Lawenda - zapewnia błogi spokój. Przez chwilę masz wrażenie, że zapadasz się w miękką, ciepłą chmurę.")
        print("Szałwia - wypędza z pomieszczenia złe duchy, pozostawiając z tobą jedynie dobrą aurę.")
        print("Te zioła do ciebie mówią, komunikują się z tobą, a ty... naprawdę je rozumiesz.")
        print("Jak to możliwe?")
        print("Co ci się przydarzyło?")
        print("")
        print("I kim... kim właściwie jesteś?")


    elif decyzje["drzwi"] == "Zielone":
        print("Przemawia do ciebie woda. Słyszysz jej cichy szept, piękny szum, obietnicę rozkosznego odpoczynku. Jest spokojna, bezpieczna, kojąca. Kiedy wyciągasz rękę w jej stronę, znika. W jednej sekundzie przyjemne uczucie błogości zamienia się w przerażenie - lecisz? spadasz? W twojej głowie pojawia się głupia, obca myśl o dryfowaniu w przestworzach. Nie jesteś przecież ptakiem. Figlarny wiatr otacza twoje ciało, głaszcze włosy, przepływa między rozczapierzonymi palcami.")
        print("Nagle czerwone płomienie liżą skórę twoich dłoni, nie niosąc ze sobą bólu. Muskają cię niemal nieśmiało, zapraszając bliżej, kusząc przyjemnym ciepłem. Robisz krok w ich stronę i czujesz pod stopami gęstą trawę. Zapach siana drażni twoje nozdrza, śpiew słowika koi nerwy. Widzisz go, wyciągasz do niego rękę, lecz nim zdołasz złapać zwierzątko, rozpadasz się na drobne kawałki.")
        print("Jesteś jednocześnie wszędzie i nigdzie. Żyjesz, chociaż nie istniejesz. Czym jesteś?")
        print("")
        print("K i m jesteś?")


    elif decyzje["drzwi"] == "Żółte":
        print("Ogłuszający krzyk, drążący umysł szept, słowa powtarzane żmudnym, nudnym tonem, od którego obiad kręci się w żołądku, a gardło blokuje wszystkie niewypowiedziane prośby. Jedyne, czego w tej chwili pragniesz, to cisza. Chwila przerwy od natłoku cudzych myśli. Od wspomnień, których nie poznajesz, od marzeń, których nigdy nie snułeś. Od żalu i nienawiści bijącej od wyimaginowanych ludzi, od świata zbudowanego z iluzji. Przecież wiesz, że to nie twoje emocje... dlaczego więc nie potrafisz się od nich uwolnić?")
        print("Miłość. Żal. Smutek. Cierpienie. Uderzają w ciebie jak twarde kamienie, jak ciosy zadawane ostrą bronią. Powoli przestajesz rozpoznawać samego siebie.")
        print("")
        print("Kim jesteś?")




def plansza1():
    clear_screen()
    print(f"-{bcolors.BOLD}{bcolors.HEADER} Kim jesteś?{bcolors.ENDC} - rozbrzmiewa w twojej głowie raz za razem i choć z całych sił próbujesz, to nie jesteś w stanie rozpoznać tego głosu. Dziwny akcent rozciąga wyrazy, urywa końcówki, zamienia proste słowa w egzotyczną melodię. (tekst wygasa)\n")
    print("Pierwsze, co zauważasz, to rozbłyski bladego światła. Przypominają unoszące się w powietrzu świetliki albo umierające gwiazdy. Im bardziej się zbliżają, tym więcej jesteś w stanie sobie przypomnieć. (tekst wygasa)\n")
    print("")
    temp = input("Wciśnij ENTER aby kontynuować\n")
    Podstawowe_komendy(temp)
    clear_screen()
    print(f"-{bcolors.BOLD}{bcolors.HEADER} Kim jesteś? {bcolors.ENDC} - powtarza głos, ale tym razem wiesz, że nie pochodzi on z twojej głowy. Uderza w ciebie zewnątrz, tak jak chemiczny zapach, który drażni gardło.\n\n")
    print(f"-{bcolors.BOLD}{bcolors.HEADER} Chłopcze, mówię do ciebie!{bcolors.ENDC}")
    print("Powoli otwierasz oczy. Malutkie świetliki zamieniają się w żarówki podwieszone pod sufitem, chemiczny zapach dobiega z ustawionych na szpitalnym stoliku butelek. Zwilżasz usta końcem języka i koncentrujesz spojrzenie na siedzącej przy tobie kobiecie.")
    print("")
    temp = input("Wciśnij ENTER aby kontynuować\n")
    Podstawowe_komendy(temp)
def plansza2():
    clear_screen()
    print(f"{bcolors.BOLD}{bcolors.HEADER}- Imię? {bcolors.ENDC} - Tym razem głos jest wyraźniejszy, bo wiesz, skąd dobiega. Czerwone jak letnie wiśnie usta dojrzałej kobiety, która pochyla się nad twoim łóżkiem, jeszcze raz układają się w to samo pytanie.")
    print("")
    print("Jak ci na imię?\n \n")
   # while postac["Imie"] == "":
    postac["Imie"] = input()
    while postac["Imie"] == "":
        postac["Imie"] =input("Proszę podać imię:\n")
    print("")
    print("Kobieta kiwa głową, jakby już wcześniej znała odpowiedź. Nie wiedzieć czemu, czujesz ulgę: zupełnie jakbyś wykonał kawał dobrej roboty.")
    print("")
    print(f"{bcolors.BOLD}{bcolors.HEADER} - Nazwisko? {bcolors.ENDC} - kontynuuje rozmówczyni. Choć starasz się unieść głowę i spojrzeć jej w oczy, to czerwone usta cię hipnotyzują. Wpatrując się w nie, od razu wyrzucasz z siebie jedno słowo.")
    print("")
    print("Jak się nazywasz?\n\n")
   # while postac["Nazwisko"] == "":
    postac["Nazwisko"] = input()
    while postac["Nazwisko"] == "":
        postac["Nazwisko"] =input("Proszę podać nazwisko:\n")
        print("")



    temp = ""
    while temp.upper() != "Y" or temp.upper != "N":
        print(postac["Imie"], postac["Nazwisko"])
        temp = input("Czy na pewno tak się nazywasz? Y/N\n")
        Podstawowe_komendy(temp)
        if temp.upper() == "N":
            print("\nKim jesteś więc?\n")
            postac["Imie"] = input("Na imie mi... \n")
            while postac["Imie"] == "":
                postac["Imie"] = input("Emm... na imię mi...\n")

            postac["Nazwisko"] = input("Nazywam się... \n")
            while postac["Nazwisko"] == "":
                postac["Nazwisko"] = input("Emm... nazywam się...\n")

        elif temp.upper() == "Y":
            print("")
            break


        elif temp.upper() == "":
            continue
def plansza3():
    clear_screen()
    print("Kobieta wreszcie siada na znajdującym się nieopodal krześle i kreśli kilka znaków na własnej dłoni. W końcu odwraca się w twoją stronę i po raz pierwszy możesz dokładnie się jej przyjrzeć. Długie, ciemnokasztanowe loki okalające podłużną twarz, usta, które w rzeczywistości wydają się znacznie mniejsze, seledynowe oczy z pionowymi źrenicami, które przywodzą na myśl polującego węża.")
    print("Nie umiesz podejść do niej inaczej niż z nieufnością. Twoja głowa świeci pustką. Bez owocnie szukasz jakichkolwiek wspomnień, które pomogłyby ci wytłumaczyć skąd się tu wziąłeś. Jedyne czego teraz chcesz to stąd wyjść.")
    print("Cały czas leżąc na niewygodnej macie widzisz jak nieznajoma kobieta opuszcza pokój. To twoja szansa. Łapiesz swój plecak i wybiegasz drzwiami prowadzącymi do holu.")
    print("")
    print("")
    input("Press ENTER to continue \n")
    clear_screen()
    print("")
def Game():
    clear_screen()
    global currentRoom
    global currentFloor
    print("Komendy:")
    print("> idz (lewo,prawo,tyl,prosto)")
    print("> quit")
    print("")
    if currentFloor =="parter":
        print("You are in " + parter[currentRoom]["name"])
        print("You can go: ", list(parter[currentRoom].keys())[1:len(parter[currentRoom].keys()) - 1])
        print(parter[currentRoom]["Opis"])
    elif currentFloor =="pietro":
        print("You are in " + pietro[currentRoom]["name"])
        print("You can go: ", list(pietro[currentRoom].keys())[1:len(pietro[currentRoom].keys()) - 1])
        print(pietro[currentRoom]["Opis"])
    elif currentFloor =="piwnica":
        print("You are in " + piwnica[currentRoom]["name"])
        print("You can go: ", list(piwnica[currentRoom].keys())[1:len(piwnica[currentRoom].keys()) - 1])
        print(piwnica[currentRoom]["Opis"])
    while True:
        # print("You are in " + rooms[currentRoom]["name"])
       # print(currentFloor)
        move = input("> ")
        if move == "":
            clear_screen()
            if currentFloor == "parter":
                print("You are in " + parter[currentRoom]["name"])
                print("You can go: ", list(parter[currentRoom].keys())[1:len(parter[currentRoom].keys()) - 1])
                print(parter[currentRoom]["Opis"])
            elif currentFloor == "pietro":
                print("You are in " + pietro[currentRoom]["name"])
                print("You can go: ", list(pietro[currentRoom].keys())[1:len(pietro[currentRoom].keys()) - 1])
                print(pietro[currentRoom]["Opis"])
            elif currentFloor == "piwnica":
                print("You are in " + piwnica[currentRoom]["name"])
                print("You can go: ", list(piwnica[currentRoom].keys())[1:len(piwnica[currentRoom].keys()) - 1])
                print(piwnica[currentRoom]["Opis"])
            continue
        move = move.lower().split()


        # print("?????" , move)
        if currentFloor == "parter":
            clear_screen()
            Podstawowe_komendy(move[0])
            if move[0] != "idz" and move[0] != "quit" and move[0] != "help" and move[0] != "statystyki" and move[0] != "postac" and move[0] != "cheatuje":
                print("You are in " + parter[currentRoom]["name"])
                print("You can go: ", list(parter[currentRoom].keys())[1:len(parter[currentRoom].keys()) - 1])
                print(parter[currentRoom]["Opis"])
                continue
            if move[0] == "cheatuje":
                lvlup()
                lvlup()
                lvlup()
                lvlup()
                lvlup()
                lvlup()
                lvlup()
                lvlup()
                lvlup()
                lvlup()
            if move[0] == "idz":

                if move[1] in parter[currentRoom]:
                    currentRoom = parter[currentRoom][move[1]]


                    print("You are in " + parter[currentRoom]["name"])
                    print("You can go: ", list(parter[currentRoom].keys())[1:len(parter[currentRoom].keys())-1])
                    print(parter[currentRoom]["Opis"])
                    if currentRoom == 2:
                        Pierwsza_minigra()
                        print("You are in " + parter[currentRoom]["name"])
                        print("You can go: ", list(parter[currentRoom].keys())[1:len(parter[currentRoom].keys()) - 1])
                        print(parter[currentRoom]["Opis"])

                    if currentRoom == 3:
                        Trzecia_minigra()
                        print("You are in " + parter[currentRoom]["name"])
                        print("You can go: ", list(parter[currentRoom].keys())[1:len(parter[currentRoom].keys()) - 1])
                        print(parter[currentRoom]["Opis"])
                    if currentRoom == 1:
                        print("You can also try: góra, dół")
                elif move[1] == "góra" and currentRoom== 1:
                    if postac["poziom"]>=5:
                        currentFloor = "pietro"
                        print("You are in " + pietro[currentRoom]["name"])
                        print("You can go: ", list(pietro[currentRoom].keys())[1:len(pietro[currentRoom].keys()) - 1])
                        print(pietro[currentRoom]["Opis"])
                    else:
                        print("You are in " + parter[currentRoom]["name"])
                        print("You can go: ", list(parter[currentRoom].keys())[1:len(parter[currentRoom].keys()) - 1])
                        print(parter[currentRoom]["Opis"])
                        print("Próbując wspiąć się po schodach zostajesz odrzucony z potężną siłą na drugi koniec pokoju")
                        print("Twój poziom jest zbyt niski. Spróbuj zrobić pare zadań, aby awansować. Potrzebny poziom: 5")

                elif move[1] == "dół" and currentRoom== 1:
                    if postac["poziom"]>=3:
                        print("Tym razem bezproblemowo udaje ci się otworzyć właz. Najwyraźniej stałeś się wystarczająco silny")
                        input("Naciśnij ENTER by kontynuować")
                        clear_screen()
                        currentFloor = "piwnica"
                        print("You are in " + piwnica[currentRoom]["name"])
                        print("You can go: ", list(piwnica[currentRoom].keys())[1:len(piwnica[currentRoom].keys())-1])
                        print(piwnica[currentRoom]["Opis"])
                    else:
                        print("You are in " + parter[currentRoom]["name"])
                        print("You can go: ", list(parter[currentRoom].keys())[1:len(parter[currentRoom].keys()) - 1])
                        print(parter[currentRoom]["Opis"])
                        print("Próbując otworzyć właz ten zatrzaskuje się jeszcze mocniej. Chroni go jakieś zaklęcie.")
                        print("Twój poziom jest zbyt niski. Spróbuj zrobić pare zadań, aby awansować. Potrzebny poziom: 3")


                else:

                    print("You can't go that way!")
                    print("You are in " + parter[currentRoom]["name"])
                    print("You can go: ", list(parter[currentRoom].keys())[1:len(parter[currentRoom].keys()) - 1])
                    print(parter[currentRoom]["Opis"])
                    continue
            if move[0] == "quit":
                Show_menu()
        elif currentFloor == "pietro":
            clear_screen()
            Podstawowe_komendy(move[0])
            if move[0] == "idz":

                if move[1] in pietro[currentRoom]:
                    currentRoom = pietro[currentRoom][move[1]]
                    print("You are in " + pietro[currentRoom]["name"])
                    print("You can go: ", list(pietro[currentRoom].keys())[1:len(pietro[currentRoom].keys())-1])
                    print(pietro[currentRoom]["Opis"])
                    if currentRoom == 1:
                        if ready() == 1:
                            pietro[1].pop("Opis")
                            pietro[1]["prosto"]=4
                            pietro[1]["Opis"]="Wielki klucz wygląda jakby pasował do masywnych drzwi w tej lokacji. Wsadzasz go, a drzwi faktycznie się otwierają"

                        print("You are in " + pietro[currentRoom]["name"])
                        print("You can go: ", list(pietro[currentRoom].keys())[1:len(pietro[currentRoom].keys()) - 1])
                        print("You can also try: dół")
                        print(pietro[currentRoom]["Opis"])

                    if currentRoom == 4:
                        clear_screen()
                        print(pietro[currentRoom]["Opis"])
                        final_bossfight()


                    if currentRoom == 3:
                        Toaleta()
                        print("You are in " + pietro[currentRoom]["name"])
                        print("You can go: ", list(pietro[currentRoom].keys())[1:len(pietro[currentRoom].keys()) - 1])
                        print(pietro[currentRoom]["Opis"])
                    if currentRoom == 2:
                        Przeszukanie_Pokoju()
                        print("You are in " + pietro[currentRoom]["name"])
                        print("You can go: ", list(pietro[currentRoom].keys())[1:len(pietro[currentRoom].keys()) - 1])
                        print(pietro[currentRoom]["Opis"])

                elif move[1] == "dół" and currentRoom== 1:
                    currentFloor="parter"
                    print("You are in " + parter[currentRoom]["name"])
                    print("You can go: ", list(parter[currentRoom].keys())[1:len(parter[currentRoom].keys()) - 1])
                    print(parter[currentRoom]["Opis"])
                else:
                    print("You can't go that way!")
                    continue
        elif currentFloor == "piwnica":
           # clear_screen()
            if move[0] == "idz":
                clear_screen()
                if move[1] in piwnica[currentRoom]:
                    currentRoom = piwnica[currentRoom][move[1]]
                    if currentRoom == 2:
                        Druga_minigra()
                    print("You are in " + piwnica[currentRoom]["name"])
                    print("You can go: ", list(piwnica[currentRoom].keys())[1:len(piwnica[currentRoom].keys()) - 1])
                    print(piwnica[currentRoom]["Opis"])
                    if currentRoom == 4:
                        Czwarta_minigra()
                        print("You are in " + piwnica[currentRoom]["name"])
                        print("You can go: ", list(piwnica[currentRoom].keys())[1:len(piwnica[currentRoom].keys()) - 1])
                        print(piwnica[currentRoom]["Opis"])

                    if currentRoom == 1:
                        print("You can also try: góra")

                    continue
                elif move[1] == "góra" and currentRoom== 1 :
                    currentFloor = "parter"
                    print("You are in " + parter[currentRoom]["name"])
                    print("You can go: ", list(parter[currentRoom].keys())[1:len(parter[currentRoom].keys()) - 1])
                    print(parter[currentRoom]["Opis"])
                elif move[1] == "dół":
                    print("You can't go deeper")
                    print("You are in " + piwnica[currentRoom]["name"])
                    print("You can go: ", list(piwnica[currentRoom].keys())[1:len(piwnica[currentRoom].keys()) - 1])
                    print(piwnica[currentRoom]["Opis"])
                else:
                    print("You can't go that way!")
                    print("You are in " + piwnica[currentRoom]["name"])
                    print("You can go: ", list(piwnica[currentRoom].keys())[1:len(piwnica[currentRoom].keys()) - 1])
                    print(piwnica[currentRoom]["Opis"])
                    continue





def lvlup():
    postac["poziom"] += 1
    statystyki["hp"] += 10
    statystyki["obrona"] += 1
    statystyki["atak"] += 2
    print("Gratulacje, awansowałeś na kolejny poziom:", postac["poziom"])
def Pierwsza_minigra():

    if minigames[0]==0:

        #print("Działa")
        timeout = 10
        zadanie = random.randint(11, 25)
        print("Wchodzisz do kuchni. Zauważasz liczbę", zadanie, "wyrytą na lodówcę oraz garść magnesów porozrzucanych po pokoju")
        print("Co stanie się jeśli podasz poprawny wynik?")
        t = Timer(timeout, print, ['Koniec czasu!'])

        t.start()
        print("Ile to",zadanie, "do kwadratu ?")
        prompt = "You have %d seconds to choose the correct answer...\n" % timeout
        answer = input(prompt)
        t.cancel()
        if answer.isdigit():
          pass
        else:
          #  print("Not gut")
            answer =0
        if int(answer)==zadanie*zadanie:
            lvlup()
            minigames[0]=1
           # print(minigames)
            input("Naciśnij enter, by kontynuować")
            clear_screen()

        else:
            print('Przegrałeś. idz, zastanów się nad swoimi poczynaniami i wróc później.')
            input("Naciśnij ENTER by kontynuować")
            clear_screen()


    else:
        print("Już tu byłeś")

def Druga_minigra():
    if minigames[1]==0:
        wybory=["papier","kamień","nożyce"]
        print("Droge zagradza ci ciemna postać. Mówi, że nie możesz przejść dalej oile nie pokonasz jej w... Papier Kamień Nożyce 3 razy")
        win_couter = 0

        while win_couter<3:
            print("Ilość wygranych:", win_couter)
            wybor_przeciwnika = wybory[random.randint(0, 2)]
            wybor_gracza = input("Kamień/Papier/Nożyce?\n")
            if wybor_przeciwnika == wybory[0] and wybor_gracza.lower() == wybory[2]:

                win_couter += 1
            elif wybor_przeciwnika == wybory[1] and wybor_gracza.lower() == wybory[0]:
               # print("Ilość wygranych:", win_couter)
                win_couter +=1
            elif wybor_przeciwnika == wybory[2] and wybor_gracza.lower() == wybory[1]:
              #  print("Ilość wygranych:", win_couter)
                win_couter +=1
            elif wybor_przeciwnika == wybor_gracza.lower():
                print("Remis")
            elif wybor_gracza == "cheat":
                break
            elif wybor_gracza.lower() != "kamień" and wybor_gracza.lower() != "papier" and wybor_gracza.lower() != "nożyce" and wybor_gracza.lower() != "cheat":
                print("Nie umiesz grać w papier kamień nożyce, czy co?")
                continue

            else:
                print("Przegrałeś")
        print("Ilość wygranych:", win_couter)
        print("Pokonałeś mnie. Pozwalam ci dalej eksplorować te piwnice.")
        minigames[1]=1
        lvlup()
        print("Na ścianie zauważasz napis: Einap muicom...")
        print("... nie wiesz jednak co znaczy")
        input("Wciśnij ENTER by kontynuować")
        clear_screen()

    else:
        print("Już tu byłeś")

def Trzecia_minigra():
    if minigames[2]==0:
        print("Kwiaty wyglądają dość mizernie - trzebaby im coś zarecytować")
        input("Kliknij ENTER aby kontynuować")
        tupel_z_przepisaniem=("Chrząszcz brzmi w trzcinie w Ścibrzyszynie", "Mój ojciec to fanatyk wędkarstwa, całe mieszkanie zawalone haczykami", "Miało być tak pięknie, miało nie wiać w oczy nam")
        los = random.randint(0,2)
        timeout = 15
        t = Timer(timeout, print, ['Koniec czasu!'])
        t.start()
        zdanie = tupel_z_przepisaniem[los]
        print(zdanie)
        prompt = "Masz %d sekund na przepisanie tego zdania...\n" % timeout
        answer = input(prompt)
        t.cancel()
        if answer == zdanie:
            print("Udało ci się! Widzisz zza filaru jak kwiaty w ogrodzie budzą się i dodają ci mocy")
            lvlup()
            minigames[2] = 1
        else:
            print("Nie udało się")
        input("Naciśnij ENTER by kontynuować")
        clear_screen()

    else:
        print("Owszem, piękne te kwiaty")

def Czwarta_minigra():
    input("Naciśnij enter,aby zacząć śpiewać z grajkiem")
    clear_screen()
    print("Może warto się zatrzymać na chwilkę i odprężyć")
    print("Pan kiedyś stanął nad brzegiem")
    print("Szukał ludzi")
    tekst = input("(Dopisz dokładnie kolejną linijkę tekstu)\n")
    if tekst.lower() == "gotowych pójść za nim":
        print("By łowić serca")
        print("Słów Bożych prawdą.")
    else:
        print("[GRAJEK] NO I ZEPSUŁEŚ. DUMNYŚ Z SIEBIE!?")
        print("[GRAJEK] Miało być |Gotowych pójść za nim|")
        print("[GRAJEK] Od początku\n")
        input("(Naciśnij enter,aby kontynuować)")
        Czwarta_minigra()
        return
    print("O Panie, to Ty na mnie spojrzałeś,")
    print("Twoje usta dziś wyrzekły me imię.")
    tekst = input("(Dopisz dokładnie kolejną linijkę tekstu)\n")
    if tekst.lower() =="swoją barkę pozostawiam na brzegu":
        print("Razem z Tobą nowy zacznę dziś łów.")
        print("[GRAJEK] No! I pięknie zagrane")
        lvlup()
        input("Naciśnij enter,aby kontynuować")
        clear_screen()
        return
    else:
        print("[GRAJEK] NO I ZEPSUŁEŚ. DUMNYŚ Z SIEBIE!?")
        print("[GRAJEK] Miało być |Swoją barkę pozostawiam na brzegu|")
        print("Od początku\n")
        input("(Naciśnij enter,aby kontynuować)")
        Czwarta_minigra()
        return

def Toaleta():
    print("/Sam nie wiesz czemu to robisz/")
    print("*Podnieś* przepychaczkę")
    teksts = input()
    if teksts.lower() == "podnieś":
        Ekwipunek.append("Przepychacz")
        print(Ekwipunek)
        print("Dodano Przepychacz do ekwipunku")
        input("Naciśnij Enter aby kontynuować")

def Przeszukanie_Pokoju():
    #print("Coś tu musi być")
   # print("łóżko wygląda jakby nadawało się do *spania*")
    #print("Wartoby też *przeszukać* szafe")
   # print("Zawsze możesz *zrobić nic*")
    print()
    check = 0
    check_lozko = 0
    if minigames[8] == 0:
        while True:
            print("Coś tu musi być")
            print("łóżko wygląda jakby nadawało się do *spania*")
            print("Wartoby też *przeszukać* szafe")
            print("Zawsze możesz *zrobić nic*")
            terminal = input("> ")
            if terminal.lower() == "przeszukaj":
                if check == 0:
                    print("Pomiędzy starymi ubraniami znajdujesz... potężnie duży klucz!")
                    Ekwipunek.append("Wielki klucz")
                    print("*Dodano Wielki Klucz do ekwipunku*\n")
                    input("Naciśnij ENTER by kontynuować")
                    clear_screen()
                    check =1
                elif check == 1:
                    print("Już przeszukałeś szafę")
            elif terminal.lower() == "śpij":
                if check_lozko ==0:
                    print("To była dobra drzemka! Twoje zdrowie wzrosło!")
                    statystyki["hp"]+=50
                    input("Naciśnij ENTER by kontynuować")
                    clear_screen()
                    check_lozko =1
                elif check_lozko !=0:
                    print("Daj spokój... ile można spać")
            if check_lozko==1 and check ==1:
                print("To chyba wszystko w tym pokoju")
                minigames[8]=1
                break
            elif terminal.lower() == "zrób nic":
                break
            if check >=2:
                break
    elif minigames[8]==1:
        print("Nie warto już się tutaj kręcić")

def ready():
    spelnienie = 0
    if len(Ekwipunek) ==1:
        if Ekwipunek[0] =="Przepychacz":
            statystyki["atak"]+=20
    elif len(Ekwipunek) ==2:
        if Ekwipunek[0] =="Przepychacz" or Ekwipunek[1] =="Przepychacz":
            statystyki["atak"]+=20
    if Ekwipunek[0] == "Wielki klucz" or Ekwipunek[1]== "Wielki klucz":
        spelnienie=1
    if spelnienie ==1:
        return 1
    elif spelnienie !=1:
        print("Nie posiadasz potrzebnego klucza")




def final_bossfight():
   # statystyki["hp"] = 444
    #statystyki["atak"] = 15
   # statystyki["obrona"] = 24
    class Boss:
        def __init__(self, klasa, hp, obrona, atak, imie):
            self.klasa = klasa
            self.hp = hp
            self.obrona = obrona
            self.atak = atak
            self.imie = imie
            print("Wszechpotężny mag", self.imie, "to twój przeciwnik")

        def Dobywanie(self):
            print("Dobyłeś broń")
        def hit(self,dmg):
            hit =  dmg - self.obrona
            self.hp = self.hp - hit
            print("Bosowi pozostało", self.hp, "zdrowia")
        def atak(self):
            return self.atak()
    class Gracz:
        def __init__(self, klasa, hp, obrona, atak, imie):
            self.klasa = klasa
            self.hp = hp
            self.obrona = obrona
            self.atak = atak
            self.imie = imie
            print("Wszechpotężny mag", self.imie, "to twój przeciwnik")

        def Dobywanie(self):
            print("Dobyłeś broń")
        def atak(self):
            return self.atak()
        def hit(self,dmg):
            hit = dmg - self.obrona
            self.hp = self.hp - hit
            print("Zostało ci", self.hp, "zdrowia")

    klasy_bosa=("Bojowa", "Uzdrawiania", "Fizyczna", "Mentalna")
    klasa_los = random.randint(0,3)

    Boss = Boss(klasy_bosa[klasa_los],random.randint(250,400),8,45,"Złol")
   # Gracz = Gracz(postac["styl_magii"],statystyki["hp"],statystyki["obrona"],statystyki["atak"],postac["Imie"])
    print("Widzisz siedzącego za biurkiem starszego mężczyznę.\n Nim zdołałeś powiedzieć słowo ten wstał i wykręcając niestworzone piruety śle w ciebie coraz to kolejne ataki. Czas na walkę!")
    input("Napiśnij ENTER, aby zacząć walkę")
    while True:
        Boss.hit(statystyki["atak"])
        boss_dmg= Boss.atak - statystyki["obrona"]
      #  print(Boss.hp)
        time.sleep(0.1)
        if(Boss.hp < 0):
            clear_screen()
            print("Starzec wiedząc, że nie ma szans zawył jak gargulec i pod osłoną światła zniknął ci z oczu.".upper().center(os.get_terminal_size().columns))
            print("Zostawił za sobą jednak księgę... Księgę, w której opisane zostało wszystko co się stało.".upper().center(os.get_terminal_size().columns))
            print("Dlaczego tu jesteś. Kim jesteś. Kim byłeś. A co najważniejsze - Kim przeznaczone jest ci być.".upper().center(os.get_terminal_size().columns))
            print("")
            print("KONIEC GRY - WYGRALEŚ".upper().center(os.get_terminal_size().columns))
            input()
            input()
            input()
            input()
            input()
            input()
            quit()
            break
        else:
            statystyki["hp"] = statystyki["hp"] - boss_dmg
            print("Zostało ci", statystyki["hp"], "zdrowia")
        if statystyki["hp"]<0:
            print("KONIEC GRY - ZGINĄLEŚ".upper().center(os.get_terminal_size().columns))
            input()
            input()
            input()
            quit()
            break

def Save():
   data = [postac,statystyki,currentRoom,currentFloor,Ekwipunek]
   print(data)
   filename = input("Podaj nazwe dla swojego zapisu:\n")
   #filename = "save.dat"
   output =  open(filename, 'wb')
   pickle.dump(data,output)
def Load():
    filename2 = input("Podaj nazwe dla swojego wczytania:\n")
   # filename = "save.dat"
    input2 = open(filename2, 'rb')
    read = pickle.load(input2)
    print(read)
    postac["Imie"] = read[0]["Imie"]
    postac["Nazwisko"] = read[0]["Nazwisko"]
    postac["poziom"] = read[0]["poziom"]
    postac["styl_magii"] = read[0]["styl_magii"]
    statystyki["hp"] = read[1]["hp"]
    statystyki["atak"] = read[1]["atak"]
    statystyki["obrona"] = read[1]["obrona"]
    global currentRoom
    global currentFloor
    currentRoom = read[2]
    currentFloor = read[3]
    for item in read[4]:
        Ekwipunek.append(item)
def Show_menu():
    clear_screen()
    print(" ####################### ".center(os.get_terminal_size().columns))
    print(" #                     # ".center(os.get_terminal_size().columns))
    print(" #        MAJOR        # ".center(os.get_terminal_size().columns).upper())
    print(" #       Arcana        # ".center(os.get_terminal_size().columns).upper())
    print(" #                     # ".center(os.get_terminal_size().columns))
    print(" ####################### ".center(os.get_terminal_size().columns))
    print()
    print()
    print("[N] - New game".upper().center(os.get_terminal_size().columns))
    print("[C] - Continue".upper().center(os.get_terminal_size().columns))
    print("[S] - Save".upper().center(os.get_terminal_size().columns))
    print("[L] - Load".upper().center(os.get_terminal_size().columns))
    print("[Q] - Quit".upper().center(os.get_terminal_size().columns))
    terminal = ""
    while terminal!="N" or terminal!="Q" or terminal!="C" or terminal.upper() != "T" or terminal.upper() == "S" or terminal.upper() == "L":
        terminal = input()
        if terminal.upper() == "N" or terminal.upper() == "Q" or terminal.upper() == "C" or terminal.upper() == "T" or terminal.upper() == "S" or terminal.upper() == "L":

            if terminal.upper() == "N":
                New_game()
            elif terminal.upper() == "C":
                Game()
                continue
            elif terminal.upper() == "Q":
                Quit_game()
            elif terminal.upper() == "S":
                Save()
                #print("Saved")
                Show_menu()
            elif terminal.upper() == "L":
                Load()
                #print("Saved")
                Show_menu()
            elif terminal.upper() == "T":
                print()
        else:
            print("Nieznana/Niedostępna komenda")
            continue


font_changes()

Show_menu()