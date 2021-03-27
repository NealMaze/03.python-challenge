import csv
import statistics as st

csvFile = open('resources/election_data.csv')
reader = csv.reader(csvFile, delimiter=',')
data = list(reader)
data.pop(0)
totalVotes = 0
candidateVotes = {}
mostVotes = 0
winner = ""
analysis = []
text = ""

def percentage(part, whole):
  return 100 * float(part)/float(whole)

for vote in data:
    totalVotes = totalVotes + 1
    if vote[2] not in candidateVotes:
        candidateVotes[vote[2]] = 1
    else:
        candidateVotes[vote[2]] += 1

for candidate in candidateVotes:
    percent = percentage(candidateVotes[candidate], totalVotes)
    roundPercent = round(percent, 1)
    text = (candidate + ": " + str(roundPercent) + "% (" + str(candidateVotes[candidate]) + ")" + "\n")
    analysis.append(text)
    if candidateVotes[candidate] > mostVotes:
        mostVotes = candidateVotes[candidate]
        winner = candidate

headText = "Election Results" + "\n" + "- - - - - - - - - - - - - - - -" + "\n" + "Total Votes: " + str(totalVotes) + "\n" + "- - - - - - - - - - - - - - - -" + "\n"
text = "".join(analysis)
tailText = "- - - - - - - - - - - - - - - -" + "\n" + "Winner: " + winner + "\n" + "- - - - - - - - - - - - - - - -" + "\n"

wholeText = f"{headText} {text} {tailText}"
print(wholeText)

saveFile = open("analysis\PollAnalysis.txt", "w")
saveFile.write(wholeText)
saveFile.close()