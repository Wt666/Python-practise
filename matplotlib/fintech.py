import numpy as np
import matplotlib.pyplot as plt
def simpmarket(win_rate, play_cnt=1000, stock_num=9, position=0.01, commission=0.01, lever=False):
        my_money = np.zeros(play_cnt)
        my_money[0] = 1000
        lose_count = 1
        binomial = np.random.binomial(stock_num, win_rate, play_cnt)
        #print(binomial)
        for i in range(1, play_cnt):
            if my_money[i-1] * position * lose_count <= my_money[i-1]: # enough money
                once_chip = my_money[i-1] * position * lose_count
            else:
                break
            if binomial[i] > stock_num//2: # half stock will rise
                # if lever == False ,result is true than we don't rise the bet，my_money[i] = my_money[i-1] + once_chip
                # if lever == False result is true than we rise the bet，my_money[i] = my_money[i-1] + once_chip*lose_count
                my_money[i] = my_money[i-1] + once_chip if lever == False else my_money[i-1] + once_chip*lose_count
                lose_count = 1
            else:
                my_money[i] = my_money[i-1] - once_chip if lever == False else my_money[i-1] - once_chip*lose_count
                lose_count += 1
            my_money[i] -= commission
            #print("lose",lose_count)
            #print("money",my_money[i])
            if my_money[i] <= 0:
                break
        return my_money
trader = 50
_ = [plt.plot(np.arange(1000), simpmarket(0.5, play_cnt=1000,  stock_num=9, commission = 0)) \
                                                                for _ in np.arange(0,trader)]
_ = plt.hist([simpmarket(0.5, play_cnt=1000, stock_num=9, commission = 0)[-1] \
                                                              for _ in np.arange(0, trader)], bins=30)
plt.xlim(0,1000)
plt.show()