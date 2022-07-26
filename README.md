# The backend for binglingual project
## package description
This repo is used to learn the difference between japanese word and english word. It is the sub project under small word project and take used the third party to visulize more info.

## package usage
all test function are located in test folder, in this project we call the api from small word project directly, and combined it with serveral api, showing as follow:

**nltk**, use it to get the definition for both english word as well as japanese words. The functions we used including <wup_similarity> and <wordnet>.
**spacy** use it to get quick response on any two word similarity.
**googleTrans**, the format of data is same as this url https://translate.google.com/?sl=en&tl=ja&text=sweet&op=translate

## route
