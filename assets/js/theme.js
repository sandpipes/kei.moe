
var currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : 'light';
if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);

    if (currentTheme === 'light') {
        switchToLight(true);
    }
} else if(window.matchMedia) {
    if(window.matchMedia('(prefers-color-scheme: dark)').matches)
        currentTheme === 'dark';
    else 
        currentTheme === 'light';
}

changeBootstrapClass(currentTheme);

document.getElementById("themeToggle").addEventListener("click", function(){
    if(currentTheme === 'dark') {
        switchToLight(false);
        currentTheme = 'light';
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
    } else {
        switchToDark();
        currentTheme = 'dark';
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    }
});

function switchToLight(delayed) {
    changeBootstrapClass('light');
    var dur = 150;
    if(delayed)
        dur = dur2 = dur3 = 0;

    anime({
        targets: '#themeToggle',
        color: '#000000',
        easing: 'linear',
        duration: dur
    });

    anime({
        targets: '#innerCircle',
        r: 5,
        cx: 30,
        cy: 0,
        easing: 'linear',
        duration: dur
    });

    anime({
        targets: '#actualCircle',
        r: 5,
        easing: 'linear',
        fill: '#000000',
        duration: dur
    });

    anime({
        targets: '#sunDashes > line',
        opacity: 1,
        duration: dur,
        easing: 'linear'
    });

    anime({
        targets: 'svg',
        rotate: 90,
        duration: dur,
        easing: 'linear'
    });
}

function switchToDark() {
    changeBootstrapClass('dark');
    anime({
        targets: '#themeToggle',
        color: '#ffd600',
        easing: 'linear',
        duration: 150,
    });

    anime({
        targets: '#innerCircle',
        r: 9,
        cx: 12,
        cy: 4,
        easing: 'linear',
        duration: 150
    });

    anime({
        targets: '#actualCircle',
        r: 9,
        easing: 'linear',
        fill: '#ffd600',
        duration: 150
    });

    anime({
        targets: '#sunDashes > line',
        opacity: 0,
        duration: 150,
        easing: 'linear'
    });

    anime({
        targets: 'svg',
        rotate: 40,
        duration: 150,
        easing: 'linear'
    });
}

function changeBootstrapClass(theme) {
    var $navbar = $("nav");
    if(theme === 'light') {
        if($navbar.hasClass("navbar-dark")) {
            $("nav").removeClass("navbar-dark");
            $("nav").addClass("navbar-light");
        }
    } else {
        if($navbar.hasClass("navbar-light")) {
            $("nav").removeClass("navbar-light");
            $("nav").addClass("navbar-dark");
        }
    }
}
