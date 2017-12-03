# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
from Departamentos import Departamentos
from datetime import date

class  TestDepartamentosTestCase(unittest.TestCase):
   
    def test_FillDepartamentos(self):
         dep = Departamentos()
         self.assertTrue(hasattr(dep, 'nombre'))
         self.assertTrue(hasattr(dep, 'nombreresponsable'))
         self.assertTrue(hasattr(dep, 'depid'))
         self.assertTrue(hasattr(dep, 'ispublico'))
         self.assertTrue(hasattr(dep, 'created'))
         self.assertTrue(hasattr(dep, 'updated'))
         self.assertTrue(hasattr(dep, 'firma'))
         dep.nombre = "Taller de Electricidad"
         dep.nombreresponsable = "Quinteros"
         dep.depid = 1
         self.assertEqual(dep.nombre, "Taller de Electricidad")
         self.assertEqual(dep.nombreresponsable, "Quinteros")
         self.assertEqual(dep.depid, 1)
         
    def test_InsertNewDepartamentos(self):
         dep = Departamentos()
         dep.nombre = "Estudios y Proyectos"
         dep.nombreresponsable = "Quinteros"
         dep.firma = 'DGOyS'
         dep.ispublico = 1
         dep.created = date.today()
         dep.updated = date.today()
         depId = dep.SaveNewDepto()
         did = depId['dptos_insert']
         self.assertIsNotNone(did)
         if did:  
             d = dep.GetById(3)
             self.assertIsNotNone(d.depid)
             
    def test_GetById(self):
         depId = 3
         dep = Departamentos()
         d = dep.GetById(depId)
         self.assertIsNotNone(d.depid)
         self.assertEqual(dep.nombre, "Taller de Red")
         self.assertEqual(dep.nombreresponsable, "Daniel Acevedo")
         
    def test_UpdateDepartamento(self):
        depId = 10
        dep = Departamentos()
        d = dep.GetById(depId)
        d.nombreresponsable = 'Lorena Garcia'
        d.Update()
        self.assertEqual(d.nombre, 'Taller de Informatica')
        self.assertEqual(d.autorespemail,'sarapuraa@unsa.edu.ar')
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()


