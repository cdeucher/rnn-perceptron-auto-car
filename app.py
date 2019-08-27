from flask import Flask, escape, request,render_template
import numpy as np
from numpy import exp, array, random, dot
import json
import network as rnn

app = Flask(__name__, static_url_path='/static')

# Create layer 1/2 (4 neurons, each with 4 inputs)
layer1 = rnn.NeuronLayer(4, 4)
layer2 = rnn.NeuronLayer(4, 4)
perceptron = rnn.NeuralNetwork(layer1, layer2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weights/<inputs>/<neurons>', methods=['POST','GET'])
def weights(inputs,neurons): 
   inputs = int(inputs)
   neurons = int(neurons)
   weights1 = 2 * random.random((inputs,neurons)) - 1
   weights2 = 2 * random.random((inputs,neurons)) - 1
   return json.dumps({'weights1':weights1.tolist(), 'weights2':weights2.tolist()})

@app.route('/get', methods=['POST','GET'])
def get(): 
   content = request.get_json()   

   inputs  = np.array(content['inputs'])
   weights1 = np.array(content['weights1'])
   weights2 = np.array(content['weights2'])
   hidden_state, output = perceptron.run(inputs, weights1, weights2) 

   print('get', inputs, output)

   return json.dumps({'index':content['index'], 'run':np.array(output).tolist()})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9800) 