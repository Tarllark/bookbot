def get_word_count(text):
	return len(text.split())

def get_character_occurences(text):
	res={}
	for char in text.lower():
		if char in res:
			res[char] += 1
		else:
			res[char]=1
	return res
	
def sort_on(dict):
    return dict["num"]
	
def sort_list(list):
	new_list=[]
	for value in list:
		if value.isalpha():
			new_list.append({"char": value, "num": list[value]})
	new_list.sort(reverse=True, key=sort_on)
	return new_list
	