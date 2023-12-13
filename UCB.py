import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#loc = "dataset.csv"

def UCB(loc):
    data = pd.read_csv(loc)
    
    N = len(data)
    I = len(data.columns)

    clickCount = [0] * I
    prizeCount = [0] * I
    selectedList = []
    total = 0

    for n in range(0, N):
      selected = 0
      maxUCB = 0
      for i in range(0, I):
          if clickCount[i] > 0:
              mean = prizeCount[i] / clickCount[i]
              delta = math.sqrt(3/2 * math.log(n) / clickCount[i])
              ucb = mean + delta
          else:
              ucb = N * 10
          if maxUCB < ucb:
              maxUCB = ucb
              selected = i

      selectedList.append(selected)
      clickCount[selected] = clickCount[selected] + 1
      prize = data.values[n, selected] #Datadaki n. satır = 1 ise ödül 1
      prizeCount[selected] = prizeCount[selected] + prize
      total = total + prize

    print("Total Prize: ", total)

    plt.hist(selectedList)
    plt.show()
