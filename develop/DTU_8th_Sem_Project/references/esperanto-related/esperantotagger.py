#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Rule-based tagger for Esperanto. Andreas van Cranenburgh, 2008
#
# Tagset based on Penn treebank tagset, see:
# ftp://ftp.cis.upenn.edu/pub/treebank/doc/tagguide.ps.gz
import codecs, operator, locale, sys
#sys.stdout = codecs.EncodedFile(sys.stdout, 'utf-8')
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
sys.stderr = codecs.getwriter(locale.getpreferredencoding())(sys.stderr)

#Closed word classes:
#personal pronouns
PRP = set(u"mi vi li ŝi ĝi ni ili oni si ci mem".split())
#possesive pronouns
PRPd = set(u"mia via lia ŝia ĝia nia ilia onia sia cia".split())
#adverbs [that do not end with -e]
RB = set(u"tie ie ĉie nenie tiam iam ĉiam neniam iel tiel ĉiel neniel ial tial ĉial iom ĉiom tiom neniom ajn mem jen ja tamen eĉ dum jam ĵus plu ĉi for nun nur tre tro tuj ne jes ju des".split())
#wh-adverbs
WRB = set(u"kiel kiam kial kiom".split())
#coordinating conjunctions
CC = set(u"kaj aŭ nek kvankam sed ĉar".split())
#prepositions and subordinating conjunctions
IN = set(u"antaŭ malantaŭ anstataŭ do dum en laŭ krom kun malgraŭ se ke al apud ĉe ĉirkaŭ kontraŭ preter de da je el ĝis ekster inter po por post per pri sen sub super sur tra trans".split())
#determiners
DT = set(u"la kiu iu ĉiu tiu kies ies ties ĉies kia tia ia ĉia".split())
#numbers written out
NUMBER = set("unu du tri kvar kvin ses sep ok naŭ dek cent mil dudek tridek kvardek kvindek sesdek sepdek okdek naŭdek ducent tricent kvarcent kvincent sescent sepcent okcent naŭcent dumil trimil kvarmil kvinmil sesmil sepmil okmil naŭmil dekmil centmil".split())
JJR = set("pli malpli ol plej".split())

def main():
	#filename to read:
	corpus = "/dev/stdin"
	#read corpus as one string:
	corpus = codecs.open(corpus, encoding='utf-8').read()
	#split punctuation:
	corpus = corpus.replace(',', ' ,').replace('.', ' .')
	corpus = corpus.replace('"', ' " ').replace(';', ' ;')
	corpus = corpus.replace('---', ' --- ').replace('--', ' -- ')

	#first split lines, then split words:
	corpus = [a.split() for a in corpus.splitlines()]
	
	tagged, untagged = [], []
	unigram = {}
	
	for line in corpus:
		result = []
		for word in line:
			result.append((word, tag(word)))
			if tag(word) == u'none':
				untagged.append(word)
		tagged.append(result)

	for line in tagged:
		for wordtag in line:
			print "%s/%s" % wordtag,
		print

	sys.stderr.write("untagged words:\n")
	for a in set(untagged): sys.stderr.write("%s " % a)

	N = sum([len(line) for line in corpus])
	u = len(untagged)
	sys.stderr.write("\n\n word count %d, tagged %d = %f%%, untagged %d\n" 
	  % (N, N - u, (N - u) / float(N) * 100, u))

def tag(word1):
	word = word1.lower()
	
	#non-words or numbers
	if len(word) <= 1: return "SYM"	
	if word in NUMBER or word.isdigit(): return "CD"
	if not any(a.isalpha() for a in word): return word
	
	#elision is only allowed on article la or nouns:
	if word == "l'": return "DT"
	if word[-1] in u"'’": return "NNS"
	#other punctuation is not part of word:
	if not word[-1].isalpha(): return tag(word1[:-1])
	if not word[0].isalpha(): return tag(word1[1:])

	if word == 'nu': return "UH"
	if word in CC: return "CC"
	if word in IN: return u"IN"
	
	#tag uninflected forms:
	if word[-1] == 'n': return tag(word[:-1])
	if word[-2:] == 'oj': return "NNP"
	if word[-2:] == 'aj': return "JJ"
	if word[-1] == 'j': return tag(word[:-1])
	
	if word in DT: return "DT"
	if word in PRP: return u"PRP"
	if word in PRPd: return u"PRP$"
	
	if word in WRB: return "WRB"
	if word in RB: return "RB"
	
	if word in JJR: return "JJR"

	if word == "kio": return "WDT"
	if word == "kiu": return "WP"
	if word == "kies": return "WP"
	
	#words like hodiaŭ, preskaŭ etc.
	if word[-2:] == u'aŭ': return "RB"
	
	#open word classes:
	if word[-1] == 'a': return "JJ"
	if word[-1] == 'e': return "RB"		#this includes "ne"!
	if word[-1] == 'i': return "ii"
	if word[-1] == 'o': return "NNS"
	if word[-1] == 'u': return "VB"
	
	#verbs	
	if word[-1:] == 's':
		if word[-2] == 'a': return "VBP"
		if word[-2] == 'i': return "VBD"
		if word[-2] == 'o': return "VBf"
		if word[-2] == 'u': return "VB"
	
	
	#proper nouns / names
	if capitalized(word1):
		if word1[-1] == "j": return u"NNPS"
		else: return "NNP"
	
	return u"none"

def capitalized(word):
	#esperanto alphabet including non-esperanto western characters
	if word[0].isupper() or word[0] in u"ĈĜĤĴŜZ":
		return True
	return False

#sort dictionary by value, highest first
def dictsort(d):
	a = d.items()
	#operator.itemgetter(1) returns the 2nd element of a sequence (in this case, value associated with key)
	a.sort(key=operator.itemgetter(1))
	a.reverse()
	return a

if __name__ == '__main__': main()
