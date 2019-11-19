#练习：编写一个函数most_frequent,接收一个字符串并按照频率的降序打印字母
#d=dict()
#def histogram(s):
#    
#    for c in s:
#        d[c]=int(d.get(c,'0'))+1
#    return d
#
#def most_frequent(a):
#    histogram(a)
#    c=[]
#    for key,val in d.items():
#        c.append((val,key))
#        c.sort(reverse=True)
#    res=[]
#    for val,key in c:
#        res.append(key)
#    print(res)
# most_frequent('adffdadfafasdfafdafadf')
# fin=open('words.txt').read()
# # for line in fin:
# #     word=line.strip()
    
# t=most_frequent(fin)
# # for x in t:
# #     print(x[1:])


import random


def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.

    s: string

    Returns: list of letters
    """
    hist = make_histogram(s)

    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    res = []
    for freq, x in t:
        res.append(x)

    return res
    

def make_histogram(s):
    """Make a map from letters to number of times they appear in s.

    s: string

    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist
def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename).read()


if __name__ == '__main__':
    s = read_file('words.txt')
    t = most_frequent(s)
    for x in t:
        print(x)

