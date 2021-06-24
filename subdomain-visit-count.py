from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        import collections
        counter = collections.defaultdict(int)
        for cpdomain in cpdomains:
            cp, domain = cpdomain.split(" ")
            cp = int(cp)
            counter[domain] += cp
            dimains = domain.split(".")
            if len(dimains) == 1:
                continue
            elif len(dimains) == 2:
                counter[dimains[1]] += cp
            elif len(dimains) == 3:
                counter[dimains[1] + "." + dimains[2]] += cp
                counter[dimains[2]] += cp
        return [f"{v} {k}" for k, v in counter.items()]
