import matplotlib.pyplot as plt
#plt.rcdefaults()
import numpy as np

plt.style.use('bmh')

# Example data
#people = set(words_types)

x_pos = np.arange(len(list_of_languages))

barlist= plt.bar(x_pos, num_pos,  color='r', align='center', alpha=0.4)

for i in range(len(barlist)):
    if barlist[i].get_height() >=15:
        barlist[i].set_color('b')

plt.xticks(x_pos,lang_names  ,  rotation=45 )

#plt.xlabel('Performance')
#plt.title('How fast do you want to go today?')

plt.show()