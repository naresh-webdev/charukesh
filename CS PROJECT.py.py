import mysql.connector as a
con=a.connect(host='localhost',user='root',passwd='prince',database='ebookstore')

def addbook():
    bn=input('Enter book name:')
    c=input('Enter book code:')
    t=input('Total books:')
    s=input('Enter subject:')
    data=(bn,c,t,sA)
    sql='insert into book values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print('Data entered successfully')
    main()
    
def issueb():
    n=input('Enter name:')
    r=input('Enter reg no:')
    co=input('Enter book code:')
    d=input('Enter date:')
    a='insert into issue values(%s,%s,%s,%s)'
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print('Book issed to:',n)
    bookup(co,-1)
    
def submitb():
    n=input('Enter Name:')
    r=input('Enter reg no:')
    co=input('Enter book code:')
    d=input('Enter date:')
    a='insert into submit values(%s,%s,%s,%s)'
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print('Book issed to:',n)
    bookup(co,-1)
    
def bookup(co,u):
    a='select TOTAL from book where BCODE=%s'
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql='update book set TOTAL=%s where BCODE=%s'
    d=(t,co)
    c.execute(sql,d)
    con.commit()
    main()
    
def dbook():
    ac=input('Enter book code:')
    a='delete from book where BCODE=%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()
    
def dispbook():
    a='select * from book'
    c=con.cursor()
    c.execute(a)
    myresult=c.fectchall()
    for i in myresult:
        print('Book Name:',i[0])
        print('Book Code:',i[1])
        print('Total:',i[2])
    main()
    
def main():
    print("""                                      EBOOKSTORE MANAGEMENT

                1.ADD BOOK
                2.ISSUE BOOK
                3.SUBMIT BOOK
                4.DELETE BOOK
                5.DISPLAY BOOKS
          """)
    choice=input('Enter Task no:')
    if (choice=='1'):
        addbook()
    elif(choice=='2'):
        issueb()
    elif (choice=='3'):
        submitb()
    elif (choice=='4'):
        dbook()
    elif (choice=='5'):
        dispbook()
    else:
        print('Wrong choice.....')
        main()
        
def pswd():
    ps=input('Enter Password:')
    if ps=='prince':
        main()
    else:
        print('Wrong Password:')
        pswd()
pswd()
          
    
