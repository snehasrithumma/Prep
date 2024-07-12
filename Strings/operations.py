text = "ABC red"
print(text.isalnum())   # Output: True (contains alphanumeric characters)
print(text.isdigit())   # Output: False (contains non-digit characters)
print(text.isdecimal()) # Output: False (contains non-decimal characters)
print(text.isspace())   # Output: False (contains non-space characters)
print(text.islower())   # Output: False (contains uppercase characters)
print(text.isupper())   # Output: False (contains lowercase characters)
print(text.istitle())   # Output: True (title case)
print(text.isidentifier()) # Output: True (valid identifier)
print(text.isprintable())  # Output: True (all characters are printable)


from string import Template

temp = Template("im practicing ${title} how to do it using ${concept}")

print(temp.substitute(title='string sustitution', concept='template strings'))

data = {"title": 'strings',
        "concept": "string formating"}
print(temp.substitute(data))