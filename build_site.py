import os
import shutil
import glob

# Paths
brain_dir = r"C:\Users\User\.gemini\antigravity\brain\45502dd0-97b4-427b-a3c4-e2c3b9d4b136"
web_dir = r"c:\Users\User\Downloads\SEO-20260506T052936Z-3-001\SEO\web4"

os.makedirs(web_dir, exist_ok=True)

# 1. Copy images
image_prefixes = ["logo", "product_1", "product_2", "product_3", "product_4", "product_5"]
image_mapping = {}

for prefix in image_prefixes:
    matches = glob.glob(os.path.join(brain_dir, f"{prefix}_*.png"))
    if matches:
        # Take the most recent if multiple
        matches.sort(reverse=True)
        src = matches[0]
        dst = os.path.join(web_dir, f"{prefix}.png")
        shutil.copy2(src, dst)
        image_mapping[prefix] = f"{prefix}.png"

# Fill missing products 6-16 with existing images (round robin)
available_products = [f"product_{i}" for i in range(1, 6) if f"product_{i}" in image_mapping]

for i in range(6, 17):
    if available_products:
        src_prefix = available_products[(i-6) % len(available_products)]
        src_path = os.path.join(web_dir, f"{src_prefix}.png")
        dst_path = os.path.join(web_dir, f"product_{i}.png")
        if os.path.exists(src_path):
            shutil.copy2(src_path, dst_path)

# Data
products = [
    {"id": 1, "category": "casual", "name": "Casual Summer Dress", "price": "NT$1,500", "image": "product_1.png"},
    {"id": 2, "category": "casual", "name": "Denim Jacket", "price": "NT$2,200", "image": "product_2.png"},
    {"id": 3, "category": "casual", "name": "Comfortable Cotton Tee", "price": "NT$800", "image": "product_3.png"},
    {"id": 4, "category": "casual", "name": "Pleated Skirt", "price": "NT$1,200", "image": "product_4.png"},
    {"id": 5, "category": "formal", "name": "Elegant Evening Gown", "price": "NT$5,000", "image": "product_5.png"},
    {"id": 6, "category": "formal", "name": "Tailored Blazer", "price": "NT$3,500", "image": "product_6.png"},
    {"id": 7, "category": "formal", "name": "Silk Blouse", "price": "NT$2,500", "image": "product_7.png"},
    {"id": 8, "category": "formal", "name": "Classic Pencil Skirt", "price": "NT$1,800", "image": "product_8.png"},
    {"id": 9, "category": "jewelry", "name": "Pearl Necklace", "price": "NT$4,200", "image": "product_9.png"},
    {"id": 10, "category": "jewelry", "name": "Diamond Stud Earrings", "price": "NT$8,500", "image": "product_10.png"},
    {"id": 11, "category": "jewelry", "name": "Gold Bangle", "price": "NT$3,800", "image": "product_11.png"},
    {"id": 12, "category": "accessories", "name": "Leather Handbag", "price": "NT$4,500", "image": "product_12.png"},
    {"id": 13, "category": "accessories", "name": "Silk Scarf", "price": "NT$1,500", "image": "product_13.png"},
    {"id": 14, "category": "accessories", "name": "Designer Sunglasses", "price": "NT$6,000", "image": "product_14.png"},
    {"id": 15, "category": "others", "name": "Fragrance Perfume", "price": "NT$2,800", "image": "product_15.png"},
    {"id": 16, "category": "others", "name": "Makeup Brush Set", "price": "NT$1,800", "image": "product_16.png"},
]

categories = {
    "casual": "休閒服飾 (Casual Wear)",
    "formal": "正式服飾 (Formal Wear)",
    "jewelry": "飾品 (Jewelry)",
    "accessories": "配件 (Accessories)",
    "others": "其它類 (Others)"
}

# HTML Templates
nav_html = """
<header class="navbar">
    <div class="nav-container">
        <a href="index.html" class="logo-link">
            <img src="logo.png" alt="Elegance Logo" class="logo">
        </a>
        <nav>
            <ul class="nav-links">
                <li><a href="index.html">首頁</a></li>
                <li><a href="about.html">公司簡介</a></li>
                <li class="dropdown">
                    <a href="#" class="dropbtn">商品分類 ▼</a>
                    <div class="dropdown-content">
                        <a href="casual.html">休閒服飾</a>
                        <a href="formal.html">正式服飾</a>
                        <a href="jewelry.html">飾品</a>
                        <a href="accessories.html">配件</a>
                        <a href="others.html">其它類</a>
                    </div>
                </li>
                <li><a href="contact.html">聯絡我們</a></li>
            </ul>
        </nav>
    </div>
</header>
"""

footer_html = """
<footer class="footer">
    <div class="footer-content">
        <p>&copy; 2026 Elegance Women's Fashion. All rights reserved.</p>
        <div class="social-links">
            <a href="#">Instagram</a>
            <a href="#">Facebook</a>
            <a href="#">Twitter</a>
        </div>
    </div>
</footer>
"""

base_template = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Elegance</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
</head>
<body>
    {nav}
    <main class="main-content">
        {content}
    </main>
    {footer}
</body>
</html>
"""

def write_html(filename, title, content):
    html = base_template.format(title=title, nav=nav_html, content=content, footer=footer_html)
    with open(os.path.join(web_dir, filename), "w", encoding="utf-8") as f:
        f.write(html)

# CSS
css_content = """
:root {
    --primary-color: #1a1a1a;
    --secondary-color: #d4af37; /* Gold */
    --background-color: #fcfcfc;
    --text-color: #333333;
    --light-text: #777777;
    --font-heading: 'Cormorant Garamond', serif;
    --font-body: 'Montserrat', sans-serif;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: var(--font-body);
    color: var(--text-color);
    background-color: var(--background-color);
    line-height: 1.6;
}

h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading);
    color: var(--primary-color);
    font-weight: 600;
}

/* Navbar */
.navbar {
    background-color: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    padding: 1rem 0;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 2rem;
}

.logo {
    height: 50px;
    width: auto;
    transition: transform 0.3s ease;
}

.logo:hover {
    transform: scale(1.05);
}

.nav-links {
    list-style: none;
    display: flex;
    gap: 2rem;
    align-items: center;
}

.nav-links a {
    text-decoration: none;
    color: var(--primary-color);
    font-weight: 500;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: color 0.3s ease;
}

.nav-links a:hover {
    color: var(--secondary-color);
}

.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: white;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.1);
    z-index: 1;
    border-radius: 4px;
    overflow: hidden;
    top: 100%;
}

.dropdown-content a {
    color: var(--text-color);
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-transform: none;
    font-size: 0.9rem;
    transition: background-color 0.2s, color 0.2s;
}

.dropdown-content a:hover {
    background-color: #f1f1f1;
    color: var(--secondary-color);
}

.dropdown:hover .dropdown-content {
    display: block;
    animation: fadeIn 0.3s;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Main Content */
.main-content {
    min-height: calc(100vh - 160px);
    padding: 3rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 4rem 2rem;
    background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    border-radius: 12px;
    margin-bottom: 4rem;
}

.hero h1 {
    font-size: 3.5rem;
    margin-bottom: 1rem;
}

.hero p {
    font-size: 1.2rem;
    color: var(--light-text);
    max-width: 600px;
    margin: 0 auto;
}

/* Product Grid */
.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 2rem;
}

.product-card {
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    text-align: center;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

.product-image {
    width: 100%;
    height: 350px;
    object-fit: cover;
    border-bottom: 1px solid #eee;
}

.product-info {
    padding: 1.5rem;
}

.product-title {
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
    color: var(--primary-color);
    text-decoration: none;
    display: block;
}

.product-title:hover {
    color: var(--secondary-color);
}

.product-price {
    color: var(--secondary-color);
    font-weight: 600;
    font-size: 1.2rem;
}

/* Product Detail Page */
.product-detail {
    display: flex;
    gap: 4rem;
    align-items: flex-start;
}

.product-detail-image {
    flex: 1;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.product-detail-image img {
    width: 100%;
    height: auto;
    display: block;
}

.product-detail-info {
    flex: 1;
    padding-top: 2rem;
}

.product-detail-info h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.product-detail-info .price {
    font-size: 2rem;
    color: var(--secondary-color);
    font-weight: 600;
    margin-bottom: 2rem;
}

.product-detail-info .description {
    font-size: 1.1rem;
    color: var(--light-text);
    margin-bottom: 2rem;
    line-height: 1.8;
}

.btn {
    display: inline-block;
    background-color: var(--primary-color);
    color: white;
    padding: 1rem 2.5rem;
    text-decoration: none;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-radius: 4px;
    transition: background-color 0.3s ease;
    border: none;
    cursor: pointer;
}

.btn:hover {
    background-color: var(--secondary-color);
}

/* Simple Pages (About, Contact) */
.page-header {
    text-align: center;
    margin-bottom: 3rem;
}

.page-header h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

.contact-form {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    padding: 2.5rem;
    border-radius: 8px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
}

.form-group input, .form-group textarea {
    width: 100%;
    padding: 0.8rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-family: var(--font-body);
}

.form-group textarea {
    height: 150px;
    resize: vertical;
}

/* Footer */
.footer {
    background-color: var(--primary-color);
    color: white;
    padding: 3rem 0;
    text-align: center;
}

.footer-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.social-links {
    margin-top: 1.5rem;
}

.social-links a {
    color: white;
    text-decoration: none;
    margin: 0 1rem;
    transition: color 0.3s ease;
}

.social-links a:hover {
    color: var(--secondary-color);
}

/* Responsive */
@media (max-width: 768px) {
    .nav-container {
        flex-direction: column;
        gap: 1rem;
    }
    .product-detail {
        flex-direction: column;
    }
}
"""
with open(os.path.join(web_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(css_content)

# Generate Home Page
home_content = """
<section class="hero">
    <h1>Discover Your Elegance</h1>
    <p>Explore our new collection of premium women's fashion, designed for the modern, confident woman.</p>
</section>
<h2 style="text-align: center; margin-bottom: 2rem;">Featured Products</h2>
<div class="product-grid">
"""
for p in products[:8]: # Show first 8 products
    home_content += f"""
    <div class="product-card">
        <a href="product_{p['id']}.html">
            <img src="{p['image']}" alt="{p['name']}" class="product-image">
        </a>
        <div class="product-info">
            <a href="product_{p['id']}.html" class="product-title">{p['name']}</a>
            <div class="product-price">{p['price']}</div>
        </div>
    </div>
    """
home_content += "</div>"
write_html("index.html", "首頁", home_content)

# Generate Category Pages
for cat_key, cat_name in categories.items():
    cat_products = [p for p in products if p['category'] == cat_key]
    cat_content = f"""
    <div class="page-header">
        <h1>{cat_name}</h1>
        <p>Explore our exclusive collection of {cat_name.split(' (')[0]}.</p>
    </div>
    <div class="product-grid">
    """
    for p in cat_products:
        cat_content += f"""
        <div class="product-card">
            <a href="product_{p['id']}.html">
                <img src="{p['image']}" alt="{p['name']}" class="product-image">
            </a>
            <div class="product-info">
                <a href="product_{p['id']}.html" class="product-title">{p['name']}</a>
                <div class="product-price">{p['price']}</div>
            </div>
        </div>
        """
    cat_content += "</div>"
    write_html(f"{cat_key}.html", cat_name, cat_content)

# Generate Product Pages
for p in products:
    p_content = f"""
    <div class="product-detail">
        <div class="product-detail-image">
            <img src="{p['image']}" alt="{p['name']}">
        </div>
        <div class="product-detail-info">
            <a href="{p['category']}.html" style="color: var(--light-text); text-decoration: none; text-transform: uppercase; font-size: 0.9rem; letter-spacing: 1px;">{categories[p['category']].split(' (')[0]}</a>
            <h1>{p['name']}</h1>
            <div class="price">{p['price']}</div>
            <p class="description">
                Experience the perfect blend of comfort and style with our {p['name']}. Carefully crafted with premium materials to ensure you look and feel your best. Perfect for any occasion, this piece is a must-have addition to your wardrobe.
            </p>
            <button class="btn" onclick="alert('Item added to cart!')">加入購物車 (Add to Cart)</button>
        </div>
    </div>
    """
    write_html(f"product_{p['id']}.html", p['name'], p_content)

# Generate About Us
about_content = """
<div class="page-header">
    <h1>關於我們 (About Us)</h1>
</div>
<div style="max-width: 800px; margin: 0 auto; text-align: center;">
    <p style="font-size: 1.2rem; margin-bottom: 2rem;">Welcome to Elegance, your number one source for premium women's fashion.</p>
    <p style="color: var(--light-text); margin-bottom: 1.5rem;">We're dedicated to giving you the very best of clothing, with a focus on quality, customer service, and uniqueness. Founded in 2026, Elegance has come a long way from its beginnings. When we first started out, our passion for helping women find their perfect style drove us to do intense research and gave us the impetus to turn hard work and inspiration into to a booming online store.</p>
    <p style="color: var(--light-text);">We hope you enjoy our products as much as we enjoy offering them to you. If you have any questions or comments, please don't hesitate to contact us.</p>
</div>
"""
write_html("about.html", "公司簡介", about_content)

# Generate Contact Us
contact_content = """
<div class="page-header">
    <h1>聯絡我們 (Contact Us)</h1>
    <p>We'd love to hear from you. Send us a message and we'll respond as soon as possible.</p>
</div>
<div class="contact-form">
    <form onsubmit="event.preventDefault(); alert('Message sent successfully!');">
        <div class="form-group">
            <label for="name">姓名 (Name)</label>
            <input type="text" id="name" required>
        </div>
        <div class="form-group">
            <label for="email">電子郵件 (Email)</label>
            <input type="email" id="email" required>
        </div>
        <div class="form-group">
            <label for="message">訊息 (Message)</label>
            <textarea id="message" required></textarea>
        </div>
        <button type="submit" class="btn" style="width: 100%;">送出 (Submit)</button>
    </form>
</div>
"""
write_html("contact.html", "聯絡我們", contact_content)

print("Website generated successfully!")
