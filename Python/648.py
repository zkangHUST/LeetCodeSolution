class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        sents = sentence.split(" ")
        dict = sorted(dict)
        for i in range(len(sents)):
            for j in range(len(dict)):
                if self.check(sents[i], dict[j]):
                    sents[i] = dict[j]

        return "".join(sents)
    
    
    def check(self, a, b):
        if len(a) < len(b):
            return False
        for i in range(len(b)):
            if a[i] != b[i]:
                return False
        return True

a = ["cat", "bat", "rat"]
"the cattle was rattled by the battery"