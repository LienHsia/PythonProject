def __init__(self,list,money):
	self.list = list
	self.money = money

def __str__(self):
	msg = ""
	for dict in list:
		for key in dict.keys():
			if key == 'brand':
				msg += "品牌："+dict[key]+','
			if key == 'price':
				msg += "单价：%d"%dict[key]+','
			if key == 'count':
				msg += "库存：%d"%dict[key]+','
		msg = msg.strip(',')
		msg+='\n'
	msg += '店铺余额：%d'%self.money
	return msg

def search_computer(self):
	a = 1#假设当前查找的电脑不存在
	print('请输入要查找的电脑品牌：')
	brand = input()
	for dict in list:
		if brand in dict.values():
			print('您要查找的品牌为%s，单价为%d'%(dict['brand'],dict['price']))
			a = 2
			break
	if a == 1:
		print('对不起，本店没有您要的电脑品牌！')


def sell_computer(self):
	isExist = False
	print('请输入您要购买的电脑品牌：')
	brand = input()
	for dict in list:
		if brand in dict.values():
			print('您要查找的品牌为%s，单价为%d'%(dict['brand'],dict['price']))
			count = dict['count']
			if count == 0:
				print('对不起，该品牌的电脑暂时无货')
			else:
				print('恭喜您购买成功，付款%d元'%dict['price'])
				dict['count'] = count - 1
				self.money += dict['price']
				isExist = True
				break
	if not isExist:
		print('对不起，本店没有您要的电脑品牌！')

def buy_computer(self):
	canBuy = False
	print('请输入您要进货的电脑品牌：')
	brand = input()
	for dict in list:
		if brand in dict.values():
			canBuy = True
			break
	if canBuy:
		number = int(input('请输入进货数量：'))
		for dict in list:
			if brand in dict.values():
				totalPrice = (dict['price'] - 1000) * number
				print('总价为：%d'%totalPrice)
				break
		if totalPrice > self.money:
			print('对不起，您的金额不足！')
		else:
			self.money -= totalPrice
			for dict in list:
				if brand in dict.values():
					dict['count'] += number
					break
	else:
		print('您要进货的品牌不再授权范围内！')
