var canvas = document.getElementById("snake");
var context = canvas.getContext("2d");
var box = 16;
var snake = [];
var direction= 'right';
var pontuation = 0;
var xf=0;var yf=0;
snake[0] = {
  x: 16*box,
  y: 16*box
}
let snakeX = snake[0].x; 
// coordenadas da cabecinha da cobra
let snakeY = snake[0].y;

function createBG(){
		context.fillStyle = "lightgreen";
		context.fillRect(0,0,32 * box, 32 * box);    
}
function createSnake(){
   for(i=0; i < snake.length;i++){
      context.fillStyle = "darkgreen";
      context.fillRect(snake[i].x,snake[i].y,box,box);
      snake[i].fillStyle = "rgb(0,255,119)"; 
   }
}
function controlMoveSnake(event){
    if ((event.keyCode == 39) && (direction != 'left')) snakeX += box;
    if ((event.keyCode == 37) && (direction != 'right')) snakeX -= box;
    if ((event.keyCode == 40) && (direction == 'down')) snakeY -= box;
    if ((event.keyCode == 38) && (direction == 'up')) snakeY += box; 
}
function createBiscoit(){
     context.fillStyle = "red";
     xf = Math.floor(Math.random()*512);   
     yf = Math.floor(Math.random()*512);
     context.fillRect(xf,yf,box,box);
}
function checkBiscoit(){
   if (xf == -1){
     createBiscoit();
   } //cria a cobra
   if((snakeX == xf) && (snakeY == yf)){ 
        snake.unshift({x: 16*box,y: 16*box});
        pontuation+=1;
        xf,yf = createBiscoit();
   }
}
function detectionCollision(){
     for(i=1;i<snake.length;i++){
       if((snake[0].x == snake[i].x)&&(snake[0].y == snake[i].y)){
          clearInterval(game); alert("Fim!");
       }
     }
}
function limitsMoveSnake(){
  if(snake[0].x < 0 && direction == 'left') snake[0].x = 32 * box;
  if(snake[0].x > 32 && direction == 'right') snake[0].x = 0;
  if(snake[0].y < 0 && direction == 'up') snake[0].y = 32 * box;//512
  if(snake[0].y > 32 && direction == 'down') snake[0].y = 0;
}
function initiateGame(){
   limitsMoveSnake();// saber se ultrapassou limites da tela
   createBG();//cria o cenario
  createSnake();
  if(direction == "right") snakeX += box;//deslocamento automatica da cobra a cada frame
  if(direction == 'left') snakeX -= box;
  if(direction == 'up') snakeY -= box;
  if(direction == 'down') snakeY += box;
  snake.pop();
  detectionCollision();// para cada progressa saber se houve colisao com a propria cauda
  checkBiscoit(); // ou se alcancou o biscoito 
  document.getElementById("points").innerHTML = pontuation;//atualiza a pontuacao da cobra
}
   
var game = document.getElementById('garden');
var tmp = 500;

if(pontuation > 3) tmp -= 50;
game.addEventListener("load",setInterval(initiateGame,tmp));
game.addEventListener("keydown",controlMoveSnake); //conferir movimentos da cobra