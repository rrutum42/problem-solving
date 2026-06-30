import string 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        BFS
        https://leetcode.com/problems/word-ladder/solutions/1764371/a-very-highly-detailed-explanation-by-hi-vcve
        we add the beginWord in queue and start with BFS from that word.
        for that word we try and replace character at every index with all the alphabets
        if the newly formed word is present in word list then we add it to queue
        we also mark it as seen (since 1 word can only be used once)
        we do this while queue is not empty
        return the count if endWord is hit
        if end word is never hit, return 0
        '''
        queue = deque([beginWord])
        visited = set([beginWord])
        wordList = set(wordList)

        changes = 1

        while queue:
            for l in range(len(queue)):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return changes
                
                for ch in range(len(curr_word)):
                    prefix, suffix = curr_word[:ch],curr_word[ch+1:]
                    for char in string.ascii_lowercase:
                        word = prefix + char + suffix 
                        if word in wordList and word not in visited:
                            queue.append(word)
                            visited.add(word)
            changes += 1

        return 0
