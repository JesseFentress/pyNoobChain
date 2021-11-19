import BankingRecord
import AES
import json

class NoobChain
  def __init__(self, blockchain, difficulty)
    self.blockchain = blockchain;
	self.difficulty = difficulty

#ArrayList<Block> blockchain = new ArrayList<Block>();
#public static int difficulty = 5

  def __main__(self) {
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
   addBlock(new Block(encryptedBankRecord, "0"))

   print("Trying to Mine block 2... ")
   bankRecord2 = BankingRecord()
   bankRecord2.setAccountNumber("1235")
   bankRecord2.setAccountType("Checking")
   bankRecord2.setTransactionType("Deposit")
   bankRecord2.setTransactionAmount("1000")
   bankRecord2.setBalance("2000")
   jsonBank = json.dumps(bankRecord2)
   encryptedBankRecord2 = AES.encrypt(jsonBank, secretKey)
   addBlock(new Block(encryptedMedicalRecord2,blockchain.get(blockchain.size()-1).hash))

   print("\nBlockchain is Valid: " + isChainValid())
   blockchainJson = StringUtil.getJson(blockchain)
   print("\nThe block chain: ", blockchainJson);
   for(int i = 0; i < blockchain.size(); i++):
     print("\nDecrypted block data for block #" + (i+1) + ": " + AES.decrypt(blockchain.get(i).getData(), secretKey))


    //method for checking the integriy of the blockchain
  def isChainValid(self)
    currentBlock;
    previousBlock;
    hashTarget = new String(new char[difficulty]).replace('\0', '0')
    for(int i=1; i < blockchain.size(); i++)
      currentBlock = blockchain.get(i)
      previousBlock = blockchain.get(i-1)
      if(!currentBlock.hash.equals(currentBlock.calculateHash()) )
        print("Current Hashes not equal")
        return false
      if(!previousBlock.hash.equals(currentBlock.previousHash) ) 
        print("Previous Hashes not equal")
        return false;
     if(!currentBlock.hash.substring( 0, difficulty).equals(hashTarget))
        print("This block hasn't been mined")
        return false
     return true

  def addBlock(newBlock)
    newBlock.mineBlock(difficulty)
    blockchain.add(newBlock)
  