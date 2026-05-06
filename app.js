const products = [
    {id: 1, category: "casual", name: "Casual Summer Dress", price: "NT$1,500", image: "product_1.png"},
    {id: 2, category: "casual", name: "Denim Jacket", price: "NT$2,200", image: "product_2.png"},
    {id: 3, category: "casual", name: "Comfortable Cotton Tee", price: "NT$800", image: "product_3.png"},
    {id: 4, category: "casual", name: "Pleated Skirt", price: "NT$1,200", image: "product_4.png"},
    {id: 5, category: "formal", name: "Elegant Evening Gown", price: "NT$5,000", image: "product_5.png"},
    {id: 6, category: "formal", name: "Tailored Blazer", price: "NT$3,500", image: "product_6.png"},
    {id: 7, category: "formal", name: "Silk Blouse", price: "NT$2,500", image: "product_7.png"},
    {id: 8, category: "formal", name: "Classic Pencil Skirt", price: "NT$1,800", image: "product_8.png"},
    {id: 9, category: "jewelry", name: "Pearl Necklace", price: "NT$4,200", image: "product_9.png"},
    {id: 10, category: "jewelry", name: "Diamond Stud Earrings", price: "NT$8,500", image: "product_10.png"},
    {id: 11, category: "jewelry", name: "Gold Bangle", price: "NT$3,800", image: "product_11.png"},
    {id: 12, category: "accessories", name: "Leather Handbag", price: "NT$4,500", image: "product_12.png"},
    {id: 13, category: "accessories", name: "Silk Scarf", price: "NT$1,500", image: "product_13.png"},
    {id: 14, category: "accessories", name: "Designer Sunglasses", price: "NT$6,000", image: "product_14.png"},
    {id: 15, category: "others", name: "Fragrance Perfume", price: "NT$2,800", image: "product_15.png"},
    {id: 16, category: "others", name: "Makeup Brush Set", price: "NT$1,800", image: "product_16.png"},
];

const categoryNames = {
    casual: "休閒服飾",
    formal: "正式服飾",
    jewelry: "飾品",
    accessories: "配件",
    others: "其它類"
};

const appContent = document.getElementById('app-content');

function renderProductCard(p) {
    return `
        <div class="product-card">
            <a href="#product/${p.id}">
                <div class="product-image-container">
                    <img src="${p.image}" alt="${p.name}" class="product-image">
                </div>
            </a>
            <div class="product-info">
                <span class="product-category-label">${categoryNames[p.category]}</span>
                <a href="#product/${p.id}" class="product-title">${p.name}</a>
                <div class="product-price">${p.price}</div>
            </div>
        </div>
    `;
}

function renderHome() {
    let html = `
        <section class="hero">
            <h1>Discover Your Elegance</h1>
            <p>Explore our new collection of premium women's fashion, designed for the modern, confident woman.</p>
            <a href="#categories" class="btn">Shop Now</a>
        </section>
        <h2 class="section-title">Featured Products</h2>
        <div class="product-grid">
    `;
    products.slice(0, 8).forEach(p => {
        html += renderProductCard(p);
    });
    html += `</div>`;
    appContent.innerHTML = html;
    document.title = "首頁 | Elegance";
}

function renderAbout() {
    appContent.innerHTML = `
        <div class="page-header">
            <h1>關於我們 (About Us)</h1>
            <p>Our story and mission</p>
        </div>
        <div class="about-content">
            <p style="font-size: 1.3rem; color: var(--primary-color); font-weight: 500;">Welcome to Elegance, your number one source for premium women's fashion.</p>
            <p>We're dedicated to giving you the very best of clothing, with a focus on quality, customer service, and uniqueness. Founded in 2026, Elegance has come a long way from its beginnings. When we first started out, our passion for helping women find their perfect style drove us to do intense research and gave us the impetus to turn hard work and inspiration into to a booming online store.</p>
            <p>We hope you enjoy our products as much as we enjoy offering them to you. If you have any questions or comments, please don't hesitate to contact us.</p>
        </div>
    `;
    document.title = "公司簡介 | Elegance";
}

function renderContact() {
    appContent.innerHTML = `
        <div class="page-header">
            <h1>聯絡我們 (Contact Us)</h1>
            <p>We'd love to hear from you. Send us a message and we'll respond as soon as possible.</p>
        </div>
        <div class="contact-form">
            <form onsubmit="event.preventDefault(); alert('Message sent successfully!');">
                <div class="form-group">
                    <label for="name">姓名 (Name)</label>
                    <input type="text" id="name" required placeholder="Your full name">
                </div>
                <div class="form-group">
                    <label for="email">電子郵件 (Email)</label>
                    <input type="email" id="email" required placeholder="Your email address">
                </div>
                <div class="form-group">
                    <label for="message">訊息 (Message)</label>
                    <textarea id="message" required placeholder="How can we help you?"></textarea>
                </div>
                <button type="submit" class="btn" style="width: 100%;">送出 (Submit)</button>
            </form>
        </div>
    `;
    document.title = "聯絡我們 | Elegance";
}

function renderCategory(category) {
    const catName = categoryNames[category] || "商品";
    const catProducts = products.filter(p => p.category === category);
    
    let html = `
        <div class="page-header">
            <h1>${catName}</h1>
            <p>Explore our exclusive collection of ${catName}.</p>
        </div>
        <div class="product-grid">
    `;
    catProducts.forEach(p => {
        html += renderProductCard(p);
    });
    html += `</div>`;
    appContent.innerHTML = html;
    document.title = `${catName} | Elegance`;
}

function renderCategories() {
    let html = `
        <div class="page-header">
            <h1>商品分類</h1>
            <p>Browse all our categories.</p>
        </div>
        <div class="product-grid">
    `;
    products.forEach(p => {
        html += renderProductCard(p);
    });
    html += `</div>`;
    appContent.innerHTML = html;
    document.title = `商品分類 | Elegance`;
}

function renderProduct(id) {
    const p = products.find(prod => prod.id == id);
    if (!p) {
        appContent.innerHTML = `<h1 style="text-align:center; padding: 5rem;">Product not found</h1>`;
        return;
    }
    
    appContent.innerHTML = `
        <div class="product-detail">
            <div class="product-detail-image">
                <img src="${p.image}" alt="${p.name}">
            </div>
            <div class="product-detail-info">
                <a href="#category/${p.category}" class="product-category-label" style="text-decoration:none; margin-bottom: 1rem;">${categoryNames[p.category]}</a>
                <h1>${p.name}</h1>
                <div class="price">${p.price}</div>
                <p class="description">
                    Experience the perfect blend of comfort and style with our ${p.name}. Carefully crafted with premium materials to ensure you look and feel your best. Perfect for any occasion, this piece is a must-have addition to your wardrobe. Elevate your everyday style effortlessly.
                </p>
                <button class="btn" onclick="alert('Item added to cart!')">加入購物車 (Add to Cart)</button>
            </div>
        </div>
    `;
    document.title = `${p.name} | Elegance`;
}

function handleRoute() {
    const hash = window.location.hash.substring(1);
    window.scrollTo(0, 0); // Scroll to top on route change

    if (!hash || hash === 'home') {
        renderHome();
    } else if (hash === 'about') {
        renderAbout();
    } else if (hash === 'contact') {
        renderContact();
    } else if (hash === 'categories') {
        renderCategories();
    } else if (hash.startsWith('category/')) {
        const cat = hash.split('/')[1];
        renderCategory(cat);
    } else if (hash.startsWith('product/')) {
        const id = hash.split('/')[1];
        renderProduct(id);
    } else {
        renderHome();
    }
}

window.addEventListener('hashchange', handleRoute);
window.addEventListener('DOMContentLoaded', handleRoute);
