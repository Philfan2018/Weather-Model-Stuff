import requests
import datetime as dt
import numpy as np
import pandas as pd
import matplotlib as plt

def get_mos_data(Station_id, Model):
    MOS_url = f"https://mesonet.agron.iastate.edu/api/1/mos.json?station={Station_id}&model={Model}"
    response = requests.get(MOS_url)
    if response.status_code == 200:
      	MOS_data = response.json()
      	return MOS_data
    else:
      	print(f"Something went wrong! {response.status_code}")

Raw_mos_data = get_mos_data("KUNV", "NBS")

for item in Raw_mos_data['data']:
    Temp = item["tmp"]
    Forecast_time = item["ftime"]

Temp = []
forecast_time = []

for item in Raw_mos_data['data']:
    Temp.append(item["tmp"])
    forecast_time.append(item["ftime"])

# This is because the arrays are not the same size
min_len = min(len(Temp), len(forecast_time))
Temp = Temp[:min_len]
forecast_time = forecast_time[:min_len]

Temp_forecast_time = np.array([Temp, forecast_time])

Forecast_time_datetime = pd.to_datetime(forecast_time)

fig, ax = plt.subplots()
ax.plot(Forecast_time_datetime, Temp)
plt.show()
