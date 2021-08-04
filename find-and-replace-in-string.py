from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        answer = []
        new_s = s
        sources = {k: v for k, v in zip(indices, sources)}
        targets = {k: v for k, v in zip(indices, targets)}
        indices.sort()
        for idx in indices:
            print(idx)
            if s[idx:].startswith(sources[idx]):
                ss = new_s.split(sources[idx], 1)
                answer.append(ss[0])
                answer.append(targets[idx])
                new_s = ss[1]
            print(answer)
        answer.append(new_s)
        return "".join(answer)


if __name__ == '__main__':
    res = Solution().findReplaceString(
        "ydrctlphryrwcelwquhlqpmrqaxgbfvwtnrvbaptfjkodhhivbwclspjldxaxwipwlfglbghdulrqxdcpxaptezogttqatiwujhwzpuveurnwsjdaqqnpfyuvihgagjyqnkmmwmsyxqjzfzvlnzzowxrjksohubkaoaeukvcomvbmcslumnndindhfuumhieoxxxshpygaivfpbjkksdpxaocdyppyjztawvbqkbioorfjfetowrblcycfnxvjriobxbyztnrtjrshwnwjxqacmcztxwajcagohobrmvrjzafijyfnphdibpjatzxhvtpselqatxkkxdqpmjspsqytdtkfgnybrxarmwvhmyesbibmxeftdoyefryydzzaedbmfwqjcqtrblrygelluoekdbpfalukhammbbaasjelbmmxxrktjxbnccpddnztxhpclghyeylioqqtzhadrtpgdcyemiojhmbqgafzlyvzuhrwturhqucmrjwkqvlrusrydduteizxzokldsyxihecrknfwjmobuxlhaxabylagfwpmkoslypcdwmpswjhapgmkwjusvikefkfvhjpwopupcatnvhyvhwyoitgwqpopljuikjodgqbqrsxmyffwriqxvpkbhrekbqoyknoejjnrhgkgpomvehdjqhebpwewlxihoxyyjjtyrbgrekypsgxyhhpxkjbakmklmmfqmwvmkkxmhlaqvhvecsvcjbrzablsycmhsiujjresmwecollpoomwzspdoqhngtpdjoplxoirerfuwizbydnltrjrmjetwyouckwhkkgulntgxbyqdvrlayykercdbghwtwcfspnlxxklltgeoyvlybjsninsqahkjhdwpdqeffqtsvamvctturqqpjptxxkvtsleceksbsixdlstlznwmzixqpbnimklaxpuqeamlsljogqweklklbuposawltjpnwzqigvpybhvmvjcskohs",
        [
            833, 829, 166, 605, 312, 581, 455, 254, 559, 505, 670, 284, 694, 90, 592, 916, 588, 628, 194, 434, 62, 564,
            953, 751, 599, 962, 491, 673, 654, 184, 700, 338, 288, 790, 146, 0, 521, 354, 38, 264, 960, 7, 900, 873,
            191, 530, 840, 111, 54, 211, 704, 862, 643, 227, 120, 892, 987, 382, 536, 324, 939, 496, 244, 446, 838, 125,
            663, 58, 365, 740, 615, 219, 52, 68, 508, 717, 27, 268, 685, 168, 970, 846, 824, 882, 635, 696, 976, 910,
            304, 776, 397, 390, 276, 805, 545, 809, 151, 990, 224, 458],
        [
            "yqdvr", "tgxb", "vc", "yvhwyoit", "jatzxhvtpse", "usv", "yli", "riobx", "kosly", "kq", "ve", "ajc", "yr",
            "tqatiwujhwzpuveurnw", "jpw", "sleceks", "kf", "qbqrs", "xx", "jxb", "ip", "pcdwmpswjhapgmkw", "am",
            "ycmhsiujjresmwecollpoomwz", "catnv", "weklk", "hrwt", "djq", "yknoejjn", "hfuumhi", "kyps", "sqyt",
            "gohobrmvrjzafijy", "lxoirerfuwi", "zzowx", "ydrct", "xzokld", "mwvhmyesbib", "ptfj", "rt", "gq",
            "hryrwcelwqu", "ctturqqpj", "jsnin", "eo", "ihecrk", "yyker", "da", "pj", "dpxa", "gxy", "lltge", "vpkb",
            "vbqkbioor", "vih", "fq", "ybh", "ed", "nf", "qat", "qpbnimklaxpu", "rhqucm", "blcycfn", "xhpcl", "la",
            "gjyqnkmmwmsyx", "hgkg", "xax", "mxe", "svcjbrzab", "qpoplj", "ppyj", "ls", "lbghdulrqxd", "lrusryddu",
            "klmmfq", "gbfvwtnrvba", "shw", "ih", "omvb", "pos", "dbghwtwcfsp", "kguln", "kjhdwp", "yffwriq", "bgr",
            "tj", "txxkvt", "fnphdibp", "sp", "ygelluoekdbpfalukhammbbaasjelbm", "cqtrb", "acmczt", "nltr", "lhaxa",
            "jrmjetwyou", "rjksohubkao", "vmvjcskohs", "ta", "oqqtzhadrtpgdcyemiojhmbq"],
        [
            "yylryi", "fgllo", "fwl", "kdhuhxvzr", "cvqhuzuoqy", "uia", "jjr", "vqfu", "cmwv", "hsi", "q", "qu", "v",
            "vvdcranjoawfmfrlmwx", "ytpw", "bedngobl", "sb", "zivt", "l", "wg", "g", "xxfnekbbvfbttmsaz", "s",
            "orsnfdemeugdbrhxoeqdrykhr", "ajbovn", "dglsi", "lfr", "dl", "dvmlejzh", "cqvogr", "vzimb", "bajwe",
            "jarxzfmrvrctxmud", "fysddvymir", "zhnopi", "khtyxs", "liqpp", "dtuacadhptc", "ubzur", "usa", "cu",
            "wuozjmtdatau", "utztuhspo", "aymcuy", "eeq", "onjmpw", "adje", "m", "jsn", "fsxsg", "kup", "esad", "fyq",
            "urtlewdiuy", "jxdh", "um", "bki", "gt", "f", "sxwa", "tfyoddzwkdvfl", "ffcwxtq", "jwkxzs", "tnnid", "f",
            "viudpwckuiue", "vctgw", "wd", "oki", "jzxxdilvxo", "gtatiw", "jtb", "hm", "ivfytknzvz", "aafzwoxoiw",
            "wdjkt", "zwdzijemosr", "tlsn", "j", "pdcck", "agnc", "xplpczgqpz", "ieinaw", "uyrmwuk", "adfardf", "wo",
            "e", "hxwgk", "owrxbdopw", "ml", "srfofdjqkcmpjtltzeuyfpvkgaudadx", "xqhay", "bnwnlrr", "xrqc", "zbiua",
            "zrxdspxjx", "tavesyitod", "bebfxxjat", "j", "iqvluqothwqbbygwrgeasavr"])

    print(
        res == "khtyxslpwuozjmtdatauhlqpmrqaxzwdzijemosrubzurkodhhivbwchmjsnldwdwgwlfgivfytknzvzcpxaptezogtvvdcranjoawfmfrlmwxsjmqqnpfyujxdhgaviudpwckuiueqjzfzvlnzhnopitavesyitodaeukfwlpdcckmcslumnndindcqvogreeqxlshpygaivfpbjkksfsxsgocdyjtbzjwurtlewdiuyfjfetowrjwkxzsxvjvqfubyztnusajrtlsnnwjxqbnwnlrrxwquajarxzfmrvrctxmudowrxbdopwcvqhuzuoqylsxwaxkkxdqpmjspbajwedtkfgnybrxardtuacadhptcokiftdoyefryydzzagtbmfwqjxqhaylrsrfofdjqkcmpjtltzeuyfpvkgaudadxmxxrktwgnccpddnzttnnidghyejjriqvluqothwqbbygwrgeasavrgafzlyvzulfruffcwxtqrjwhsivaafzwoxoiwteizliqppsyxonjmpwfwjmobuxzbiuabylagfwpmcmwvxxfnekbbvfbttmsazjuiaikefsbvhytpwopupajbovnhkdhuhxvzrgwgtatiwuikjodgzivtxmadfardfxfyqhrekbqodvmlejzhrvctgwpomqhdlhebpwewlxjoxyyjjtvwoevzimbkuphhpxkjbakmwdjktmwvmkkxmhlaqvhvecjzxxdilvxolsorsnfdemeugdbrhxoeqdrykhrmldoqhngtpdjopfysddvymirzbydxrqczrxdspxjxckwhkieinawfglloyylryifadjecxplpczgqpznlxxkesadoyvlybaymcuysqahuyrmwukdqefumtsvamvutztuhspophxwgkbedngoblbsixdlstlznwmzixtfyoddzwkdvflqeslsljocudglsilbuagncawlepnwzqigvpbkibebfxxjat")
