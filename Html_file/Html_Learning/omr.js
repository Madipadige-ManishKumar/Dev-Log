document.addEventListener("DOMContentLoaded", function() {
    const timerInput = document.getElementById("timerInput");
    const startButton = document.getElementById("startButton");
    const navbarTimer = document.getElementById("navbarTimer");

    let countdown;
    
    function startTimer(duration) {
        const startTime = Date.now();
        clearInterval(countdown);

        countdown = setInterval(function() {
            const elapsedTime = Date.now() - startTime;
            const remainingTime = Math.max(duration * 60 * 1000 - elapsedTime, 0);
            
            const minutes = Math.floor(remainingTime / 1000 / 60);
            const seconds = Math.floor((remainingTime / 1000) % 60);
            
            const formattedTime = `${minutes}:${seconds.toString().padStart(2, '0')}`;
            navbarTimer.textContent = `Time remaining: ${formattedTime}`;
            
            if (remainingTime === 0) {
                clearInterval(countdown);
                navbarTimer.textContent = "Time's up!";
            }
        }, 1000);
    }
    
    startButton.addEventListener("click", function() {
        const timerDuration = parseInt(timerInput.value, 10);
        if (!isNaN(timerDuration) && timerDuration > 0) {
            startTimer(timerDuration);
        }
    });
});
