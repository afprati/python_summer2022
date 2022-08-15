# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

class Portfolio:
    def __init__(self):
        self.cash = 0
        self.stocks = {}
        self.stock_prices = {}
        self.mutualFunds = {}
        self.hist = []
    def addCash(self, money):
        #self.cash = self.cash + money
        self.cash += money
        self.hist.append(f"Cash added: {money}")
    def withdrawCash(self, money):
        if self.cash >= money:
            self.cash -= money
            self.hist.append(f"Cash withdrawn: {money}")
        else:
            raise Exception("Not enough money on account!")
    def buyStock(self,stock_number, stock):
        cost = stock_number * stock.getPrice()
        if self.cash >= cost:
            self.cash -= cost
            self.stocks[stock.getSymbol()] = self.stocks.get(stock.getSymbol(),0) + stock_number
            self.stock_prices[stock.getSymbol()] = stock.getPrice()
            self.hist.append(f"{stock_number} stock {stock.getSymbol()} purchased")
        else:
            raise Exception("Not enough money on account to buy stock!")
    def sellStock(self, symbol, stock_number):
        stock_available = self.stocks.get(symbol,0)
        if stock_available >= stock_number:
            buy_price = self.stock_prices[symbol]
            stock_price = random.uniform(0.5*buy_price, 1.5*buy_price )
            self.cash += stock_price*stock_number
            self.stocks[symbol] -= stock_number
            self.hist.append(f"{stock_number} stocks {symbol} sold at ${stock_price} each stock")
        else:
            raise Exception("Lorem ipsum")
    def buyMutualFund(self, stock_number, mf):
        cost = stock_number * mf.getPrice()
        if self.cash >= cost:
            self.cash -= cost
            self.mutualFunds[mf.getSymbol()] = self.mutualFunds.get(mf.getSymbol(),0) + stock_number
            self.hist.append(f"{stock_number} mutual fund {mf.getSymbol()} purchased")
        else:
            raise Exception("Not enough money on account to buy mutual fund!")
    def sellMutualFund(self, symbol, stock_number):
        stock_available = self.mutualFunds.get(symbol,0)
        if stock_available >= stock_number:
            stock_price = random.uniform(0.9,1.2)
            self.cash += stock_price*stock_number
            self.mutualFunds[symbol] -= stock_number
            self.hist.append(f"{stock_number} mutual fund {symbol} sold at ${stock_price} each stock")
        else:
            raise Exception("Not enough stocks!")
    
    def history(self):
        for i, tx in enumerate(self.hist):
            print(f"{i}:: {tx}")

    def __str__(self):
        p = f"""
        Portfolio:
            Cash: ${self.cash}
            Stock: {self.stocks}
            Mutual funds: {self.mutualFunds}
        """
        return p
class Stock:
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol
    def getPrice(self):
        return self.price
    def getSymbol(self):
        return self.symbol

class MutualFund(Stock):
    def __init__(self, symbol):
        self.symbol = symbol
        self.price = 1
        

portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.sellMutualFund("BRT", 3)
portfolio.sellStock("HFH", 1)
portfolio.history()






