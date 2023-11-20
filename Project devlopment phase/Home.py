import streamlit as st

st.title(":white[SMARTINTERNZ  EXTERNSHIP]")

st.title(":violet[Time Series Analysis For Bitcoin Price Prediction using Prophet]")

bullet_points = [
    "Bitcoin has gained significant popularity worldwide as a decentralized digital currency, disrupting traditional financial systems.",
    "Operating on blockchain technology, Bitcoin ensures transparency, security, and immutability of transactions across the globe.",
    "Bitcoin provides a decentralized alternative to traditional fiat currencies, enabling direct peer-to-peer transactions without the need for intermediaries.",
    "It has empowered individuals globally, including the unbanked population, by allowing them to participate in the financial ecosystem.",
    "Cryptocurrency exchanges worldwide facilitate the buying, selling, and trading of Bitcoin, offering users convenient platforms to engage with the digital asset.",
    "The regulatory landscape for cryptocurrencies varies across countries, with governments striving to develop frameworks that balance innovation and investor protection.",
    "Central banks, including the Reserve Bank of India (RBI), have expressed concerns and issued warnings about cryptocurrencies due to their volatile nature and potential risks.",
    "Governments around the world have explored the introduction of regulatory frameworks for cryptocurrencies to ensure consumer protection and mitigate risks.",
    "Despite regulatory challenges, interest in Bitcoin and cryptocurrencies continues to grow globally, with many individuals viewing it as an investment opportunity and a hedge against inflation.",
    "Bitcoin's decentralized nature and limited supply have contributed to its appeal as a store of value and a potential future global currency."
]

for point in bullet_points:
    st.write("- " + point)
    
st.write("Please refer to the Dashboard and Forecasting from the side menu.")

st.header(":green[Our Team:]")
col1, col2, col3, col4 = st.columns(4)
with col1:
        st.write("- Aavugari Vivek Vardhan 21BAI10029")
with col2:
        st.write("- Anudeep Venigalla 21BAI10466")
with col3:
        st.write("- Nagula Rachit 21BAI10260")
with col4:
        st.write("- Nihal Sanjay Jasti 21BCE11039")

