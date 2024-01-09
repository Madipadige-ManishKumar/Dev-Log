// Created by Rull Deef 🐺

var W, H, ctx;

var balls = [], k = 500;

onload = function() {
  var canvas = document.querySelector('canvas');
  canvas.width = W = window.innerWidth;
  canvas.height = H = window.innerHeight;
  ctx = canvas.getContext('2d');
  //ctx.shadowBlur = 15;
  
  for(var i = 0; i < k; i++)
    balls.push({x:0, y:0, r:6});
  
  animate();
}

function animate() {
  window.requestAnimationFrame(animate);
  ctx.clearRect(0, 0, W, H);
  
  var t = Date.now()/0.3e3;
  
  for(var i = 0; i < k; i++) {
    var ball = balls[i];
    var a = t + 2*Math.PI*i/k;
    
    var rx = W/40*Math.cos(3*t + 20*a);
    var ry = W/40*Math.sin(4*t + 30*a);
    
    var x = W/3*Math.cos(a) + rx;
    var y = W/7*Math.sin(a*2) + ry;
    
    y *= Math.sin(t/4);
    
    var u = 3*Math.sin(t/2);
    ball.x = x*Math.cos(u) - y*Math.sin(u);
    ball.y = x*Math.sin(u) + y*Math.cos(u);
    
    ball.x += W/2;
    
    
    ball.y += H/2;
    
    ball.r = 20 * (Math.abs(Math.sin(t+a)*Math.cos(t+a/2)));
    
    var hue = 360*(Math.sin(4*a + t)/2 + 0.5);
    var c = 255*(Math.sin(4*a + t)/2 + 0.5);
    ctx.fillStyle = ctx.shadowColor =
      //'hsl('+hue+', 50%, 50%)';
      'rgba('+c/2+','+(255-c)+',255,0.3)';
      
      // 128 0 255
      // 0 128 255
    
    draw(ball);
  }
}

function draw(obj) {
  ctx.beginPath();
  ctx.arc(obj.x, obj.y, obj.r, 0, 2*Math.PI);
  ctx.fill();
}
