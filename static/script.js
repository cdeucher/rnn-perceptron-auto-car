/* 
 * https://medium.com/machina-sapiens/aprendizagem-de-m%C3%A1quina-%C3%A9-divertido-parte-2-7c00d034e1d5 
 * https://medium.com/@peterkrauss/como-criar-uma-rede-neural-em-javascript-em-apenas-30-linhas-de-c%C3%B3digo-b8f09eb4439a
 * 
*/
class network{
  sigmoid(t) {
    //console.log('sigmoid',t)
    return 1/(1+Math.exp(-t));
  }
  neuronio(quartos, metros_quadrados, bairro, pesos){
      price = 0
      price += quartos * pesos.q1
      price += metros_quadrados * pesos.q2
      price += bairro * pesos.q3
    return this.sigmoid(price)
  }
  neuronio_saida(d1,d2,d3,d4, pesos){
      price = 0
      price += d1 * pesos.q1
      price += d2 * pesos.q2
      price += d3 * pesos.q3
      price += d4 * pesos.q4
    return this.sigmoid(price)
  }    

}
var rnn = new network()

//4 neuronios com 3 imputs e 3 pesos (hidden layer)
var d1 = rnn.neuronio(3, 2000, 1, { q1: -0.956,q2: -0.041,q3: 0.057 })
var d2 = rnn.neuronio(3, 2000, 1, { q1: 0.571, q2: 0.998, q3: 0.001 })
var d3 = rnn.neuronio(3, 2000, 1, { q1: 0.001, q2: 0.998, q3: 0.002 })
var d4 = rnn.neuronio(3, 2000, 1, { q1: 0.087, q2: 0.101, q3: 0.023 })
console.log(d1,d2,d3,d4)

//2 neuronios com 4 imputs (neuronios) e 4 pesos (out layer), 2 saidas
var price  = rnn.neuronio_saida(d1,d2,d3,d4, {q1: 0.20, q2:0.15, q3:0.05, q4:0.60})
var price2 = rnn.neuronio_saida(d1,d2,d3,d4, {q1: 0.18, q2:0.25, q3:0.05, q4:0.60})
console.log(price,price2)