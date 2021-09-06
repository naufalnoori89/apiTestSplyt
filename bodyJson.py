import json

class BodyJson:
    
    def createRecord(self, header, row):
        if row[6] == "N":
            pickup = {header[4]: row[4],\
                  header[5]: row[5]}
            passenger = {header[7]: row[7],\
                    header[8]: row[8],}      
            record = {header[10]: row[10],\
                    header[3]: pickup,\
                    header[6]: passenger}
        else:
            pickup = {header[4]: row[4],\
                  header[5]: row[5]}
            passenger = {header[7]: row[7],\
                    header[8]: row[8],\
                    header[9]: row[9]}      
            record = {header[10]: row[10],\
                    header[3]: pickup,\
                    header[6]: passenger}

        return record
    
####### UNIT TEST PURPOSE ONLY. NOT MAIN CLASS
# if __name__ == '__main__':
#     createRecord();
