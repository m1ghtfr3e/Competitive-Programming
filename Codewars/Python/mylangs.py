# my languages

def my_languages(results):

    #return [lang for lang, score in results.items() if score ==60 or score > 60]
    
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    
    submit = []
    for i in range(len(sorted_results)):
        if sorted_results[i][1] >= 60:
            submit.append(sorted_results[i][0])
    
    return submit

if __name__ == '__main__':

    print(my_languages({"Hindi": 60, "Dutch" : 93, "Greek": 71}))
    print(my_languages({"Java": 10, "Ruby": 80, "Python": 65}))