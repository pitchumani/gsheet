import utils
import sys
from mf import mf

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

    # create a object of 'mf' class,
    # takes gspread spreadsheet instance
    mfsheet = mf(spsheet)

    # dump all data from spreadsheet into a file
    mf_json_file = sheetname + ".json"
    mfsheet.dump(mf_json_file)

    # output the summary sheet data
    mfsheet.get_summary()

    # dump summary data into a file
    mf_summary_json_file = sheetname + "-summary.json"
    mfsheet.dump_summary(mf_summary_json_file)
    
main()
