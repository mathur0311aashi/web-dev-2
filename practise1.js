function formatTime(unit) {
    return unit < 10 ? '0' + unit : unit;

}
function updateClock() {
    const now = new Date();
    const hours = formatTime(now.getHours());
    const minutes = formatTime(now.getMinutes());
    const seconds = formatTime(now.getSeconds());
    document.getElementById('Clock').textContent = `${hours}:${minutes}:${seconds}`;
}
updateClock();
setInterval(updateClock, 1000);