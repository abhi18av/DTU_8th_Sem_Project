# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 08:43:26 2016

@author: user
"""

#import nltk
# eo_words = nltk.corpus.udhr.word_tokenizer('Esperanto-UTF8')
# eo_words = nltk.corpus.udhr.raw('Esperanto-UTF8')
# eo_words
#print(eo_words)

######################################

""" 
English

English-Latin1

"""

import nltk

nltk.pos_tag(nltk.corpus.udhr.words('English-Latin1'))



######################################
""" 
Esperanto
Esperanto-UTF8
"""
import nltk
eo_words = nltk.corpus.udhr.words('Esperanto-UTF8')
nltk.pos_tag(eo_words)

#######################################

""" 
German
German_Deutsch-Latin1
"""

import nltk

nltk.pos_tag(nltk.corpus.udhr.words('German_Deutsch-Latin1'))


######################################



""" 
French

French_Francais-Latin1

"""

import nltk

nltk.pos_tag(nltk.corpus.udhr.words('French_Francais-Latin1'))

######################################


""" 
Russian

Russian-UTF8
Russian_Russky-Cyrillic
Russian_Russky-UTF8

"""


import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Russian-UTF8'))

######################################

"""
Farsi

Farsi_Persian-UTF8
Farsi_Persian-v2-UTF8

"""

## something is wrong as most words are just NNP !!!!
import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Farsi_Persian-UTF8'))

######################################


""" 
Finnish

Finnish_Suomi-Latin1

"""

import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Finnish_Suomi-Latin1'))

######################################

"""
Hungarian

Hungarian_Magyar-Latin1
Hungarian_Magyar-Latin2
Hungarian_Magyar-UTF8
"""

import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Hungarian_Magyar-Latin1'))

######################################
""" 
Turkish

Turkish_Turkce-Turkish
Turkish_Turkce-UTF8

"""


import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Turkish_Turkce-Turkish'))

######################################

""" 
Mongolian

Mongolian_Khalkha-Cyrillic
Mongolian_Khalkha-UTF8

"""

import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Mongolian_Khalkha-Cyrillic'))


######################################

""" 
Chinese

Chinese_Mandarin-GB2312

"""

## SEEMS WRONG!

import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Chinese_Mandarin-GB2312'))



######################################

""" 
Japanese


Japanese_Nihongo-EUC 
Japanese_Nihongo-SJIS
Japanese_Nihongo-UTF8
"""

import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Japanese_Nihongo-EUC'))




######################################

""" 
Korean

Korean_Hankuko-UTF8

"""


import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Korean_Hankuko-UTF8'))


######################################


""" 
Hebrew

Hebrew_Ivrit-Hebrew
Hebrew_Ivrit-UTF8

"""


import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Hebrew_Ivrit-Hebrew'))


######################################


"""
Hindi

Hindi-UTF8
Hindi_web-UTF8
"""


import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Hindi-UTF8'))


#######################################


"""
Kazakh

Kazakh-Cyrillic
Kazakh-UTF8

"""


import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Kazakh-UTF8'))



#######################################

"""
Swedish

Swedish_Svenska-Latin1

"""


import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Swedish_Svenska-Latin1'))


#######################################


"""
Icelandic

Icelandic_Yslenska-Latin1

"""

import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Icelandic_Yslenska-Latin1'))

#######################################

"""
Sanskrit 
Sanskrit-UTF8

"""


import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Sanskrit-UTF8'))

########################################

"""
Latin

Latin_Latina-Latin1
Latin_Latina-v2-Latin1

"""

import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Latin_Latina-Latin1'))

#######################################

"""
Greek

Greek_Ellinika-Greek
Greek_Ellinika-UTF8

"""


import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Greek_Ellinika-Greek'))


######################################

"""

Swahili

Swaheli-Latin1
Swahili_Kiswahili-Latin1

"""


import nltk

nltk.pos_tag(nltk.corpus.udhr.words('Swahili_Kiswahili-Latin1'))


########################################


"""

Chechewa_Nyanja-Latin1


Mayan_Yucateco-Latin1


'Miskito_Miskito-Latin1',
 'Mixteco-Latin1',
 
'Nahuatl-Latin1'

 Quechua-Latin1
 
"""

###############################################

###################
##################
################
##################
################




tagged_token = '''Sur/IN tiu/DT dolca/JJ tero/NNS vivas/VBP jam/RB de/IN miljaroj/NNP unu/CD el/IN plej/RB malnovaj/JJ gentoj/NNP de/IN
la/DT aria/JJ mondo./NNS En/IN la/DT norda/JJ parto/NNS estas/VBP parolata/JJ ankorau/RB la/DT antikva/JJ
lingvo/NNS litova,/JJ proksima/JJ a /IN la/DT sanskrita./JJ En/IN puraj/JJ moroj/NNP kaj/CC popolaj/JJ
kantoj/NNP iel/RB regas/VBP atmosfero/NNS mistera/JJ kun/IN influoj/NNP pensigaj/JJ al/IN Hindujo/NNS pratempa./JJ'''

[nltk.tag.str2tuple(t) for t in tagged_token.split()]

#############################
############################
##############################
##############################
############################

text = '''
Longe/RB vivadis/VBD en/IN paco/NNS tiu/DT gento/NNS trankvila,/JJ de/IN Kristanismo/NNS netusita/JJ gis/IN
dek-tria/dek-tria jarcento./NNS De/IN la/DT cetera/JJ mondo/NNS forkasita/JJ per/IN marcoj/NNP kaj/CC densaj/JJ
arbaregoj,/NNP kie/RB kuras/VBP gis/IN nun/VB sovagaj/JJ urbovoj,/NNP la/DT popolo/NNS dauris/VBD adori/ii la/DT
fortojn/NNP de/IN la/DT naturo/NNS sub/IN gigantaj/JJ kverkoj,/NNP vivanta/JJ templo/NNS de/IN la/DT dioj./NNP

Tie/RB tamen/RB ekbatalis/VBD okcidenta/JJ volo/NNS kun/IN orienta/JJ pacienco./NNS En/IN la/DT mezepoko/NNS
teutonaj/JJ kavaliroj/NNP tiun/DT landon/NNS almilitis,/VBD polaj/JJ nobeloj/NNP gin/PRP ligis/VBD al/IN sia/PRP$
stato,/NNS moskova/JJ caro/NNS gin/PRP atakis./VBD Dume/RB alkuradis/VBD el/IN tuta/JJ mondo/NNS
persekutataj/JJ Hebreoj/NNP por/IN starigi/ii manlaboron/NNS kaj/CC komercon/NNS lau/IN invito/NNS
rega./JJ Tiel/RB alia/JJ gento/NNS tre/RB maljuna/JJ trovis/VBD tie/RB novan/JJ Palestinon/NNS kaj/CC fondis/VBD
urbojn/NNP au/CC plenigis/VBD ilin./PRP'''

[nltk.tag.str2tuple(t) for t in text.split()]


#############################################




import nltk

en_words = nltk.pos_tag(nltk.corpus.udhr.words('Icelandic_Yslenska-Latin1'))

en_words_types = []
for i in range(len(en_words)):
    en_words_types.append(en_words[i][1])
    
print(set(en_words_types))





list_of_languages = [


['English', ['English-Latin1'] ]
,['Esperanto', ['Esperanto-UTF8']]
,['German', ['German_Deutsch-Latin1']]
,['French', ['French_Francais-Latin1']]
,['Russian', ['Russian-UTF8','Russian_Russky-Cyrillic','Russian_Russky-UTF8']]
,['Farsi', ['Farsi_Persian-UTF8', 'Farsi_Persian-v2-UTF8']]
,['Finnish',['Finnish_Suomi-Latin1']]
,['Hungarian',['Hungarian_Magyar-Latin1','Hungarian_Magyar-Latin2','Hungarian_Magyar-UTF8']]
,['Turkish', ['Turkish_Turkce-Turkish','Turkish_Turkce-UTF8']]
,['Mongolian', ['Mongolian_Khalkha-Cyrillic','Mongolian_Khalkha-UTF8']]
,['Chinese',['Chinese_Mandarin-GB2312']]
,['Japanese',['Japanese_Nihongo-EUC','Japanese_Nihongo-SJIS','Japanese_Nihongo-UTF8']]
,['Korean',['Korean_Hankuko-UTF8']]
,['Hebrew',['Hebrew_Ivrit-Hebrew','Hebrew_Ivrit-UTF8']]
,['Hindi',['Hindi-UTF8','Hindi_web-UTF8']]
,['Kazakh',['Kazakh-Cyrillic','Kazakh-UTF8']]
,['Swedish',['Swedish_Svenska-Latin1']]
,['Icelandic' ,['Icelandic_Yslenska-Latin1']]
,['Sanskrit ' ,['Sanskrit-UTF8']]
,['Latin',['Latin_Latina-Latin1', 'Latin_Latina-v2-Latin1']]
,['Greek', ['Greek_Ellinika-Greek', 'Greek_Ellinika-UTF8']]
,['Swahili', ['Swaheli-Latin1','Swahili_Kiswahili-Latin1']]


]



for i in range(len(list_of_languages)):
    print(list_of_languages[i][0])
    
    



####################################


import nltk

for i in range(len(list_of_languages)):
    print(list_of_languages[i][0])
    words = nltk.pos_tag(nltk.corpus.udhr.words(list_of_languages[i][1][0]))

    words_types = []
    for i in range(len(words)):
        words_types.append(words[i][1])
    
    print(set(words_types))

    print("\n\n\n\n\n\n\n")


"""
for removing the non-alphanumeric characters

cadena = re.sub(r'[^0-9a-zA-Z\\/@+\-:,|#]+', '', cadena)


"""


#####################
#####################
#####################


"""

Working on graphs now

"""
#############################
"""
Simple demo of a horizontal bar chart.
"""
import matplotlib.pyplot as plt
#plt.rcdefaults()
import numpy as np

plt.style.use('bmh')

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 5 + 10 * np.random.rand(len(people))


plt.bar(y_pos, performance,  align='center', alpha=0.4)
plt.yticks(y_pos, people)

plt.xlabel('Performance')
plt.title('How fast do you want to go today?')

plt.show()


################################

import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (20, 35, 30, 35, 27)
#menStd = (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r')

#womenMeans = (25, 32, 34, 20, 25)
#womenStd = (3, 5, 2, 3, 3)
#rects2 = ax.bar(ind + width, womenMeans, width, color='y')

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

## error with the legends
#ax.legend()
#ax.legend(loc='upper center', shadow=True)

#def autolabel(rects):
#    # attach some text labels
#    for rect in rects:
#        height = rect.get_height()
#        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
#                '%d' % int(height),
#                ha='center', va='bottom')

#autolabel(rects1)
#autolabel(rects2)

plt.show()