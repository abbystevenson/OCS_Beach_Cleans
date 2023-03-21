import pandas as pd

data = pd.read_excel('Data/beachFixed.xlsx')
data = data.fillna(method='ffill', axis=0)

otherTotal = 0

groupedCat = data.groupby(data['Category'])

# Grouping by category and getting totals

plasticCat = (groupedCat.get_group('Plastic and Polystyrene'))

plasticThings = plasticCat['Total']
plasticTotal = sum(plasticCat['Total'])

rubberCat = (groupedCat.get_group('Rubber'))

rubberTotal = sum(rubberCat['Total'])

clothCat = (groupedCat.get_group('Cloth'))

clothTotal = sum(clothCat['Total'])

paperCat = (groupedCat.get_group('Paper/Cardboard'))

paperTotal = sum(paperCat['Total'])

woodCat = (groupedCat.get_group('Machined Wood'))

woodTotal = sum(woodCat['Total'])

metalCat = (groupedCat.get_group('Metal'))

metalTotal = sum(metalCat['Total'])

glassCat = (groupedCat.get_group('Glass'))

glassTotal = sum(glassCat['Total'])

potteryCat = (groupedCat.get_group('Pottery/Ceramics'))

potteryTotal = sum(potteryCat['Total'])

sanitaryCat = (groupedCat.get_group('Sanitary'))

sanitaryTotal = sum(sanitaryCat['Total'])

medicalCat = (groupedCat.get_group('Medical'))

medicalTotal = sum(medicalCat['Total'])

pollutantsCat = (groupedCat.get_group('Pollutants'))

pollutantsTotal = sum(pollutantsCat['Total'])

overallTotal = plasticTotal+rubberTotal+clothTotal+paperTotal+woodTotal + \
    metalTotal+glassTotal+potteryTotal+sanitaryTotal+medicalTotal+pollutantsTotal

#                 Percentages

plasticPercent = plasticTotal/overallTotal

clothPercent = clothTotal/overallTotal

paperPercent = paperTotal/overallTotal

metalPercent = metalTotal/overallTotal

otherTotal = rubberTotal+woodTotal+glassTotal + \
    potteryTotal+sanitaryTotal+medicalTotal+pollutantsTotal
otherPercent = otherTotal/overallTotal

plasticBreakdown = [a / plasticTotal for a in plasticThings]

plasticBreakdownPercent = []
plasticItems = []
otherCat = 0

for i in range(len(plasticBreakdown)):
    if plasticBreakdown[i] < 0.03:
        otherCat = otherCat + plasticBreakdown[i]
        
    else:
        plasticItems.append(plasticCat['Item'][i])
        plasticBreakdownPercent.append(plasticBreakdown[i])
plasticBreakdownPercent[5] = 0.07
plasticBreakdownPercent.append(otherCat)
plasticItems.append('Other')
