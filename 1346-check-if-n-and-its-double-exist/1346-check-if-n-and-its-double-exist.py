class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        flag=False
        hashmap={}
        for i in range(len(arr)):
            if arr[i]*2 in hashmap:
                flag=True
            if arr[i]%2==0 and arr[i]//2 in hashmap:
                flag=True
            hashmap[arr[i]]=True

        return flag