import streamlit as st

st.title("Inventario Escolar")

productos = {
    "Mouse": 10,
    "Teclado": 20,
    "Monitor": 150,
    "Laptop": 600
}

if "carrito" not in st.session_state:
    st.session_state.carrito = []

producto = st.selectbox("Seleccione un producto", list(productos.keys()))

if st.button("Agregar al carrito"):
    if producto not in st.session_state.carrito:
        st.session_state.carrito.append(producto)

st.subheader("Carrito")

total = 0

for p in st.session_state.carrito:
    cantidad = st.number_input(f"Cantidad de {p}", min_value=1, step=1, key=p)
    subtotal = productos[p] * cantidad
    total += subtotal

if st.button("Calcular total"):
    st.write("### Resumen")
    for p in st.session_state.carrito:
        st.write(f"{p}: ${productos[p]}")
    st.success(f"Total a pagar: ${total}")