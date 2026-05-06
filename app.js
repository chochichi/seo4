const products = [
    {id: 1, category: "casual", name: "休閒夏日洋裝", price: "NT$1,500", image: "product_1.png"},
    {id: 2, category: "casual", name: "經典牛仔外套", price: "NT$2,200", image: "product_2.png"},
    {id: 3, category: "casual", name: "舒適純棉 T 恤", price: "NT$800", image: "product_3.png"},
    {id: 4, category: "casual", name: "優雅百褶裙", price: "NT$1,200", image: "product_4.png"},
    {id: 5, category: "formal", name: "優雅晚禮服", price: "NT$5,000", image: "product_5.png"},
    {id: 6, category: "formal", name: "剪裁西裝外套", price: "NT$3,500", image: "product_6.png"},
    {id: 7, category: "formal", name: "絲綢襯衫", price: "NT$2,500", image: "product_7.png"},
    {id: 8, category: "formal", name: "經典鉛筆裙", price: "NT$1,800", image: "product_8.png"},
    {id: 9, category: "jewelry", name: "珍珠項鍊", price: "NT$4,200", image: "product_9.png"},
    {id: 10, category: "jewelry", name: "鑽石耳釘", price: "NT$8,500", image: "product_10.png"},
    {id: 11, category: "jewelry", name: "黃金手環", price: "NT$3,800", image: "product_11.png"},
    {id: 12, category: "accessories", name: "真皮手提包", price: "NT$4,500", image: "product_12.png"},
    {id: 13, category: "accessories", name: "絲綢圍巾", price: "NT$1,500", image: "product_13.png"},
    {id: 14, category: "accessories", name: "設計師墨鏡", price: "NT$6,000", image: "product_14.png"},
    {id: 15, category: "others", name: "精緻香水", price: "NT$2,800", image: "product_15.png"},
    {id: 16, category: "others", name: "專業刷具組", price: "NT$1,800", image: "product_16.png"},
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
            <h1>探索妳的優雅</h1>
            <p>探索我們全新的頂級女性服飾系列，專為現代且自信的女性設計。</p>
            <a href="#categories" class="btn">立即選購</a>
        </section>
        <h2 class="section-title">精選商品</h2>
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
            <h1>關於我們</h1>
            <p>我們的故事與使命</p>
        </div>
        <div class="about-content">
            <p style="font-size: 1.3rem; color: var(--primary-color); font-weight: 500;">歡迎來到 Elegance，您頂級女性服飾的首選。</p>
            <p>我們致力於為您提供最好的服飾，專注於品質、客戶服務與獨特性。Elegance 成立於 2026 年，從最初的起步已經走過了很長的路。當我們剛起步時，我們對於幫助女性找到完美風格的熱情，驅使我們進行深入的研究，並讓我們有動力將辛勤工作與靈感轉化為蓬勃發展的線上商店。</p>
            <p>我們希望您喜歡我們的產品，就像我們喜歡將它們提供給您一樣。如果您有任何問題或意見，請隨時與我們聯絡。</p>
        </div>
    `;
    document.title = "公司簡介 | Elegance";
}

function renderContact() {
    appContent.innerHTML = `
        <div class="page-header">
            <h1>聯絡我們</h1>
            <p>我們很樂意聽取您的意見。發送訊息給我們，我們將盡快回覆。</p>
        </div>
        <div class="contact-form">
            <form onsubmit="event.preventDefault(); alert('訊息已成功送出！');">
                <div class="form-group">
                    <label for="name">姓名</label>
                    <input type="text" id="name" required placeholder="您的全名">
                </div>
                <div class="form-group">
                    <label for="email">電子郵件</label>
                    <input type="email" id="email" required placeholder="您的電子郵件地址">
                </div>
                <div class="form-group">
                    <label for="message">訊息</label>
                    <textarea id="message" required placeholder="我們能如何幫助您？"></textarea>
                </div>
                <button type="submit" class="btn" style="width: 100%;">送出</button>
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
            <p>探索我們獨家的 ${catName} 系列。</p>
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
            <p>瀏覽我們所有的分類。</p>
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
        appContent.innerHTML = `<h1 style="text-align:center; padding: 5rem;">找不到商品</h1>`;
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
                    透過我們的 ${p.name} 體驗舒適與風格的完美結合。採用優質材料精心製作，確保您展現最佳狀態並感到舒適。無論任何場合都非常適合，這是您衣櫃中必備的單品。輕鬆提升您的日常風格。
                </p>
                <button class="btn" onclick="alert('已將商品加入購物車！')">加入購物車</button>
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
