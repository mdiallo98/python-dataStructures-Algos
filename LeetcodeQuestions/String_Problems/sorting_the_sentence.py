class Solution:
    def sortSentence(self, s: str) -> str:
        #  we are giving a sentence, each word in the sentence ends with a number which indicates the odering of that word if the sentence was to be sorted
        #  Our objective is to capture the last char in each word and use it to place the other words in the sentence
        #  i can use a dictionary, take the last char and use it as the key, finally i will map each word excluding the last char as the value

        words = s.split(' ')
        Map = {}
        for wrd in words:
            Map[int(wrd[-1])] = wrd[:-1]
        n = len(words) + 1
        #  since the keys are 1 indexed we need to make the list one element larger so that we dont over indexed
        store = [None] * n
        for key, val in Map.items():
            store[key] = val

        return ' '.join(store[1:])
