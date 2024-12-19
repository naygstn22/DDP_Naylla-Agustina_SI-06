import streamlit as st

st.title("Halaman Dasbord")
st.image("imagess.jpg", caption="Gambar Rumah")


# fungsi menghitung dan menyiapkan total
def total():
    total_nabung = sum(t["Jumlah"]
                       for t in st.session_state["total_semua"]
                       if t ["Tipe"] == "Menabung")
    
    return total_nabung

total_semua = st.session_state["total_semua"]
total_nabung = total()
 
st.metric("Total Menabung", f"Rp {total_nabung}")