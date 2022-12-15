##
#author: Trinity Ung
#date: November 13th, 2022
#This program prints out different information from 2 different files and outputs it in a text file

#function created to add capital information to a list
def loadCSVDataCapitals(loadCapital):
    #if the file is not found it will tell the user in the output.txt
    outfile = open("output.txt","w")
    #try-except created to check if the file exist
    try:
        capitalList = []
        capitalCVS = loadCapital
        #opens the file
        capitalFile = open(capitalCVS, "r", encoding = 'utf8')
        #skips the first line in the header
        next(capitalFile)
        #goes through the file
        for line in capitalFile:
            #seperates the information
            lineFix = line.strip("\n").split(",")
            #gets rid of the unnecessary information
            lineFix.pop(2)
            lineFix.pop(2)
            lineFix.pop(2)
            #adds the needed information into a list
            for i in lineFix:
                capitalList.append(i)
        capitalFile.close()
    #if file not found it will let the user know and stop the program
    except FileNotFoundError:
        outfile.write("File not found")
        outfile.close()
        #print("File not found")
        quit()
    #returns the information from captials.csv
    return capitalList

#function created to add uni information to a list
def loadCSVDataTopUni(loadUni):
    #if the file is not found it will tell the user in the output.txt
    outfile = open("output.txt","w")
    try:
        topUniList = []
        uniCvs = loadUni
        #opens the file
        topUniFile = open(uniCvs, "r", encoding = 'utf8')
        #skips the first line in the header
        next(topUniFile)
        #goes through the file
        for line in topUniFile:
            #seperates the information
            lineFix = line.strip("\n").split(",")
            #gets rid of the unnecessary information
            lineFix.pop(4)
            lineFix.pop(4)
            lineFix.pop(4)
            lineFix.pop(4)
            #adds the needed information into a list
            for i in lineFix:
                topUniList.append(i)
        topUniFile.close()
    #if file not found it will let the user know and stops the program
    except FileNotFoundError:
        outfile.write("File not found")
        outfile.close()
        #print("File not found")
        quit()
    #return the list that contians information from TopUni.csv
    return topUniList

#function counts how many universities there are
def universitiesCount(uniListCount):
    #a is the list that contains the information from TopUni.csv
    a = uniListCount
    count = 0
    #for loop only checks the universites as it skips the unnecessary information
    for i in range(1,len(a),5):
        count = count + 1
    #returns the number of universities
    return count

#function checks the avaible countries
def availableCountries(uniListCountires):
    #a is the list that contains the information from TopUni.csv
    a = uniListCountires
    countires = []
    #skips unnecessary information to only look at the countires
    for i in range(2,len(a),5):
        #changes it to upper cases
        upperCountry = a[i].upper()
        #adds the country if it's not already in the list
        if upperCountry not in countires:
            countires.append(upperCountry)
    #returns the list that contains the avaliable countries
    return countires

#function created to check what continents are available
def availableContinents(captialsListContinents,countryListContinents):
    #a is the list that contains the information from capitals.csv
    a = captialsListContinents
    #b is the list that contains the information from TopUni.csv
    b = countryListContinents
    continents = []
    #nested for loop checks that the university country exist and then finds the contient
    for i in range(len(b)):
        for j in range(0,len(a),3):
            upperCountry = b[i].upper()
            upperCapital = a[j].upper()
            #checks if the country is the same in capitals.csv and TopUni.csv
            if upperCountry == upperCapital:
                #find the continent by adding 2 as contients are 2 down from where the country is in the index of the list
                upper = a[j+2].upper()
                #adds the conitnents to a list if it is not already there
                if upper not in continents:
                    continents.append(upper)
    #returns the lsit that contains the available continents
    return continents

#function finds the uni with the top international rank in the selected country
def topInternationalRank(countryInternational,uniListInternational):
    #a is the list that contains the information from TopUni.csv
    a = uniListInternational
    choosenCountry = countryInternational
    rank = a[0]
    #set this variable to the lowest ranking in the file
    internationalRank = int(a[-5])
    uniInternational = a[0]
    upperUniInternational = a[0]
    #loop goes through the list to find the country
    for i in range(2,len(a),5):
        #if the country matches it will go to the international rank index
        if a[i].upper() == choosenCountry.upper():
            rank = int(a[i - 2])
            #if statement finds the lowest number as the higest rank is the lowest number
            if rank < internationalRank:
                internationalRank = rank
                uniInternational = a[i - 1]
                upperUniInternational = uniInternational.upper()
    #returns the international rank and the name of the uni
    return internationalRank, upperUniInternational

#function finds the uni with the top national rank
def topNationalRank(countryNational,uniListNational):
    #a is the list that contains the information from TopUni.csv
    a = uniListNational
    choosenCountry = countryNational
    #index of where the lowest national rank is
    nationalRank = int(a[-2])
    uniNational = a[0]
    upperUniNational = a[0]
    #loop finds the matching country
    for i in range(2,len(a),5):
        if a[i].upper() == choosenCountry.upper():
            #once the same country is found it goes to the index of the countries national rank
            rank = int(a[i + 1])
            #finds the lowest number as it will be the highest national rank
            if rank < nationalRank:
                nationalRank = rank
                uniNational = a[i - 1]
                upperUniNational = uniNational.upper()
    #returns the national rank and name of the uni
    return nationalRank, upperUniNational

#function finds the average score of all universites at the selected country
def averageScore(countryScore,uniListScore):
    #a is the list that contains the information from TopUni.csv
    a = uniListScore
    choosenCountry = countryScore
    addScore = 0
    numberOfUni = 0
    averageScore = 0
    roundAverageScore = 0
    #for loop goes through the list to find the the matching country
    for i in range(2,len(a),5):
        #if the same country is found then it will add their score and add up the number of universites
        if a[i].upper() == choosenCountry.upper():
            numberOfUni = 1 + numberOfUni
            addScore = float(a[i + 2]) + addScore
    #calculates the average
    averageScore = addScore/numberOfUni
    #rounf the average to 2 decimal places
    roundAverageScore = "%.2f" % round(averageScore,2)
    #returns the rounded average score
    return roundAverageScore

#function finds the continent relative score
def continentRelativeScore(countryRelative,uniListRelative,captialsListRelative,scoreRelative):
    #a is the list that contains the information from capitals.csv
    a = captialsListRelative
    #b is the list that contains the information from TopUni.csv
    b = uniListRelative
    choosen = countryRelative
    averageScoreRelative = scoreRelative
    finalScore = 0.0
    continent = a[0]
    #index of the lowest score in TopUni.csv
    highestScore = float(b[-1])
    #finds the continent of the selected country
    for i in range(0,len(a),3):
        if a[i].upper() == choosen.upper():
            continent = a[i+2]

    #goes through a nested loop to find which universites have the same continent
    for i in range(len(b)):
        for j in range(len(a)):
            #checks if the countries are the same
            if b[i] == a[j]:
                #checks if the country has the same continent of the country that was selected
                if a[j+2] == continent:
                    score = float(b[i+2])
                    #finds the highest
                    if score >= highestScore:
                        highestScore = score
    #calculates the continent relative score
    finalScore = (float(averageScoreRelative)/float(highestScore)) * 100
    #rounds the continent relative score
    roundFinalScore = "%.2f" % round(finalScore,2)
    #returns the rounded continent relative score, continent and highest score in the continent
    return roundFinalScore, continent, highestScore

#function finds the capital city of the selected country
def capitalCity(countryCapital,capitalsListCapital):
    #a is the list that contains the information from capitals.csv
    a = capitalsListCapital
    choosen = countryCapital
    upperCapital = a[0]
    #for loop goes through the list to find the correct country
    for i in range(0,len(a),3):
        #if the country is the same it will change the index to the captial
        if a[i].upper() == choosen.upper():
            #captial is the 1 more than the country in the index
            capital = a[i + 1]
            upperCapital = capital.upper()
    #returns the captial name
    return upperCapital

#function finds universities that contain the name of the captial
def universitiesWithCapitalName(capitalName,uniListCapitalName):
    capitalUniName = capitalName.upper()
    #a is the list that contains the information from TopUni.csv
    a = uniListCapitalName
    uniCapitalNameList = []
    #for loop goes through the list to check all the universities
    for i in range(1,len(a),5):
        upperCapital = a[i].upper()
        #checks to see if the captial name is in the university name and if it is then it will be added to the list
        if capitalUniName in upperCapital:
            upperUniCapitalName = a[i].upper()
            uniCapitalNameList.append(upperUniCapitalName)
    #returns the list that contains all the universities that have the capital name in them
    return uniCapitalNameList

#function prints all the information into a text file
def getInformation(selectedCountry,rankingFileName,captialsFileName):
    country = selectedCountry
    rankName = rankingFileName
    capitalName = captialsFileName
    #opens the text file
    outfile = open("output.txt","w")

    #calls all the necessary funtions
    capitalsList = loadCSVDataCapitals(capitalName)
    uniList = loadCSVDataTopUni(rankName)

    numOfUni = universitiesCount(uniList)
    #change the information to a string so that it can be written in the text file
    numOfUniString = str(numOfUni)
    outfile.write("Total number of universites => ")
    outfile.write(numOfUniString)

    countryList = availableCountries(uniList)
    outfile.write("\n")
    outfile.write("Available countries => ")
    #prints out the list without brackets
    outfile.write(", ".join(str(x) for x in countryList))


    contientList = availableContinents(capitalsList,countryList)
    outfile.write("\n")
    outfile.write("Available continents => ")
    #prints out the list without brackets
    outfile.write(", ".join(str(x) for x in contientList))


    #get the multiple return values
    a,b = topInternationalRank(country,uniList)
    outfile.write("\n")
    outfile.write("At international rank => ")
    #change the information to a string so that it can be written in the text file
    outfile.write(str(a))
    outfile.write(" the university name is => ")
    #change the information to a string so that it can be written in the text file
    outfile.write(str(b))

    #get the multiple return values
    c,d = topNationalRank(country,uniList)
    outfile.write("\n")
    outfile.write("At national rank => ")
    #change the information to a string so that it can be written in the text file
    outfile.write(str(c))
    outfile.write(" the university name is => ")
    #change the information to a string so that it can be written in the text file
    outfile.write(str(d))

    score = averageScore(country,uniList)
    #change the information to a string so that it can be written in the text file
    scoreString = str(score)
    outfile.write("\n")
    outfile.write("The average score => ")
    outfile.write(scoreString)
    outfile.write("%")

    #get the multiple return values
    e,f,g = continentRelativeScore(country,uniList,capitalsList,score)
    outfile.write("\n")
    outfile.write("The relative score to the top university in ")
    #change the information to a string so that it can be written in the text file
    outfile.write(str(f))
    outfile.write(" is => (")
    outfile.write(scoreString)
    outfile.write(" / ")
    #change the information to a string so that it can be written in the text file
    outfile.write(str(g))
    outfile.write((") x 100% = "))
    #change the information to a string so that it can be written in the text file
    outfile.write(str(e))
    outfile.write("%")

    capital = capitalCity(country,capitalsList)
    #change the information to a string so that it can be written in the text file
    capitalString = str(capital)
    outfile.write("\n")
    outfile.write("The capital is => ")
    outfile.write(capitalString)

    uniCapitalNameList = universitiesWithCapitalName(capital,uniList)
    count = 0
    outfile.write("\n")
    outfile.write("The universities that contain the capital name => \n")
    for word in uniCapitalNameList:
        count = count + 1
        outfile.write("#")
        #change the information to a string so that it can be written in the text file
        outfile.write(str(count))
        outfile.write(" ")
        outfile.write(word)
        outfile.write("\n")

    #close the file
    outfile.close()
