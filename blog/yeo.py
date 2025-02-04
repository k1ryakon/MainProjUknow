def cache(func):
    def wrapper(product):
        some = []
        for i in product.split():
            if i not in some:
                gega = i + ' from db'
                some.append(i + ' from db')
                print(gega)
            else:
                goga = i + ' from cache'
                some.append(i + ' from cache')
                print(goga)       
    return wrapper



@cache
def anjy(product):
    return product

aga = anjy('Помидоры Огурцы Помидоры Картошка')
print(aga)