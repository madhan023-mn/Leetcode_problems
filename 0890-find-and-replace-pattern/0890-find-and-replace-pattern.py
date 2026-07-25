class Solution(object):
    def match(self, word, pattern):
        w_to_p = {}
        p_to_w = {}

        for w, p in zip(word, pattern):
            if w not in w_to_p and p not in p_to_w:
                w_to_p[w] = p
                p_to_w[p] = w
            elif w_to_p.get(w) != p or p_to_w.get(p) != w:
                return False
        return True

    def findAndReplacePattern(self, words, pattern):
        return [word for word in words if self.match(word, pattern)]