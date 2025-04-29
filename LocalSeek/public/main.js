// Sample data
const categories = [
    {
        id: 1,
        name: "Electronics",
        icon: "fa-laptop",
        image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
    },
    {
        id: 2,
        name: "Fashion",
        icon: "fa-tshirt",
        image: "https://images.unsplash.com/photo-1529634885322-b17ffaf423ac"
    },
    {
        id: 3,
        name: "Home & Living",
        icon: "fa-home",
        image: "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d"
    }
];

const products = [
    {
        id: 1,
        name: "Wireless Headphones",
        price: 79.99,
        description: "High-quality wireless headphones with noise cancellation",
        image: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e"
    },
    {
        id: 2,
        name: "Smart Watch",
        price: 199.99,
        description: "Modern smartwatch with health tracking features",
        image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
    },
    {
        id: 3,
        name: "Designer T-Shirt",
        price: 29.99,
        description: "Comfortable cotton t-shirt with modern design",
        image: "https://images.unsplash.com/photo-1509695507497-903c140c43b0"
    }
];

// Load categories
function loadCategories() {
    const container = document.getElementById('categories-container');
    categories.forEach(category => {
        const categoryHtml = `
            <div class="col-md-4">
                <div class="card h-100 category-card">
                    <img src="${category.image}" class="card-img-top product-image" alt="${category.name}">
                    <div class="card-body text-center">
                        <i class="fas ${category.icon} category-icon"></i>
                        <h5 class="card-title">${category.name}</h5>
                    </div>
                </div>
            </div>
        `;
        container.innerHTML += categoryHtml;
    });
}

// Load products
function loadProducts() {
    const container = document.getElementById('products-container');
    products.forEach(product => {
        const productHtml = `
            <div class="col-md-4">
                <div class="card h-100 product-card">
                    <img src="${product.image}" class="card-img-top product-image" alt="${product.name}">
                    <div class="card-body">
                        <h5 class="card-title">${product.name}</h5>
                        <p class="card-text">$${product.price.toFixed(2)}</p>
                        <button class="btn btn-primary view-stores" data-product-id="${product.id}">View Stores</button>
                    </div>
                </div>
            </div>
        `;
        container.innerHTML += productHtml;
    });
}

// Handle search
document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const query = this.querySelector('input[name="q"]').value.toLowerCase();
    const container = document.getElementById('products-container');
    container.innerHTML = '';
    
    const filteredProducts = products.filter(product => 
        product.name.toLowerCase().includes(query) || 
        product.description.toLowerCase().includes(query)
    );
    
    if (filteredProducts.length === 0) {
        container.innerHTML = '<div class="col-12 text-center"><p class="lead">No products found matching your search.</p></div>';
    } else {
        filteredProducts.forEach(product => {
            const productHtml = `
                <div class="col-md-4">
                    <div class="card h-100 product-card">
                        <img src="${product.image}" class="card-img-top product-image" alt="${product.name}">
                        <div class="card-body">
                            <h5 class="card-title">${product.name}</h5>
                            <p class="card-text">$${product.price.toFixed(2)}</p>
                            <button class="btn btn-primary view-stores" data-product-id="${product.id}">View Stores</button>
                        </div>
                    </div>
                </div>
            `;
            container.innerHTML += productHtml;
        });
    }
});

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    loadCategories();
    loadProducts();
});
