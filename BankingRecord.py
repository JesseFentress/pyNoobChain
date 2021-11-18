
class BankingRecord
  def __int__(self, accountNumber, accountType, transactionType, transactionAmount, balance)
    self.accountNumber = accountNumber
	self.accountType = accountType
	self.transactionType = transactionType
	self.transactionAmount = transactionAmount
	self.balance = balance

    //Now start setters and getters
    def getAccountNumber(self)
	  return self.accountNumber
    def setAccountNumber(self, _ActN)
	  self.accountNumber = _ActN
    def getAccountType() {return accountType
    def setAccountType(String _ActT) {this.accountType = _ActT
    def getTransactionType() {return transactionType
    def petTransactionType(String _TraT) {this.transactionType = _TraT
    def getTransactionAmount() {return transactionAmount
    def setTransactionAmount(String _TraA) {this.transactionAmount = _TraA
    def getBalance() {return balance
    def setBalance(String _Bal) {this.balance = _Bal
}