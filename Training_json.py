import json
from pprint import pprint
with open(r"newsafr.json") as f:
    json_data = json.load(f)

description = json_data["rss"]["channel"]["description"]
category = json_data["rss"]["channel"]["category"]
title = json_data["rss"]["channel"]["title"]
all_items = json_data["rss"]["channel"]["items"]

new_list_of_words = []

# here I split the text in separated items
new_list_of_words.extend(description.split(" "))
new_list_of_words.extend(category.split(" "))
new_list_of_words.extend(title.split(" "))

for item in all_items:
  new_list_of_words.extend(item["description"].split(" "))
  new_list_of_words.extend(item["title"].split(" "))

# Here I count the number of identical items in the list. For this purpose I create a dictionary: key corresponds to a word, value corresponds to the number of times this word is repeated

dictionary = {}
for word in new_list_of_words:
  if len(word) > 6:
    lower_word = word.lower()
    if lower_word in dictionary.keys():
      dictionary[lower_word] = dictionary[lower_word] + 1
    else:
      dictionary[lower_word] = 1


# # here I sort the list
list_d = list(dictionary.items())
list_d.sort(key=lambda i: i[1])
list_d.reverse()

new_list = []
# # here I append the first 10  elements of the list_d to the new_list

i = 0
while i < 10 and i <= len(list_d):
    new_list.append(list_d[i])
    i = i + 1

print("Топ", len(new_list), "слов длиннее 6 символов:","\n")
for i in new_list:
  print(i[0])
