import streamlit as st

st.set_page_config(page_title="Lovely Loveseats Store", layout="wide")

st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🛋️ Lovely Loveseats for Neat Suites</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #306998;'>Your friendly furniture receipt generator</h3>", unsafe_allow_html=True)
st.markdown("---")

# Furniture catalog with prices and image URLs (replace with your images or URLs)
catalog = {
    "Loveseat": {"price": 300, "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"},
    "Armchair": {"price": 150, "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"},
    "Coffee Table": {"price": 120, "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"},
    "Bookshelf": {"price": 200, "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"},
    "Floor Lamp": {"price": 80, "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"},
}

# Sidebar Cart summary
st.sidebar.header("🛒 Your Cart")

if "cart" not in st.session_state:
    st.session_state.cart = {}

def update_cart(item, qty):
    if qty > 0:
        st.session_state.cart[item] = qty
    elif item in st.session_state.cart:
        del st.session_state.cart[item]

# Main layout: display items in cards with images and quantity selectors
cols = st.columns(len(catalog))

for idx, (item, data) in enumerate(catalog.items()):
    with cols[idx]:
        st.image(data["img"], width=120)
        st.markdown(f"### {item}")
        st.markdown(f"**Price:** ${data['price']}")
        qty = st.selectbox(
            "Quantity",
            options=list(range(0, 11)),
            index=st.session_state.cart.get(item, 0),
            key=f"qty_{item}"
        )
        update_cart(item, qty)

# Display receipt summary in sidebar
if st.session_state.cart:
    total = 0
    for item, qty in st.session_state.cart.items():
        price = catalog[item]["price"]
        cost = price * qty
        total += cost
        st.sidebar.write(f"{item} x {qty} = ${cost}")
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### Total: ${total}")
else:
    st.sidebar.info("Select items to add to your cart.")

# Optional: Clear cart button
if st.sidebar.button("Clear Cart"):
    st.session_state.cart = {}
    st.experimental_rerun()
