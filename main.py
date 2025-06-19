from stats import *
import sys

def main():
	args=sys.argv
	if len(args)<2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book = get_book_text(args[1])
	word_count = get_word_count(book)
	occurences=get_character_occurences(book)
	sorted_list=sort_list(occurences)
	print("============ BOOKBOT ============")
	print(f"----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for res in sorted_list:
		print(f"{res["char"]}: {res["num"]}")
	print("============= END ===============")
	
	
def get_book_text(title):
	print(f"Analyzing book found at {title}.txt...")
	with open(title) as f:
		return f.read()

		
main()