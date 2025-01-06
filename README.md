# 🔓 **SSH Breaker**

**SSH Breaker** is a Python-based brute force tool designed to test SSH login credentials using a list of passwords. It automates the process of attempting multiple password combinations to gain access to an SSH service, making it a useful tool for penetration testing.

## 🚀 Features

- 🔐 **Brute force SSH login attempts** using a password list.
- 🛠️ **Displays information** about the progress and status of each login attempt.
- ✅ Provides **success/failure messages** and logs for every password tried.
- 💡 Clear, easy-to-use **interface** with a **banner display**.
- ⚙️ Supports customizable configurations, such as **SSH port** and **password list file**.

## 📝 Prerequisites

To run **SSH Breaker**, you'll need:

- Python 3.x
- `paramiko` library for SSH functionality.
- `pyfiglet` library for banner display.

### Install Required Libraries

Run the following command to install the necessary Python libraries:

```bash
pip install paramiko pyfiglet
```
🔧 Usage
Clone this repository to your local machine:

```Copy code
git clone https://github.com/yourusername/ssh-breaker.git
cd ssh-breaker
```
Run the script:

```Copy code
python SSHBreaker.py
```
Enter the following information when prompted:
```Target IP address (e.g., 192.168.1.10).
SSH port (default is 22).
SSH username.
Path to your password list file.
```

Example Usage

```Copy code
$ python SSHBreaker.py
Hedef IP: 192.168.1.10
Port (varsayılan: 22): 22
Kullanıcı adı: root
Parola dosyasının yolu: /path/to/password_list.txt
```

Sample Output:

```Copy code
[INFO] SSH Bruteforce başlatılıyor: 192.168.1.10:22 (Kullanıcı: root)
[DENEME] root:password123
[HATA] Şifre yanlış.
[DENEME] root:admin123
[BAŞARILI] Şifre bulundu: root:admin123
```
🤝 Contributing
If you'd like to contribute to SSH Breaker, follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes.
Commit your changes (git commit -am 'Add feature').
Push to the branch (git push origin feature-name).
Create a new Pull Request.

