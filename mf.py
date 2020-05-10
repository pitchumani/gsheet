import json

class mf:
    """A class to handle mutual fund transactions data (google sheet).

    Constructor takes the gspread spreadsheet instance as only argument.

    METHODS
    dump(OUTPUTFILE): outputs the data from the spreadsheet into OUTPUTFILE
      in JSON format.

    dump_summary(OUTPUTFILE): outputs the summary sheet data from the
      spreadsheet into the OUTPUTFILE in JSON format.

    get_summary(): outputs the summary sheet data from the spreadsheet into
      STDOUT in JSON format.
    """
    def __init__(self, sheet):
        self.__sheet = sheet

    def __get_summary_data(self):
        summary_sheet = self.__sheet.worksheet('summary')
        if (summary_sheet == None):
            return None
        rows = summary_sheet.get_all_records()
        num_rows = len(rows)
        entries = []
        for i in range(num_rows - 1):
            # skip the empty rows
            mf_id = rows[i]['AMFI Number']
            if (mf_id == ""):
                continue
            rows[i]['AMFI Number'] = str(mf_id)
            entries.append(rows[i])
        #print ("~~~~~")    
        #print (entries)
        #print ("~~~~~")    
        return entries

    def __get_fund_data(self, mf_id, sheetname, headrow=2):
        fund_sheet = self.__sheet.worksheet(sheetname)
        
        rows = fund_sheet.get_all_records(head=headrow)
        num_rows = len(rows)
        #print ("found %d rows of data (headrow %d)" %(num_rows, headrow))
        transaction_entries = []
        for i in range(num_rows - 1):
            # skip the empty rows
            if (rows[i]['Date'] == ""):
                continue
            transaction_entries.append(rows[i])

        fund_data = {
            "amfiId": mf_id,
            "purchases": transaction_entries
        }
        return fund_data
    
    def __get_all_funds_data(self, summary_data):
        sheets_list = self.__sheet.worksheets()
        num_sheets = len(sheets_list)
        all_funds_list = []
        mf_id_list = []
        for fund in summary_data:
            #print ("ID: %s Name: %s\n", fund['AMFI Number'], fund['Fund name'])
            mf_id_list.append(str(fund['AMFI Number']))
            
        for i in range(num_sheets):
            sheet = sheets_list[i]
            # summary, <nnnnnn>-text, any-text
            sheetname = sheet.title
            mf_id = sheetname[0:6] # amfi identification number
            if mf_id not in mf_id_list:
                continue
            #print ("%d: %s:%s " %(i, mf_id, sheetname))
            fund_data = self.__get_fund_data(mf_id, sheetname, 2)

            if (fund_data != None):
                all_funds_list.append(fund_data)
        
        return all_funds_list
            
    def get_summary(self):
        """get_summary(): outputs the summary sheet data from the
        spreadsheet into STDOUT in JSON format."""

        print(json.dumps(self.__get_summary_data(), indent=4))

    def dump_summary(self,filename):
        """dump_summary(OUTPUTFILE): outputs the summary sheet data from the
        spreadsheet into the OUTPUTFILE in JSON format."""

        with open(filename, 'w') as jsonfile:
            json.dump(self.__get_summary_data(), jsonfile)

    def dump(self,filename):
        """dump(OUTPUTFILE): outputs the data from the spreadsheet into
        OUTPUTFILE in JSON format."""

        name = self.__sheet.title
        summary_data = self.__get_summary_data()
        all_funds_data = self.__get_all_funds_data(summary_data)
        data = {
            "name": name,
            "mfsummary": summary_data,
            "mfunds": all_funds_data
        }
        with open(filename, 'w') as jsonfile:
            json.dump(data, jsonfile)
