from datetime import datetime


def textExtraction():
    today = datetime.now().day

    if today == 1 or today == 15:
        print("Definitely is one or fifteen")
    else:
        print(today)