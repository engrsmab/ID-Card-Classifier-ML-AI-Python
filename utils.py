import json
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'] 
alphabet_id = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':0, 'k':0, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':0, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':0, 'x':0, 'y':0, 'z':0} 
headings = ["birth","last","given","middle","date","address"]

def save_json(file,data):
    data = json.dumps(data)
    with open(file,"a") as f:
        json.dump(data,f)

def save_data(file,data):
    f = open(file,"a")
    f.write(str(data)+"\n")
    f.close()