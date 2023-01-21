from BankingRecord import BankingRecord
from Block import Block
from AES import AESEncryptor
import json

class NoobChain:
  
  def __init__(self, difficulty: int):
    NoobChain.blockchain: list[Block] = []    # Static list
    self.difficulty: int = 2                  # Blockchain difficulty

  def is_chain_valid(self) -> bool:
    target = "".join(['0' for i in range(0, self.difficulty)]).encode('utf-8')
    for index in range(1, len(NoobChain.blockchain) - 1):
      currentBlock = NoobChain.blockchain[index]
      previousBlock = NoobChain.blockchain[index - 1]
      if not (currentBlock.hash == currentBlock.calculate_hash()):
        print("Current Hashes not equal")
        return False
      if not (previousBlock.hash == currentBlock.previous_hash):
        print("Previous Hashes not equal")
        return False
      if not (currentBlock.hash[0 : self.difficulty] == target):
        print("This block hasn't been mined")
        return False
    return True

  def add_block(self, new_block: Block) -> None:
    NoobChain.blockchain.append(new_block)
  
def main():
  noobchain = NoobChain(4)
  secretKey = b"keykeykeykeykeykeykeykeykeykeyke"

  aes = AESEncryptor(secretKey) # Consider making the key a static variable so do not need to instantiate and object
  
  bankRecord = BankingRecord()
  bankRecord.setAccountNumber("1234")
  bankRecord.setAccountType("Savings")
  bankRecord.setTransactionType("Deposit")
  bankRecord.setTransactionAmount("100")
  bankRecord.setBalance("200")

  jsonBank = json.dumps(bankRecord.__dict__)
  encryptedBankRecord = aes.encrypt(jsonBank.encode('utf-8')) 
  print(encryptedBankRecord)
  b = Block(encryptedBankRecord, "0".encode('utf-8'))
  noobchain.add_block(Block(encryptedBankRecord, "0".encode('utf-8')))
  print("Trying to mine block 1...")
  noobchain.blockchain[0].mine_block(noobchain.difficulty)

  bankRecord2 = BankingRecord()
  bankRecord2.setAccountNumber("1235")
  bankRecord2.setAccountType("Checking")
  bankRecord2.setTransactionType("Deposit")
  bankRecord2.setTransactionAmount("1000")
  bankRecord2.setBalance("2000")
  
  jsonBank2 = json.dumps(bankRecord2.__dict__)
  encryptedBankRecord2 = aes.encrypt(jsonBank2.encode('utf-8'))
  noobchain.add_block(Block(encryptedBankRecord2, noobchain.blockchain[len(noobchain.blockchain) - 1].hash))
  print("Trying to mine block 2...")
  noobchain.blockchain[1].mine_block(noobchain.difficulty)
  
  bankRecord3 = BankingRecord()
  bankRecord3.setAccountNumber("1235232")
  bankRecord3.setAccountType("Checking")
  bankRecord3.setTransactionType("Deposit")
  bankRecord3.setTransactionAmount("100220")
  bankRecord3.setBalance("20030")
  
  jsonBank3 = json.dumps(bankRecord3.__dict__)
  encryptedBankRecord3 = aes.encrypt(jsonBank3.encode('utf-8'))
  noobchain.add_block(Block(encryptedBankRecord3, noobchain.blockchain[len(noobchain.blockchain) - 1].hash))
  print("Trying to mine block 3...")
  noobchain.blockchain[2].mine_block(noobchain.difficulty)
  
  print("\nBlockchain is Valid: " + str(noobchain.is_chain_valid()))

  blockchainJson = json.dumps([block.__dict__ for block in noobchain.blockchain]) # In order to do this the byte values in the Block objs need to be decoded to str
  print("\nThe block chain: ", blockchainJson)
  
if __name__ == '__main__':
  main()
