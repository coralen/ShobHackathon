import random
import time

ERRORS_LIST = list(range(400,599)) 
SUCCESS_LIST = ["200"]*2000
HTTP_STATUS_LIST = ERRORS_LIST+SUCCESS_LIST #errors list will form 10% of all return codes
CLIENTS_LIST = ["Omer","Dan","Osnat","Shira","Idan","Avi","Eli","Arnit","Coral","yair","Dominos Pizza","Small Business"]
BUSINESS_LIST = ["Dominos Pizza","Small Business"]
AMOUNT_LIST = range(1,3600)
IS_BUSINESS_DICT = {True:"business",False:"client"}

def main():

    while True:
        status = random.choice(HTTP_STATUS_LIST)
        client = random.choice(CLIENTS_LIST)
        is_business = False
        if (client in BUSINESS_LIST):
            is_business = True
        amount = random.choice(AMOUNT_LIST)
        user_desc = IS_BUSINESS_DICT[is_business]
        print ("The "+ user_desc+" "+client+" paid "+str(amount)+" with bit. Return Code: "+str(status))
        time.sleep(30)

if __name__ == "__main__":
    main()
