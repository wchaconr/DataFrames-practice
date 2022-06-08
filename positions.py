def calculatePositions (arr1, arr2):
  import main
  Pts_gA0 = 0
  PG_gA0 = 0
  PE_gA0 = 0
  PP_gA0 = 0
  
  for i in arr1:
    if main.dfResultsTable.at[i,'GOLES1'] == main.dfResultsTable.at[i,'GOLES2']:
      Pts_gA0 = Pts_gA0 + 1
      PE_gA0 = PE_gA0 + 1
    if main.dfResultsTable.at[i,'GOLES1'] > main.dfResultsTable.at[i,'GOLES2']:
      Pts_gA0 = Pts_gA0 + 3
      PG_gA0 = PG_gA0 + 1
    if main.dfResultsTable.at[i,'GOLES1'] < main.dfResultsTable.at[i,'GOLES2']:
      PP_gA0 = PP_gA0 + 1
  
  for i in arr2:
    if main.dfResultsTable.at[i,'GOLES2'] == main.dfResultsTable.at[i,'GOLES1']:
      Pts_gA0 = Pts_gA0 + 1
      PE_gA0 = PE_gA0 + 1
    if main.dfResultsTable.at[i,'GOLES2'] > main.dfResultsTable.at[i,'GOLES1']:
      Pts_gA0 = Pts_gA0 + 3
      PG_gA0 = PG_gA0 + 1
    if main.dfResultsTable.at[i,'GOLES2'] < main.dfResultsTable.at[i,'GOLES1']:
     PP_gA0 = PP_gA0 + 1

  narr = [3, PG_gA0, PE_gA0, PP_gA0, Pts_gA0]
      
  return narr
  