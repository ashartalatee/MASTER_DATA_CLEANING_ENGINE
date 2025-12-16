from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("output.txt", "a") as f:
    f.write(f"Script jalan pada: {now}\n")

print("Script berhasil dijalankan")
