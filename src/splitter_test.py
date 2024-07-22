from splitting import Textsplitter

from loader import load_json

combined_data,combined_text=load_json()

def main():
    splitter = Textsplitter()

    # Ask user for the type of splitter
    print("Choose a splitter method:")
    print("1: Split by chunks")
    print("2: Split by line")
    print("3: Split by word")
    print("4: Split by character")

    choice = input("Enter the number of your choice: ").strip()

    if choice == "1":
        chunk_size = int(input("Enter chunk size: ").strip())
        result=splitter.set_splitter(combined_text, splitter.split_by_chunks, chunk_size)
        print(result)
  
        
    elif choice == "2":
        splitter.set_splitter(combined_text, splitter.split_by_line)


    elif choice == "3":
        splitter.set_splitter(combined_text, splitter.split_by_word)


    elif choice == "4":
        delimiter = input("Enter the delimiter to split by: ").strip()
        splitter.set_splitter(combined_text, splitter.split_by_character, delimiter)


    else:
        print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
