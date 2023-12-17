import paramiko
import os

def create_sftp_client(host, port, username, password):
    """
    Tạo một kết nối khách hàng SFTP.
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=username, password=password)
    return client.open_sftp()

def download_file(sftp, remote_path, local_filepath):
    """
    Tải xuống một tập tin từ máy chủ.
    """
    sftp.get(remote_path, local_filepath)

def upload_file(sftp, local_filepath, remote_path):
    """
    Tải lên một tập tin lên máy chủ.
    """
    sftp.put(local_filepath, remote_path)

def create_hyperlink(host, remote_path):
    """
    Tạo một liên kết siêu văn bản đến tập tin trên máy chủ từ xa.
    """
    return f"http://{host}/{remote_path}"

# Chi tiết kết nối máy chủ
host = "14.238.34.140"
port = 22  # Cổng SSH mặc định
username = "PKT"
password = "123456#"
remote_path = "/path/to/remote/file.txt"  # Thay đổi thành đường dẫn thực tế trên máy chủ
local_download_path = "downloaded_file.txt"
local_upload_path = "file_to_upload.txt"

# Kết nối với máy chủ
sftp = create_sftp_client(host, port, username, password)

# Tải xuống một tập tin
download_file(sftp, remote_path, local_download_path)
print(f"Đã tải xuống tập tin vào {local_download_path}")

# Tải lên một tập tin
upload_file(sftp, local_upload_path, remote_path)
print(f"Đã tải lên tập tin từ {local_upload_path}")

# Đóng kết nối
sftp.close()

# Tạo một liên kết siêu văn bản đến tập tin đã tải lên
hyperlink = create_hyperlink(host, remote_path)
print(f"Liên kết đến tập tin đã tải lên: {hyperlink}")
