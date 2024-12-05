from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = './kommo.json'  # Ruta al archivo JSON con las credenciales
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = '1h1ncs46M0x8qB1dzlAaeFD2ZY6m_oBBtycIswlW8A-8'
RANGE_NAME = 'Hoja1!A1:D10'

# Busca el valor junto a la celda con el id especificado
def findValue(id):
    # Autenticación con credenciales de la cuenta de servicio
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Construcción del servicio de Google Sheets
    service = build('sheets', 'v4', credentials=creds)

    # Llamada para obtener los datos del rango especificado
    try:
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No se encontraron datos en el rango especificado.')
        else:
            for row in values:
                if row[0] == id: # Primera colunma ID                
                    return row[1] # Segunda columna valor

    except Exception as e:
        print(f'Ocurrió un error: {e}')

if __name__ == '__main__':
    findValue()
