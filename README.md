1. Mô tả tổng quan
Dự án xây dựng một ứng dụng web cho phép người dùng thực hiện mã hóa và giải mã tệp tin bằng thuật toán AES (Advanced Encryption Standard).
Đây là một thuật toán mã hóa đối xứng hiện đại, được sử dụng rộng rãi nhờ tính an toàn và hiệu quả cao.
Ứng dụng hỗ trợ người dùng tải tệp lên, nhập khóa bí mật, lựa chọn thao tác (mã hóa hoặc giải mã), và nhận lại kết quả là tệp đã được xử lý.
2. Mục tiêu
Tăng cường bảo mật thông tin khi lưu trữ hoặc truyền tải qua mạng.
Hỗ trợ người dùng dễ dàng thực hiện mã hóa/giải mã mà không cần kiến thức chuyên sâu về mã hóa.
Thay thế các thuật toán cũ, không còn an toàn như DES bằng AES hiện đại.
3. Công nghệ sử dụng
Thành phần
Python
Flask	
PyCryptodome
HTML, CSS, Bootstrap
4. Cơ chế mã hóa và giải mã
Thuật toán sử dụng: AES, chế độ CBC (Cipher Block Chaining).
Khóa mã hóa: người dùng nhập vào, yêu cầu tối thiểu 8 ký tự, được xử lý chuẩn hóa thành 16 byte để phù hợp với yêu cầu của AES-128.
IV (Initialization Vector): được tạo ngẫu nhiên và gắn kèm vào đầu dữ liệu mã hóa.
Padding: sử dụng kỹ thuật bổ sung dữ liệu để đảm bảo độ dài khối theo chuẩn AES.
5. Các chức năng chính
Cho phép người dùng tải tệp lên từ máy tính cá nhân.
Nhập khóa mã hóa/giải mã (chuỗi ký tự tối thiểu 8 ký tự).
Lựa chọn thao tác: mã hóa hoặc giải mã tệp.
Trả về kết quả là tệp đã được xử lý để người dùng tải về.
6. Ưu điểm
Giao diện thân thiện, dễ sử dụng cho cả người không chuyên.
![image](https://github.com/user-attachments/assets/93f8b36d-432c-47c1-aa26-5ad3fe7ec233)
Đảm bảo bảo mật nhờ sử dụng AES – một trong những chuẩn mã hóa an toàn nhất hiện nay.
Dữ liệu được xử lý trực tiếp, không lưu trữ vĩnh viễn trên máy chủ.
Có thể mở rộng hỗ trợ các thuật toán mã hóa khác như RSA, Blowfish, Twofish,…
