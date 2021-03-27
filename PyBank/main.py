
import csv
import statistics as st
csvFile = open('resources/budget_data.csv')
reader = csv.reader(csvFile, delimiter=',')
data = list(reader)
data.pop(0)
previousCoffers = int(data[1][1])
totalMonths = 0
sumCoffers = 0
change = 0
changeList = []
greatestIncrease = 0
increaseMonth = ""
greatestDecrease = 0
decreaseMonth = ""

def printTerminal():
    print(wholeText)

def printText():
    saveFile = open("analysis\FinancialAnalysis.txt", "w")
    saveFile.write(wholeText)
    saveFile.close()

def finishProgram():
    printTerminal()
    printText()

for line in data:
    totalMonths = totalMonths + 1
    sumCoffers = sumCoffers + int(line[1])
    change = int(previousCoffers) - int(line[1])
    previousCoffers = int(line[1])
    changeList.append(change)
    if int(line[1]) > greatestIncrease:
        greatestIncrease = int(line[1])
        increaseMonth = line[0]
    if int(line[1]) < greatestDecrease:
        greatestDecrease = int(line[1])
        decreaseMonth = line[0]

averageChange = st.mean(changeList)

# double checking the average change result because the number does not match the example given
total = 0
for item in changeList:
    total = total + 1
sumChanges = sum(changeList)

textOne = "Financial Analysis" + "\n" + "- - - - - - - - - - - - - - - - - - - - - - - - "
textTwo = "Total Months: " + str(totalMonths)
textThree = "Total: $" + str(sumCoffers)
textFour = "Average Change: $" + str(averageChange)
textFive = "Greatest Increase in Profits: " + str(increaseMonth) + " ($" + str(greatestIncrease) + ")"
textSix = "Greatest Decrease in Profits: " + str(decreaseMonth) + " ($" + str(greatestDecrease) + ")"
wholeText = textOne  + "\n" + textTwo  + "\n" + textThree  + "\n" + textFour  + "\n" + textFive  + "\n" + textSix

finishProgram()