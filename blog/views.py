class MagicBank:
    money = 1000
    
    @classmethod
    def add_money(cls):
        some = int(input('введи тогда число'))
        amount = some
        cls.reduce_money(amount)

    
    @classmethod
    def reduce_money(cls, amount):
        cls.amount = amount
        if cls.amount > 1000:
            print('Нельзя тратить больше 1000 за один раз')
            cls.add_money()
        else:
            print(f"Покупка на сумму {amount} осуществлена")
            



# код ниже пожалуйста не удаляйте 
masha = MagicBank()
masha.reduce_money(100)
masha.reduce_money(999)
masha.reduce_money(1000000000)