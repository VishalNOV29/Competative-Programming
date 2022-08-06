# list1=[1,4,3,5,6,'_']
# print(list1)
# list1.sort()
# print(list1)

# list1=[1,2,3,4,4,5,6,6,7,7,7,7,7,7]
# new_list1=[]
# for ele in list1:
#     if ele not in new_list1:
#         new_list1.append(ele)
# print(new_list1)
# bar_len=len(list1)-len(new_list1)
# for i in range(bar_len):
#     new_list1.insert(len(new_list1)+i,"_")
# print(new_list1)

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         # list1=[1,2,3,4,4,5,6,6,7,7,7,7,7,7]
#         list1=nums
#         new_list1=[]
#         for ele in list1:
#             if ele not in new_list1:
#                 new_list1.append(ele)
#         bar_len=len(list1)-len(new_list1)
#         for i in range(bar_len):
#             new_list1.insert(len(new_list1)+i,"_")
#         # print(new_list1)
#         print(new_list1)


# Longest substring without repition of chracters.
# string=input("Enter the string.")
# max=0
# for i in range(len(string)):
#     sub_string=""
#     for j in range(i,len(string)):
#         if string[j] not in sub_string:
#             sub_string+=string[j]
#             if len(sub_string)>max:
#                 max=len(sub_string)
#         else:
#             break
# print(max)


# Longest palindrome sub-string.

max = ""
string = input("Enter the substring :")
for i in range(len(string)):
    for j in range(i, len(string)):
        temp_str = string[i:j+1]
        if temp_str == temp_str[::-1]:
            if len(temp_str) > len(max):
                max = temp_str
print("Result is :::::::::::::::::::::")
print(max)
# qbmhukucteihghldwdobtvgwwnhflpceiwhbkmvxavmqxedfndegztlpjptpdowwavemasyrjxxnhldnloyizyxgqlhejsdylvkpdzllrzoywfkcamhljminikvwwvqlerdilrdgzifojjlgeayprejhaequyhcohoeonagsmfrqhfzllobwjhxdxzadwxiglvzwiqyzlnamqqsastxlojpcsleohgtcuzzrvwzqugyimaqtorkafyebrgmrfmczwiexdzcokbqymnzigifbqzvfzjcjuugdmvegnvkgbmdowpacyspszvgdapklrhlhcmwkwwqatfswmxyfnxkepdotnvwndjrcclvewomyniaefhhcqkefkyovqxyswqpnysafnydbiuanqphfhfbfovxuezlovokrsocdqrqfzbqhntjafzfjisexcdlnjbhwrvnyabjbshqsxnaxhvtmqlfgdumtpeqzyuvmbkvmmdtywquydontkugdayjqewcgtyajofmbpdmykqobcxgqivmpzmhhcqiyleqitojrrsknhwepoxawpsxcbtsvagybnghqnlpcxlnshihcjdjxxjjwyplnemojhodksckmqdvnzewhzzuswzctnlyvyttuhlreynuternbqonlsfuchxtsyhqlvifcxerzqepthwqrsftaquzuxwcmjjulvjrkatlfqshpyjsbaqwawgpabkkjrtchqmriykbdsxwnkpaktrvmxjtfhwpzmieuqevlodtroiulzgbocrtiuvpywtcxvajkpfmaqckgrcmofkxynjxgvxqvkmhdbvumdaprijkjxxvpqnxakiavuwnifvyfolwlekptxbnctjijppickuqhguvtoqfgepcufbiysfljgmfepwyaxusvnsratn
class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        if len(s) <= 1:
            return s
        start = end = 0
        length = len(s)
        for i in range(length):
            max_len_1 = self.get_max_len(s, i, i + 1)
            max_len_2 = self.get_max_len(s, i, i)
            max_len = max(max_len_1, max_len_2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start: end+1]
        
    def get_max_len(self, s: 'list', left: 'int', right: 'int') -> 'int':
        length = len(s)
        i = 1
        max_len = 0
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1