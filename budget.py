class Category:
	def __init__(self, name):
		self.name=name
		self.ledger=[]

	def deposit(self, amount, description=""):
		self.ledger.append({"amount": amount, "description": description})

	def withdraw(self, amount, description=""):
		if (self.check_funds(amount)):
			self.ledger.append({"amount": -amount, "description": description})
			return True
		return False

	def get_balance(self):
		balance=0
		for o in self.ledger:
			balance+=o["amount"]
		return balance

	def transfer(self,amount,target):
		if(self.check_funds(amount)):
			self.withdraw(amount,"Transfer to "+target.name)
			target.deposit(amount,"Transfer from "+self.name)
			return True
		return False

	def check_funds(self,amount):
		if (self.get_balance()>=amount):
			return True
		return False

	def __str__(self):
		s=f"{self.name:*^30}\n"
		for val in self.ledger:
			s=f"{s}{val['description'][:23]:<23}{val['amount']:>7.2f}\n"
		s=s+"Total: "+"{:.2f}".format(self.get_balance())
		return s
		
def create_spend_chart(categories):
	p="Percentage spent by category\n"
	for number in range(100, -1, -10):
		p=p+f"{number:>3d}|"+" "*(len(categories)*3+1)+"\n"
	p=p+" "*4+"-"*(len(categories)*3+1)+"\n"
	max=CountMaxName(categories)
	for i in range(0, max, 1):
		p=p+" "*(len(categories)*3+5)+"\n"
	p=p[:-1]
	spent=[]
	for o in categories:
		a=0
		for l in o.ledger:
			if(l["amount"]<0):
				a+=(-l["amount"])
		spent.append(a)
	totalSpent=sum(spent)
	spentP=[]
	for s in spent:
		spentP.append(s/totalSpent)
	pL=list(p)
	for i in range(0,len(spentP)):
		e=0
		for p in range(100,-1,-10):
			if(spentP[i]*100>=p):
				pL[28+(len(spentP)*3+6)*e+6+i*3]="o"
			e=e+1
		for c in categories[i].name:
			e=e+1
			pL[28+(len(spentP)*3+6)*e+6+i*3]=c
	return("".join(pL))
def CountMaxName(categories):
	max=0
	for o in categories:
		if(len(o.name)>max):
			max=len(o.name)
	return max