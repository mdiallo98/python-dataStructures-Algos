class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        #  our goal is detect whether the usage of the capital letters is done correctly
        #  for it to be correct all letters are capitalized or only the first letter is capitalize
        #  what i am think is to have some counter that will check, the count should either equal one or equal to the length of the string
        #  for example "ABC" => count = 3 or "Magic" -> count = 1 return True
        #  if we have this case "BestPlayer" count != 1 or the length of string return False

        count = 0
        for i in range(len(word)):
            if word[i].isupper():
