# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from SqlProvider import SqlProvider

class Departamentos:
    nombre =''
    nombreresponsable = ''
    depid =''
    ispublico =''
    created = ''
    updated = ''
    firma = ''
    autorespemail = ''
    
    def __init__(self):
         pass        
     
    def Copy(self,row):
        for (key, value) in row.items():
            setattr(self, key, value)
        
    def SaveNewDepto(self):
        isp = 'false'
        if(str(self.ispublico)=='1'): isp = 'true'
        query = "Select * from dptos_insert('"+str(self.nombre)+"','"+str(self.nombreresponsable)+"',"+isp+",'"+str(self.created)+"','"+str(self.updated)+"','"+str(self.autorespemail)+"','"+str(self.firma)+"');" 
        sql = SqlProvider()
        rows = sql.Execute(query)
        return rows[0]
#    
    def GetById(self,depid):
        query = "select * from dptos_getbyid() where DepId =" + str(depid) +";" 
        sql = SqlProvider()
        row = sql.Execute(query)
        self.Copy(row[0])   
        return self
    def Update(self):
        ip = 'false'
        if(str(self.ispublico)=='1'): isp = 'true'
        query = "select * from dptos_update('" + self.nombre + "','" + self.nombreresponsable + "'," + ip + ",'"+ self.autorespemail + "','" + self.firma + "'," + str(self.depid) + ");";
        sql = SqlProvider()
        row = sql.Execute(query)
        self.Copy(row[0])   
        return self