# Desarrollado por Wilder Chacón
import pandas as pd
import calculate
import scorers


datafile = pd.ExcelFile("TABLA RETO7.xlsx");

grupsTable = datafile.parse("GRUPOS");
dfGrupsTable = pd.DataFrame(grupsTable);

resultsTable = datafile.parse("RESULTADOS");
dfResultsTable = pd.DataFrame(resultsTable);

scorersTable = datafile.parse("GOLEADORES");
dfScorersTable = pd.DataFrame(scorersTable);

countrys = dfGrupsTable['PAIS']
gA = countrys[0:4].tolist();
gB = countrys[4:8].tolist();
gC = countrys[8:12].tolist();
gD = countrys[12:16].tolist();
gE = countrys[16:20].tolist();
gF = countrys[20:24].tolist();

print('*'*50)
print('       Tabla de posiciones - Copa mundial')
print('               Por Wilder Chacón')
print('*'*50)
print(' ')

arrA = calculate.calculatePts(gA)
positionxA = pd.DataFrame(arrA, columns=['Grupo A', 'PJ', 'PG', 'PE', 'PP', 'Pts']);
positionxA = positionxA.sort_values(by=['Pts'])
print(positionxA)

print(' ')
arrB = calculate.calculatePts(gB)
positionxB = pd.DataFrame(arrB, columns=['Grupo B', 'PJ', 'PG', 'PE', 'PP', 'Pts']);
positionxB = positionxB.sort_values(by=['Pts'])
print(positionxB)

print(' ')
arrC = calculate.calculatePts(gC)
positionxC = pd.DataFrame(arrC, columns=['Grupo C', 'PJ', 'PG', 'PE', 'PP', 'Pts']);
positionxC = positionxC.sort_values(by=['Pts'])
print(positionxC)

print(' ')
arrD = calculate.calculatePts(gD)
positionxD = pd.DataFrame(arrD, columns=['Grupo D', 'PJ', 'PG', 'PE', 'PP', 'Pts']);
positionxD = positionxD.sort_values(by=['Pts'])
print(positionxD)

print(' ')
arrE = calculate.calculatePts(gE)
positionxE = pd.DataFrame(arrE, columns=['Grupo E', 'PJ', 'PG', 'PE', 'PP', 'Pts']);
positionxE = positionxE.sort_values(by=['Pts'])
print(positionxE)

print(' ')
arrF = calculate.calculatePts(gF)
positionxF = pd.DataFrame(arrF, columns=['Grupo F', 'PJ', 'PG', 'PE', 'PP', 'Pts']);
positionxF = positionxF.sort_values(by=['Pts'])
print(positionxF)

print('*'*50)
print('        Tabla de goleadores - Copa mundial')
print('*'*50)
print(' ')

# countrys = dfGrupsTable['PAIS'].tolist();
# index_goals1 = dfResultsTable[dfResultsTable['PAIS1']==countrys[0]].index.tolist();
# index_goals2 = dfResultsTable[dfResultsTable['PAIS2']==countrys[0]].index.tolist();

# goals = scorers.calculateScorers(index_goals1, index_goals2)
# goals.insert(0, countrys[0])
# goals.insert(0, countrys[0])

