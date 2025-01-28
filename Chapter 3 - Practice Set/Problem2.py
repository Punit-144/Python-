# WAP to fill a letter template given below with the name and date 

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Punit").replace("<|Date|>", "29 Januare 2025"))
