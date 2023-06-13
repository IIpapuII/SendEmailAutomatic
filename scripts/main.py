
from controller.shippingControl  import sendInventorySupplier
from controller.icomeController import sendIcomesJson
import sys

if __name__ == "__main__":
    if len(sys.argv)> 1:
        if sys.argv[1] == 'a':
            sendInventorySupplier()
        elif sys.argv[1] == 'b':
            sendIcomesJson()
    else:
        print('Error')