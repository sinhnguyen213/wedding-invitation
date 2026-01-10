# 📖 HƯỚNG DẪN CUSTOM WEBSITE THIỆP CƯỚI

## 🔍 PHẦN 1: GIẢI THÍCH CHI TIẾT PHẦN HEADER (IMPORT)

### 1. META TAGS & SEO (Dòng 1-26)

```html
<!-- Các thẻ meta cơ bản -->
<meta charset="UTF-8">                    # Định dạng ký tự UTF-8 (hỗ trợ tiếng Việt)
<meta name="viewport" content="width=device-width, initial-scale=1">  # Responsive cho mobile

<!-- SEO Meta Tags -->
<title>...</title>                        # Tiêu đề hiển thị trên tab trình duyệt
<meta name="robots" content="...">        # Hướng dẫn bot tìm kiếm (index, follow)
<link rel="canonical" href="...">         # URL chính thức của trang (quan trọng cho SEO)

<!-- Open Graph Tags (Facebook, LinkedIn) -->
<meta property="og:title" content="...">  # Tiêu đề khi share lên Facebook
<meta property="og:image" content="...">   # Hình ảnh preview khi share
<meta property="og:url" content="...">     # URL khi share

<!-- Twitter Card Tags -->
<meta name="twitter:title" content="..."> # Tiêu đề khi share lên Twitter
<meta name="twitter:image" content="..."> # Hình ảnh preview khi share
```

**Chức năng:** 
- Tối ưu SEO để website xuất hiện trên Google
- Hiển thị đẹp khi share lên Facebook/Twitter
- Responsive trên mọi thiết bị

---

### 2. DNS PREFETCH (Dòng 28-29)

```html
<link rel="dns-prefetch" href="//cdn.jsdelivr.net">
<link rel="dns-prefetch" href="//unpkg.com">
```

**Chức năng:** 
- Tăng tốc độ tải trang bằng cách resolve DNS sớm
- Chuẩn bị kết nối đến các CDN (Content Delivery Network)

---

### 3. INLINE STYLES (Dòng 32-403)

#### 3.1. WordPress Emoji Styles (Dòng 32-45)
```html
<style id="wp-emoji-styles-inline-css">
```
**Chức năng:** Style cho emoji và icon WordPress

#### 3.2. Rank Math TOC Styles (Dòng 47-60)
```html
<style id="rank-math-toc-block-style-inline-css">
```
**Chức năng:** Style cho bảng mục lục (Table of Contents) từ plugin Rank Math

#### 3.3. Classic Theme Styles (Dòng 61-78)
```html
<style id="classic-theme-styles-inline-css">
```
**Chức năng:** Style cho button và file button theo chuẩn WordPress

#### 3.4. Global Styles (Dòng 79-403) - QUAN TRỌNG NHẤT
```html
<style id="global-styles-inline-css">
    :root {
        --wp--preset--color--black: #000000;
        --wp--preset--color--white: #ffffff;
        --wp--preset--gradient--...: ...;
        --wp--preset--font-size--small: 13px;
        --wp--preset--spacing--...: ...;
        --wp--preset--shadow--...: ...;
    }
</style>
```

**Chức năng:**
- Định nghĩa CSS Variables (biến CSS) cho toàn bộ website
- Màu sắc, gradient, font-size, spacing, shadow
- Có thể tùy chỉnh màu sắc theme tại đây

---

### 4. CSS FILES (Dòng 404-415)

```html
<!-- Framework CSS -->
<link rel="stylesheet" href="css/uikit.min.css">        # UIKit framework (grid, components)
<link rel="stylesheet" href="css/reset1.css">          # Reset CSS (xóa style mặc định)
<link rel="stylesheet" href="css/reset-wedding.css">   # Reset CSS riêng cho wedding

<!-- Icon Font -->
<link rel="stylesheet" href="css/remixicon.css">      # Icon font RemixIcon (ri-phone-fill, ri-map-2-fill...)

<!-- Preloader -->
<link rel="stylesheet" href="css/preload.css">        # Style cho màn hình loading

<!-- Libraries CSS -->
<link rel="stylesheet" href="css/fancybox.css">       # Lightbox gallery (xem ảnh phóng to)
<link rel="stylesheet" href="css/swiper-bundle.min.css">  # Slider/Carousel (album ảnh trượt)
<link rel="stylesheet" href="css/aos.css">            # Animate On Scroll (hiệu ứng khi scroll)
<link rel="stylesheet" href="css/animation.css">     # Animation tùy chỉnh

<!-- Custom CSS -->
<link rel="stylesheet" href="css/footer.css">          # Style cho footer
<link rel="stylesheet" href="css/wedding.css">         # Style chính cho wedding (QUAN TRỌNG)
<link rel="stylesheet" href="css/theme.css">          # Theme colors, fonts
<link rel="stylesheet" href="css/style.css">          # Style tổng hợp
<link rel="stylesheet" href="css/style.min.css">      # Style minified (tối ưu)
```

**Chức năng từng file:**
- **uikit.min.css**: Framework UI, grid system, utilities
- **remixicon.css**: Icon font (phone, map, volume...)
- **fancybox.css**: Lightbox để xem ảnh fullscreen
- **swiper-bundle.min.css**: Slider cho album ảnh
- **aos.css**: Animation khi scroll xuống
- **wedding.css**: Style chính của website thiệp cưới ⭐
- **theme.css**: Màu sắc, font chữ theme

---

### 5. JAVASCRIPT FILES (Dòng 416-418, 431)

```html
<!-- jQuery Core -->
<script src="js/jquery.min_1.js"></script>           # jQuery phiên bản 1
<script src="js/jquery-migrate.min.js"></script>     # jQuery migration (tương thích)
<script src="js/jquery.min.js"></script>              # jQuery phiên bản chính

<!-- WordPress Emoji -->
<script src="js/wp-emoji-release.min.js" defer></script>  # Emoji support
```

**Chức năng:**
- **jQuery**: Thư viện JavaScript phổ biến, dùng cho DOM manipulation, AJAX
- **wp-emoji-release.min.js**: Hỗ trợ emoji WordPress

**Lưu ý:** Các script khác được load ở cuối body (dòng 995-1002):
- fancybox.umd.js (lightbox)
- uikit.min.js (UI framework)
- preloader.js (loading screen)
- aos.js (scroll animation)
- swiper-bundle.min.js (slider)
- main-wedding.js (script chính) ⭐

---

## 🎨 PHẦN 2: CÁC VỊ TRÍ CẦN THAY ĐỔI ĐỂ CUSTOM

### 📝 A. THAY ĐỔI TÊN CẶP ĐÔI

#### 1. **SEO Meta Tags** (Dòng 8, 10, 13-15, 24)
```html
<!-- Thay đổi tại đây: -->
<title> [Tên Chú Rể] ❤️ [Tên Cô Dâu] - Thiệp cưới online</title>
<link rel="canonical" href="https://[username].github.io/[repo-name]/">
<meta property="og:title" content="[Tên Chú Rể] ❤️ [Tên Cô Dâu]">
<meta property="og:url" content="https://[username].github.io/[repo-name]/">
<meta property="og:site_name" content="[Tên Chú Rể] ❤️[Tên Cô Dâu]">
<meta name="twitter:title" content="[Tên Chú Rể]❤️ [Tên Cô Dâu]">
```

#### 2. **Preloader Screen** (Dòng 442-445)
```html
<h2 class="uk-text-center uk-marign-remove uk-text-bold uk-h4 uk-animation-slide-bottom">
    [Tên Chú Rể]
    ❤️
    [Tên Cô Dâu]
</h2>
```

#### 3. **Banner Section** (Dòng 460-463)
```html
<div class="banner-name">
    [Tên Chú Rể]<br>
    <span>&</span><br>
    [Tên Cô Dâu]
</div>
```

#### 4. **About Section** (Dòng 510, 522)
```html
<!-- Cô dâu -->
<h3 class="bride_name"> [Tên Cô Dâu]</h3>

<!-- Chú rể -->
<h3 class="groom_name">[Tên Chú Rể]</h3>
```

---

### 🖼️ B. THAY ĐỔI HÌNH ẢNH

#### 1. **SEO Preview Image** (Dòng 5, 17-18, 25)
```html
<!-- Thay URL ảnh preview khi share Facebook/Twitter -->
<meta property="og:image" content="https://[your-domain]/images/[your-image].jpg">
<meta property="og:image:secure_url" content="https://[your-domain]/images/[your-image].jpg">
<meta name="twitter:image" content="https://[your-domain]/images/[your-image].jpg">
```

#### 2. **Preloader Logo** (Dòng 440)
```html
<img src="images/logo-doc3.png" alt="" style="max-width: 150px;">
```
**Thay đổi:** `logo-doc3.png` → tên file logo của bạn

#### 3. **Banner Background** (Dòng 453)
```html
<img src="images/9qLFct59duNq3dnGdobuk7UqOgSLFeAv7VnhQSze.jpg" alt="" class="banner_top">
```
**Thay đổi:** `9qLFct59duNq3dnGdobuk7UqOgSLFeAv7VnhQSze.jpg` → ảnh banner của bạn

#### 4. **Ảnh Cô Dâu & Chú Rể** (Dòng 507, 519)
```html
<!-- Ảnh cô dâu -->
<img src="images/ZJDDjVNCXKTxZeOkL5pEenKiYPZMb2BRdTVSj1AL.jpg" alt="" class="bride_img">

<!-- Ảnh chú rể -->
<img src="images/4KC9FO2oXohLeQQgYpMQZL5Xe1RO4qITVjqrt35A.jpg" alt="" class="groom_img">
```

#### 5. **Countdown Background** (Dòng 538)
```html
<div class="count-down" style="background-image:url(images/5UYAH2HaQvebgXKjTN60aF8YtXuguvwq5WGrnDqX.jpg)">
```

#### 6. **Invitation Cards** (Dòng 581, 625)
```html
<!-- Tiệc Nhà Trai -->
<img src="images/4KC9FO2oXohLeQQgYpMQZL5Xe1RO4qITVjqrt35A.jpg" alt="">

<!-- Tiệc Nhà Gái -->
<img src="images/ZJDDjVNCXKTxZeOkL5pEenKiYPZMb2BRdTVSj1AL.jpg" alt="">
```

#### 7. **Timeline Background** (Dòng 677)
```html
<section style="background-image:url(images/OSSZZ2rshgdAN00xbqY7oqCeiDTtSFmfVu2h2hJQ.jpg)">
```

#### 8. **Love Story Timeline Images** (Dòng 698, 710, 722, 734)
```html
<!-- Hẹn Hò -->
<img src="images/8PksSCWR1WLXH3OCVHhyFtmnlGwSvwaGMkEpYGHp.jpg" alt="">

<!-- Tỏ Tình -->
<img src="images/ebx5uOymorDgzf5utdtorGKG1WbdFzJbye6eEuGr.jpg" alt="">

<!-- Đính Hôn -->
<img src="images/NUksQm7H9UnMPfm0motw7RJhnX43FnzVj23a879J.jpg" alt="">

<!-- Kết Hôn -->
<img src="images/y5yS5PQ0JFrLHoz3Br66mhDIlpZ3U8DsIoDEXk2N.jpg" alt="">
```

#### 9. **Album Gallery** (Dòng 765-811)
```html
<!-- Thay tất cả 10 ảnh trong album -->
<a href="images/[your-image-1].jpg" data-fancybox="gallery">
    <img src="images/[your-image-1].jpg">
</a>
<!-- ... lặp lại cho các ảnh khác -->
```

#### 10. **QR Code Gift** (Dòng 944-945)
```html
<!-- QR code chú rể -->
<img src="images/Huqd3bBOdU1ZmohSXecpE1pQ5FrLBIagbuB7eiWk.jpg" alt="" class="groom_qr">

<!-- QR code cô dâu -->
<img src="images/EVdFVxMYc0ritAOAVAyb3mbyuRrxpcu47EIzKvKW.jpg" alt="" class="groom_qr">
```

#### 11. **Thank You Background** (Dòng 965)
```html
<img src="images/edJEj5BwLbdjVTwagrmXzBYwOnomUVZGL3uieY8Q.jpg" alt="" class="thankyou-bg">
```

---

### 📅 C. THAY ĐỔI THÔNG TIN KHÁC

#### 1. **Ngày Cưới** (Dòng 466-469, 548, 600-606, 633-648)
```html
<!-- Banner date -->
<span class="day_name">Tháng [MM]</span>
<span class="banner_date">[DD]</span>
<span class="banner_month">[YYYY]</span>

<!-- Countdown timer -->
<div uk-countdown="date: [YYYY]-[MM]-[DD] [HH]:[mm]:00">

<!-- Invitation date -->
<p class="invi_date">[DD]</p>
<p class="invi_month">[MM]</p>
<span class="invi_year_text">[YYYY]</span>
```

#### 2. **Địa Chỉ & Số Điện Thoại** (Dòng 474-475, 586, 614-620, 629, 656-661)
```html
<!-- Banner location -->
<p class="banner_location_name">[Địa chỉ]</p>
<p class="banner_location_adress">[Địa chỉ chi tiết]</p>

<!-- Phone number -->
<a href="tel:[số-điện-thoại]">

<!-- Google Maps link -->
<a href="https://maps.app.goo.gl/[your-map-link]" target="_blank">
```

#### 3. **Thời Gian Tiệc** (Dòng 592-593, 634-635)
```html
<span class="invi_hours">[HH]:[mm]</span>
```

#### 4. **Âm Lịch** (Dòng 609, 651)
```html
<p class="invi_amlich">Tức ngày [DD] tháng [MM] năm [Tên Năm] (Âm Lịch)</p>
```

#### 5. **Love Story Dates** (Dòng 702, 714, 726, 738)
```html
<span class="story-date">[DD]/[MM]/[YYYY]</span>
<span class="title">[Tên sự kiện]</span>
```

---

## 📋 CHECKLIST CUSTOM CHO GITHUB PAGES

### ✅ Bước 1: Thay đổi tên cặp đôi
- [ ] Dòng 8: Title tag
- [ ] Dòng 10, 14: Canonical URL và OG URL (đổi thành repo GitHub của bạn)
- [ ] Dòng 13, 15, 24: OG title, site name, Twitter title
- [ ] Dòng 442-445: Preloader
- [ ] Dòng 460-463: Banner name
- [ ] Dòng 510, 522: About section names

### ✅ Bước 2: Thay đổi hình ảnh
- [ ] Dòng 5, 17-18, 25: SEO preview images (dùng URL GitHub Pages)
- [ ] Dòng 440: Logo preloader
- [ ] Dòng 453: Banner background
- [ ] Dòng 507, 519: Ảnh cô dâu & chú rể
- [ ] Dòng 538: Countdown background
- [ ] Dòng 581, 625: Invitation cards
- [ ] Dòng 677: Timeline background
- [ ] Dòng 698, 710, 722, 734: Love story images (4 ảnh)
- [ ] Dòng 765-811: Album gallery (10 ảnh)
- [ ] Dòng 944-945: QR codes (2 ảnh)
- [ ] Dòng 965: Thank you background

### ✅ Bước 3: Thay đổi thông tin
- [ ] Dòng 466-469: Ngày cưới banner
- [ ] Dòng 548: Countdown date
- [ ] Dòng 474-475: Địa chỉ banner
- [ ] Dòng 477, 614, 656: Số điện thoại
- [ ] Dòng 480, 618, 659: Google Maps links
- [ ] Dòng 586, 629: Địa chỉ tiệc
- [ ] Dòng 592-593, 634-635: Giờ tiệc
- [ ] Dòng 600-606, 641-648: Ngày tiệc
- [ ] Dòng 609, 651: Âm lịch
- [ ] Dòng 702, 714, 726, 738: Love story dates

### ✅ Bước 4: Chuẩn bị cho GitHub Pages
- [ ] Đổi tên repository thành tên bạn muốn
- [ ] Upload tất cả ảnh vào thư mục `images/`
- [ ] Cập nhật tất cả URL trong meta tags thành: `https://[username].github.io/[repo-name]/`
- [ ] Test website trên local trước khi push lên GitHub
- [ ] Enable GitHub Pages trong Settings → Pages → Source: main branch

---

## 💡 LƯU Ý QUAN TRỌNG

1. **Tên file ảnh:** Giữ nguyên định dạng `.jpg` hoặc `.png`, đảm bảo tên file không có ký tự đặc biệt
2. **Kích thước ảnh:** 
   - Banner: Khuyến nghị 1920x1080px hoặc lớn hơn
   - Ảnh cô dâu/chú rể: Tỷ lệ vuông hoặc 3:4
   - Album: Tỷ lệ 16:9 hoặc 4:3
3. **URL GitHub Pages:** Format: `https://[username].github.io/[repository-name]/`
4. **SEO Images:** Nên dùng URL đầy đủ từ GitHub Pages để hiển thị đúng khi share
5. **Test local:** Luôn test trên local server trước khi deploy

---

## 🚀 QUY TRÌNH DEPLOY LÊN GITHUB PAGES

1. **Tạo repository mới trên GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/[username]/[repo-name].git
   git push -u origin main
   ```

2. **Enable GitHub Pages**
   - Vào Settings → Pages
   - Source: Deploy from a branch
   - Branch: main, folder: / (root)
   - Save

3. **Truy cập website**
   - URL: `https://[username].github.io/[repo-name]/`
   - Đợi vài phút để GitHub build xong

---

Chúc bạn custom thành công! 🎉💒
