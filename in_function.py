
def float_to_text(num):
    str1 = str(num)
    if '.' in str1:
        res1 = str1.split('.')[0]
        res2 = str1.split('.')[1] 
        if len(res2)>2:
            return res1 + '.' + res2[:2]
        else:
            return res1 + '.' + res2
    else:
        return str1
    
