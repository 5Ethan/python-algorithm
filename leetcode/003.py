class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        ss=set()
        ans=i=0
        for j,c in enumerate(s):
            while c in ss:
                ss.remove(s[i])
                i+=1
            ss.add(c)
            ans=max(ans,j-i+1)

        return ans


s = "pwwkew"

# -----0-----
# j=0, c=p, i=0, ans=1, ss={'p'}
# -----1-----
# j=1, c=w, i=0, ans=2, ss={'w', 'p'}
# -----2-----
# j=2, c=w, i=2, ans=2, ss={'w'}
# -----3-----
# j=3, c=k, i=2, ans=2, ss={'w', 'k'}
# -----4-----
# j=4, c=e, i=2, ans=3, ss={'w', 'k', 'e'}
# -----5-----
# j=5, c=w, i=3, ans=3, ss={'w', 'k', 'e'}

caller=Solution()

result=caller.lengthOfLongestSubstring(s)

print(result)