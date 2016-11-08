### this is a script that goes through a list of text and asks the user
### to select if it is "correct" or not. upon input, the script will 
### remember the selection for each item and apply it to the next
### occurrence of identical item. it does so through an interactive 
### interface (prompts)

class text_normal():
    def __init__(self, array):
        self.lookup_table = {}
        self.original_data = array
        self.processed_data = []
        for i in self.original_data:
            if i not in self.lookup_table: # if this term isn't in lookup table
                print i, "-- I haven't seen this label before. Type in correct label"
                response = raw_input() # ask for what user wants it to be
                if response == "%options": # options to view existing labels
                    print self.lookup_table.values()
                    print '>>'
                    response = raw_input()
                if response == "%die":
                    return None
                if response == '':
                    self.lookup_table[np.nan] = np.nan
                    self.processed_data.append(np.nan)
                    print i, "updated as", response, '\n'

                else: 
                    self.processed_data.append(response)
                    print i, "updated as", response, '\n'

                self.lookup_table[i] = response
            else:
                self.processed_data.append(self.lookup_table[i])
        print len(self.original_data), "records processed!"    
        tmp = []
        for i in self.processed_data:
            if i == "":
                tmp.append(np.nan)
            else:
                try:
                    tmp.append(" ".join([j.capitalize() for j in i.split(" ")]))
                except: 
                    tmp.append(i)
        self.processed_data = tmp
    def uniques(self):
        return list(set(self.processed_data))