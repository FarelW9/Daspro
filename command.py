import os
from function import *

def login(user):
    Username=input("Username : ")
    Password=input("Password : ")
    user_valid=False
    pass_valid=False
    for i in range (1,length(user)):
        if Username == user[i][0] :
            user_valid=True
            if Password==user[i][1]:
                pass_valid=True
                break
    
    if user_valid==True and pass_valid==True:
        print (f'\nSelamat datang, {Username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')
        return (user[i][2],user[i][0])
    elif user_valid==True and pass_valid==False:
        print("\nPassword salah!")
        return 0,0
    else:
        print("\nUsername tidak terdaftar!")
        return 0,0

def logout(role):
    if role == 0 :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        role=0
    else :
        role=0
    
    return role

def summonjin(user,role):
    if length(user)<104 and role=="bandung_bondowoso":
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")
        valid=False
        new_user=[0,0,0]
        while valid==False:
            nomor=input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")
            if nomor=="1" or nomor=="Pengumpul":
                print("\nMemilih jin “Pengumpul”.")
                valid=True
                new_user[2]="jin_pengumpul"
            elif nomor=="2" or nomor=="Pembangun":
                print("\nMemilih jin “Pembangun”.")
                valid=True
                new_user[2]="jin_pembangun"
            elif nomor!="1" or nomor!="2" or nomor!="Pembangun" or nomor!="Pengumpul" :
                print(f"\nTidak ada jenis jin bernomor “{nomor}”!")
        valid=False
        while valid==False:
            nama=input("\nMasukkan username jin: ")
            j=1
            while j<length(user):
                if user[j][0]==nama:
                    print(f"\nUsername “{nama}” sudah diambil!")
                    valid=False
                    break
                else :
                    j+=1            
                
            if j == length(user):
                valid=True
                new_user[0]=nama

        valid=False
        password=input("Masukkan password jin: ")
        while valid==False:
            len_pass=0
            for i in password:
                len_pass+=1
            if 5<=len_pass<=25 :
                valid=True
                new_user[1]=password
                print("\nMengumpulkan sesajen...")
                print("Menyerahkan sesajen...")
                print("Membacakan mantra...")
                print(f"\nJin {new_user[0]} berhasil dipanggil!")
            else:
                print("\nPassword panjangnya harus 5-25 karakter!")
                password=input("\nMasukkan password jin: ")  
                valid=False              
        
        return new_user
    elif length(user)>=104:
        return 0
    if role!="bandung_bondowoso":
        return 1

def hapusjin(user,candi,role):
    if role=="bandung_bondowoso":
        name_del=input("Masukkan username jin : ")
        if name_del=="Bondowoso":
            print("Tidak bisa menghapus Bandung Bondowoso")
        elif name_del=="Roro":
            print("Tidak bisa menghapus Roro Jonggrang")
        else:
            j=3
            while j < length(user):
                if name_del==user[j][0] :
                    break
                else :
                    j+=1
            if j==length(user):
                print("\nTidak ada jin dengan username tersebut.")
            else:
                valid=input(f"Apakah anda yakin ingin menghapus jin dengan username {name_del} (Y/N)? ")
                if valid=="Y" or valid=="y":
                    user=delete_user(user,j)
                    habis=False
                    while habis==False:
                        for i in range (1,length(candi)):
                            if candi[i][1]==name_del:
                                candi=delete_candi(candi,i)
                                break
                        if i==length(candi)-1:
                            habis=True
                    print("Jin telah berhasil dihapus dari alam gaib.")
                    return user,candi
                else:
                    return user,candi
    else :
        return 1

def ubahjin(user,role):
    if role=="bandung_bondowoso":
        role_change=input("Masukkan username jin : ")
        j=1
        while j < length(user):
            if role_change==user[j][0] :
                break
            else :
                j+=1
        if j==length(user):
            print("\nTidak ada jin dengan username tersebut.")
        else:
            if user[j][2]=="jin_pengumpul":
                valid=input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                if valid=="Y" or valid=="y":
                    user[j][2]="jin_pembangun"
                    print("\nJin telah berhasil diubah.")
                    return user
                else:
                    return user            
            elif user[j][2]=="jin_pembangun":
                valid=input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")               
                if valid=="Y" or valid=="y":
                    user[j][2]="jin_pengumpul"
                    print("\nJin telah berhasil diubah.")
                    return user
                else:
                    return user
    else :
        return 1

def bangun(candi,username,bahan,role,seed):
    if role=="jin_pembangun":
        temp=seed
        pasir,seed=random(1,5,seed)
        batu,seed=random(1,5,seed)
        air,seed=random(1,5,seed)
        if int(bahan[1][2])>=pasir and int(bahan[2][2])>=batu and int(bahan[2][2])>=air:
            pasir_new=int(bahan[1][2])-pasir
            batu_new=int(bahan[2][2])-batu
            air_new=int(bahan[3][2])-air
            bahan[1][2]=pasir_new
            bahan[2][2]=batu_new
            bahan[3][2]=air_new

            data_add=[str(ID_generator(candi)),username,str(pasir),str(batu),str(air)]
            for i in range(101):
                if candi[i]=="%":
                    candi[i]=data_add
                    break
            
            id_list=["%" for i in range (101)]
            k=0
            valid=True
            for i in range(1,101):
                if length(id_list)==0 and candi[i]!="%":
                    id_list[k]=candi[i][0]
                    k+=1
                for j in range(length(id_list)):
                    valid=True
                    if candi[i][0]==id_list[j][0] and candi[i]!="%":
                        valid=False
                if valid==True and candi[i]!="%":
                    id_list[k]=candi[i][0]
                    k+=1
            
            count=length(id_list)

            if count>=100:
                sisa=0
            else:
                sisa=100-count
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {sisa}")
            return seed,candi,bahan
        else:
            print("Bahan bangunan tidak mencukupi")
            print("Candi tidak bisa dibangun.")
            return temp,candi,bahan
    else :
        return "%"

def kumpul(bahan,role,seed):
    if role=="jin_pengumpul":
        pasir,seed=random(0,5,seed)
        batu,seed=random(0,5,seed)
        air,seed=random(0,5,seed)
        pasir_new=int(bahan[1][2])+pasir
        batu_new=int(bahan[2][2])+batu
        air_new=int(bahan[3][2])+air
        bahan[1][2]=str(pasir_new)
        bahan[2][2]=str(batu_new)
        bahan[3][2]=str(air_new)

        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air")

        return seed,bahan

    else :
        return "%"

def batchkumpul(user,bahan,role,seed):
    if role=="bandung_bondowoso":
        pengumpul=0
        for i in range(length(user)):
            if user[i][2]=="jin_pengumpul":
                pengumpul+=1
        
        if pengumpul==0:
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon\nterlebih dahulu.")
        else:
            pasir_temp=int(bahan[1][2])
            batu_temp=int(bahan[2][2])
            air_temp=int(bahan[3][2])
            temu_pasir=0
            temu_batu=0
            temu_air=0
            for i in range (pengumpul):
                pasir,seed=random(0,5,seed)
                batu,seed=random(0,5,seed)
                air,seed=random(0,5,seed)
                pasir_temp+=pasir
                batu_temp+=batu
                air_temp+=air
                temu_pasir+=pasir
                temu_batu+=batu
                temu_air+=air
            bahan[1][2]=str(pasir_temp)
            bahan[2][2]=str(batu_temp)
            bahan[3][2]=str(air_temp)

            print(f"Mengerahkan {pengumpul} jin untuk mengumpulkan bahan.")
            print(f"Jin menemukan {temu_pasir} pasir, {temu_batu} batu, dan {temu_air} air")

            return seed,bahan
    
    else :
        return "%"

def batchbangun(user,candi,bahan,role,seed):
    if role=="bandung_bondowoso":
        pembangun=0
        for i in range (length(user)):
            if user[i][2]=="jin_pembangun":
                pembangun+=1
        
        if pembangun==0:
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon\nterlebih dahulu.")
        else:
            temp=seed
            pasir_temp=int(bahan[1][2])
            batu_temp=int(bahan[2][2])
            air_temp=int(bahan[3][2])
            perlu_pasir=0
            perlu_batu=0
            perlu_air=0
            pasir_list=["%" for i in range (pembangun)]
            batu_list=["%" for i in range (pembangun)]
            air_list=["%" for i in range (pembangun)]
            for i in range (pembangun):
                pasir,seed=random(1,5,seed)
                batu,seed=random(1,5,seed)
                air,seed=random(1,5,seed)
                perlu_pasir+=pasir
                perlu_batu+=batu
                perlu_air+=air
                pasir_list[i]=pasir
                batu_list[i]=batu
                air_list[i]=air
            
            if pasir_temp-perlu_pasir>=0 and batu_temp-perlu_batu>=0 and air_temp-perlu_air>=0:
                pasir_new=pasir_temp-perlu_pasir
                batu_new=batu_temp-perlu_batu
                air_new=air_temp-perlu_air
                bahan[1][2]=str(pasir_new)
                bahan[2][2]=str(batu_new)
                bahan[3][2]=str(air_new)

                print(f"Mengerahkan {pembangun} jin untuk menmbangun candi dengan total bahan {perlu_pasir} pasir, {perlu_batu} batu, dan {perlu_air} air.")
                print(f"Jin berhasil membangun total {pembangun} candi")

                kontributor=["%" for i in range(pembangun)]

                j=0
                for i in range(length(user)):
                    if user[i][2]=="jin_pembangun":
                        kontributor[j]=user[i][0]
                        j+=1

                for i in range (pembangun):

                    data_add=[str(ID_generator(candi)),kontributor[i],str(pasir_list[i]),str(batu_list[i]),str(air_list[i])]
                    for j in range(101):
                        if candi[j]=="%":
                            candi[j]=data_add
                            break

                return seed,candi,bahan
            
            else:
                kurang_pasir =pasir_temp-perlu_pasir
                if kurang_pasir<0:
                    kurang_pasir=(-1)*kurang_pasir
                kurang_batu=batu_temp-perlu_batu
                if kurang_batu<0:
                    kurang_batu=(-1)*kurang_batu
                kurang_air=air_temp-perlu_air
                if kurang_air<0:
                    kurang_air=(-1)*kurang_air
                print(f"Mengerahkan {pembangun} jin untuk menmbangun candi dengan total bahan {perlu_pasir} pasir, {perlu_batu} batu, dan {perlu_air} air.")
                print(f"Bangun gagal. Kurang {kurang_pasir} pasir, {kurang_batu} batu, dan {kurang_air} air")
                return temp,candi,bahan
    
    else :
        return "%"

def laporanjin(user,candi,bahan,role):
    if role=="bandung_bondowoso":
        total=length(user)-3
        total_pengumpul=0
        total_pembangun=0
        for i in range(3,length(user)):
            if user[i][2]=="jin_pengumpul":
                total_pengumpul+=1
            if user[i][2]=="jin_pembangun":
                total_pembangun+=1
        if total_pembangun==0:
            malas="-"
            rajin="-"
        else:
            user_list=["%" for i in range (length(user)+1)]
            for i in range (length(user)):
                user_list[i]=user[i][0]
            malas=(2**32)
            rajin=-(2**32)
            siapa_malas="z"*(2**10)
            siapa_rajin="z"*(2**10)
            for i in range(3,length(user_list)):
                kontribusi=0
                for j in range(1,102):
                    if candi[j]!="%" and user_list[i]==candi[j][1]:
                        kontribusi+=1
                print(user_list[i])
                if kontribusi>rajin:
                    rajin=kontribusi
                    siapa_rajin=user_list[i]
                elif kontribusi==rajin and user_list[i]<siapa_rajin:
                    rajin=kontribusi
                    siapa_rajin=user_list[i]                    
                if kontribusi<malas:
                    malas=kontribusi
                    siapa_malas=user_list[i]
                elif kontribusi==malas and user_list[i]<siapa_rajin:
                    malas=kontribusi
                    siapa_malas=user_list[i] 

        pasir=bahan[1][2]
        batu=bahan[2][2]
        air=bahan[3][2]

        print(f"\n> Total Jin: {total}")
        print(f"> Total Jin Pengumpul: {total_pengumpul}")
        print(f"> Total Jin Pembangun: {total_pembangun}")
        print(f"> Jin Terajin: {siapa_rajin}")
        print(f"> Jin Termalas: {siapa_malas}")
        print(f"> Jumlah Pasir: {pasir} unit")
        print(f"> Jumlah Air: {air} unit")
        print(f"> Jumlah Batu: {batu} unit")


    else :
        return 1

def laporancandi(candi,role):
    if role=="bandung_bondowoso":
        candi_list=["%" for i in range (100)]
        k=0
        valid=True
        for i in range(1,101):
            if length(candi_list)==0 and candi[i]!="%":
                candi_list[k]=candi[i][0]
                k+=1
            for j in range(length(candi_list)):
                valid=True
                if candi[i][0]==candi_list[j][0] and candi[i]!="%":
                    valid=False
            if valid==True and candi[i]!="%":
                candi_list[k]=candi[i][0]
                k+=1

        pasir_total=0
        batu_total=0
        air_total=0
        id_mahal=0
        id_murah=0
        mahal=-(2**32)
        murah=2**32
        for i in range(1,101):
            if candi[i]!="%":
                harga=int(candi[i][2])*10000+int(candi[i][3])*15000+int(candi[i][4])*7500
                pasir_total+=int(candi[i][2])
                batu_total+=int(candi[i][3])
                air_total+=int(candi[i][4])
                for j in range(1,101):
                    if candi[i]!="%" and i!=j and candi[i][0]==candi[j][0]:
                        harga+=int(candi[j][2])*10000+int(candi[j][3])*15000+int(candi[j][4])*7500
                if harga>mahal:
                    mahal=harga
                    id_mahal=int(candi[i][0])
                if harga<murah:
                    murah=harga
                    id_murah=int(candi[i][0])

        if length(candi_list)==0:
            print(f"\n> Total Candi: {length(candi_list)}")
            print(f"> Total Pasir yang digunakan: {pasir_total}")
            print(f"> Total Batu yang digunakan: {batu_total}")
            print(f"> Total Air yang digunakan: {air_total}")
            print(f"> ID Candi Termahal: -")
            print(f"> ID Candi Termurah: -")            

        else:
            print(f"\n> Total Candi: {length(candi_list)}")
            print(f"> Total Pasir yang digunakan: {pasir_total}")
            print(f"> Total Batu yang digunakan: {batu_total}")
            print(f"> Total Air yang digunakan: {air_total}")
            print(f"> ID Candi Termahal: {id_mahal} (Rp {mahal})")
            print(f"> ID Candi Termurah: {id_murah} (Rp {murah})")

    else :
        return 1

def hancurkancandi(candi,role):
    if role=="roro_jonggrang":
        ID=input("Masukkan ID candi: ")
        ada=False
        for i in range(length(candi)):
            if i>0 and candi[i][0]==ID:
                ada=True
                break
        if ada==True:
            valid=input(f"Apakah anda yakin ingin menghancurkan candi ID: {ID} (Y/N)? ")
            if valid=="Y" or valid=="y":
                print("\nCandi telah berhasil dihancurkan.")
                candi=delete_candi(candi,i)
                return candi
            else:
                return candi
        else:
            print("\nTidak ada candi dengan ID tersebut.")
            return candi

    else :
        return 1

def ayamberkokok(candi,role):
    if role=="roro_jonggrang":
        print("Kukuruyuk.. Kukuruyuk..")
        print(f"\nJumlah Candi: {length(candi)}")
        if 0<=length(candi)<100:
            print("\nSelamat, Roro Jonggrang memenangkan permainan!")
            print("\n*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
        elif length(candi)>=100:
            print("\nYah, Bandung Bondowoso memenangkan permainan!")

    else :
        return 1

def save(user,bahan,candi):
    nama_folder=input("Masukkan nama folder: ")
    if os.path.exists("Save"):
        cd=os.path.join("Save",nama_folder)
        if not os.path.exists(cd):
            print("\nSaving...")
            print(f"\nMembuat folder {nama_folder}!")
            print(f"\nBerhasil menyimpan data di folder {nama_folder}")
            os.makedirs(cd)
            with open(f"Save/{nama_folder}/user.csv", 'w') as csv:
                for i in range(length(user)):
                    data=user[i]
                    csv_line = ';'.join(str(x) for x in data) + '\n'
                    csv.write(csv_line)
            with open(f"Save/{nama_folder}/bahan_bangunan.csv", 'w') as csv:
                for i in range(length(bahan)):
                    data=bahan[i]
                    csv_line = ';'.join(str(x) for x in data) + '\n'
                    csv.write(csv_line)
            with open(f"Save/{nama_folder}/candi.csv", 'w') as csv:
                for i in range(length(candi)):
                    data=candi[i]
                    csv_line = ';'.join(str(x) for x in data) + '\n'
                    csv.write(csv_line)
        else:
            print("\nSaving...")
            print(f"\nBerhasil menyimpan data di folder {nama_folder}")
            with open(f"Save/{nama_folder}/user.csv", 'w') as csv:
                for i in range(length(user)):
                    data=user[i]
                    csv_line = ';'.join(str(x) for x in data) + '\n'
                    csv.write(csv_line)
            with open(f"Save/{nama_folder}/bahan_bangunan.csv", 'w') as csv:
                for i in range(length(bahan)):
                    data=bahan[i]
                    csv_line = ';'.join(str(x) for x in data) + '\n'
                    csv.write(csv_line)
            with open(f"Save/{nama_folder}/candi.csv", 'w') as csv:
                for i in range(length(candi)):
                    data=candi[i]
                    csv_line = ';'.join(str(x) for x in data) + '\n'
                    csv.write(csv_line)
    else:
        os.makedirs("Save")
        cd=os.path.join("Save",nama_folder)
        print("\nSaving...")
        os.makedirs(cd)
        with open(f"Save/{nama_folder}/user.csv", 'w') as csv:
            for i in range(length(user)):
                data=user[i]
                csv_line = ';'.join(str(x) for x in data) + '\n'
                csv.write(csv_line)
        with open(f"Save/{nama_folder}/bahan_bangunan.csv", 'w') as csv:
            for i in range(length(bahan)):
                data=bahan[i]
                csv_line = ';'.join(str(x) for x in data) + '\n'
                csv.write(csv_line)
        with open(f"Save/{nama_folder}/candi.csv", 'w') as csv:
            for i in range(length(candi)):
                data=candi[i]
                csv_line = ';'.join(str(x) for x in data) + '\n'
                csv.write(csv_line)

def help(role):
    if role=="bandung_bondowoso":
        print("===================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. hapusjin")
        print("   Untuk menghapus jin")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin")
        print("5. batchkumpul")
        print("   Untuk mengumpulkan bahan")
        print("6. batchbangun")
        print("   Untuk mengumpulkan jin bangun")
        print("7. laporanjin")
        print("   Untuk mengetahui kinerja jin")
        print("8. laporancandi")
        print("   Untuk mengetahui proses pembangunan candi")
        print("9. save")
        print("   Untuk menyimpan data")

    elif role=="roro_jonggrang":
        print("===================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok")
        print("   Untuk menyelesaikan permainan.")
        print("4. save")
        print("   Untuk menyimpan data")
    
    elif role=="jin_pengumpul":
        print("====================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan resource candi")

    elif role=="jin_pembangun":
        print("====================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")

    elif role==0:
        print("====================== HELP ======================")
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
        print("3. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")

    else:
        return None

def exit(Exit,user,bahan,candi):
    valid=False
    while valid==False:
        simpan=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        if simpan == "y" or simpan=="Y":
            save(user,bahan,candi)
        elif simpan=="n"or simpan=="N" :
            valid=True
            Exit=True
            return Exit
        