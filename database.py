import os
def database(file,mode="r",data_dict={},username="",password=""):

    #Read file if exists, else create it.
    if os.path.isfile(file):
        with open(file) as f:
            data = eval(f.read())
            
    else:
        with open(file,"w") as f:
            f.write("{}")
            data = {}

    #If the function was called using read mode, return data
    if mode == "r":
        return data

    #else, if the mode is write mode, write appropriate data
    elif mode == "w":
        if username!="" and password!="":
            data[username] = password
                
        elif data_dict != {} and type(data_dict) == dict:
            for i in data_dict:
                data[i] = data_dict[i]
                
        else:
            raise Exception("No username and/or password provided in the argument.")

        #Write the updated data back into the file
        with open(file,"w") as f:
            f.write(str(data))
    else:
        raise Exception("Invalid mode, check documentation.")

if __name__ == "__main__":
    
    print(database("db.txt","w",username="barath",password="30.12.2004")) 