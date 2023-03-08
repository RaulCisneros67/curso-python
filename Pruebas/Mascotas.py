class Mascota(object):
    
    def_init_(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        
    def darNombre(self):
        return self.nombre
    
    def darEspecie(self):
        return self.especie
    
    def_str_(self):
        return "%s es un %s" % (self.nombre, self.especie)