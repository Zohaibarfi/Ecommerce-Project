document.addEventListener('DOMContentLoaded', function () {
    // Retrieve existing cart items from localStorage
    let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

    // Select the cart items container and total element
    const cartItemsContainer = document.getElementById('cart-items');
    const totalPriceElement = document.getElementById('total-price');
    const cartSubtotalElement = document.getElementById('cart-subtotal'); // Add this line

    // Function to create a product row HTML based on product data
    function createProductRow(product, index) {
        const row = document.createElement('tr');

        // Create cells for each column
        const removeCell = document.createElement('td');
        const imageCell = document.createElement('td');
        const productCell = document.createElement('td');
        const priceCell = document.createElement('td');
        const quantityCell = document.createElement('td');
        const subtotalCell = document.createElement('td');

        // Add content to cells
        const removeButton = document.createElement('button');
        removeButton.textContent = 'Remove';
        removeButton.addEventListener('click', function() {
            removeProduct(index);
        });
        removeCell.appendChild(removeButton);

        imageCell.innerHTML = `<img src="${product.image}" alt="Product Image">`;
        productCell.textContent = product.name;
        priceCell.textContent = product.price; // Set price text content
        var price = product.price.split('.')[1];
        priceCell.dataset.price = product.price; // Set data-price attribute
        quantityCell.textContent = 1; // For now, assuming quantity is always 1
        subtotalCell.textContent = calculateSubtotal(Number(price), 1); // Calculate subtotal

        // Append cells to the row
        row.appendChild(removeCell);
        row.appendChild(imageCell);
        row.appendChild(productCell);
        row.appendChild(priceCell);
        row.appendChild(quantityCell);
        row.appendChild(subtotalCell);

        return row;
    }

    // Calculate subtotal
    function calculateSubtotal(price, quantity) {
        return price * quantity;
    }

    // Remove product from cart
    function removeProduct(index) {
        cartItems.splice(index, 1);
        localStorage.setItem('cartItems', JSON.stringify(cartItems));
        renderCartItems();
    }

    // Render cart items
    function renderCartItems() {
        cartItemsContainer.innerHTML = ''; // Clear existing items
        let totalPrice = 0;
        cartItems.forEach((product, index) => {
            const productRow = createProductRow(product, index);
            cartItemsContainer.appendChild(productRow);
            var price = product.price.split('.')[1];
            totalPrice += calculateSubtotal(Number(price), 1);
        });
    
        totalPriceElement.textContent = 'Rs.' + totalPrice.toFixed(2); // Update total price
        cartSubtotalElement.textContent = 'Rs.' + totalPrice.toFixed(2);
    }

    // Initial rendering
    renderCartItems();
});
