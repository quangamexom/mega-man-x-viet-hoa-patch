# Mega Man X Việt hóa · SNES · V25 R2

Bản vá của Quán Game Xóm cho **Mega Man X (Europe)**. V25 R2 đưa lời thoại MUSE vào 35 khối văn bản, dùng font tiếng Việt hai hàng và sửa dấu còn sót khi Sigma chuyển trang sau credits. Tám hồ sơ boss ở màn chọn màn vẫn dùng tiếng Anh.

**[Tải gói patch và hướng dẫn](https://github.com/quangamexom/mega-man-x-viet-hoa-patch/releases/download/v25-r2/MegaManX_VN_V25_R2.zip)** · [Xem 10 ảnh trong game](screenshots/)

## Cách chơi

1. Giải nén gói ZIP vào một thư mục. Chuẩn bị bản **Mega Man X (Europe) có copier header 512 byte**, kích thước **1.573.376 byte**. ROM gốc do người chơi tự cung cấp.
2. Nếu máy có Python 3, mở terminal tại thư mục vừa giải nén và chạy lệnh bên dưới. Thay đường dẫn trong ngoặc kép bằng đường dẫn tới ROM gốc của bạn. Trên macOS/Linux có thể dùng `python3` thay `python`.

   ```powershell
   python ap_patch.py "D:\Game\Mega Man X (E).smc"
   ```

3. Khi thấy `OK`, mở file `MegaManX_VN_v25_muse_r2.smc` vừa tạo cùng thư mục với ROM gốc trong Mesen. Khởi động game từ đầu ở lần mở đầu tiên để game nạp bộ font mới.

Nếu dùng công cụ vá IPS có sẵn, chọn `MegaManX_VN_v25_muse_r2.ips`, chọn bản sao ROM gốc và áp patch lên **toàn bộ file gồm cả header**. Lưu kết quả bằng tên mới rồi kiểm tra hash ở bảng dưới. Trong Windows PowerShell dùng `Get-FileHash -Algorithm SHA256 -LiteralPath "đường dẫn tới file"`.

| File | Số byte | SHA-256 |
| --- | ---: | --- |
| ROM gốc Europe | 1.573.376 | `2B648ECBEBF0659A22910C6ADA44D4440CFA19DF96F2207A7ED5F56E5DFBB402` |
| Patch IPS V25 R2 | 113.086 | `BAF1D51D006737426241530772069F7477B10F1DF8B4728B40F40F3C8C532355` |
| ROM sau khi vá | 2.097.664 | `5DCDA6994F9620F413EABE80175D3642B020B2EE17840B50978DBF6C61571F6E` |

Nếu công cụ báo sai hash nguồn, kiểm tra vùng Europe, header và việc ROM đã được vá trước đó. Nếu hash đầu ra đúng nhưng chữ lạ sau khi nạp save-state cũ, thử mở lại ROM từ đầu. Khi báo lỗi, gửi tên giả lập, cảnh, thao tác tái hiện và ảnh chụp.

Patch đã được áp lại trên ROM sạch và so từng byte với bản V25 R2. Các cảnh đã kiểm trong Mesen gồm Vile trên cao tốc, khoang Dr. Light, Dung nạp, Zero và Sigma sau credits. Chưa có biên bản chơi liên tục toàn game từ đầu đến cuối.

Việt hóa bởi **Quán Game Xóm**. Mega Man X thuộc Capcom.
