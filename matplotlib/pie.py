import matplotlib.pyplot as plt
import numpy as np
man=71351
woman=68187
man_perc=man/(man+woman)
woman_perc=woman/(man+woman)
labels=['male','female'] # add label
colors=['blue','red']
# labels colors explode autopct shows the percentage
paches,texts,autotexts=plt.pie([man_perc,woman_perc],labels=labels,colors=colors,explode=(0,0.05),autopct='%0.1f%%')
# set the font color of pie
for text in autotexts:
    text.set_color('white')
#set the font size
for text in texts+autotexts:
    text.set_fontsize(20)
plt.show()