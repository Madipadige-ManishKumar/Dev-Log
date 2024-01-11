const timerDisplay = document.getElementById('timer');
const inputMinutes = document.getElementById('inputMinutes');
const startButton = document.getElementById('startButton');
let timerInterval;

function startTimer(minutes) {
    clearInterval(timerInterval);

    const endTime = new Date().getTime() + (minutes * 60 * 1000);
    
    timerInterval = setInterval(() => {
        const now = new Date().getTime();
        const timeLeft = endTime - now;

        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        timerDisplay.textContent = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

        if (timeLeft < 0) {
            clearInterval(timerInterval);
            timerDisplay.textContent = '00:00:00';
        }
    }, 1000);
}

startButton.addEventListener('click', () => {
    const minutes = parseInt(inputMinutes.value);
    if (!isNaN(minutes)) {
        startTimer(minutes);
    }
});
