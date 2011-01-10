#!/usr/bin/python
def psycologist():
    print "Please tell me your problems"
    while True:
        answer = yield
        if answer is not None:
            print answer
            if answer.endswith('?'):
                print("Don't ask yourself too much questions")
            elif 'good' in answer:
                print("A that's good, go on")
            elif 'bad' in answer:
                print("Don't be so negative")
            else:
                print("please calm down and say it again")
        else:
            print("Silence is not golden now")
            
if __name__=='__main__':
    free = psycologist()
    next(free)
    free.send('How do I do?')
    free.send('ok then i should find what is good for me')
    free.send('I feel bad')
    free.send('aaa bbb ccc')
    free.send(None)
        
