

class oGenome{
   betters = [] 
   constructor(){  
   }
   get_betters(list){            
        //get betters
        console.log('listPlayers',list.length)
        var list_betters = {sum:90000};
        var newList = []
        var count = 0
        for (var i in list) {                       
            list[i].sum = parseInt((list[i].y).toFixed(5));            

            if(list[i].sum < list_betters.sum){
                list_betters = list[i]
                console.log('sum',list[i].sum, 'xy',list[i].x , list[i].y) 
            }

            count++
        }
        newList[0] = {'weights1': list_betters.rnn.weights1, 'weights2': list_betters.rnn.weights2 }

        var tmp = list.sort((v1, v2) => v1.sum - v2.sum).map((v) => v);
        //copy 3 better positions 
        for (let i=1; i<4 ; i++) {
            if(tmp[i] != undefined){ 
                newList[i] = tmp[i]
            }
        }
        // replay 10 with better
        for (let i=4; i<=14 ; i++) {
            if(tmp[i] != undefined){                                               
                //returnList[i] = this.mutate(list_betters)                                               
            }
        }         

        return newList
   }
   update(){     
   
   } 
 
 }
 var genome = new oGenome()