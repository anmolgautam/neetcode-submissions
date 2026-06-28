class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        answer = []
        for ele in strs:
            key = "".join(sorted(ele))
            if key in hm:
                hm[key].append(ele)
            else:
                hm[key]=[ele]
        #print(hm)
        for value in hm.values():
            answer.append(value)
        return answer
