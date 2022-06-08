def calculatePts (arr):
  import main
  import positions as pt

  index_gA01 = main.dfResultsTable[main.dfResultsTable['PAIS1']==arr[0]].index.tolist();
  index_gA02 = main.dfResultsTable[main.dfResultsTable['PAIS2']==arr[0]].index.tolist();
  index_gA11 = main.dfResultsTable[main.dfResultsTable['PAIS1']==arr[1]].index.tolist();  
  index_gA12 = main.dfResultsTable[main.dfResultsTable['PAIS2']==arr[1]].index.tolist();
  index_gA21 = main.dfResultsTable[main.dfResultsTable['PAIS1']==arr[2]].index.tolist();  
  index_gA22 = main.dfResultsTable[main.dfResultsTable['PAIS2']==arr[2]].index.tolist();
  index_gA31 = main.dfResultsTable[main.dfResultsTable['PAIS1']==arr[3]].index.tolist();  
  index_gA32 = main.dfResultsTable[main.dfResultsTable['PAIS2']==arr[3]].index.tolist();
  
  gA0 = pt.calculatePositions(index_gA01, index_gA02)
  gA0.insert(0, arr[0])
  
  gA1 = pt.calculatePositions(index_gA11, index_gA12)
  gA1.insert(0, arr[1])
  
  gA2 = pt.calculatePositions(index_gA21, index_gA22)
  gA2.insert(0, arr[2])
  
  gA3 = pt.calculatePositions(index_gA31, index_gA32)
  gA3.insert(0, arr[3])

  array = [gA0, gA1, gA2, gA3]
  return array
