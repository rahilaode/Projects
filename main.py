from flask import Flask, request, jsonify, render_template, url_for

import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

scaler = MinMaxScaler(feature_range=(0,1))
model = load_model('my_model.h5')
df = pd.read_csv('commodity_trade_statistics_data.csv')
    
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/predict_api', methods=['POST'])
def predict_():
    
    #commodity = str(request.form['commodity'])
    #country = str(request.form['country'])
    json_ = request.json
    nation = str(json_["country"])
    comodity = str(json_["commodity"])
    
    data_com = df[df.commodity == comodity]
    data_nation = data_com[data_com.country_or_area == nation]
    data_flow = data_nation[data_nation.flow == 'Import']
    sort_year = data_flow.sort_values('year')   #sort year
    data_reindex = sort_year.reset_index(drop=True) #reindex
  
    quantity = []
    for index, rows in data_reindex.iterrows():
        my_list = [rows.quantity]
        quantity.append(my_list)
    
    real_quantity = []
    for index, rows in data_reindex.iterrows():
        my_list = rows.quantity
        real_quantity.append(my_list)

    year = []
    for index, rows in data_reindex.iterrows():
        my_list = rows.year
        year.append(my_list)
    
    df1 = scaler.fit_transform(np.array(quantity).reshape(-1,1))
    
    
    x_input = df1[-3:].reshape(1,-1) #pick the last 3  number in dataset as Input 
    x_input.shape 

    temp_input = list(x_input)
    temp_input = temp_input[0].tolist()
    #print(temp_input)


    lst_output=[] # to store number predictions of the next 3 years
    n_steps=3
    i=0
    while(i<3):

        if(len(temp_input)>3):
            #print(temp_input)
            x_input=np.array(temp_input[1:])
            #print("{} day input {}".format(i,x_input))
            x_input=x_input.reshape(1,-1)
            x_input = x_input.reshape((1, n_steps, 1))
            #print(x_input)
            yhat = model.predict(x_input, verbose=0)
            #print("{} day output {}".format(i,yhat))
            temp_input.extend(yhat[0].tolist())
            temp_input=temp_input[1:]
            #print(temp_input)
            lst_output.extend(yhat.tolist())
            i=i+1
        else:
            #
            x_input = x_input.reshape((1, n_steps,1))
            yhat = model.predict(x_input, verbose=0)
            #print(yhat[0])
            temp_input.extend(yhat[0].tolist())
            #print(len(temp_input))
            lst_output.extend(yhat.tolist())
            i=i+1
    
    
    last_year = year[-1:]
    last_year = [str(integer) for integer in last_year] #convert to string
    last_year = "".join(last_year) #convert to string
    last_year = int(last_year) #convert to integer

    for i in range(1,4):
        last_year = last_year + 1
        year.append(last_year)
        
    predict_quantity = lst_output
    predict_quantity = scaler.inverse_transform(predict_quantity)
    predict_quantity = predict_quantity.tolist()
    predict_quantity = [ix[0] for ix in predict_quantity]
    predict_quantity = [int(predict_quantity) for predict_quantity in predict_quantity]
    full_quantity = real_quantity + predict_quantity
    
    to_json = {"Year":year, "Quantity":full_quantity}
    data = jsonify(to_json)
    return data


if __name__ == '__main__':
    app.run(port=8080, debug=True)