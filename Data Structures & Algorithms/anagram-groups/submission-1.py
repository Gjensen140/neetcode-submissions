class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        counts = collections.defaultdict(list)


        for s in strs:
            chars = [0] * 26

            key = sorted(s)

            key = "".join(key)

            if counts[key]:
                counts[key].append(s)
            else:
                counts[key] = [s]

        output = []

        for k in counts.keys():
            output.append(counts[k])

        return output

        