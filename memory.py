import sqlite3, time

class Memory:
    
    def storeData(quote, joke):
        connect = sqlite3.connect('Client_data.db')
        cur = connect.cursor()
        cur.execute("INSERT INTO jokes (joke) VALUES (?)", (joke,))
        cur.execute("INSERT INTO quotes (quote) VALUES (?)", (quote,))
        connect.commit()
        connect.close()

    def hasQuote(quote):
        connect = sqlite3.connect('Client_data.db')
        cur = connect.cursor()
        cur.execute("SELECT EXISTS(SELECT 1 FROM quotes WHERE quote = ?)", (quote,))
    
        # Fetch the result (it will return a tuple, (1,) if exists, or (0,) if not)
        result = cur.fetchone()[0]
        
        connect.close()
        
        # Return True if the result is 1 (exists), otherwise False
        if result == 1:
            print("This exists!")
            return True
        else:
            return False
        
    def hasJoke(joke):
        connect = sqlite3.connect('Client_data.db')
        cur = connect.cursor()
        try:
            cur.execute("SELECT * FROM UsedDb WHERE JOKE =:JOKE", {'QUOTE':joke})
            return True
        except:
            return False
        
    def delete(id):
        connect = sqlite3.connect('Client_data.db')
        cur = connect.cursor()
        cur.execute("""DELETE FROM UsedDb WHERE ID =ID """, {'ID':id})
        connect.commit()
        connect.close()
    
    def updateTime(id):
        connect = sqlite3.connect('Client_data.db')
        cur = connect.cursor()
        cur.execute("UPDATE UsedDb SET UPDATED_AT=:UPDATED_AT WHERE ID =:ID", {'UPDATED_AT':get_time(), 'ID':id})
        connect.commit()
        connect.close()

        
def get_time():
    return time.time()

def timePassed(time1, time2):
    if (time2 - time1 > 1000):
        return True
    else:
        return False
    
if __name__  == "__main__":
    Memory.storeData("quote here", "joke here")