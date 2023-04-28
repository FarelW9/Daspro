
def length (list:list) -> int: #Fungsi menghitung panjang list / array
    count=0
    while list[count]!="%":
        count+=1
    return count

def read_user(file_csv:str) -> list: #Fungsi membaca file user.csv
    with open(file_csv) as csv: 
        data=csv.readlines()
        data_fix=["%" for i in range (104)]
        k=0
        for baris in data :
            j=0
            part=["%" for i in range(3)]
            temp=""
            for huruf in baris:
                if huruf==";" or huruf=="\n":
                    part[j]=temp
                    j+=1
                    temp=""
                else :
                    temp+=huruf
            data_fix[k]=part
            k+=1
        return (data_fix)

def read_bahan(file_csv:str) -> list: #Fungsi membaca file bahan_bangunan.csv
    with open(file_csv) as csv: 
        data=csv.readlines()
        data_fix=["%" for i in range (5)]
        k=0
        for baris in data :
            j=0
            part=["%" for i in range(3)]
            temp=""
            for huruf in baris:
                if huruf==";" or huruf=="\n":
                    part[j]=temp
                    j+=1
                    temp=""
                else :
                    temp+=huruf
            data_fix[k]=part
            k+=1
        return (data_fix)

def read_candi(file_csv:str) -> list: #Fungsi membaca file candi.csv
    with open(file_csv) as csv: 
        data=csv.readlines()
        data_fix=["%" for i in range (102)]
        k=0
        for baris in data :
            j=0
            part=["%" for i in range(5)]
            temp=""
            for huruf in baris:
                if huruf==";" or huruf=="\n":
                    part[j]=temp
                    j+=1
                    temp=""
                else :
                    temp+=huruf
            data_fix[k]=part
            k+=1
        return (data_fix)

def delete_user(list:list,j:int) -> list: #Fungsi menghapus data user
    list_new=["%" for i in range(104)]
    k=0
    for i in range(3):
        list_new[k]=list[i]
        k+=1
    for i in range(3,104):
        if i!=j:
            list_new[k]=list[i]
            k+=1
    return list_new

def delete_candi(list:list,j:int) -> list: #Fungsi menghapus data candi
    list_new=["%" for i in range(102)]
    k=0
    for i in range(1):
        list_new[k]=list[i]
        k+=1
    for i in range(1,102):
        if i!=j:
            list_new[k]=list[i]
            k+=1
    return list_new

def random(min:int, max:int, seed:int) -> int and int: #Fungsi LCG (Random Number Generator)
    seed1= (1103515245 * seed + 12345) % 2**31
    random_number = (seed1 % (max - min + 1)) + min
    seed=seed1
    return random_number,seed

def isibahan(data_bahan:list) -> list: #Fungsi pengecekan data bahan
    if length(data_bahan)==1:
        data_bahan[1]=["pasir","bahan",0]
        data_bahan[2]=["batu","bahan",0]
        data_bahan[3]=["air","bahan",0]
    return data_bahan

def ID_generator(candi:list) -> int: #Fungsi menentukan ID Candi
    id_list=["%" for i in range (100)]
    k=0
    for i in range(1,length(candi)):
        id_list[k]=int(candi[i][0])
        k+=1
    for i in range(1,101):
        Ada=True
        for j in range(100):
            if id_list[j]!="%" and i==id_list[j] :
                Ada=False
                break
        if Ada==True:
            return i
