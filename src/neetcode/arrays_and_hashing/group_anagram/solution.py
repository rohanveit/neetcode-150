class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen_strings = dict()
        ret = list()
        for word in strs:
            word_sorted = ''.join(sorted(word))
            print(word_sorted)
            ret_idx = seen_strings.get(word_sorted)
            print(ret_idx)
            if ret_idx is not None:
                ret[ret_idx].append(word)
            else:
                ret.append([word])
                seen_strings[word_sorted] = len(ret) - 1
        return ret

        