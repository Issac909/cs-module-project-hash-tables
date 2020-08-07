def word_count(s):
    # Your code here
    dictionary = {}
    words = ""
    ignore = '":;,.-+=/\|[]{}()*^&'
    count = 0
    
    for char in s:
        if char not in ignore:
            words += char
        
        else:
            count += 1

    if count == 0:
        return dictionary
    
    else:
        words = words.split()
        words = [word.lower() for word in words]
        
        for word in words:
            if word in dictionary:
                dictionary[word] += 1
                
            else:
                dictionary[word] = 1
                
        return dictionary
    
if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))