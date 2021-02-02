import csv

pathToCSV = "path/to/csvfile.csv"
uniqueDomains = set()

with open(pathToCSV, "r") as file:
    reader = csv.reader(file)
    for line in reader:
        domain = line[0].split("@")
        if len(domain) > 1:
            uniqueDomains.add(domain[1])

for domain in uniqueDomains:
    print(domain)
