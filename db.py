import sqlite3

naver_list = []
google_list = []


def update(n_id,n_pw,g_id,g_pw):
    print("변경")

    conn = sqlite3.connect('main.db')

    cursor = conn.cursor()



    cursor.execute("UPDATE email_data SET  id = ?,pw=? WHERE name = ?", (n_id, n_pw,"naver"))
    cursor.execute("UPDATE email_data SET  id = ?,pw=? WHERE name = ?", (g_id, g_pw,"google"))

    conn.commit()
    conn.close()

def select():

    # SQLite 데이터베이스 연결
    conn = sqlite3.connect('main.db')

    cursor = conn.cursor()

    cursor.execute('select * from email_data;')
   
    data_list = cursor.fetchall()
    naver_list.clear()
    google_list.clear()

    for i in range(0,3):
        naver_list.append(data_list[0][i])
        google_list.append(data_list[1][i])


    conn.close()
 
