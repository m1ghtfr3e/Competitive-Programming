def to_camel_case(text):
    if len(text) == 0:
        return text
    else:
        text = [i for i in text]
        for i in range(len(text)):
            if text[i] == '_' or text[i] == '-':
                # If index == '_' then replace with upper after
                text[i] = text[i+1].upper()
                # Overwrite the overwritten index
                text[i+1] = '0'
        # Remove 'placeholer'
        for i in text:
            if i == '0':
                text.remove(i)
        t = ''.join(text).strip(' ')
        return t


if __name__ == '__main__':
    print(to_camel_case('the_stealth_warrior'))
