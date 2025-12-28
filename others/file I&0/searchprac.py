
def check_word():
    word="learning"
    with open("prac.txt","r") as f:
        data=f.read()
        
        if(word in data):
            print("found")
        else:
            print("not found")

check_word()

def check_line():    
    word="learning"
    data=True
    line_no=1
    with open("prac.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1

    return -1

check_line()