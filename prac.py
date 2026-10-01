from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []

        for word in strs:
            result.append(sorted(word))
        return result 

        for lst in result:
            if 


sol = Solution()
result = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)