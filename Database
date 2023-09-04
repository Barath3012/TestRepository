import os
def database(file,mode='',data_dict={},username='',password=''):
    if os.path.isfile(file):
        with open (file) as f:
            data=eval(f.read())
    else:
        with open (file,'w') as f:
            f.write({})
            data={}
    if mode=='r':
        return data
    elif mode=='w':
        if password!='' and username!='':
            data[username]=password
        elif data_dict!={} and type(data_dict)==dict:
            for i in data_dict:
                data[i]==data_dict[i]
        else:
            raise Exception ('No username and/or provided in the arguement')
        with open (file,'w') as f:
            f.write(str(data))
    else:
        raise Exception ('invalid mode')
if __name__ == "__main__":
    print(database("db.txt","w",username="barath",password="30.12.2004"))