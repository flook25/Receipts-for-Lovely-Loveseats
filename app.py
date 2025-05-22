import streamlit as st

st.set_page_config(page_title="Lovely Loveseats Store", layout="wide")

# Initialize session state for cart if not present
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Furniture catalog with images and prices
catalog = {
    "Loveseat": {
        "price": 300,
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png",
        "desc": "Comfortable 2-seater sofa."
    },
    "Armchair": {
        "price": 150,
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png",
        "desc": "Cozy single-seat armchair."
    },
    "Coffee Table": {
        "price": 120,
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png",
        "desc": "Stylish wooden coffee table."
    },
    "Bookshelf": {
        "price": 200,
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png",
        "desc": "Spacious bookshelf for your books."
    },
    "Floor Lamp": {
        "price": 80,
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png",
        "desc": "Elegant floor lamp with warm light."
    },
}

def display_product_card(item, data):
    """Display product info and quantity selector in a card style."""
    st.image(data["img"], width=150)
    st.markdown(f"### {item}")
    st.markdown(f"**Price:** ${data['price']}")
    st.markdown(f"*{data['desc']}*")
    qty = st.selectbox(
        "Quantity",
        options=list(range(0, 11)),
        index=st.session_state.cart.get(item, 0),
        key=f"qty_{item}"
    )
    return qty

def update_cart_from_selection():
    """Update session_state.cart based on selected quantities."""
    for item in catalog.keys():
        qty = st.session_state.get(f"qty_{item}", 0)
        if qty > 0:
            st.session_state.cart[item] = qty
        elif item in st.session_state.cart:
            del st.session_state.cart[item]

def clear_cart():
    st.session_state.cart = {}
    for item in catalog.keys():
        st.session_state[f"qty_{item}"] = 0

# Title and description
st.markdown("<h1 style='text-align:center; color:#4B8BBE;'>🛋️ Lovely Loveseats for Neat Suites</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#306998;'>Create your receipt with ease</h4>", unsafe_allow_html=True)
st.markdown("---")

# Layout: products on left, cart summary on right
left_col, right_col = st.columns([3, 1])

with left_col:
    st.header("Select Your Furniture")
    product_cols = st.columns(2)
    for i, (item, data) in enumerate(catalog.items()):
        with product_cols[i % 2]:
            qty = display_product_card(item, data)

    # Button to update cart after selection
    if st.button("Update Cart"):
        update_cart_from_selection()
        st.success("Cart updated!")

    if st.button("Clear Cart"):
        clear_cart()
        st.success("Cart cleared!")

with right_col:
    st.header("🛒 Your Cart")
    if st.session_state.cart:
        total = 0
        for item, qty in st.session_state.cart.items():
            price = catalog[item]["price"]
            cost = price * qty
            total += cost
            st.write(f"**{item}** x {qty} = ${cost}")
        st.markdown("---")
        st.markdown(f"### Total: ${total}")
    else:
        st.info("Your cart is empty. Add items to see your receipt here.")

# Footer or additional info
st.markdown("---")
st.markdown("© 2025 Lovely Loveseats for Neat Suites")

