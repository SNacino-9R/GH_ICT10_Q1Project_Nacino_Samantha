from pyscript import document

def make_order(event):
    name = document.getElementById("cust_name").value
    address = document.getElementById("cust_address").value
    contact = document.getElementById("cust_contact").value

    total = 0
    orders = []

    if document.getElementById("angus_steak").checked:
        orders.append("Angus Steak")
        total += 499
    if document.getElementById("crispy_chicken_wings").checked:
        orders.append("Crispy Chicken Wings")
        total += 399
    if document.getElementById("creme_brulee").checked:
        orders.append("Crème Brûlée")
        total += 199
    if document.getElementById("meat_platter").checked:
        orders.append("Meat Platter")
        total += 599

    if not orders:
        order_text = "No items selected."
    else:
        order_text = ", ".join(orders)

    result = f"""
    <div class="p-3 border rounded bg-white shadow-sm">
        <h4>Order Summary</h4>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Address:</strong> {address}</p>
        <p><strong>Contact:</strong> {contact}</p>
        <p><strong>Items:</strong> {order_text}</p>
        <p><strong>Total:</strong> ₱{total:.2f}</p>
        <p class="text-success"><strong>Thank you for ordering from Aromata!</strong></p>
    </div>
    """

    document.getElementById("output").innerHTML = result
