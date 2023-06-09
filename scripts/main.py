from controller.shippingControl  import sendInventorySupplier
from controller.icomeController import sendIcomesJson
from controller.shippingParretto import sendParrettoCurrent
from controller.shippingSeries import sendSeriesInvoiceCurrent
from controller.shippingCustomerCollection import sendCustomerCollectionMail
from controller.test import textExtraction
import sys

if __name__ == "__main__":
    if len(sys.argv)> 1:
        if sys.argv[1] == 'a':
            sendInventorySupplier()
        elif sys.argv[1] == 'b':
            sendIcomesJson()
        elif sys.argv[1] == 'c':
            sendParrettoCurrent()
        elif sys.argv[1] == 'd':
            sendSeriesInvoiceCurrent()
        elif sys.argv[1] == 'e':
            sendCustomerCollectionMail()
        elif sys.argv[1] == 'f':
            textExtraction()

    else:
        print('Error')