def readGoogleSheet(sheet_id, sheet_name):
  # Gets and returns data from a google sheet
  sheetId = sheet_id
  sheetName = sheet_name
  url = f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}"

  sheetData = pd.read_csv(url)

  return sheetData


def makeScript(sheet_data):
  # Write script for https://coronate.netlify.app/players

  dataText = '{"config": {"avoidPairs": [], "byeValue": 1, "lastBackup": "1970-01-01T00:00:00.000Z"}, "players": {'

  for row in range(len(sheet_data)):
      firstName = sheet_data.iloc[row,0].strip()   #strip trailing spaces
      lastName = sheet_data.iloc[row,1].strip()    #strip trailing spaces
      id = firstName + "-" + lastName
      dataText = dataText + '"{id}": {{'.format(id=id)
      dataText = dataText + '"firstName": "{firstName}", "id": "{id}", "lastName": "{lastName}", "matchCount": 0, "rating": 1, "type_": "person"'\
      .format(firstName=firstName, id=id, lastName=lastName)
      dataText = dataText + '}'

      if row != len(sheet_data)-1:                 #don't add a comma after the last item
        dataText = dataText + ','

  dataText = dataText + '}, "tournaments": {}}'

  return dataText


def main():
  import pandas as pd
  names = readGoogleSheet("1X1rPI1x6GYm2mRRofPEyDdCNArYjO7mWQefBOTK5xxc", "Names")
  text = makeScript(names)
  print(text)


main()
