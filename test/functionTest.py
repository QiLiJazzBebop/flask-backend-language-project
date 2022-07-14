# from util.wordConvertUtil import *
#
# print(bilingualConvertOri("en", "get"))

# # test input jsonify
# @convertRoute.get("/jp")
# def bilingualJpConvertGet():
#     data = request.form.to_dict()
#     words = (data['words']).strip('][').split(', ')
#     print(len(words))
#     resDict = {'words': {}}
#     for word in words:
#         resDict['words'][word] = ja2en(word)
#     return jsonify(resDict)