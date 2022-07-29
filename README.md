# The backend for binglingual project
## package description
This repo is used to learn the difference between japanese word and english word. It is the sub project under small word project and take used the third party to visulize more info.

## package usage
all test function are located in test folder, in this project we call the api from small word project directly, and combined it with serveral api, showing as follow:

- **nltk**, get the definition for multi-language word, and similarity value between definition pairs.
- **spacy** get quick response on any two english words similarity value.
- **googleTrans**, the format of data is same as this url https://translate.google.com/?sl=en&tl=ja&text=sweet&op=translate

## route group
- Hello Word: Test whether website in online
- Bilingual view
  - Main view
    - Input a word, return list of available tran option(already test from ori api)
    - Input the user selected word, return bilingual nodes, if no tran, then back monolingual nodes
    - Input the word, then back the trans result, note jp word already attach nltk info
- Word similarity
  - Check how much two word closeness
    - general, return the value.
    - specification, return the definition list as well as definition pair closeness value.


