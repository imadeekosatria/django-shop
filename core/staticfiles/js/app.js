const menuBtn = document.getElementById('menu-toggle');

menuBtn.addEventListener('click', ()=>{
    const menu = document.getElementById('menu');
    menu.classList.toggle('hidden');
});

const langBtn = document.getElementById('lang-toggle');

langBtn.addEventListener('click', ()=>{
    const lang = document.getElementById('lang');

    lang.classList.toggle('hidden');
});

// const accountBtn = document.getElementById('accountBtn');

// accountBtn.addEventListener('click', ()=>{
//     const account = document.getElementById('account');

//     if (account.classList.contains('flex')) {
//         account.classList.replace('flex','hidden');
//     }else{
//         account.classList.replace('hidden','flex');
//     }
// });

// const closeModalBtn = document.getElementById('closeModalBtn');

// closeModalBtn.addEventListener('click', () =>{
//     const productModal = document.getElementById('productModal');

//     productModal.classList.replace('flex', 'hidden');
// });

// const loveSVG = document.querySelector('.love-svg');

// loveSVG.addEventListener('click', ()=>{
//     loveSVG.classList.replace('text-gray-500', 'text-red-500');
// });

window.addEventListener('scroll', ()=>{
    const topBtn = document.getElementById('to-top');
    if (window.pageYOffset > 100) {
        topBtn.classList.remove('hidden');
    }else {
        topBtn.classList.add('hidden');
    }
});

const price = document.querySelectorAll('.price');
price.forEach(element => {
    const text = element.textContent;
    element.innerHTML = new Intl.NumberFormat('id-ID',{style: 'currency', currency:'IDR', minimumFractionDigits: 0}).format(text);
});

// Detail Page


if (window.location.pathname.startsWith('/detail')) {
    const shareBtn = document.getElementById('share');
    shareBtn.addEventListener('click', () => {
        const shareData = {
            title: document.getElementById('title').innerText,
            text: document.getElementById('title').innerText + ' ' + document.getElementById('price').innerText,
            url: window.location.href,
        };

        try{
            navigator.share(shareData);
        }catch(err){
            console.log(err);
        }
    });

}

const contact = async ()=>{
    const url = window.location.protocol+'//'+window.location.host+'/'+'contact';
    const response = await fetch(url, {method: 'GET'});
    const data = await response.json();
    console.log(data);
};


if (window.location.pathname.startsWith('/')) {
    const loadBtn = document.getElementById('loadBtn');
    
    loadBtn.addEventListener('click', async ()=>{
        const url = loadBtn.getAttribute('data-next');
        const loader = document.getElementById('loader');
        const baseUrl = window.location.protocol+'//'+window.location.host+'/'+url;
        loader.classList.toggle('hidden');
        loadBtn.classList.toggle('hidden');
        

        await fetch(baseUrl).then((response)=>response.json())
            .then((response)=>{
                const data = response.success
                const container = document.getElementById('beforeBtn');
                for (key in data) {
                    // console.log(data[key].nama);
                    const el = `<div class="w-full md:w-1/3 xl:w-1/4 p-6 flex flex-col">
                                    <a href="detail/${data[key].slug}">
                                        <img class="hover:grow hover:shadow-lg object-cover w-52 h-52" src="${data[key].gambar}" alt="${data[key].nama}">
                                        
                                        
                                        <div class="pt-3 flex items-center justify-between">
                                            <p class="">${data[key].nama}</p>
                                        </div>
                                        <p class="pt-1 text-gray-900 price">${data[key].harga}</p>
                                    </a>
                                </div>`;
                    container.insertAdjacentHTML('beforebegin', el);
                }
                if (response.next === 'last page') {
                    loadBtn.classList.toggle('hidden');

                }else{
                    loadBtn.setAttribute('data-next',response.next)
                }
            });
        loader.classList.toggle('hidden');
        loadBtn.classList.toggle('hidden');
    });
}

