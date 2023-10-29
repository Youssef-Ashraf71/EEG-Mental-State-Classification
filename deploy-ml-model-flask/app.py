from flask import Flask, render_template, request
import pickle
import numpy as np

import serial
import time
import csv
import serial.tools.list_ports

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = float(request.form['a'])
    data2 = float(request.form['b'])
    data3 = float(request.form['c'])
    data4 = float(request.form['d'])
    data5 = float(request.form['e'])
    data6 = float(request.form['f'])
    data7 = float(request.form['g'])
    data8 = float(request.form['h'])
    data9 = float(request.form['i'])
    data10 = float(request.form['j'])
    data11= float(request.form['k'])
    data12 = float(request.form['l'])
    data13 = float(request.form['m'])
    data14 = float(request.form['n'])
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7 , data8 , data9 , data10 , data11 , data12 , data13 , data14] ])
    # Closed data
 #   arr = np.array([[0.03503525, 1.43524487, 1.88139447, 0.0105765, 1.11845685 , 0.00897306, 0.0108704 , 1.86962095 , 0.01065082 , 1.01391014 , 0.88439326 , 1.49230906 , 0.03518974 , 0.00733689]])
    # Opened data
   # arr = np.array([1.35028199e-02,7.56459287e-01,9.65610139e-02,5.89455442e-04,7.87779742e-01,8.78033824e-03,1.00374913e-02,1.43783667e+00,2.52279581e-02,5.71930891e-01,2.32738258e-01,6.84049957e-01,1.26348531e-02,4.14011694e-04])
    arr = np.array(arr).reshape(-1,14,1) 
    pred = model.predict(arr)
    pred = np.array(pred >= 0.5, dtype = np.int64)
    # pred2 = (pred[0])
    # pred2 = (pred2[0])
    # # Establish serial communication with Arduino
    # arduino = serial.Serial('COM10', 9600)  # Replace with the appropriate port and baud rate
    # print(pred2.encode())
    # arduino.write((pred2).encode())
    # arduino.close()
       # Establish a serial connection
    # serial_inst = serial.Serial()
    # serial_inst.baudrate = 9600
    # serial_inst.port = "COM10"
    # serial_inst.open()
    # command: str =('Arduino Command: (ON/OFF): ')
    # print(command)
    # serial_inst.write(command.encode('utf-8'))
    # serial_inst.close()
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)















