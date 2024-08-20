document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');
    const userNavItem = document.getElementById('user');

    // Check if the user is already signed up
    const signedUpUsername = localStorage.getItem('signupUsername');
    if (signedUpUsername) {
        const navbar = document.getElementById('navbar');
        const loginNavItem = navbar.querySelector('li:last-child');
        loginNavItem.innerHTML = `Welcome, ${signedUpUsername}!`;
    }

    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form submission

            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Retrieve signup data from localStorage
            const storedUsername = localStorage.getItem('signupUsername');
            const storedPassword = localStorage.getItem('signupPassword');

            if (username === storedUsername && password === storedPassword) {
                // Store login data in localStorage
                localStorage.setItem('username', username);

                // Redirect to the home page or perform other actions
                window.location.href = 'index.html';
            } else {
                alert('Invalid username or password');
            }
        });
    }

    if (signupForm) {
        signupForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form submission

            const signupUsername = document.getElementById('signupUsername').value;
            const email = document.getElementById('email').value;
            const signupPassword = document.getElementById('signupPassword').value;

            // Store signup data in localStorage
            localStorage.setItem('signupUsername', signupUsername);
            localStorage.setItem('email', email);
            localStorage.setItem('signupPassword', signupPassword);

            // Display confirmation message
            const confirmationMessage = document.createElement('p');
            confirmationMessage.textContent = 'Your account has been created!';
            confirmationMessage.style.color = 'green';
            signupForm.parentNode.insertBefore(confirmationMessage, signupForm.nextSibling);

            // Display the signed-up username in the navbar
            const navbar = document.getElementById('navbar');
            const loginNavItem = navbar.querySelector('li:last-child');
            loginNavItem.innerHTML = `Welcome, ${signupUsername}!`;

            // Redirect to the home page or perform other actions
            setTimeout(function () {
                window.location.href = 'index.html';
            }, 2000); // 5000 milliseconds (5 seconds) delay
        });
    }

    // Event listener for adding products to the cart
    const addToCartButtons = document.querySelectorAll('.fa-cart-shopping');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent default action

            // Retrieve product details from the clicked product element
            const productContainer = event.target.closest('.pro');
            const productName = productContainer.querySelector('.des h5').textContent;
            const productPrice = productContainer.querySelector('.des h4').textContent;
            const productImage = productContainer.querySelector('img').src;

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

    // Check if user is logged in and display username in the navbar
    const username = localStorage.getItem('username');
    if (username) {
        userNavItem.innerHTML = `Welcome, ${username}! <a href="#" id="logout">Logout</a>`;
        const logoutButton = document.getElementById('logout');
        logoutButton.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default link behavior
            localStorage.removeItem('username'); // Clear the stored username
            userNavItem.innerHTML = '<a href="login.html">Login</a>'; // Update navbar to display login link
        });
    } else {
        userNavItem.innerHTML = '<a href="login.html">Login</a>'; // Display login link if no user is logged in
    }
});
