import streamlit as st
import speedtest

st.title("Test speed")
st.write("Click the button below to start measuring your internet speed:")


if st.button("Measure Speed"):
    with st.spinner("Measuring..."):
        test = speedtest.Speedtest()
        
    
        download_speed = test.download() / (1024 * 1024)
        upload_speed = test.upload() / (1024 * 1024)
        
    
        st.success("Measurement complete!")
        st.metric(label="Download Speed", value=f"{download_speed / 1024 / 1024:.2f} Mbps")
        st.metric(label="Upload Speed", value=f"{upload_speed:.2f} Mbps")
