# brute force
def to_camel_case(text):
    result = ""
    for i, lett in enumerate(text):
        if i > 0 and text[i-1] == '-' or i > 0 and text[i-1] == '_':
            result += lett.upper()
            continue
        if lett == '-' or lett == '_':
            continue
        result += lett
    return result

# improved
def to_camel_case2(text):
    # return empty
    if not text:
        return ''
    
    # replace and split text into a 'words' list, then join appropriately.
    words = text.replace('-','_').split('_')
    result = words[0] + ''.join(word.capitalize() for word in words[1:])
    return result
    

test_strings = ["hello_world", "some-text_here", "test", "", "A_B_C"]
results1 = [to_camel_case(s) for s in test_strings]
results = [to_camel_case2(s) for s in test_strings]

print(results == results1)