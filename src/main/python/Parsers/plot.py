import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 9
data_g1 = (168131,3460,77705,174639,10669,11673,134755,83153,195725)
data_gss = (94796,2695,33608,91646,5347,7969,61245,60995,96728)
data_ss = (66279,2393,35739,37166,5440,7876,42965,45004,65973)

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
plt.ylabel('Total Reclaimed (MB)')
plt.title('Heap Size 1024MB')
plt.xticks(index + bar_width, ('Compiler','Compress','Crypto','Derby','Mpegaudio','Scimark.large','Serial','Sunflow','Xml'))
plt.legend()

plt.tight_layout()
plt.show()
