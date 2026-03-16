const canvas = document.getElementById('pongCanvas');
const ctx = canvas.getContext('2d');

canvas.width = 600;
canvas.height = 400;

const ball = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    radius: 10,
    dx: 4,
    dy: 4,
    color: '#FFD700' // Golden Sun
};

const paddleHeight = 80;
const paddleWidth = 20;

const user = {
    x: 0,
    y: canvas.height / 2 - paddleHeight / 2,
    width: paddleWidth,
    height: paddleHeight,
    color: '#008080'
};

const com = {
    x: canvas.width - paddleWidth,
    y: canvas.height / 2 - paddleHeight / 2,
    width: paddleWidth,
    height: paddleHeight,
    color: '#FF69B4'
};

function drawBall(x, y, r, color) {
    // Draw Golden Sun Ball
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2, false);
    ctx.closePath();
    ctx.fill();
    
    // Sun Rays
    ctx.strokeStyle = color;
    ctx.lineWidth = 2;
    for(let i=0; i<8; i++) {
        const angle = (i * Math.PI) / 4;
        ctx.beginPath();
        ctx.moveTo(x + Math.cos(angle)*r, y + Math.sin(angle)*r);
        ctx.lineTo(x + Math.cos(angle)*(r+5), y + Math.sin(angle)*(r+5));
        ctx.stroke();
    }
}

function drawLeafPaddle(x, y, w, h, color) {
    // Stylized Leaf Paddle
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.moveTo(x + w/2, y);
    ctx.quadraticCurveTo(x + w*1.5, y + h/2, x + w/2, y + h);
    ctx.quadraticCurveTo(x - w/2, y + h/2, x + w/2, y);
    ctx.fill();
    
    // Leaf Vein
    ctx.strokeStyle = 'rgba(255,255,255,0.3)';
    ctx.beginPath();
    ctx.moveTo(x + w/2, y);
    ctx.lineTo(x + w/2, y + h);
    ctx.stroke();
}

function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    drawBall(ball.x, ball.y, ball.radius, ball.color);
    drawLeafPaddle(user.x, user.y, user.width, user.height, user.color);
    drawLeafPaddle(com.x, com.y, com.width, com.height, com.color);
}

canvas.addEventListener('mousemove', (e) => {
    let rect = canvas.getBoundingClientRect();
    user.y = e.clientY - rect.top - user.height / 2;
});

function update() {
    ball.x += ball.dx;
    ball.y += ball.dy;

    // AI
    com.y += (ball.y - (com.y + com.height / 2)) * 0.1;

    if (ball.y + ball.radius > canvas.height || ball.y - ball.radius < 0) {
        ball.dy = -ball.dy;
    }

    let player = (ball.x < canvas.width / 2) ? user : com;

    if (collision(ball, player)) {
        ball.dx = -ball.dx;
    }

    if (ball.x < 0 || ball.x > canvas.width) {
        ball.x = canvas.width / 2;
        ball.y = canvas.height / 2;
        ball.dx = -ball.dx;
    }
}

function collision(b, p) {
    p.top = p.y;
    p.bottom = p.y + p.height;
    p.left = p.x;
    p.right = p.x + p.width;

    b.top = b.y - b.radius;
    b.bottom = b.y + b.radius;
    b.left = b.x - b.radius;
    b.right = b.x + b.radius;

    return b.right > p.left && b.top < p.bottom && b.left < p.right && b.bottom > p.top;
}

function game() {
    update();
    render();
}

setInterval(game, 1000 / 60);
