import twstock

# 取得上市股票代碼
all_stocks = twstock.twse                #{()'2330', StockCodeInfo(type, code, name, ISIN, start, market, group, CFI )}
print('all_stocks type = ',type(all_stocks))  # dict 
#print('all_stocks = ',all_stocks)
print(type(all_stocks['2330']))         #<class 'twstock.codes.codes.StockCodeInfo'>
print(all_stocks['2330'].name)          # Tupples in dictionary


all_stocks_view = all_stocks.items()
print('all_stocks_view type = ',type(all_stocks_view))   #all_stocks_view type =  <class 'dict_items'>. This is iterable and can be accessed by the for...loop

#print('all_stocks_view = ',all_stocks_view)  #all_stocks_view =  dict_items([ (),().....]) Tupple in list
for code , info in all_stocks_view:
    if code == '2317':print(code,info)



stock_codes = ['2317', '2330', '2357']

results = []
stock_dict = {}
for i in stock_codes:
    stock = twstock.codes[i]
    results.append({
        'code': stock.code,
        'name': stock.name,
        'market': stock.market,
        'group': stock.group
    })


#print(results)


person = {
    'name': 'Amy',
    'age': 30,
    'city': 'Taipei'
}

print('Person.items()= ',person.items())

for key, value in person.items():
    print(f"Key: {key}, Value: {value}")
