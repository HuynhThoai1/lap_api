from fastapi import FastAPI, UploadFile, File, HTTPException
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io

# Khởi tạo ứng dụng FastAPI
app = FastAPI() # gọi constructor và gán vào biến app

# Tải trước mô hình BLIP khi server khởi động để giảm thời gian chờ lúc dự đoán
print("Đang khởi động mô hình BLIP...")
try:
    # Bộ xử lý đầu vào/đầu ra cho mô hình BLIP
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    # Mô hình sinh mô tả ảnh
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
    print("Khởi tạo mô hình thành công!")
except Exception as e:
    # In lỗi nếu không tải được mô hình
    print(f"Lỗi khi tải mô hình: {e}")

# Endpoint gốc để chào mừng và hiển thị thông tin mô hình
@app.get("/") 
async def root(): 
    return {
        "message": "Chào mừng đến với hệ thống API Sinh mô tả ảnh",
        "model": "Salesforce/blip-image-captioning-large"        
    }


# Endpoint kiểm tra trạng thái hoạt động của API
@app.get("/health")
async def health():
    return {
        "status": "ok",
        "message": "API đang hoạt động bình thường"
    }

# Endpoint nhận ảnh tải lên và trả về mô tả ảnh
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Kiểm tra kiểu dữ liệu tải lên có phải ảnh hay không
        if file.content_type is None or not file.content_type.startswith("image/"):
            raise HTTPException(status_code = 400, detail = "File tải lên không phải định dạng ảnh")
        
        # Đọc dữ liệu nhị phân của file ảnh
        image_data = await file.read()

        # Chuyển dữ liệu bytes thành ảnh RGB để mô hình xử lý
        raw_image = Image.open(io.BytesIO(image_data)).convert('RGB')

        # Tiền xử lý ảnh để tạo tensor đầu vào cho mô hình
        inputs = processor(raw_image, return_tensors = "pt")

        # Sinh chuỗi token mô tả ảnh (giới hạn 50 token mới)
        out = model.generate(**inputs, max_new_tokens = 50)

        # Giải mã token thành câu mô tả văn bản
        caption = processor.decode(out[0], skip_special_tokens = True)

        # Trả về thông tin file và kết quả mô tả ảnh
        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "caption": caption
        }
    
    except Exception as e:
        
        # Ghi log chi tiết lỗi để dễ theo dõi khi debug
        print(f"Chi tiết lỗi 500: {str(e)}")

        # Trả lỗi HTTP 500 nếu có sự cố trong quá trình xử lý
        raise HTTPException(status_code = 500, detail = f"Lỗi hệ thống trong quá trình xử lý: {str(e)}")
    