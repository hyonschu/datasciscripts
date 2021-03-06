### tl;dr - script runs through list, asks for changes, changes get
### applied to every occurrence automatically.
### it should help with data janitorialism

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
