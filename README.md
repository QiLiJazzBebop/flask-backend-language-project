# The backend for binglingual project
##
package usage
all test function are located in test folder, in this project we call the api from small word project directly, and combined it with serveral api, showing as follow:
**jisho**, a dictionary for both japanese and english, it reflicated the subsititution suggestion for word in english and japanes.
**nltk**, use it to get the dictionary for english sense
**spacy**, use it to denote the similarity between doc and word(only for english word), and tag the phrase.

## route
search/nodes function
I combined the two sides nodes, named en and jp, there are leftdata and rightdata you told me before.
Besides, I add new functions.similarity value between en word and jp word.
it indicate the sense closeness between en and jp, bigger means it close, vice versa

search/node function
Giving jp or en name, return the specific definition, both url return the same format, using jisho api

search/link function
Giving two english word, return realtion tag between two word
