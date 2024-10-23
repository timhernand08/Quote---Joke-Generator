import sqlite3, time
from datetime import datetime


    
def storeData(quote, joke):
    connect = sqlite3.connect('Client_data.db')
    cur = connect.cursor()
    cur.execute("INSERT INTO jokes (joke) VALUES (:joke)", {'joke': joke})
    cur.execute("INSERT INTO quotes (quote) VALUES (:quote)", {'quote': quote})
    connect.commit()
    connect.close()
    timePassed("quotes")
    timePassed("jokes")

def hasQuote(quote):
    connect = sqlite3.connect('Client_data.db')
    cur = connect.cursor()
    cur.execute("SELECT EXISTS(SELECT 1 FROM quotes WHERE quote = ?)", (quote,))

    result = cur.fetchone()[0]
    connect.close()
    
    if result == 1:
        print("This exists!")
        return True
    else:
        return False
    
def hasJoke(joke):
    connect = sqlite3.connect('Client_data.db')
    cur = connect.cursor()
    cur.execute("SELECT EXISTS(SELECT 1 FROM jokes WHERE joke = ?)", (joke,))

    result = cur.fetchone()[0]
    connect.close()
    
    if result == 1:
        print("This exists!")
        return True
    else:
        return False
    
def delete(id, table):
    connect = sqlite3.connect('Client_data.db')
    cur = connect.cursor()
    cur.execute("""DELETE FROM table=:table WHERE id =:ID """, {'table':table, 'ID':id})
    connect.commit()
    connect.close()


def update_time_trigger():
    connect = sqlite3.connect('Client_data.db')
    cur = connect.cursor()
    cur.execute('''
        CREATE TRIGGER IF NOT EXISTS update_all_updated_at
        AFTER INSERT ON jokes 
        BEGIN 
            UPDATE jokes
            SET updated_at = CURRENT_TIMESTAMP;
            UPDATE quotes
            SET updated_at = CURRENT_TIMESTAMP;
        END;
    ''')
    connect.commit()
    connect.close()
        

def timePassed(table):
    connect = sqlite3.connect('Client_data.db')
    cur = connect.cursor()
    cur.execute("SELECT id, created_at, updated_at FROM table=:table;", {'table': table})
    table = cur.fetchall()
    connect.close()
    for times in table:
        created = datetime.strptime(times[1], "%Y-%m-%d %H:%M:%S")
        updated = datetime.strptime(times[2], "%Y-%m-%d %H:%M:%S")
        id = times[0]
        if ((updated - created).days > 5):
            delete(id, table)
        
    


if __name__  == "__main__":
    timePassed()
