
import hashlib
from datetime import datetime

class Block:

  def __init__(self, data: bytes, previous_hash: bytes):
    self.previous_hash: bytes = previous_hash
    self.data: bytes = data
    self.timestamp: datetime = datetime.now()
    self.nonce: int = 0
    self.hash: bytes = self.calculate_hash()
   
  def calculate_hash(self) -> bytes:
    block = self.previous_hash + str(self.timestamp).encode('utf-8') + str(self.nonce).encode('utf-8') + self.data
    sha256 =  hashlib.sha256()
    sha256.update(block)
    calculated_hash = sha256.digest()
    return calculated_hash   

  def mine_block(self, difficulty: int) -> None: 
    target = "".join(['0' for i in range(0, difficulty)]).encode('utf-8')
    while not (self.hash[0: difficulty] == target):
      self.nonce = self.nonce + 1
      self.hash = self.calculate_hash()
    print('Block Mined!!! : ', self.hash)

  def getData(self) -> str:
    return self.data
  
  
def main():
  b1 = Block(b"Hi im the first block", b"0") # Need previous hash to be bytes, should find good spot to encode
  print("hash for b:", b1.hash)
  b2 = Block(b"Hi im the second block", b1.hash)
  print("hash for b:", b2.hash)
  b3 = Block(b"Hi im the third block", b2.hash)
  print("hash for b:", b3.hash)
    
if __name__ == '__main__':
  main()