window.addEventListener('load', function () {
    resizeImage();
    window.addEventListener('resize', resizeImage);

    function resizeImage() {
        var img = document.querySelector('.bg-img');
        var screenWidth = window.innerWidth;
        var screenHeight = window.innerHeight;

        var imgSize = Math.min(screenWidth, screenHeight);

        var passwordInput = document.querySelector('.password-input');
        var submitInput = document.querySelector('.submit-input');

        var passwordInputWidthRatio = 1.2; // Пример: 30% от ширины изображения
        var submitInputWidthRatio = 0.5; // Пример: 20% от ширины изображения

        var passwordInputWidth = imgSize * passwordInputWidthRatio;
        var submitInputWidth = imgSize * submitInputWidthRatio;

        passwordInput.style.width = passwordInputWidth + 'px';
        submitInput.style.width = submitInputWidth + 'px';

        img.style.width = imgSize + 'px';
        img.style.height = imgSize + 'px';
    }
});

function onInputFocus() {
    setBg('light-blue');
}

function onInputBlur() {
    setBg('light-grey');
}

function onAdminClick() {
    console.log("admin click");
    
}

function onSignUpFailed() {
    setBg('light-red');

    showFailMsg();
}

function showFailMsg() {
    const failMsg = document.querySelector('.fail-msg');

    failMsg.style.opacity = '1';    
}

function setBg(color) {
    var img = document.querySelector('.bg-img');
    const curSrc = img.src;

    const colorSrc = {
        'light-red': 'lr',
        'light-grey': 'lg',
        'light-blue': 'lb'
    };

    var newSrc = curSrc.replace(/dvo-ran-(lg|lb|lr)\.png$/, 'dvo-ran-' + colorSrc[color] + '.png');
    img.src = newSrc;
}