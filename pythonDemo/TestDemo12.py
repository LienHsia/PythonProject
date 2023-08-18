from datetime import datetime
class Medicine:
    name = ''
    price = 0
    PD = ''
    Exp = ''
    def __init__(self, name, price, PD, Exp):
        self.name = name
        self.price = price
        self.PD = PD
        self.Exp = Exp
    def get_name(self):
        return self.name
    def get_GP(self):
        start = datetime.strptime(self.PD, '%Y-%m-%d')
        end = datetime.strptime(self.Exp, '%Y-%m-%d')
        return (end - start).days
medicine = Medicine(name='格列宁', price=2000, PD='2022-2-22', Exp='2023-2-21')
name = medicine.get_name()
GP = medicine.get_GP()
print('药品名称:{}'.format(name))
print('药品保质期:{}天'.format(GP))
