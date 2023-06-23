import pandas as pd
import os

currentDir = os.getcwd()
customers = pd.read_csv(currentDir + "/brazilian_customers/olist_customers_dataset.csv")

grouped = customers.groupby("customer_state")

for state in grouped:
    stateName = state[0]
    stateCustomers = state[1]
    citiesAtState = stateCustomers.groupby("customer_city")

    cities = []
    for city in citiesAtState:
        cityName = city[0]
        cityCustomers = city[1]

        cities.append({"cidade": cityName, "clientes": cityCustomers["customer_city"].count()})    
    
    cities.append({"cidade": "TOTAL", "clientes": stateCustomers["customer_state"].count()})

    stateDataFrame = pd.DataFrame(cities, columns=["cidade", "clientes"])
   
    outdir = './output'
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    fullpath = os.path.join(outdir, stateName + '.csv')
    stateDataFrame.to_csv(fullpath, index=False, columns=["cidade", "clientes"])
    
    print("Arquivo do estado " + stateName + " criado")
