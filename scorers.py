def calculateScorers (arr1, arr2):
  import main
  goals = 0
  
  for i in arr1:
    goals = goals + main.dfResultsTable.at[i,'GOLES1']
   
  for i in arr2:
    goals = goals + main.dfResultsTable.at[i,'GOLES2']

  narr = [3, goals]
      
  return narr