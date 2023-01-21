from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

class AESEncryptor:

  def __init__(self, key: str):
    self._key: str = key                                    # Encryption key
    self._cipher = AES.new(self._key, AES.MODE_EAX)         # Encryption cipher
    self._iv: bytes = get_random_bytes(16)                  # Initialization vector

  def encrypt(self, data: bytes) -> bytes:
    cipher = AES.new(self._key, AES.MODE_EAX, self._iv)
    cipher_text = cipher.encrypt(pad(data, 16))
    return cipher_text

  def decrypt(self, encrypted_data: bytes) -> bytes:
    cipher = AES.new(self._key, AES.MODE_EAX, self._iv)
    data = unpad(cipher.decrypt(encrypted_data), 16)
    return data
  

def main():
  keyAES = b"keykeykeykeykeykeykeykeykeykeyke"
  message = "Come over here Waston"
  aes = AESEncryptor(keyAES)
  
  e = aes.encrypt(message.encode('utf=8'))
  print(e) 
  
  d = aes.decrypt(e)
  print(d)
  
  print(message == d.decode('utf-8'))
  
if __name__ == '__main__':
  main()
  
    
    