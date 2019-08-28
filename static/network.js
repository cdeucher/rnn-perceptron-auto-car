
class network{
   myNetwork;
   player;
   play;

  constructor(player, weights1, weights2){  
      this.player    = player       
      this.index     = player.index
      this.weights1   = weights1
      this.weights2   = weights2
  }
  update(){     
     let plataforma = 900; 
     if(this.player.y > 350 && this.player.x < 250)
        plataforma = 200; 
     if(this.player.y > 270 && this.player.x > 550)
        plataforma = 500;       

      $.ajax({ 
         url:"/get",
         type: "POST",
         data: JSON.stringify({ index:this.index
                              , weights1: this.weights1
                              , weights2: this.weights2
                              , inputs: [this.player.x, this.player.y, plataforma, 0] 
         }),
         contentType: "application/json; charset=utf-8"
      , success: ( data ) => {
            this.play = JSON.parse(data);
            //console.log(play);
            var max = this.play.run.reduce(function(a, b) {
               return Math.max(a, b);
            });

            this.player.max = this.play.run.indexOf(max);
            //console.log(this.index, this.player.max, this.play.run[this.player.max])
            console.log(this.index, this.player.x, this.player.y, plataforma) 
        }
      })  
     //console.log('player.max',this.player.max)     
     return this.player.max
  } 

}
//var rnn = new network()