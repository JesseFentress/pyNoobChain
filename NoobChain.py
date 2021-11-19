import BankingRecord
import Block
import AES
import json


class NoobChain:

  blockchain = []
  difficulty = 5

  def __init__(self, blockchain, difficulty):
    self.blockchain = blockchain
    self.difficulty = difficulty

  def __main__(self):
   secretKey = "this is a password";
   print("Trying to Mine block 1... ")
   bankRecord = BankingRecord()
   bankRecord.setAccountNumber("1234")
   bankRecord.setAccountType("Savings")
   bankRecord.setTransactionType("Deposit")
   bankRecord.setTransactionAmount("100")
   bankRecord.setBalance("200")
   jsonBank = json.dumps(bankRecord)
   encryptedBankRecord = AES.encrypt(jsonBank, secretKey) 
   addBlock(Block(encryptedBankRecord, "0"))

   print("Trying to Mine block 2... ")
   bankRecord2 = BankingRecord()
   bankRecord2.setAccountNumber("1235")
   bankRecord2.setAccountType("Checking")
   bankRecord2.setTransactionType("Deposit")
   bankRecord2.setTransactionAmount("1000")
   bankRecord2.setBalance("2000")
   jsonBank = json.dumps(bankRecord2)
   encryptedBankRecord2 = AES.encrypt(jsonBank, secretKey)
   addBlock(Block(encryptedBankRecord2,blockchain.get(blockchain.len()-1).hash))

   print("\nBlockchain is Valid: " + isChainValid())
   blockchainJson = StringUtil.getJson(blockchain)
   print("\nThe block chain: ", blockchainJson);
   #for( x in blockchain):
     #print("\nDecrypted block data for block #" + (i+1) + ": " + AES.decrypt(blockchain.get(i).getData(), secretKey))

  def isChainValid(self):
    #hashTarget = new String(new char[difficulty]).replace('\0', '0')
    for index, b in enumerate(blockchain):
      currentBlock = b
      previousBlock = b[index-1]
      if(not(currentBlock.hash.equals(currentBlock.calculateHash()) )
        print("Current Hashes not equal")
        return false
      if(not(previousBlock.hash.equals(currentBlock.previousHash) ) 
        print("Previous Hashes not equal")
        return false;
     if(not(currentBlock.hash.substring( 0, difficulty).equals(hashTarget))
        print("This block hasn't been mined")
        return false
     return true

  def addBlock(newBlock)
    newBlock.mineBlock(difficulty)
    blockchain.add(newBlock)
  