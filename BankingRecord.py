
class BankingRecord:
  
  def __init__(self):
   self.accountNumber: str
   self.accountType:str
   self.transactionType:str
   self.transactionAmount:str 
   self.balance: str

  def getAccountNumber(self):
    return self.accountNumber
  
  def setAccountNumber(self, _ActN):
    self.accountNumber = _ActN
    
  def getAccountType(self):
    return self.accountType
  
  def setAccountType(self, _ActT):
   self.accountType = _ActT
   
  def getTransactionType(self):
   return self.transactionType
 
  def setTransactionType(self, _TraT):
   self.transactionType = _TraT
   
  def getTransactionAmount(self):
   return self.transactionAmount
 
  def setTransactionAmount(self, _TraA):
   self.transactionAmount = _TraA
   
  def getBalance(self):
   return self.balance
 
  def setBalance(self, _Bal):
   self.balance = _Bal
