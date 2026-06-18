import requests

print("HTTP-response MADE BY aCoDeR RUNNING")
print("UNDER MIT LIECENCE")

target = input("TARGET SITE (for example: http://examplesite.com): ")

how = input("DO YOU WANT HEADER OR ALL OF THE TEXT (HEADER, ALL): ")

try:
    if how.lower() == "header":
        try:
            response = requests.get(target)

            print(response.status_code)
            print(response.headers)

        except:
            print("SOMETHING WENT WRONG, CHECK IF YOU WROTE THE URL CORRECTLY")
    
    if how.lower() == "all":
        try:
            response = requests.get(target)

            print(response.status_code)
            print(response.text)
        except:
            print("SOMETHING WENT WRONG, CHECK IF YOU WROTE THE URL CORRECTLY")

    print("FINISHED")

    if how.lower() != "all" and how.lower() != "header":
        print("SOMETHING WENT WRONG, MAKE SURE YOU CHOOSED HEADER OR ALL AND WROTE IT")

except:
    print("SOMETHING WENT WRONG")
