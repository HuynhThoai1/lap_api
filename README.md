# Lab 01: Hệ thống API Sinh Mô Tả Ảnh (Image Captioning)

**Môn học:** Tư duy tính toán  
**Giảng viên hướng dẫn:** Lê Đức Khoan

## I. Thông tin thực hiện
* **Họ và tên:** Huỳnh Chí Thoại
* **MSSV:** 24120457

---

## II. Giới thiệu về bài tập thực hành
Bài tập này cung cấp một RESTful API được xây dựng bằng **FastAPI** cho phép người dùng tải lên một bức ảnh và nhận về câu mô tả ngắn về ảnh bằng tiếng Anh.
Hệ thống tích hợp mô hình AI [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large) (mô hình Vision-Language) thông qua thư viện `transformers` của Hugging Face.

### Các API Endpoints:
* `GET /`: Kiểm tra thông tin cơ bản của hệ thống và mô hình.
* `GET /health`: Kiểm tra trạng thái hoạt động của API.
* `POST /predict`: Nhận file ảnh (`UploadFile`) và trả về kết quả dự đoán (caption).

---

## III. Yêu cầu hệ thống & Cài đặt

### 1. Yêu cầu môi trường
* Python 3.8 trở lên.
* Sử dụng môi trường ảo (Virtual Environment).

### 2. Cài đặt đặt thư viện và chạy chương trình
Clone repository này về máy và chạy lệnh sau trong terminal để cài đặt các thư viện cần thiết:
```bash
# Tải thư viện
pip install -r requirements.txt

# Khởi tạo môi trường ảo venv
source .venv/Scripts/activate

# Chạy server
uvicorn main:app --reload

# Kiểm thử 
## Sử dụng mã nguồn được thực hiện nhờ vào thư viện requests
python test_api.py

## Sử dụng giao diện Swagger UI qua đường link:
http://127.0.0.1:8000/docs

```

**Ví dụ kết quả (Response) trả về từ hệ thống:**
```json
{
  "filename": "anh_duong_pho.png", "content_type": "image/png", "caption": "cars are driving down a highway with tall buildings in the background"
}
```

## IV. Video demo

https://github.com/user-attachments/assets/52e486a1-f38d-435b-9c81-34db86692985


