delimiter = ','


# file format : token,timestamp(yyyy-MM-dd-HH-mm),price(INR)
def read_data(file_name):
    try:
        data = {}
        with open(file_name, 'r') as f:
            for line in f:
                tokens = line.split(delimiter)
                if len(tokens) == 3:
                    key = tokens[0] + "_" + tokens[1]
                    data[key] = float(tokens[2])
        return data
    except FileNotFoundError as e:
        print(file_name + " not found error : " + str(e))
        return {}


def write_data(data, file_name):
    try:
        with open(file_name, 'w') as f:
            for line in data:
                tokens = line.split('_')
                f.write(tokens[0] + "," + tokens[1] + "," + str(data[line]))
                f.write("\n")
        f.close()
    except FileNotFoundError as e:
        print(file_name + " not found error : " + str(e))
