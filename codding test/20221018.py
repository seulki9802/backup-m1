def solution(new_id):
    
    #1
    new_id = new_id.lower()
    
    #2
    for i in '~!@#$%^&*()=+[{]}:?,<>/':
        new_id = new_id.replace(i, '')
    
    #3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    #4
    if new_id[:1] == '.': new_id = new_id[1:]
    if new_id[-1:] == '.': new_id = new_id[:-1]
    
    #5
    if new_id == '': new_id = 'a'
    
    #6
    if len(new_id) > 15: new_id = new_id[:15]
    while new_id[-1:] == '.':
        new_id = new_id[:-1]
    
    #7
    if len(new_id) < 3:
        new_id += new_id[-1] * (3 - len(new_id))
    
    return new_id
f

new_id = "=.="
solution(new_id)