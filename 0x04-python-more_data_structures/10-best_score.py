#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        maximum = 0
        answer = ""
        for key, value in a_dictionary.items():
            if value > maximum:
                maximum = value
                answer = key
        return answer
    else:
        return None
