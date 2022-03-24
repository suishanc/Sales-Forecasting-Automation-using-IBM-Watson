def main()
    from waston_machine_learning_client import WastonMachineLearningAPIClient

    # WML credentials
    wml_credentials = {
        "apikey": "<insert apikey here>"
        "instance_id": "<insert instance here>"
        "url": "<insert url here>"
    }

    # Create a new instance of client
    client = WastonMachineLearningAPIClient(wml_credentials)
    
    # Generate an iam token
    iam_token = client.wml_token

    # Extract ML Instance to a variable
    ml_instance_id = wml_credentials["instance_id"]

    # Request header
    import urllib3, requests, json
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer' + iam_token, "ML_Instance_ID": ml_instance_id}

    # Get data from Excel Document
    import pandas as pd
    df = pd.read_ecxel('Store Sales.xlsx')
    df['Date'] = df['Date'].astype(str)
    df.fillna(0, inplace = True)

    # Setup data from Excel Documents
    payload_scoring = {"input_data": [{"fields": ["Store", "Date", "Open", "Prom", "StateHoliday", "ScoolHoliday", "StoreType", "Assortment", "CompetitionDistance", "CompetitionOpenSinceMonth", "CompetitionOpenSinceYear", "Promo2", "Promo2ScinceWeek", "Promo2ScinceYear"], "values": df.values.tolist()}]}

    # Execute the request
    response_scoring = requests.post('https://')

    # Reformat predictions
    predictions = response_scoring.json()
    df['Sales'] = [x[0] for x in preditions['prediction'][0]['values']]

    # Export to Excel
    df.to_excel('Predicted Sales.xlsx')

if __name__ == "__main__":
    main()