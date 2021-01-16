let btn = document.getElementById('btn');

btn.addEventListener('contextmenu', (event) => {
    event.preventDefault();
});

btn.addEventListener('mouseup', (event) => {
    let msg = document.querySelector('#message');
    switch (event.button) {
        case 0:
            msg.textContent = 'left';
            break;
        case 1:
            msg.textContent = 'middle';
            break;
        default:
            msg.textContent = 'right';
    }
});