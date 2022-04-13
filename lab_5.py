def pr_1_swap(text):
   result_str = ""
   for item in text:
       if item.isupper():
           result_str += item.lower()
       else:
           result_str += item.upper()
   return result_str
print(pr_1_swap("HackerRank.com presents 'Pythonist2'."))

