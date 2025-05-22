import streamlit as st

st.set_page_config(page_title="Lovely Loveseats Store", layout="wide")

catalog = {
    "Loveseat": {"price": 300, "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"},
    "Armchair": {"price": 150, "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"},
    "Coffee Table": {"price": 120, "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"},
    "Bookshelf": {"price": 200, "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"},
    "Floor Lamp": {"price": 80, "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"},
}

# Initialize session state keys for quantities and cart
if "cart" not in st.session_state:
    st.session_state.cart = {}

for item in catalog.keys():
    key = f"qty_{item}"
    if key not in st.session_state:
        st.session_state[key] = 0

def update_cart():
    for item in catalog.keys():
        qty = st.session_state[f"qty_{item}"]
        if qty > 0:
            st.session_state.cart[item] = qty
        elif item in st.session_state.cart:
            del st.session_state.cart[item]

def clear_cart():
    st.session_state.cart = {}
    for item in catalog.keys():
        key = f"qty_{item}"
        st.session_state[key] = 0

st.title("🛋️ Lovely Loveseats for Neat Suites")

cols = st.columns(2)
for i, (item, data) in enumerate(catalog.items()):
    with cols[i % 2]:
        st.image(data["img"], width=150)
        st.markdown(f"### {item}")
        st.markdown(f"**Price:** ${data['price']}")
        st.session_state[f"qty_{item}"] = st.selectbox(
            "Quantity",
            options=list(range(0, 11)),
            index=st.session_state[f"qty_{item}"],
            key=f"qty_{item}"
        )

if st.button("Update Cart"):
    update_cart()
    st.success("Cart updated!")

if st.button("Clear Cart"):
    clear_cart()
    st.success("Cart cleared!")

st.sidebar.header("🛒 Your Cart")
if st.session_state.cart:
    total = 0
    for item, qty in st.session_state.cart.items():
        cost = catalog[item]["price"] * qty
        total += cost
        st.sidebar.write(f"{item} x {qty} = ${cost}")
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### Total: ${total}")
else:
    st.sidebar.info("Your cart is empty.")
