class Coin(object):
    def __init__(self,coin,value,change_rate,market_cap,today_high,today_low):
        self.__coin = coin
        self.__value = value
        self.__change_rate = change_rate
        self.__market_cap = market_cap
        self.__today_high = today_high
        self.__today_low = today_low

    def get_coin(self):
        return self.__coin

    def set_coin(self,newcoin):
        self.__coin = newcoin

    def get_val(self):
        return self.__value

    def get_rate(self):
        return self.__change_rate

    def get_cap(self):
        return self.__market_cap

    def get_24high(self):
        return self.__today_high

    def get_24low(self):
        return self.__today_low

    def __repr__(self):
        return ('Current value of {} with respect to USD is: '.format(self.__coin) + self.__value +'\n'
                '24 Hour change rate of {} is: '.format(self.__coin) + self.__change_rate + '\n'
        'Market capacity of the {} is: '.format(self.__coin) + self.__market_cap + '\n'
        'Highest value of {} today is: '.format(self.__coin) + self.__today_high + '\n'
        'Lowest value of {} today is: '.format(self.__coin) + self.__today_low)

