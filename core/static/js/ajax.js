const product_visit = async (slug) => {
    const url = window.location.protocol+'//'+window.location.host+'/'+'visitor/'+slug;
    const response = await fetch(url, {method: 'GET'});
    const data = await response.json();
    console.log(data);
}

if (window.location.pathname.startsWith('/detail')) {
    const pathArray = window.location.pathname.split("/");
    product_visit(pathArray[2])
}



