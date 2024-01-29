window.addEventListener('load', function () {
    const headerElement = document.querySelector('.header');
    const headerHeight = headerElement.offsetHeight;

    headerElement.style.lineHeight = `${headerHeight}px`;
});

const container = document.querySelector('.container');

const buttons = document.querySelectorAll('.btn');
const checkboxes = document.querySelectorAll('.hidden-checkbox');

const candidatesCount = document.querySelectorAll('.candidate').length;
const choiceMade = new Array(candidatesCount).fill(false);

const endPopup = document.getElementById('end-popup');
const infoPopupTrigger = document.querySelector('.info-popup-btn');
const infoPopup = document.getElementById('info-popup');
let endPopupOpened = false;
let infoPopupOpened = false;

infoPopupTrigger.addEventListener('mouseenter', openInfoPopup);
infoPopupTrigger.addEventListener('mouseleave', closeInfoPopup);

const warningPopup = document.querySelector('.warning-popup');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        if (!(endPopupOpened || infoPopupOpened)) {
            const checkboxId = Math.floor(button.id / 2) + (Math.floor(button.id / 2) == button.id / 2 ? 0 : 1) - 1;

            if (button.id % 2 != 0) {
                if (button.classList.contains('recommend')) {
                    button.classList.toggle('recommend');
                    choiceMade[checkboxId] = false;
                    checkboxes[checkboxId].checked = false;
                } else if (buttons[button.id].classList.contains('reject')) {
                    buttons[button.id].classList.toggle('reject');
                    button.classList.add('recommend');
                    choiceMade[checkboxId] = true;
                    checkboxes[checkboxId].checked = true;
                } else {
                    button.classList.add('recommend');
                    choiceMade[checkboxId] = true;
                    checkboxes[checkboxId].checked = true;
                }
            } else {
                if (button.classList.contains('reject')) {
                    button.classList.toggle('reject');
                    choiceMade[checkboxId] = false;
                } else if (buttons[button.id - 2].classList.contains('recommend')) {
                    buttons[button.id - 2].classList.toggle('recommend');
                    button.classList.add('reject');
                    choiceMade[checkboxId] = true;
                } else {
                    button.classList.add('reject');
                    choiceMade[checkboxId] = true;
                }
            }
        }
    });
});

function checkFormValidness() {
    for (let i = 0; i < choiceMade.length; i++) {
        if (!choiceMade[i]) {
            return false;
        }
    }

    return true;
}

function openEndPopup() {
    if (!checkFormValidness()) {
        openWarningPopup();
        return;
    }

    closeWarningPopup();

    if (!infoPopupOpened) {
        endPopup.classList.add('open');
        endPopup.style.opacity = '1';
        endPopupOpened = true;

        container.style.overflow = 'hidden';

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                const target = entry.target;

                if (entry.isIntersecting && target.id !== 'end-popup') {
                    target.style.filter = 'blur(5px)';
                } else {
                    target.style.filter = 'none';
                }
            });
        });

        const elementsToBlur = document.querySelectorAll('.container > *:not(#end-popup)');

        elementsToBlur.forEach((element) => {
            observer.observe(element);
        });

        if (endPopup) {
            observer.observe(endPopup);
        }
    }
}

function closeEndPopup() {
    endPopup.classList.remove('open');
    endPopup.classList.add('close');
    endPopupOpened = false;

    container.style.overflow = 'none';
    container.style.overflowY = 'scroll';

    endPopup.addEventListener('transitionend', function () {
        endPopup.classList.remove('close');
    }, { once: true });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            entry.target.style.filter = 'none';
        });
    });

    const elementsToBlur = document.querySelectorAll('.container > *:not(#end-popup)');

    elementsToBlur.forEach((element) => {
        observer.observe(element);
    });

    if (endPopup) {
        observer.observe(endPopup);
    }
}

function manageInfoPopup() {
    if (!endPopupOpened) {
        if (infoPopupOpened) {
            closeInfoPopup();
        } else {
            openInfoPopup();
        }
    }
}

function openInfoPopup() {
    infoPopup.classList.remove('close');
    infoPopup.classList.add('open');
    infoPopupOpened = true;

    container.style.overflowY = 'hidden';
}

function closeInfoPopup() {
    infoPopup.classList.remove('open');
    infoPopup.classList.add('close');
    infoPopupOpened = false;
    
    container.style.overflowY = 'scroll';
}

function openWarningPopup() {
    warningPopup.classList.remove('close');
    warningPopup.classList.add('open');
}

function closeWarningPopup() {
    warningPopup.classList.remove('open');
    warningPopup.classList.add('close');
}