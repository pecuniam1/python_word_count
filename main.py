#complete_lyrics = "thEre is a qu!i hEre   anD here? and ? here"
common_words = ['a', 'an', 'the']
remove_common_words_boolean = True
file_object = open(r"C:\Users\kevjo\Documents\workspace\python\lyrics.txt", "r")
complete_lyrics = file_object.read()

def remove_punctuation(lyrics):
	punctuation_list = ["$", "@", "$", "%", "^", "&", "?", "!", ".", ",", ";", ":", "-", "--", "[", "]", "(", ")", "{", "}", "'", "\"", "*", "/", "\\"]
	for punc in punctuation_list:
		lyrics = lyrics.replace(punc, "")
	return lyrics

def convert_to_lowercase(lyrics):
	return lyrics.lower()

def itemize_words(lyrics):
	word_list = list(lyrics.split(" "))
	if remove_common_words_boolean: word_list = remove_common_words(word_list)
	word_freq = [word_list.count(p) for p in word_list]
	word_dict = dict(list(zip(word_list, word_freq)))
	if '' in word_dict:  del word_dict[''] # delete blanks
	return word_dict

def remove_common_words(lyrics):
	return [word for word in lyrics if word not in common_words]


#include function to remove or include numbers

print(complete_lyrics)
complete_lyrics = remove_punctuation(complete_lyrics)
complete_lyrics = convert_to_lowercase(complete_lyrics)
complete_lyrics = itemize_words(complete_lyrics)
print("==============================")
print(complete_lyrics)
