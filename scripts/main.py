
from sendMail import sendMail

if __name__ == "__main__":
    data = sendMail('wilmer','compras','HI')
    data.sendProviderEmail('Inventario kimberly.xlsx')