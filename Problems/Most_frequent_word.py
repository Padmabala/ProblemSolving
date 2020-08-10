import string;
class Solution:
    def mostCommonWord(self, paragraph, banned):
        for c in "!?',:.;":
            if c in paragraph:
                paragraph=paragraph.replace(c," ")
        print(paragraph)
        p=paragraph.split(' ')
        hash={}
        max=0
        hash[max]=0

        for i in range(len(p)):
            if p[i]:
                word = p[i].lower()
                if (word not in hash):
                    hash[word] = 1
                else:
                    hash[word] += 1
                if (word not in banned and hash[word] > hash[max]):
                    max = word
        print(hash)
        return max
s=Solution()
print(s.mostCommonWord("k. U; A! V? R? C' x! X. M; z' V! w. N. T? Y' w? n, Z, Z? Y' R; V' f; V' I; t? X? Z; l? R, Q! Z. R. R, O. S! w; p' T. u? U! n, V, M. p? Q, O? q' t. B, k. u. H' T; T? S; Y! S! i? q! K' z' S! v; L. x; q; W? m? y, Z! x. y. j? N' R' I? r? V! Z; s, O? s; V, I, e? U' w! T? T! u; U! e? w? z; t! C! z? U, p' p! r. x; U! Z; u! j; T! X! N' F? n! P' t, X. s; q'",
["m","i","s","w","y","d","q","l","a","p","n","t","u","b","o","e","f","g","c","x"]))
