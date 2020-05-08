#ESTE PASARLO A JUPITER
import modulo2 #importamos un modulo
import paquete.modulo1 # un modulo incluido dentro de un paquete
import paquete.subpaquete.modulo1  # un modulo en un subpaquete

##### namespaces
'''
Para acceder a elementos del modulo importado se usa el namespace del modulo
'''
print modulo2.CONST
print paquete.CONST
print paquete.subpaquete.CONST

#### alias
'''
se puede abreviar el namespace con un alias para acceder mas facilmente a el
'''

import modulo2 as m_2
import paquete.modulo1 as pm_1
import paquete.subpaquete.modulo1 as psm_1

print m_2.CONST
print pm_1.CONST
print psm_1.CONST

#### importacion sin namespace
from paquete.modulo1 import CONST
print CONST

from paquete.modulo1 import CONST,VAR_2
print CONST + VAR_2

#evitar declaraciones duplicadas
from modulo2 import CONST
from paquete.modulo1 import CONST

print CONST

#usando alias 
from modulo2 import CONST as C1
from paquete.modulo1 import CONST as C2
print C2








