import utils
import sys

def main():
    if (len(sys.argv) != 3):
        print ("usage: %s <credentials.json> <sheetname>" %(sys.argv[0]))
        return 1

    creds = sys.argv[1]
    sheetname = sys.argv[2]
    # authorize returns gspread client instance
    gc = utils.authorize(creds)

    # client.open returns the gspread spreadsheet instance
    spsheet = gc.open(sheetname)

    # spreadsheet.worksheets returns the list of worksheets
    wsheet_list = spsheet.worksheets()

    # print all worksheet titles
    print ("List of sheets in ", sheetname)
    for sheet in wsheet_list:
        print ("- %s" %(sheet.title))

main()
