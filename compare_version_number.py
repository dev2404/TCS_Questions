class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(v) for v in version1.split(".")]
        v2 = [int(v) for v in version2.split(".")]
        
        
        i = 0
        
        while i < max(len(v1), len(v2)):
            a = v1[i] if i<len(v1) else 0
            b = v2[i] if i<len(v2) else 0
            
            if a < b:
                return -1
            elif a > b:
                return 1
            i += 1
        else:
            return 0
#####################################################
#EXAMPLE
#Input: version1 = "0.1", version2 = "1.1"
#Output: -1