document.addEventListener("DOMContentLoaded", function() {
    hljs.highlightall();
});

let alerWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert_close');

if (alerWrapper) {
    alertClose.addEventListener('click', () =>
    alertWrapper.style.display = 'none'
    )
}