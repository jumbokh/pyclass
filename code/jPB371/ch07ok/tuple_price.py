money = [['書籍', 250, 480, 365],
	 ['音樂CD', 450, 380, 600],
	 ['POLO上衣', 680, 390, 480]]

for(product, price1, price2, price3) in money:
    print('%6s'%product,' 三次購買價格總和:',
              (price1 + price2 + price3))
