def content(passs):
    import mysql.connector as mp

    conn =mp.connect(host='localhost',user='root',password=passs) 
    if conn.is_connected():
        print('Connected to MySQL database')
    else:
        print("not Connected")
    mycursor=conn.cursor()
    mycursor.execute("create database stationary")
    mycursor.execute("use stationary")

    mycursor.execute("create table Geometry_stuff(GID char(20),ITEM_NAME char(20),TYPE char(10) default NULL,COMPANY char(20),Quantity INT(10),PRICE INT(10))")
    mycursor.execute("insert into Geometry_stuff values('G01','Pen','Ball','Flair',230,5)")
    mycursor.execute("insert into Geometry_stuff values('G02','Pen','Ball','Griper',200,8)")
    mycursor.execute("insert into Geometry_stuff values('G03','Pen','Ball','Cello',240,5)")
    mycursor.execute("insert into Geometry_stuff values('G13','Scale','30cm','Domc',120,35)")
    mycursor.execute("insert into Geometry_stuff values('G14','Scale','30cm','Nataraj',100,28)")
    mycursor.execute("insert into Geometry_stuff values('G15','Scale','30cm','Camel',110,30)")
    mycursor.execute("insert into Geometry_stuff values('G19','Pencil','','Nataraj',120,5)")
    mycursor.execute("insert into Geometry_stuff values('G21','Pencil','','Domc',140,8)")
    mycursor.execute("insert into Geometry_stuff values('G22','Eraser','','Domc',100,5)")
    mycursor.execute("insert into Geometry_stuff values('G23','Eraser','','Nataraj',80,2)")
    mycursor.execute("insert into Geometry_stuff values('G25','Sharpner','','Domc',100,10)")
    mycursor.execute("insert into Geometry_stuff values('G26','Sharpner','','Nataraj',80,3)")
    mycursor.execute("insert into Geometry_stuff values('G28','Geometrybox','','Camel',40,60)")
    mycursor.execute("insert into Geometry_stuff values('G30','Geometrybox','','Invento',40,90)")
    mycursor.execute("insert into Geometry_stuff values('G31','Geometrybox','','Domc',70,75)")
                     
    mycursor.execute("create table Class_Book_Copy(BID varchar(20),BOOK_NAME char(20),CLASS varchar(10), COMPANY varchar(20), Quantity int(4), PRICE int(10))");
    mycursor.execute("insert into Class_Book_Copy values('b01', 'English',1,'ncert',200,120)")
    mycursor.execute("insert into Class_Book_Copy values('b02', 'Maths',1,'ncert',240,180)")
    mycursor.execute("insert into Class_Book_Copy values('b03', 'Evs',1,'ncert',180,160)")
    mycursor.execute("insert into Class_Book_Copy values('b04', 'Hindi',1,'ncert',160,140)")
    mycursor.execute("insert into Class_Book_Copy values('b05', 'English',2,'ncert',210,130)")
    mycursor.execute("insert into Class_Book_Copy values('b06', 'Maths',2,'ncert',240,190)")
    mycursor.execute("insert into Class_Book_Copy values('b07', 'Evs',2,'ncert',160,170)")
    mycursor.execute("insert into Class_Book_Copy values('b08', 'Hindi',2,'ncert',150,145)")
    mycursor.execute("insert into Class_Book_Copy values('b09', 'English',3,'ncert',220,140)")
    mycursor.execute("insert into Class_Book_Copy values('b10', 'Maths',3,'ncert',240,200)")
    mycursor.execute("insert into Class_Book_Copy values('b11', 'Evs',3,'ncert',190,175)")
    mycursor.execute("insert into Class_Book_Copy values('b12', 'Hindi',3,'ncert',140,150)")
    mycursor.execute("insert into Class_Book_Copy values('b13', 'English',4,'ncert',230,150)")
    mycursor.execute("insert into Class_Book_Copy values('b14', 'Maths',4,'ncert',240,210)")
    mycursor.execute("insert into Class_Book_Copy values('b15', 'Evs',4,'ncert',185,180)")
    mycursor.execute("insert into Class_Book_Copy values('b16', 'Hindi',4,'ncert',165,160)")
    mycursor.execute("insert into Class_Book_Copy values('b17', 'English',5,'ncert',200,160)")
    mycursor.execute("insert into Class_Book_Copy values('b18', 'Maths',5,'ncert',240,220)")
    mycursor.execute("insert into Class_Book_Copy values('b19', 'Evs',5,'ncert',180,195)")
    mycursor.execute("insert into Class_Book_Copy values('b20', 'Hindi',5,'ncert',160,180)")

    mycursor.execute("create table Sports(SID varchar(20),Name char(20),Company char(20),Quantity int(20),Price int(20))")
    mycursor.execute("insert into Sports values('S01','Ball','Vicky',20,60)")
    mycursor.execute("insert into Sports values('S02','Bat','SS',20,5000)")
    mycursor.execute("insert into Sports values('S03','Football','Nevo',20,700)")
    mycursor.execute("insert into Sports values('S04','Basketball','Nevo',20,800)")
    mycursor.execute("insert into Sports values('S05','Vollyball','Nevo',20,900)")
    mycursor.execute("insert into Sports values('S06','Badmintion','Yonex',20,400)")
    mycursor.execute("insert into Sports values('S07','Corck','Yonex',20,50)")
    mycursor.execute("insert into Sports values('S08','Baseball','SG',20,600)")
    mycursor.execute("insert into Sports values('S09','Chess Board','CSRE',20,100)")
    mycursor.execute("insert into Sports values('S10','Cream Board','JYGF',20,250)")

    mycursor.execute("create table Projects_stuff(PID varchar(20),Name char(20),Company char(20),Quantity int(20),Price int(20))")
    mycursor.execute("insert into Projects_stuff values('P01','Thermacol','HGV',20,30)")
    mycursor.execute("insert into Projects_stuff values('P02','Paper Cutter','UJG',20,20)")
    mycursor.execute("insert into Projects_stuff values('P03','Glaze Paper','Nevo',20,15)")
    mycursor.execute("insert into Projects_stuff values('P04','Motor','Nevo',20,40)")
    mycursor.execute("insert into Projects_stuff values('P05','Battery','Nevo',20,20)")
    mycursor.execute("insert into Projects_stuff values('P06','Copper Wire','Yonex',20,10)")
    mycursor.execute("insert into Projects_stuff values('P07','LED','Yonex',20,7)")
    mycursor.execute("insert into Projects_stuff values('P08','Paper Pins','SG',20,30)")
    mycursor.execute("insert into Projects_stuff values('P09','Carboard','CSRE',20,25)")
    mycursor.execute("insert into Projects_stuff values('P10','Gelatin Cover','JYGF',20,20)")

    mycursor.execute("create table CART(PID varchar(20),QUANTITY int(10),Address varchar(50),Payment_method varchar(20))")
    mycursor.execute("insert into CART values('G22',2,'H.no-567,Aya Nagar,New Delhi','COD')")
    mycursor.execute("insert into CART values('S03',1,'H.no-347,Gitorni,New Delhi','Debit Card')")
    mycursor.execute("insert into CART values('P10',6,'H.no-844,Rohani,New Delhi','COD')")

    mycursor.execute("create table info(Username varchar(20),Password varchar(20))")


    conn.commit()
    conn.close()
