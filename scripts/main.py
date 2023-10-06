from controller.shippingKccParretto import sendKccParretto
from controller.shippingControl  import sendInventorySupplier
from controller.icomeController import sendIcomesJson
from controller.shippingParretto import sendParrettoCurrent
from controller.shippingSeries import sendSeriesInvoiceCurrent
from controller.IrShippingInventoryReport import sendInventoryReport
from controller.shippingCustomerCollection import sendCustomerCollectionMail
from controller.controllerProject import ejecuteProjectAccounting
from controller.ShippingSpecificParreto import sendSpecificParreto
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
            ejecuteProjectAccounting()
        elif sys.argv[1] == 'g':
            sendInventoryReport()
        elif sys.argv[1] == 'h':
            sendKccParretto()
        elif sys.argv[1] == 'i':
            sendSpecificParreto()
        elif sys.argv[1] == 'test':
            textExtraction()

    else:
        print('Error')