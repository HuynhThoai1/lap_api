import requests

# URL của endpoint predict trên máy cá nhân
url = "http://127.0.0.1:8000/predict"

# Đường dẫn tới một bức ảnh
image_path = "meo.png"

print(f"Đang gửi ảnh {image_path} lên server...")

# Mở file ảnh dưới dạng đọc nhị phân (binary read - 'rb')
with open(image_path, "rb") as file:
    files = {"file": (image_path, file, "image/png")}

    response = requests.post(url, files = files)

# In kết quả trả về từ server
print("\n--- KẾT QUẢ TỪ API ---")
if response.status_code == 200:
    print("Test thành công! Kết quả từ API:")
    print(response.json())
else:
    print(f"Lỗi {response.status_code}:", response.text)