import os
import easyocr
import cv2
import glob
from nlp_waight import *


reader = easyocr.Reader(['en']) 


def driving_lic(data):
    print("It's driving lic.")
    lic_data = {}

    
def id_card(data,Word):
    print("This is ID Card")
    id_data = {}
    id_data["idType"] = "Philipine Identification Card"
    new_line = str(data[0]).split(" ")
    if Word in new_line:
        index = new_line.index(Word)
        if validate_waight((Word.lower(),"card")):
            id_data["idNumber"] = new_line[index+1]
        elif validate_waight((Word.lower(),"identification")):
            id_data["idNumber"] = new_line[index+2]
        else:
            id_data["idNumber"] = new_line[index]

    index_count = 0
    
    
    for word in new_line:
        words = str(word).split("/")
        if len(words) > 1:
            word = words[1]
        word = word.lower()
        if word in months:
            id_data["dateOfBirth"] = f"{word} {new_line[index_count+1]} {new_line[index_count+2]}"

        for tries in headings:
            if validate_waight((word,tries)):
                if tries == "given":
                    id_data["firstName"] = new_line[index_count+2]
                elif tries == "last":
                    id_data["lastName"] = new_line[index_count+2]
                elif tries == "middle":
                    id_data['middleName'] = new_line[index_count+2]
                elif tries == "birth":
                    id_data["dateOfBirth"] = f"{new_line[index_count+1]} {new_line[index_count+2]} {new_line[index_count+3]}"
                elif tries == "address":
                    id_data["Address"] = " ".join(new_line[index_count+1:])
        index_count += 1

    save_data("National_ID.txt",id_data)
    
    print(id_data)

def multi_card(data):
    print("This is Multi-Purpose Cart")

def rotate_img(img):
    return cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
def read_img(path):
    return cv2.imread(path)

def read_text(gray_img):
    try: 
        result = reader.readtext(gray_img,paragraph="False")
    except:
        return "None",True
    data = []
    for line in result:
        data.append(line[1])
    data = " ".join(data)
    found = False
    valid = False
  
       
    for word_cap in str(data).split(" "):
        if len(word_cap) > 2:
            valid = True
            word = word_cap.lower()
            #print("Data: ",data)
            if validate_waight((word,"driver")) or validate_waight((word,"license")) or validate_waight((word,"transportation")):
                print(word)
                driving_lic([data])
                found = True 
                break
            elif validate_waight((word,"identification")) or validate_waight((word,"card")) or (len(word) == 19 and len(word.split("-")) == 4):
                print(word)
                id_card([data],word_cap)
                found = True
                break
            elif validate_waight((word,"unified")) or validate_waight((word,"multi")):
                multi_card(data)
                break
        if found == True:
            break
    return found,valid
url = "/Users/macbookpro/Desktop/Projects/Machine_Learning_Projects/ID_Card_Info_Extractor/Sample Data/Drivers License/14.jpg"         
for folder in os.listdir("Sample Data"):

    # if folder != ".DS_Store":
    if folder == "Drivers License":
        print("Folder: ",folder)
        files_path = glob.glob("Sample Data/"+folder+"/*.jpg") + glob.glob("Sample Data/"+folder+"/*.jpeg") + glob.glob("Sample Data/"+folder+"/*.webp") 
        for path in files_path:
            print("image: ",path.split("/")[-1])
            
            img = read_img(path)
            try:
                gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            except:
                continue
            found,valid = read_text(gray)
                  
           
            if not valid:
                print("rotating image...")
                img = rotate_img(img)
                found,valid = read_text(img)
            if type(found) == str:
                print("Skipping image: ",str(path).split("/")[-1])
        

            





