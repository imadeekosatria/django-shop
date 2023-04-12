var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

// Change the icons inside the button based on previous settings
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    themeToggleLightIcon.classList.remove('hidden');
} else {
    themeToggleDarkIcon.classList.remove('hidden');
}

var themeToggleBtn = document.getElementById('theme-toggle');

themeToggleBtn.addEventListener('click', function() {

    // toggle icons inside button
    themeToggleDarkIcon.classList.toggle('hidden');
    themeToggleLightIcon.classList.toggle('hidden');

    // if set via local storage previously
    if (localStorage.getItem('color-theme')) {
        if (localStorage.getItem('color-theme') === 'light') {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        }

    // if NOT set via local storage previously
    } else {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        }
    }
    
});

if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
} else {
    document.documentElement.classList.remove('dark')
}

if (window.location.pathname === '/members/page') {
    const delete_profile = document.getElementById('delete_profile').getAttribute('data-toko-id');
    const yesBtn = document.getElementById('yes_del_profile');
    yesBtn.addEventListener('click', () =>{
        window.location.href = window.location.protocol + '//' + window.location.host+ '/members/profile/'+delete_profile;
    });
    // console.log('delete_profile');
}

if (window.location.pathname === '/members/products') {
    const del_product = document.querySelectorAll('.del_product');
    
    del_product.forEach((item) => {
        item.addEventListener('click', () =>{
            const url = item.getAttribute('data-href')
            const yesBtn = document.getElementById('yesBtn');
            yesBtn.addEventListener('click', () =>{
                window.location.href = url;
            });
        });
    });
}

const price = document.querySelectorAll('.price');
price.forEach(element => {
    const text = element.textContent;
    element.innerHTML = new Intl.NumberFormat('id-ID',{style: 'currency', currency:'IDR', minimumFractionDigits: 0}).format(text);
});
