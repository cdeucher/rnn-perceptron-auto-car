/* 
 * https://medium.com/machina-sapiens/aprendizagem-de-m%C3%A1quina-%C3%A9-divertido-parte-2-7c00d034e1d5 
 * https://medium.com/@peterkrauss/como-criar-uma-rede-neural-em-javascript-em-apenas-30-linhas-de-c%C3%B3digo-b8f09eb4439a
 * 
*/
class network{
    max = 1000
    min = -1000
    peso1 = { q1: Math.floor(Math.random() * (this.max - this.min + 1)) + this.min,  q2: Math.floor(Math.random() * (this.max - this.min + 1)) + this.min };
    peso2 = { q1: Math.floor(Math.random() * (this.max - this.min + 1)) + this.min,  q2: Math.floor(Math.random() * (this.max - this.min + 1)) + this.min };
    peso3 = { q1: Math.floor(Math.random() * (this.max - this.min + 1)) + this.min,  q2: Math.floor(Math.random() * (this.max - this.min + 1)) + this.min };
    S1 = { q1: Math.floor(Math.random() * (this.max - this.min + 1)) + this.min,  q2: Math.floor(Math.random() * (this.max - this.min + 1)) + this.min };
    S2 = { q1: Math.floor(Math.random() * (this.max - this.min + 1)) + this.min,  q2: Math.floor(Math.random() * (this.max - this.min + 1)) + this.min };
    S3 = { q1: Math.floor(Math.random() * (this.max - this.min + 1)) + this.min,  q2: Math.floor(Math.random() * (this.max - this.min + 1)) + this.min };
       
    
    sigmoid(t) {
      //console.log('sigmoid',t,  (1/(1+Math.pow(Math.E, -t))))
      //return 1/(1+Math.exp(-t));
      return (1/(1+Math.pow(Math.E, -t)) > 0 ? 1 : 0);
    }
    neuronio(x , y, pesos){
        let price = 0
        price += x * pesos.q1
        price += y * pesos.q2
      return Number(this.sigmoid(price)).toFixed(3)
    }
    neuronio_saida(neuro1,neuro2,neuro3, pesos){
        console.log(neuro1,neuro2,neuro3, pesos)
        let price = 0
        price += neuro1 * pesos.q1
        price += neuro2 * pesos.q2
        price += neuro3 * pesos.q3
      return Number(this.sigmoid(price)).toFixed(50)
    }
    update(player, game){       
 
       let d1 = this.neuronio(player.x,player.y, this.peso1)
       let d2 = this.neuronio(player.x,player.y, this.peso2)
       let d3 = this.neuronio(player.x,player.y, this.peso3)

       let result1 = this.neuronio_saida(d1,d2,d3, this.S1)
       let result2 = this.neuronio_saida(d1,d2,d3, this.S2)
       let result3 = this.neuronio_saida(d1,d2,d3, this.S3)

       console.log('result1',this.peso1,result1)
       console.log('result2',this.peso2,result2)
       console.log('result3',this.peso3,result3)
    } 
  
  }
  var rnn = new network()