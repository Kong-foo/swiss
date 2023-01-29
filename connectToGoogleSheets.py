# Code to read a google sheet

import pandas as pd
sheet_id = "1X1rPI1x6GYm2mRRofPEyDdCNArYjO7mWQefBOTK5xxc"
sheet_name = "First_Round"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

firstRound = pd.read_csv(url)
print(firstRound)
print(firstRound.iloc[0:])
