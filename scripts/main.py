from controller.shippingKccParretto import sendKccParretto
from controller.shippingControl  import sendInventorySupplier
from controller.icomeController import sendIcomesJson
from controller.shippingParretto import sendParrettoCurrent
from controller.shippingSeries import sendSeriesInvoiceCurrent
from controller.IrShippingInventoryReport import sendInventoryReport
from controller.shippingCustomerCollection import sendCustomerCollectionMail
from controller.controllerProject import ejecuteProjectAccounting
from controller.ShippingSpecificParreto import sendSpecificParreto
from controller.shippingLVPreports import sendLVPreport
from controller.shippingCLGTparretto import sendCLGTparretto
from controller.shippingSendMessageClients import sendMessageClients
from controller.test import textExtraction
import sys

if __name__ == "__main__":
    if len(sys.argv)> 1:
        if sys.argv[1] == 'a':
            sendInventorySupplier() # Inventarios a proveedores
        elif sys.argv[1] == 'b':
            sendIcomesJson() # Sabanas de ventas
        elif sys.argv[1] == 'c':
            sendParrettoCurrent() # Sabanas de ventas actuales (mes)
        elif sys.argv[1] == 'd':
            sendSeriesInvoiceCurrent() # Series de facturas y fechas de vencimiento
        elif sys.argv[1] == 'e':
            sendCustomerCollectionMail() # Cobro a clientes con mora
        elif sys.argv[1] == 'f':
            ejecuteProjectAccounting() # Desconocido
        elif sys.argv[1] == 'g':
            sendInventoryReport() # Inventario - Productos de baja rotacion
        elif sys.argv[1] == 'h':
            sendKccParretto() # Inventario de kimberly
        elif sys.argv[1] == 'i':
            sendSpecificParreto() # Por si Camilo Osorio lo requiere
        elif sys.argv[1] == 'j':
            sendLVPreport() # Sabana e Inventario Levapan
        elif sys.argv[1] == 'k':
            sendCLGTparretto() # Sabana de Ventas de Colgate
        elif sys.argv[1] == 'test':
            textExtraction() # No tocar
        elif sys.argv[1] == 'message':
            sendMessageClients() #Envio manual de mensajes

    else:
        print('Error')