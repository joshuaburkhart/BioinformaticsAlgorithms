

s = 'ABABABABABABABWWWWWWWWRRRRRRRXXXXXXXX'

def short_u_sub_strs(s):
    """
    This function assumes |s| is finite and fits in RAM.
    
    Runtime is bound by the triangle number of |s|,
    approx. O((n^2)/2), though an average case execution
    would run in O(((n/2)^2)/2) = O((n^2)/8).
    :param s: input string
    :return: list of shortest unique substrings
    """
    u_sub_strs = []
    for l in range(1,len(s)+1):
        found_u_sub_strs = False
        sub_strs = {}
        for i in range((len(s)-l)+1):
            sub_str = str(s[i:i+l])
            if sub_str in sub_strs:
                sub_strs[sub_str] += 1
            else:
                sub_strs[sub_str] = 1
        for sub_str in sub_strs:
            if sub_strs[sub_str] == 1:
                u_sub_strs.append(sub_str)
                found_u_sub_strs = True
        if found_u_sub_strs:
            break
    return u_sub_strs

shortlist = short_u_sub_strs(s)

print(shortlist)
print(len(shortlist[0]) if len(shortlist) > 0 else 0)