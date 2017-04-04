import numpy, csv

PERFORMING_COUNTRIES = ['Ukraine','Belarus','Azerbaijan','Iceland','Norway','Romania','Armenia','Montenegro','Poland','Greece','Austria', 'Germany','Sweden','France','Russia', 'Italy','Slovenia','Finland','Spain','Switzerland','Hungary','Malta','Denmark','The Netherlands','San Marino','United Kingdom']

scoreboard = numpy.zeros((26, 37), dtype=numpy.int)

with open('../ESC-2014-grand_final-full_results.csv', 'rbU') as csvfile:
    results = csv.reader(csvfile)
    results.next() # skip the first two lines
    results.next()
    i = 0
    k = 0
    
    for row in results:
        fromCountry = row[0]
        j = i%26
        if j == 0:
            k = k+1
        points = 0
        
        if fromCountry == PERFORMING_COUNTRIES[j]:
            # print(fromCountry, fromCountry, 0, i%26, k-1)
            numpy.insert(scoreboard, i%26, k-1)
            # scoreboard[i%26][k-1] = 0 # add to scoreboard
            i = i+1
        if row[-1] != '\n':
            points = row[-1]              
        
        # print(row[0], row[1], points, i%26, k-1)
        scoreboard[i%26][k-1] = points # add to scoreboard
        numpy.insert(scoreboard, i%26, k-1)
        i = i+1
        # scoreboard[j][k-1] = points
        # currentRow.append(int(points))
    # print(row[0], row[0], 0, i%26, k-1)
    scoreboard[i%26][k-1] = 0 # add to scoreboard
    numpy.insert(scoreboard, i%26, k-1)
    
print(scoreboard.tolist())
