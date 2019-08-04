
def splitToWords(sent):
	current_word = ""
	for i in range(len(sent)):
	    if sent[i] == " ":
	        words.append(current_word)
	        current_word = ""
	    elif i==len(sent)-1:
	    	current_word += sent[i]
	    	words.append(current_word)
	    else:
	        current_word += sent[i]

	return words

def sortList(words):
	for i in range(len(words)-1):
		for j in range(len(words)-i-1):
			if words[j]>words[j+1]:
				temp=words[j+1]
				words[j+1]=words[j]
				words[j]=temp

	return words

def sortLetters(words):
	sorted=[]
	for w in words:
		word=list(w)
		for i in range(len(word)-1):
			for j in range(len(word)-i-1):
				if word[j]>word[j+1]:
					temp=word[j+1]
					word[j+1]=word[j]
					word[j]=temp
		sorted.append(''.join(word))

	return sorted

if __name__ == '__main__':
	words = []
	sent="i love to code in python"
	print("Input:", sent)

	print("\nSplitting sentence to words")
	words = splitToWords(sent)
	print(words)

	print("\nSorting words in the list")	
	words = sortList(words)
	print(words)

	print("\nSorting letters in the list of words")
	sorted = sortLetters(words)
	print(sorted)