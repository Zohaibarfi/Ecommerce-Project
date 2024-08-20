document.addEventListener('DOMContentLoaded', function () {
    const userNavItem = document.getElementById('user');
    const username = localStorage.getItem('username');

    if (username) {
        userNavItem.innerHTML = `Welcome, ${username}! <a href="#" id="logout">Logout</a>`;
        const logoutButton = document.getElementById('logout');
        logoutButton.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default link behavior
            localStorage.removeItem('username'); // Clear the stored username
            localStorage.removeItem('cartItems');
            location.reload()

            userNavItem.innerHTML = '<a href="login.html">Login</a>'; // Update navbar to display login link
            removeProduct();
        });
    } else {
        userNavItem.innerHTML = '<a href="login.html">Login</a>'; // Display login link if no user is logged in
    }

    // Add event listener for adding product to cart in index.html
    const addToCartIcons = document.querySelectorAll('.fa-cart-shopping');
    addToCartIcons.forEach(icon => {
        icon.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default link behavior
            const productContainer = icon.closest('.product'); // Update the class name to match your HTML structure
            const productName = productContainer.querySelector('td:nth-child(3)').innerText; // Adjust the selector based on your HTML structure
            const productPrice = productContainer.querySelector('td:nth-child(4)').innerText; // Adjust the selector based on your HTML structure
            const productImage = productContainer.querySelector('img').getAttribute('src');

            // Create an object to store the product details
            const product = {
                name: productName,
                price: productPrice,
                image: productImage
            };

            // Retrieve existing cart items from localStorage
            let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

            // Add the product to the cart
            cartItems.push(product);

            // Update the cart items in localStorage
            localStorage.setItem('cartItems', JSON.stringify(cartItems));

            // Optionally, you can display a message or perform other actions to indicate that the product has been added to the cart
            alert('Product added to cart!');
        });
    });
});
