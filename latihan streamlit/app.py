import streamlit as st

dashbord = st.Page("./fitur/dashboard.py", title="Dashbord")
nabung = st.Page("./fitur/nabung.py", title="Menabung")

pg = st.navigation(
    {
     "Menu Utama" : [dashbord],
     "Transaksi"  : [nabung],
    }
)

if "total_semua" not in st.session_state:
    st.session_state["total_semua"] = []

pg.run()