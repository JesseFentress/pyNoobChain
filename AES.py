
import 

class AES
  def __init__(self, secretKey, key)
    self.secretKey = secretKey
	self.key = key

  def setKey(self, myKey)
    MessageDigest sha = null
     try
       self.key = myKey.getBytes("UTF-8")
       sha = MessageDigest.getInstance("SHA-1")
       self.key = sha.digest(self.key)
       self.key = Arrays.copyOf(self.key, 16)
       self.secretKey = new SecretKeySpec(self.key, "AES")
     except
	   print("Log excpetion: ", sys.exc_info()[0])
	 
  def encrypt(self, strToEncrypt, secret)
    try
      setKey(secret)
      cipher = Cipher.getInstance("AES/ECB/PKCS5Padding")
      cipher.init(Cipher.ENCRYPT_MODE, secretKey)
      return Base64.getEncoder().encodeToString(cipher.doFinal(strToEncrypt.getBytes("UTF-8")))
   except(Exception e)
      print("Error while encrypting: ", e.toString())
      return null

  def decrypt(self, strToDecrypt, secret)
      try
        setKey(secret)
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5PADDING")
        cipher.init(Cipher.DECRYPT_MODE, secretKey);
        return new String(cipher.doFinal(Base64.getDecoder().decode(strToDecrypt)))
	  except
	    print("Log excpetion: ", sys.exc_info()[0])
        return null

