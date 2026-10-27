import requests

def check_urls(url):
    try:
        response =requests.get(url,timeout=10)
        if response.status_code ==200:
            print("url is online")
        elif response.status_code <400:
            print ("url is online but it redirect to other response")
        else:
            print ("website responsed with an error")
            return False
        print("status_code",response.status_code)
    except requests.exceptions.Timeout:
        print(" request timed out")
    except requests.exceptions.ConnectionError:
        
         print("website could not be reached")
         return False
       
    except requests.exceptions.RequestException as e :
        print("error", e)
        return False 
# check_urls("http://ad;lsjlkdjfksd")