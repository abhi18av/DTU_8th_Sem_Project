import numpy as np
import matplotlib.pyplot as plt

plt.style.use('bmh')
%matplotlib inline 

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 14
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size



lang_names=[]
for i in range(len(list_of_languages)):
    lang_names.append((list_of_languages[i][0]))



import matplotlib.pyplot as plt
#plt.rcdefaults()
import numpy as np

plt.style.use('bmh')

# Example data
#people = set(words_types)

x_pos = np.arange(len(list_of_languages))

plt.bar(x_pos, num_pos,  color='r', align='center', alpha=0.4)

plt.xticks(x_pos,lang_names  ,  rotation=45 )

#plt.xlabel('Performance')
#plt.title('How fast do you want to go today?')

plt.show()
