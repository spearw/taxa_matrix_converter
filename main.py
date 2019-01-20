import re

def run(inputpath):

    output = ""
    data_rows = []

    with open(inputpath) as f:
        content = f.readlines()
        
        line = get_starting_line(content)

        #taxa_name = content[line].strip()
        
        #data_rows = content[line+1:-2]

        while ";" not in content[line]:

            if is_any_alpha(content[line]):

                taxa_name = re.search(r'[A-Z][a-z]*', content[line]).group()

                if re.search(r' [?0-9]+', content[line]) != None: 
                    print re.search(r' [?0-9]+', content[line]).group()
                    data_rows += re.search(r' [?0-9]+', content[line]).group()

            

            else:

                data_rows +=  content[line]

                if is_any_alpha(content[line+1]) or ";" in content[line +1] :

                    data = "".join(data_rows)
                    data = data.translate(None, ' \n\t\r')
                    data = deal_with_polymorphism(data)
                    #print data

                    output = output + combine_taxa_and_data(taxa_name, data) + "\n"
                    del data_rows[:]
                    data_rows = []
            
            line += 1





        return output


    



def get_starting_line(content):

    for line_number, line in enumerate(content):
        if "MATRIX" in line: return (line_number + 1)



def is_any_alpha(s):

    return any(c.isalpha() for c in s)

def combine_taxa_and_data(taxa_name, data):

    return taxa_name + "," + data


def deal_with_polymorphism(data):
    data = data.translate(None, ' \n\t\r')
    formatted_data = ""
    should_pass = False
    index = -1

    for char in data:
        index = index + 1

        TYPES_OF_OPENING_BRACKETS = ["{", "(", "["]
        TYPES_OF_ClOSING_BRACKETS = ["}", ")", "]"]

        if char in TYPES_OF_OPENING_BRACKETS:
            polymorphism = ""
            data_subset= data[index+1: -1]
            for char in data_subset:
                if char in TYPES_OF_ClOSING_BRACKETS:
                    polymorphism = "&".join(polymorphism)
                    formatted_data = formatted_data + polymorphism + ","
                    break
                else:
                    polymorphism += char
            should_pass = True

        elif char in TYPES_OF_ClOSING_BRACKETS:
            should_pass = False
        elif should_pass:
            pass
        else:
            formatted_data = formatted_data + char + ","

    return formatted_data[0:-1]




   
