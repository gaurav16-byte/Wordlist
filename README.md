### Read Changelog file
# This creates wordlists based on your arguments

## Argument order is 

'--type [len] [word] [filename] --t [pattern]'
pattern is in the order ???text or text???
It is not compulsary to use the pattern argument.
**The length of the password and pattern length should be same**

*Next update will contain support for multiple words but for now provide the characters as required. *
**Advantage over crunch tool - Less size wordlist completely based on Python_3**

### Ex. usage python3 wordlist.py --p/ --pr / --c /--cr 5 goodmorning file
*Here 5 is the length of the passwords in the wordlist
*goodmorning is the word
*file is the filename
