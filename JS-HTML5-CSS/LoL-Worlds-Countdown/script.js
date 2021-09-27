const daysElement = document.getElementById('days')
const hoursElement = document.getElementById('hours');
const minutesElements = document.getElementById('minutes');
const secondsElements = document.getElementById('seconds');

const worlds = '5 Oct 2021';

function countDown() {
    const worldsDate = new Date(worlds);
    const currentDate = new Date();
    const total = worldsDate - currentDate;

    const seconds = Math.floor((total/1000)%60);
    const minutes = Math.floor((total/1000/60)%60);
    const hours = Math.floor((total/(1000*60*60))%24);
    const days = Math.floor(total/(1000*60*60*24));

    daysElement.innerHTML = formatTime(days);
    hoursElement.innerHTML = formatTime(hours);
    minutesElements.innerHTML = formatTime(minutes);
    secondsElements.innerHTML = formatTime(seconds);
}

function formatTime(time) {
    return time < 10 ? `0${time}` : time;
}

countDown()
setInterval(countDown, 1000);