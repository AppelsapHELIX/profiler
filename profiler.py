from termcolor import colored

# Template [Name|Gender|Date of Birth|Place of Birth|Languages|Work|Family|Residence|Address|Relations|Phone Number]
database = {"Anne-Sophie Bodelier":"Anne-Sophie Bodelier|Female|Unknown|Heerlen, Netherlands|Dutch|Unknown|Marie Bodelier|NL - Limburg - Kerkrade|Lambertistraat 7|Unknown|Unknown",
            "Ania Polaczek":"Ania Polaczek|Female|Unknown|Poznan, Poland|Dutch, Polish|Sushi Vandaag|Unknown|NL - Limburg - Heerlen|Unknown|Unknown|+31615394414",
            "Anouck Berger":"Anouck Berger|Female|Unknown|Heerlen, Netherlands|Dutch|Unknown|Unknown|NL - Limburg - Hoensbroek|Unknown|Unknown|+31613782453",
            "Anne Schlechtriem":"Anne Schlechtriem|Female|Unknown|Unknown|Dutch|Unknown|Bas Schlechtriem|NL - Limburg - Heerlen|Unknown|Unknown|Unknown",
            "Alicia Alawerdjan":"Alicia Alawerdjan|Female|Unknown|Unknown|Dutch|Unknown|Emily Doveren, Emma Alawerdjan, Winny Doveren|NL - Limburg - Kerkrade|Unknown|Sem Weijers|Unknown",
            "Bas Schlechtriem":"Bas Schlechtriem|Male|16 September 2003|Unknown|Dutch|Unknown|Anne Schlechtriem|NL - Limburg - Heerlen|Unknown|Unknown|Unknown",
            "Bas Harsin":"Bas Harsin|Male|Unknown|Heerlen, Netherlands|Dutch|Unknown|Unknown|NL - Limburg - Heerlen|Unknown|Unknown|Unknown",
            "Bishoy Rezk":"Bishoy Rezk|Male|Unknown|Unknown|Dutch|Unknown|Unknown|NL - Limburg - Heerlen|Unknown|Unknown|Unknown",
            "Charissa Torralba":"Charissa Torralba|Female|Unknown|Unknown|Dutch|Plus Wetzels/Hovenstraat|Unknown|NL - Limburg - Landgraaf|Unknown|Unknown|Unknown",
            "Dirk Douma":"Dirk Douma|Male|Unknown|Heerlen, Netherlands|Dutch, Italian|Unknown|Luuk Douma|NL - Limburg - Heerlen|Unknown|Unknown|+31631635686",
            "Daryl Pappin":"Daryl Pappin|Male|Unknown|Unknown|Dutch|Unknown|Unknown|Unknown|Unknown|Unknown|+31640059348",
            "Demy Sijben":"Demy Sijben|Female|Unknown|Unknown|Dutch|AH Hertogenlaan|Unknown|NL - Limburg - Kerkrade|Unknown|Unknown|Unknown",
            "Dani Heesbeen":"Dani Heesbeen|Male|Unknown|Brunssum, Netherlands|Dutch|Ronnies BBQ Ribs|Ron Heesbeen|NL - Limburg - Brunssum|Unknown|Mara de Wolf|Unknown",
            "Dilysia Kaminiarz":"Dilysia Kaminiarz|Female|6 May 2004|Heerlen, Netherlands|Dutch|Unknown|Nicolle Vondenhoff|NL - Limburg - Heerlen|Hamerstraat 18|Unknown|Unknown",
            "Emily Doveren":"Emily Doveren|Female|Unknown|Unknown|Dutch|Unknown|Alicia Alawerdjan|Unknown|Unknown|Unknown|Unknown",
            "Esmee Reuleaux":"Esmee Reuleaux|Female|Unknown|Unknown|Dutch|Unknown|Unknown|NL - Limburg - Kerkrade|Unknown|Unknown|Unknown",
            "Eef Vluggen":"Eef Vluggen|Female|Unknown|Unknown|Dutch|Unknown|Unknown|Unknown|Unknown|Lorenzo Maurmair|Unknown",
            "Emma Alawerdjan":"Emma Alawerdjan|Female|Unknown|Unknown|Dutch|Unknown|Emily Doveren, Winny Doveren|Unknown|Unknown|Unknown|Unknown",
            "Estelle Souren":"Estelle Souren|Female|Unknown|Unknown|Dutch|Unknown|Esmee Souren|NL - Limburg - Simpelveld|Unknown|Unknown|Unknown",
            "Esmee Souren":"Esmee Souren|Female|Unknown|Unknown|Dutch|Unknown|Estelle Souren|NL - Limburg - Simpelveld|Unknown|Unknown|Unknown",
            "Erica Perez":"Erica Perez|Female|Unknown|Unknown|Dutch, Spanish|Unknown|Unknown|NL - Limburg - Heerlen|Unknown|Unknown|Unknown",
            "Indy Weegels":"Unknown|Unknown|Unknown|Unknown|Unknown|Unknown|Unknown|Unknown|Unknown|Unknown|Unknown",
            "Jesse Dohmen":"Jesse Dohmen|Male|Unknown|Heerlen, Netherlands|Dutch|Unknown|Mick Dohmen|NL - Limburg - Mezenbroek/Welten|Unknown|Unknown|Unknown",
            "Julien Basters":"Julien Basters|Male|Unknown|Unknown|Dutch, German|Unknown|Unknown|Unknown|Unknown|Unknown|+31630902893",
            "Justin Erdweg":"Justin Erdweg|Male|Unknown|Unknown|Dutch, German|Unknown|Unknown|NL - Limburg - Geleen|Unknown|Unknown|Unknown",
            "Jewel Offermans":"Jewel Offermans|Female|Unknown|Heerlen, Netherlands|Dutch|Unknown|Unknown|NL - Limburg - Kerkrade|Unknown|Unknown|Unknown",
            "Jaden van Duurenn":"Jaden van Duurenn|Female|Unknown|Heerlen, Netherlands|Dutch|Unknown|Unknown|NL - Limburg - Heerlen|Unknown|Unknown|Unknown",
            "Jill Bleijlevens":"Jill Bleijlevens|Female|17 February 2003|Heerlen, Netherlands|Dutch|Unknown|Nancy van Damme|NL - Limburg - Kerkrade|Unknown|Unknown|Unknown",
            "Josja Fober":"Josja Fober|Male|Unknown|Heerlen, Netherlands|Dutch|Unknown|Unknown|NL - Limburg - Heerlen|Unknown|Unknown|Unknown",
            "Kaylie Scholz":"Kaylie Scholz|Female|Unknown|Unknown|Dutch|Unknown|Unknown|NL - Limburg - Kerkrade|Unknown|Unknown|Unknown",
            "Kimberley Odekerken":"Kimberley Odekerken|Female|Unknown|Unknown|Dutch|AH Schandelerboord|Unknown|NL - Limburg - Heerlen|Eindhovenstraat 4|Unknown|Unknown",
            "Luna Stolzenhoff":"Luna Stolzenhoff|Female|20 September 2003|Heerlen, Netherlands|Dutch|Unknown|Unknown|NL - Limburg - Heerlen|Keizerstraat 11|Unknown|Unknown",
            "Luca Mroczek":"Luca Mroczek|Male|2 January 2003|Heerlen, Netherlands|Dutch, German|Unknown|Unknown|NL - Limburg - Kerkrade|Unknown|Unknown|Unknown",
            "Luna Jaspers":"Luna Jaspers|Female|Unknown|Unknown|Dutch|Unknown|Guido Steins, Andrea Immelen|NL - Limburg - Kerkrade|Unknown|Unknown|Unknown",
            "Laura Soder":"Laura Soder|Female|Unknown|Unknown|Dutch|Unknown|Unknown|NL - Limburg - Kerkrade|Unknown|Unknown|Unknown",
            "Lindsey Bakker":"Lindsey Bakker|Female|Unknown|Heerlen, Netherlands|Dutch|Unknown|Hannie Bakker|NL - Limburg - Heerlen|Unknown|Unknown|Unknown",
            "Lana Mroczek":"Lana Mroczek|Female|28 May 2004|Heerlen|Dutch, German|Unknown|Luca Mroczek|NL - Limburg - Kerkrade|Unknown|Unknown|Unknown",
            "Laurens Fuchs":"Laurens Fuchs|Male|Unknown|Unknown|Dutch|Unknown|Unknown|Unknown|Unknown|Unknown|Unknown",
            "Lisa Starmans":"Lisa Starmans|Female|Unknown|Unknown|Dutch|Unknown|Unknown|NL - Limburg - Kerkrade|Unknown|Unknown|Unknown",
            "Mick Dohmen":"Mick Dohmen|Male|Unknown|Heerlen, Netherlands|Dutch|Unknown|Jesse Dohmen|NL - Limburg - Mezenbroek/Welten|Unknown|Unknown|Unknown",
            "Marie Bodelier":"Marie Bodelier|Female|Unknown|Heerlen, Netherlands|Dutch|Unknown|Anne-Sophie Bodelier|NL - Limburg - Kerkrade|Lambertistraat 7|Unknown|Unknown",
            "Nina Huisman":"Nina Huisman|Female|Unknown|Unknown|Dutch|Unknown|Unknown|NL - Limburg - Kerkrade|Unknown|Unknown|Unknown",
            "Niels Salis":"Niels Salis|Male|Unknown|Heerlen, Netherlands|Dutch|Unknown|Unknown|NL - Limburg - Heerlen|Unknown|Unknown|Unknown",
            "Ole Mertens":"Ole Mertens|Male|Unknown|Unknown|Dutch, German|Unknown|Unknown|DE - Unknown - Unknown|Unknown|Unknown|Unknown",
            "Rayen Jeridi":"Rayen Jeridi|Male|Unknown|Unknown|Dutch, Arabic|Unknown|Unknown|NL - Limburg - Heerlen|Unknown|Unknown|+31628232470",
            "Ron Heesbeen":"Ron Heesbeen|Male|Unknown|Brunssum, Netherlands|Dutch, English, German|Ronnies BBQ Ribs|Dani Heesbeen|NL - Limburg - Brunssum|Unknown|Anita Heesbeen|+31644169958",
            "Sietske Vijgen":"Sietske Vijgen|Female|Unknown|Heerlen, Netherlands|Dutch|Unknown|Unknown|NL - Limburg - Heerlen|Unknown|Unknown|+31640810371",
            "Saydou Bangura":"Saydou Bangura|Male|Unknown|Unknown|Dutch|Unknown|Unknown|Unknown|Unknown|Unknown|Unknown",
            "Sheryn Hassouna":"Sheryn Hassouna|Female|Unknown|Unknown|Dutch, Morrocan|Unknown|Unknown|NL - Limburg - Kerkrade|Unknown|Unknown|+31641195273",
            "Sylvanah Coelingh":"Sylvanah Coelingh|Female|Unknown|Unknown|Dutch|Unknown|Rita Tielens|Unknown|Unknown|Unknown|Unknown",
            "Sidney Quaiser":"Sidney Quaiser|Male|Unknown|Heerlen, Netherlands|Dutch|Samos|Yvon Keulen|NL - Limburg - Heerlen|Unknown|Unknown|Unknown",
            "Selisa Dogru":"Selisa Dogru|Female|Unknown|Unknown|Dutch, Turkish|Unknown|Selim Dogru|NL - Limburg - Valkenburg|Unknown|Lucky Specht|Unknown",
            "Tahne Brendt":"Tahne Brendt|Female|Unknown|Unknown|Dutch|Unknown|Unknown|NL - Limburg - Spaubeek|Unknown|Unknown|Unknown",
            "Teun Vinken":"Teun Vinken|Female|Unknown|Unknown|Dutch|Unknown|Unknown|Unknown|Unknown|Unknown|Unknown",
            "Tom Erens":"Tom Erens|Male|Unknown|Heerlen, Netherlands|Dutch|Unknown|John Erens, Marjolein Erens, Jacqueline Erens|NL - Limburg - Kerkrade|Unknown|Unknown|Unknown",
            "Vince Schoonbeek":"Vince Schoonbeek|Male|16 May 2003|Heerlen, Netherlands|Dutch|Ronnies BBQ Ribs|Unknown|NL - Limburg - Heerlen|Donker Curtiushof 13|Unknown|Unknown",
            "Valerie Ivanyuk":"Valerie Ivanyuk|Female|2 January 2003|Unknown|Dutch, Russian|Unknown|Unknown|NL - Limburg - Kerkrade|Unknown|Unknown|Unknown",
            "Vivian Kockelkoren":"Vivian Kockelkoren|Female|Unknown|Heerlen, Netherlands|Dutch|Grotius College Heerlen|Milan Kockelkoren|NL - Limburg - Heerlen|Dr.Clemens Meulemanstraat 54|Unknown|+31645114967",
            "Ymani Kohnen":"Ymani Kohnen|Female|Unknown|Heerlen, Netherlands|Dutch|Unknown|Unknown|NL - Limburg - Kerkrade|Groot-Nullandstraat 15|Unknown|Unknown",
            "Zakaryae Talhaoui":"Zakaryae Talhaoui|Male|Unknown|Heerlen, Netherlands|Dutch, Morrocan|Unknown|Lamijae Talhaoui|NL - Limburg - Heerlen|Unknown|Unknown|+31617141047"}

while True:
    print(colored("  _____            __ _ _     ", "white", attrs=['bold']))
    print(colored(" |  __ \          / _(_) |          ", "red", attrs=['bold']))
    print(colored(" | |__) | __ ___ | |_ _| | ___ _ __ ", "white", attrs=['bold']))
    print(colored(" |  ___/ '__/ _ \|  _| | |/ _ \ '__|", "red", attrs=['bold']))
    print(colored(" | |   | | | (_) | | | | |  __/ |   ", "white", attrs=['bold']))
    print(colored(" |_|   |_|  \___/|_| |_|_|\___|_|   ", "red", attrs=['bold']))
    print("")
    print("BOI WHAT YOU DOING")
    print("")
    print(colored("Choose an option:", "white", attrs=['bold']))
    print("")
    print(colored("[", "red", attrs=['bold']) + colored("1", "white", attrs=['bold']) + colored("]", "red", attrs=['bold']) + " " +colored("A-Z Person List", "white", attrs=['bold']))
    print(colored("[", "red", attrs=['bold']) + colored("2", "white", attrs=['bold']) + colored("]", "red", attrs=['bold']) + " " +colored("Search Person", "white", attrs=['bold']))
    print("")
    menu = input(colored(">", "red", attrs=['bold']) + colored(">", "white", attrs=['bold']) + colored(">", "red", attrs=['bold']) + " ")
    if menu == "1":
        print(colored("A", "white", attrs=['bold']))
        print(colored("Anne-Sophie Bodelier\n" + "Ania Polaczek\n" + "Anouck Berger\n" + "Anne Schlechtriem\n" + "Alicia Alawerdjan\n", "red", attrs=['bold']))
        print(colored("B", "white", attrs=['bold']))
        print(colored("Bas Schlechtriem\n" + "Bas Harsin\n" + "Bishoy Rezk\n", "red", attrs=['bold']))
        print(colored("C", "white", attrs=['bold']))
        print(colored("Charissa Torralba\n", "red", attrs=['bold']))
        print(colored("D", "white", attrs=['bold']))
        print(colored("Dirk Douma\n" + "Daryl Pappin\n" + "Demy Sijben\n" + "Dani Heesbeen\n" + "Dilysia Kaminiarz\n", "red", attrs=['bold']))
        print(colored("E", "white", attrs=['bold']))
        print(colored("Emily Doveren\n" + "Esmee Reuleaux\n" + "Eef Vluggen\n" + "Emma Alawerdjan\n" + "Estelle Souren\n" + "Esmee Souren\n" + "Erica Perez\n", "red", attrs=['bold']))
        print(colored("F", "white", attrs=['bold']))
        print(colored("Unavailable\n", "red", attrs=['bold']))
        print(colored("G", "white", attrs=['bold']))
        print(colored("Unavailable\n", "red", attrs=['bold']))
        print(colored("H", "white", attrs=['bold']))
        print(colored("Unavailable\n", "red", attrs=['bold']))
        print(colored("I", "white", attrs=['bold']))
        print(colored("Indy Weegels\n", "red", attrs=['bold']))
        print(colored("J", "white", attrs=['bold']))
        print(colored("Julien Basters\n" + "Justin Erdweg\n" + "Jaden van Duurenn\n" + "Jill Bleijlevens\n" + "Josja Fober\n" + "Jewel Offermans\n", "red", attrs=['bold']))
        print(colored("K", "white", attrs=['bold']))
        print(colored("Kaylie Scholz\n" + "Kimberley Odekerken\n", "red", attrs=['bold']))
        print(colored("L", "white", attrs=['bold']))
        print(colored("Luna Stolzenhoff\n" + "Luca Mroczek\n" + "Luna Jaspers\n" + "Laura Soder\n" + "Lindsey Bakker\n" + "Lana Mroczek\n" + "Laurens Fuchs\n" + "Lisa Starmans\n", "red", attrs=['bold']))
        print(colored("M", "white", attrs=['bold']))
        print(colored("Mick Dohmen\n" + "Marie Bodelier\n", "red", attrs=['bold']))
        print(colored("N", "white", attrs=['bold']))
        print(colored("Nina Huisman\n" + "Niels Salis\n", "red", attrs=['bold']))
        print(colored("O", "white", attrs=['bold']))
        print(colored("Ole Mertens\n", "red", attrs=['bold']))
        print(colored("P", "white", attrs=['bold']))
        print(colored("Unavailable\n", "red", attrs=['bold']))
        print(colored("Q", "white", attrs=['bold']))
        print(colored("Unavailable\n", "red", attrs=['bold']))
        print(colored("R", "white", attrs=['bold']))
        print(colored("Rayen Jeridi\n" + "Ron Heesbeen\n", "red", attrs=['bold']))
        print(colored("S", "white", attrs=['bold']))
        print(colored("Sietske Vijgen\n" + "Saydou Bangura\n" + "Sheryn Hassouna\n" + "Sylvanah Coelingh\n" + "Sidney Quaiser\n" + "Selisa Dogru\n", "red", attrs=['bold']))
        print(colored("T", "white", attrs=['bold']))
        print(colored("Tahne Brendt\n" + "Teun Vinken\n" + "Tom Erens\n", "red", attrs=['bold']))
        print(colored("U", "white", attrs=['bold']))
        print(colored("Unavailable\n", "red", attrs=['bold']))
        print(colored("V", "white", attrs=['bold']))
        print(colored("Vince Schoonbeek\n" + "Valerie Ivanyuk\n" + "Vivian Kockelkoren\n", "red", attrs=['bold']))
        print(colored("W", "white", attrs=['bold']))
        print(colored("Unavailable\n", "red", attrs=['bold']))
        print(colored("X", "white", attrs=['bold']))
        print(colored("Unavailable\n", "red", attrs=['bold']))
        print(colored("Y", "white", attrs=['bold']))
        print(colored("Ymani Kohnen\n", "red", attrs=['bold']))
        print(colored("Z", "white", attrs=['bold']))
        print(colored("Zakaryae Talhaoui\n", "red", attrs=['bold']))
        input("")
    elif menu == "2":
        person = input(colored("Name:", "white", attrs=['bold']) + " ")
        for key in database:
            if person.lower() in key.lower():
                print(colored(key, "white", attrs=['bold']))
                print("")
                values = database[key].split('|')
                print(colored("Name", "white", attrs=['bold']))
                print(colored(values[0], "red", attrs=['bold']))
                print("")
                print(colored("Gender", "white", attrs=['bold']))
                print(colored(values[1], "red", attrs=['bold']))
                print("")
                print(colored("Date of Birth", "white", attrs=['bold']))
                print(colored(values[2], "red", attrs=['bold']))
                print("")
                print(colored("Place of Birth", "white", attrs=['bold']))
                print(colored(values[3], "red", attrs=['bold']))
                print("")
                print(colored("Languages", "white", attrs=['bold']))
                print(colored(values[4], "red", attrs=['bold']))
                print("")
                print(colored("Work", "white", attrs=['bold']))
                print(colored(values[5], "red", attrs=['bold']))
                print("")
                print(colored("Family", "white", attrs=['bold']))
                print(colored(values[6], "red", attrs=['bold']))
                print("")
                print(colored("Residence", "white", attrs=['bold']))
                print(colored(values[7], "red", attrs=['bold']))
                print("")
                print(colored("Address", "white", attrs=['bold']))
                print(colored(values[8], "red", attrs=['bold']))
                print("")
                print(colored("Relations", "white", attrs=['bold']))
                print(colored(values[9], "red", attrs=['bold']))
                print("")
                print(colored("Phone Number", "white", attrs=['bold']))
                print(colored(values[10], "red", attrs=['bold']))
                input("")
        else:
            print(colored("Person not found", "white", attrs=['bold']) + colored("!", "red", attrs=['bold']))
            input("")
