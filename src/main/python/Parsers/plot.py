import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 9
data_g1 = (90, 55, 40, 65, 0, 12, 33, 44, 55)
data_gss = (85, 62, 54, 20, 14, 0, 32, 66, 33)
data_ss = (44,33,23,11, 55, 22, 43, 54, 11)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8

rects1 = plt.bar(index, data_ss, bar_width,
                 alpha=opacity,
                 color='b',
                 label='SemiS_Maxine')

rects2 = plt.bar(index + bar_width, data_gss, bar_width,
                 alpha=opacity,
                 color='g',
                 label='GenSS_Maxine')

rects3 = plt.bar(index + 2*bar_width, data_g1, bar_width,
                 alpha=opacity,
                 color='r',
                 label='G1_HotSpot')

plt.xlabel('Specjvm2008')
plt.ylabel('Total collection time (ms)')
plt.title('Heap Size 64MB')
plt.xticks(index + bar_width, ('Compiler','Compress','Crypto','Derby','Mpegaudio','Scimark.large','Serial','Sunflow','Xml'))
plt.legend()

plt.tight_layout()
plt.show()
