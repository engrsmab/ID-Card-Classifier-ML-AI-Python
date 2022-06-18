from utils import *

def calculate_waight(words):
    original_count = 0
    predict_count = 0
    compare_list = []
    compare_rate = 0
    for index in range(len(words)):
        count = 0
        for alpha in words[index]:
            if index == 0:
                compare_list.append(alpha)
                try:
                    predict_count += alphabet_id[alpha]
                except:
                    pass
            else:
                try:
                    original_count += alphabet_id[alpha]
                except:
                    pass
                try:
                    if alpha == compare_list[count]:
                        compare_rate += 1
                except:
                    pass
            count += 1
    matched = False
    if compare_rate > len(words[1])//2:
        matched = True
    return original_count,predict_count,matched
def validate_waight(words):
    orignal_waight, predict_waight,matched = calculate_waight(words)
    validate = False
    if matched:
        half_v = orignal_waight//2
        if orignal_waight != predict_waight:
            if predict_waight < orignal_waight and predict_waight > (half_v + half_v//2):
                validate = True
            elif predict_waight > orignal_waight and (predict_waight - orignal_waight) < (orignal_waight//2 - half_v//2):
                validate = True
            else:
                validate = False
        else:
            validate = True
    return validate


def set_data(data):
    final_data = []
    for line in data:
        final_data.append(line)
    final_data = " ".join(final_data)
    
    return [final_data]

