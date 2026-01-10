# SinhTrang-Wedding - Thiệp Cưới Online

Website thiệp cưới online cho Nguyễn Văn Sinh ❤️ Lê Thu Trang

## Cách xem website

### Cách 1: Mở trực tiếp file HTML
- Double-click vào file `index.html` để mở trong trình duyệt
- Hoặc chuột phải vào `index.html` → Open with → Chọn trình duyệt

### Cách 2: Sử dụng Local Server (Khuyến nghị)

#### Với Python:
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```
Sau đó mở trình duyệt và truy cập: `http://localhost:8000`

#### Với Node.js (nếu đã cài đặt):
```bash
# Cài đặt http-server (chỉ cần 1 lần)
npm install -g http-server

# Chạy server
http-server -p 8000
```

#### Với VS Code:
- Cài đặt extension "Live Server"
- Click chuột phải vào `index.html` → "Open with Live Server"

## Cấu trúc thư mục

```
SinhTrang-Wedding/
├── index.html          # File HTML chính
├── css/                # Các file CSS
├── js/                 # Các file JavaScript
├── images/             # Hình ảnh
├── fonts/              # Font chữ
└── media/              # File âm thanh
```

## Tính năng

- ✅ Thiệp cưới online với thiết kế đẹp mắt
- ✅ Countdown timer đến ngày cưới
- ✅ Album ảnh
- ✅ Love Story timeline
- ✅ Thông tin địa điểm và thời gian
- ✅ Nhạc nền tự động phát
- ✅ Responsive design

## Lưu ý

- Website sử dụng các thư viện: jQuery, Swiper, AOS, Fancybox, UIKit
- File nhạc nền: `media/Shane-Filan-Beautiful-In-White-Official-Video.mp3`
- Website hoạt động tốt nhất khi chạy trên local server để tránh các vấn đề về CORS
