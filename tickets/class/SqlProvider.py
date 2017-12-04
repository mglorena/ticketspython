# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import psycopg2
import psycopg2.extras
        
class SqlProvider:
    hostname = 'localhost'
    username = 'tdd'
    password = 'tdd'
    database = 'tdd'   
    
    def Execute(self,query):       
        conn = psycopg2.connect( host=self.hostname, user=self.username, password=self.password, dbname=self.database )
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query)
        conn.commit()
        rows = cur.fetchall()
        conn.close()
        return rows

        
if __name__ == "__main__":
    print "Hello World"
