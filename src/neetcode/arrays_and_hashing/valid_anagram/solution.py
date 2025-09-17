class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_occ = dict()
        t_occ = dict()
        if len(s) != len(t):
            return False
        zipped = zip(s, t)
        for idx, (s_char, t_char) in enumerate(zipped):
            s_occ[s_char] = s_occ.get(s_char, 0) + 1
            t_occ[t_char]= t_occ.get(t_char, 0) + 1
        if s_occ == t_occ:
            return True
        return False
        