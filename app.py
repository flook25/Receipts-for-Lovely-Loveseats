import streamlit as st
from io import BytesIO, StringIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Page Configuration
st.set_page_config(page_title="Lovely Loveseats Store", layout="wide")

# Initialize cart in session state
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Product Catalog
catalog = {
    "Loveseat": {
        "price": 300,
        "img": "https://cdn-icons-png.flaticon.com/128/2123/2123765.png",
        "desc": "Comfortable 2-seater sofa."
    },
    "Armchair": {
        "price": 150,
        "img": "https://cdn-icons-png.flaticon.com/128/1606/1606478.png",
        "desc": "Cozy single-seat armchair."
    },
    "Coffee Table": {
        "price": 120,
        "img": "https://cdn-icons-png.flaticon.com/128/2007/2007904.png",
        "desc": "Stylish wooden coffee table."
    },
    "Bookshelf": {
        "price": 200,
        "img": "https://cdn-icons-png.flaticon.com/128/1133/1133864.png",
        "desc": "Spacious bookshelf for your books."
    },
    "Floor Lamp": {
        "price": 80,
        "img": "https://cdn-icons-png.flaticon.com/128/5445/5445890.png",
        "desc": "Elegant floor lamp with warm light."
    },
}

def update_qty(item_name: str):
    qty = int(st.session_state.get(f"qty_{item_name}", 0))
    if qty > 0:
        st.session_state.cart[item_name] = qty
    else:
        st.session_state.cart.pop(item_name, None)

def display_product_card(item_name: str, item_data: dict):
    """Renders a product card UI element with selection."""
    st.image(item_data["img"], width=150)
    st.markdown(f"### {item_name}")
    st.markdown(f"**Price:** ${item_data['price']}")
    st.markdown(f"*{item_data['desc']}*")
    st.number_input(
        label="Quantity",
        min_value=0,
        max_value=10,
        value=int(st.session_state.cart.get(item_name, 0)),
        step=1,
        key=f"qty_{item_name}",
        on_change=update_qty,
        args=(item_name,)
    )

def clear_cart():
    """Clears the shopping cart and resets quantities."""
    st.session_state.cart.clear()
    for item in catalog:
        st.session_state[f"qty_{item}"] = 0

def generate_pdf_receipt():
    """Generates a PDF receipt from the cart, handling pagination."""
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    y = height - 50

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Lovely Loveseats Receipt")
    y -= 30

    p.setFont("Helvetica", 12)
    total = 0
    for item, qty in st.session_state.cart.items():
        qty = int(qty)
        price = catalog[item]['price']
        cost = qty * price
        total += cost
        line = f"{item} x {qty} = ${cost}"
        if y < 100:
            p.showPage()
            p.setFont("Helvetica", 12)
            y = height - 50
        p.drawString(50, y, line)
        y -= 20

    if y < 100:
        p.showPage()
        y = height - 50

    y -= 10
    p.line(50, y, width - 50, y)
    y -= 20
    p.drawString(50, y, f"Total: ${total}")
    y -= 30
    p.drawString(50, y, "Thank you for shopping with us!")

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer.getvalue()

# Page Header
st.markdown("""
    <h1 style='text-align:center; color:#4B8BBE;'>🛋️ Lovely Loveseats for Neat Suites</h1>
    <h4 style='text-align:center; color:#306998;'>Create your receipt with ease</h4>
    <hr>
""", unsafe_allow_html=True)

# Layout: Product Selection (Left), Cart Summary (Right)
left_col, right_col = st.columns([3, 1])

with left_col:
    st.header("Select Your Furniture")
    product_cols = st.columns(2)
    for idx, (item, data) in enumerate(catalog.items()):
        with product_cols[idx % 2]:
            display_product_card(item, data)

    if st.button("Clear Cart"):
        clear_cart()
        st.success("Cart cleared!")

with right_col:
    st.header("🛒 Your Cart")
    if st.session_state.cart:
        total = 0
        for item, qty in st.session_state.cart.items():
            item_price = catalog[item]["price"]
            item_total = item_price * qty
            total += item_total
            st.write(f"**{item}** x {qty} = ${item_total}")
        st.markdown("---")
        st.markdown(f"### Total: ${total}")

        pdf_bytes = generate_pdf_receipt()
        st.download_button(
            label="📄 Download PDF Receipt",
            data=pdf_bytes,
            file_name="lovely_loveseats_receipt.pdf",
            mime="application/pdf"
        )
    else:
        st.info("Your cart is empty. Add items to see your receipt here.")

# Footer
st.markdown("<hr>\n<p style='text-align:center;'>© 2025 Lovely Loveseats for Neat Suites</p>", unsafe_allow_html=True)
