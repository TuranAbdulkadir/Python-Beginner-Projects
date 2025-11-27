import speedtest
print("Testing internet speed...")
st = speedtest.Speedtest()
print(f"Download: {st.download()/1024/1024:.2f} Mbps")
print(f"Upload: {st.upload()/1024/1024:.2f} Mbps")