import streamlit as st

st.set_page_config(page_title="Lovely Loveseats Receipt", layout="centered")

st.title("🛋️ Lovely Loveseats for Neat Suites")
st.subheader("Create your receipt easily")

# Furniture catalog with prices
catalog = {
    "Loveseat": 300,
    "Armchair": 150,
    "Coffee Table": 120,
    "Bookshelf": 200,
    "Floor Lamp": 80,
}

st.markdown("### Select items and quantities:")

# Create columns for better layout
cols = st.columns(2)

selected_items = {}
total_price = 0

# Quantity options for dropdown (0 to 10)
quantity_options = list(range(0, 11))

for i, (item, price) in enumerate(catalog.items()):
    with cols[i % 2]:
        quantity = st.selectbox(
            f"{item} (${price})",
            options=quantity_options,
            index=0,
            key=item
        )
        if quantity > 0:
            selected_items[item] = quantity
            total_price += price * quantity

# Display receipt if any item selected
if selected_items:
    st.markdown("---")
    st.header("🧾 Receipt")
    for item, qty in selected_items.items():
        cost = catalog[item] * qty
        st.write(f"**{item}** x {qty} = ${cost}")
    st.markdown(f"## Total: ${total_price}")
else:
    st.info("Please select quantities for the items you want to purchase.")

# Optional: Add a button to clear selections (refresh page)
if st.button("Clear selections"):
    st.experimental_rerun()
