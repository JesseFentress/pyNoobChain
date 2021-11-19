
import hashlib

class Block:
  def __init__(self, index,hash, previousHash, data, timeStamp, nonce):
   self.index = index
   self.hash = hash
   self.previousHash = previousHash
   self.data = data
   self.timeStamp = timeStamp
   self.nonce = nonce
   
  def calculateHash(self):
   block = self.previousHash + self.timeStamp + self.nonce + data
   calculatedhash = hashlib.sha256(block.encode())
   return calculatedhash   

  def mineBlock(self, difficulty): 
   #target = StringUtil.getDificultyString(difficulty); 
   while not(hash[0: difficulty] == "0000"):
     self.nonce = self.nonce + 1
     self.hash = calculateHash();
   print("Block Mined!!! : ", self.hash)

  def getData(self):
    return self.data