# 给你一个长度为 n 的字符串数组 names 。你将会在文件系统中创建 n 个文件夹：在第 i 分钟，新建名为 names[i] 的文件夹。
# 由于两个文件 不能 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以 (k) 的形式为新文件夹的文件名添加后缀，其中 k 是能保证文件名唯一的 最小正整数 。
# 返回长度为 n 的字符串数组，其中 ans[i] 是创建第 i 个文件夹时系统分配给该文件夹的实际名称
from typing import List


def getFolderNames(names: List[str]) -> List[str]:
    res = []
    _num = {}
    for name in names:
        if name not in _num:
            res.append(name)
            _num[name] = 0
            continue
        idx = _num.get(name) + 1
        _name = "{}({})".format(name, idx)
        while _name in _num:
            idx += 1
            _name = "{}({})".format(name, idx)
        res.append(_name)
        _num[name] = idx
        _num[_name] = 0
    return res


if __name__ == '__main__':
    print(getFolderNames(["pes", "fifa", "gta", "pes(2019)"]))
    print(getFolderNames(["gta", "gta(1)", "gta", "avalon"]))
    print(getFolderNames(["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]))
    print(getFolderNames(["wano", "wano", "wano", "wano"]))
    print(getFolderNames(["kaido","kaido(1)","kaido","kaido(1)"]))
    print(getFolderNames(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]))
