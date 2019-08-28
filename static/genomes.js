
function copy(nestedNumbers){
    return JSON.parse(JSON.stringify(nestedNumbers))
}
class oGenome{
   betters = [] 
   constructor(){  
   }
   get_betters(list){            
        //get betters
        console.log('listPlayers',list.length)
        var list_betters = {sum:9999999};
        var newList = []
        var count = 0
        for (var i in list) {                       
            list[i].sum = parseFloat((list[i].y).toFixed(5));            

            if(list[i].sum < list_betters.sum){
                list_betters = list[i].rnn
                list_betters.sum = list[i].sum
                console.log('list_betters',list_betters) 
            }

            count++
        }
        //newList[0] = {'weights1': list_betters.rnn.weights1, 'weights2': list_betters.rnn.weights2 }

        var tmp = list.sort((v1, v2) => v1.sum - v2.sum).map((v) => v);
        //copy 3 better positions 
        for (let i=0; i<2 ; i++) {
            if(tmp[i] != undefined){ 
                newList[i] =  {'weights1': copy(tmp[i].rnn.weights1), 'weights2': copy(tmp[i].rnn.weights2) }
                //console.log('better',i, ':',tmp[i].sum, 'xy',tmp[i].x , tmp[i].y) 
            }
        }
        // replay 10 with better
        for (let i=2; i<=25 ; i++) {                                           
            newList[i] = this.mutate(list_betters)                                               
        }         

        return newList
   }
   update(){     
   
   } 
   mutate(rnn){
      let weights1 = copy(rnn.weights1);
      let weights2 = copy(rnn.weights2);
      if(Math.random() <= 1){
        for(let i =0; i < 4; i++){
            if(Math.random() <= 0.2){
                weights1[i] = get_weight()
                console.log(rnn.weights1[i],' ->', weights1[i])
            }   
            if(Math.random() <= 0.2){
                weights2[i] = get_weight()
                console.log(rnn.weights2[i],' ->', weights2[i])
            }           
        }  
      }
      return {'weights1':weights1,'weights2':weights2}
   }
 
 }
 var genome = new oGenome()