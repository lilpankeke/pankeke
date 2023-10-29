def file_write():
    num_words = int(input("How many words will you write in a file? "))
    
    with open("words.txt", "w") as f:
        for i in range(num_words):
            word = input(f"Enter your chosen word {i+1}: ")
            f.write(word + "\n")
            
    print(f"{num_words} words are written insdie the file 'words.txt'.")


file_write()