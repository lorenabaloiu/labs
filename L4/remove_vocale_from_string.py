import re
def remove_vowels(s):
    return re.sub(r"[aeiouAEIOUáàâäãåāÁÀÂÄÃÅĀéèêëēėęÉÈÊËĒĖĘíìîïīįÍÌÎÏĪĮóòôöõōÓÒÔÖÕŌúùûüũūÚÙÛÜŨŪýÿÝŸаеёиоуыэюяАЕЁИОУЫЭЮЯαειουωΑΕΗΙΟΥΩاويאועअआइईउऊएऐओऔあいうえおアイウエオㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣıöüİÖÜäöÄÖáéíóúőűÁÉÍÓÚŐŰ]", "", s)
input_string = input("Enter a string: ")
result = remove_vowels(input_string)
print("Without vowels:",result)