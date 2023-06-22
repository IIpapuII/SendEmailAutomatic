
from controller.shippingControl  import sendInventorySupplier
from controller.icomeController import sendIcomesJson
from controller.shippingParretto import sendParrettoCurrent
import sys

if __name__ == "__main__":
    if len(sys.argv)> 1:
        if sys.argv[1] == 'a':
            sendInventorySupplier()
        elif sys.argv[1] == 'b':
            sendIcomesJson()
        elif sys.argv[1] == 'c':
            sendParrettoCurrent()
    else:
        print('Error')