class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        occurences = dict()
        # create dict of occurences
        for num in nums:
            if not occurences.get(num):
                occurences[num] = 1
            else:
                occurences[num] += 1

        # sort by top occurences
        sorted_occs = sorted(occurences.items(), key=lambda tup: tup[1])
        # return key (number)
        return sorted([el[0] for el in sorted_occs[-k:]])
