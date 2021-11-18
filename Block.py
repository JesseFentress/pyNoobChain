
import hashlib

class Block
  def __init__(self, index,hash, previousHash, data, timeStamp, nonce)
   self.index = index
   self.hash = hash
   self.previousHash = previousHash
   self.data = data
   self.timeStamp = timeStamp
   self.nonce = nonce
   
  def calculateHash(self)
   block = self.previousHash + self.timeStamp + self.nonce + data
   calculatedhash = hashlib.sha256(block.encode())
   return calculatedhash   
   