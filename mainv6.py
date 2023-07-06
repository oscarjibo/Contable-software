import libraries
from libraries import*
from modulos import  clases_agregar_COP
import mysql.connector
import ctypes
from datetime import datetime
import numpy_financial as npf
# empezamos con los 3 buffer 

from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidget,QPushButton,QWidget,QVBoxLayout

version=[1]

componente=[]

CRM=[]

cliente=[]
############
today = date.today()
qtCreatorFile = "archivos_interfaz/principal.ui" 
filesheet = "formatos.\ejercicio1.xlsx"
filesheet2 = "formatos.\ejercicio2.xlsx"
miarchivo ="formatos.\ejercicio.xlsx"
archivo_adicion="formatos.\\adicion.docx"
archivo_salarios="formatos.\\salarios.xlsx"
archivo_nuevo="formatos.\\nuevo.docx"
archivo_contactos="formatos.\\contactos.xlsx"
archivo_usuarios="formatos.\\usuarios.xlsx"
archivo_reportes="formatos.\\registros.xlsx"
archivo_comerciales="formatos.\Directorio.pdf"
mipdf="formatos.\oferta.pdf"

# lista para el combobox
registros=archivo_reportes
reg = pd.read_excel(registros)
reg1=reg.loc[:,'cliente']
reg1=list(reg1)

#datos nombres
preventa=[]
comercial=[]
cliente=[]
fecha=date.today()
total=[]
# DATOS
diaspago=[]
moneda=[]
cliente=[] 
tipoofer=[]
tasa_financiacion_general=[]
tasa_capex=[]
tasa_opex1t=[]
tasa_otroopex=[]
tasa_personal=[]
mesesfact=[]
TRM=[]
TRM_SERV=[]
TRM2=[]
riesgototal=[]
imprevistos_1=[]
ipc=[]

linea=["MDS"]
#empiezo a crear mi dataframe 
#TOTALEs
total_personal=[0]
total_otroopex=[0]
total_opex1t=[0]
total_capex=[0]

##### editables

total_personaled=[0]
total_otroopexed=[0]
total_opex1ted=[0]
total_capexed=[0]


# datos para mi datafrma
costo_producto=[]
articulos=[]
costos=[]
cantidades=[]
tipo=[]
seguro=[]
componente=[]
componente_status=[]
# meter el dataframe de los sueldos 
version="1"
nm=[]
filee=[]
m = archivo_salarios
df = pd.read_excel(m)
Analista1=df.iloc [0, 7]
Analista2=df.iloc [1, 7]
Analista3=df.iloc [2, 7]
Profesional1=df.iloc [3, 7]
Profesional2=df.iloc [4, 7]
Profesional3=df.iloc [5, 7]
Profesional4=df.iloc [6, 7]
Profesional5=df.iloc [7, 7]
Profesional6=df.iloc [8, 7]
Profesional7=df.iloc [9, 7]
Profesional8=df.iloc [10, 7]
Experto=df.iloc [11, 7]
En1=651900  
En2=296150
En3=647500
En4=291750
En5=225800
En6=581550
En7=392630
En8=196315
En9=130877
En10=80550
DATA=pd.DataFrame()

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

from PyQt5.QtWidgets import *
#VARIABLE MAS IMNPORTANTE EL CRM
CRMID=0
CLIENTE=str()
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Logo.png")
class Ventana(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.boton_iniciar.clicked.connect(self.Variables) # abro la ventana de variables
        self.boton_salir.clicked.connect(self.close)# boton salir 
        self.boton_iniciar_3.clicked.connect(self.admin2)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowIcon(QtGui.QIcon('Logo.png'))
    def Variables(self):
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        aa=0
        bb=0
        cursor1=conexion1.cursor()
        cursor1.execute("select Usuario, Contraseña from usuarios")
        user=self.textEdit.toPlainText()
        pasw=self.lineEdit.text()

        
        for i in cursor1:
            print(i[0])
            print(i[1])
            us=i[0]
            ps=i[1]
            if (us==user ):
                aa=1    
            if (ps==pasw):
                bb=1
            if (len(pasw)>0 ):
                aa=1
            if (len(user)>0 ):
                aa=1    
  
        
        if (aa==1 & bb==1):

             otraventana=Variables(self)
             otraventana.show()
             conexion1.close()
        else:
             QMessageBox.about(self, ' ', 'USUARIO O CONTRASEÑA INCORRECTO')
             conexion1.close()
        
            
   
    def admin2(self):
        otraventana=Crearuser(self)
        otraventana.show()
        
class Crearuser(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 
    def __init__(self,parent=None):
        super(Crearuser, self).__init__(parent)
        loadUi('archivos_interfaz/crearuser.ui', self)     
        self.pushButton_2.clicked.connect(self.Regresar)
        self.pushButton.clicked.connect(self.crear)
    def crear(self):
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        a=self.textEdit_6.toPlainText()#usuario
        b=self.textEdit_7.toPlainText()#contraseña
        c=self.textEdit_5.toPlainText()#telefono
        cursor1=conexion1.cursor()
        sql="insert into usuarios(Usuario, Contraseña, Telefono_Preventa ) values (%s,%s,%s)"
        datos=(a,b,c)
        cursor1.execute(sql, datos)
        conexion1.commit()
        d=self.textEdit_8.toPlainText() #nombre
        e=self.textEdit_2.toPlainText()#cargo
        f=self.textEdit_3.toPlainText()#vertical
        g=self.textEdit_4.toPlainText()#ciudad
        cursor1=conexion1.cursor()
        sql="insert into preventas(Nombre, Cargo, Vertical, Ciudad, Telefono_Preventa ) values (%s,%s,%s,%s,%s)"
        print(3)
        datos=(d,e,f,g,c)
        cursor1.execute(sql, datos)
        conexion1.commit()
        conexion1.close()
        QMessageBox.about(self, ' ', 'Su cuenta ha sido creada con éxito ')
    def Regresar(self):
         self.close()
class Variables(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de las variables 

    def __init__(self,parent=None):
        super(Variables,self).__init__(parent)
        loadUi('archivos_interfaz/Variables.ui', self)
        self.boton_infocliente.clicked.connect(self.infocliente)# boton abre info cliete
        self.boton_parametros.clicked.connect(self.Parametros)# boton abre info parametros
        
        self.boton_salir.clicked.connect(self.close)# boton salir
        self.boton_agregar.clicked.connect(self.agregar)# boton salir 
        self.boton.clicked.connect(self.generar)# GENERAR
        self.boton_2.clicked.connect(self.generarofer)# GENERAR
        self.boton_3.clicked.connect(self.modificar)# GENERAR  
        self.boton_infocliente_2.clicked.connect(self.crearopor)# crearoportunidad 
        self.boton_iniciar_2.clicked.connect(self.admin)


    def admin(self):
         self.hide()
         otraventana=Admin(self)
         otraventana.show()
        

    def crearopor(self):
         self.hide()
         otraventana=Crearopor(self)
         otraventana.show()
         
    def buscar(self):
        
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if filePath != "":
            filee.append(str(filePath))

            archi1=open("formatos/editable.txt","w") 
            archi1.write(filePath)  
            archi1.close() 
            
    def generarofer(self):
         self.hide()
         otraventana=Tipooferta(self)
         otraventana.show()
         
    def infocliente(self):
         print(CLIENTE)
         self.hide()
         otraventana=infocliente(self)
         otraventana.show()
         
    def Parametros(self):
         self.hide()
         otraventana=Parametros(self)
         otraventana.show()

    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show()
        
    def modificar(self):
        self.hide()
        otraventana=Modificar(self)
        otraventana.show()
        
    def generar(self):
       print("aca genero los numeros")
       ## lo mismo de cuando busco 
       #empecemos con capex
       conexion1=mysql.connector.connect(host="localhost", 
                                         user="root", 
                                         passwd="", 
                                         database="cotizador_servicios_gestionados")
       cursor2=conexion1.cursor()
       
       totales=0
       sumacostocapex=0
       sumacostoopex=0
       sumacostootroopex=0
       sumacostopersonal=0
       
       
       cursor2.execute("select * from cotizacion where CRM = " + CRM[-1])
       for a in cursor2:
           print(a)
           print("TRM :")
           print(a[16])
           tasa=a[16]
           print("MESES FACT ")
           mfact=a[14]

           riesgototal=a[17]
           tasa_capex=a[13]
           tasa_opex1t=a[11]
           tasa_otroopex=a[12]
           tasa_personal=a[10]
           imprevistos_1=a[18]
           ipc=a[19]
           tasa_financiacion_general=a[9]
          
       cursor1=conexion1.cursor()
       cursor1.execute("select * from capex where CRM = " + CRM[-1])
              
       for i in cursor1:

           mesesnofact=i[3]
           if i[11]=="USD":
               costo=i[7]*tasa
           
           elif i[11]=="COP":
               costo=i[7]
           nacionalizacion=i[4]
           
           iva=i[5]
           
           mesesfact=mfact
           unitario= ((1+nacionalizacion/100)*(1+iva/100))*((mesesfact+mesesnofact)/mesesfact)
           unit=unitario*costo
           
           

           
           tasa_financiacion=i[5]
           cantidad=i[6]

           #cuota = npf.pmt(tasa_financiacion, mesesfact, unit*-1*cantidad , 0,1)
           cuota = npf.pmt(tasa_financiacion/100, mesesfact, unit*-1*cantidad , 0,1)

           sumacostocapex+=cuota
       # aca traigo el dinero 

       a=sumacostocapex
       #b=sum(total_opex1t)
       #c=sum(total_otroopex)
       #d=sum(total_personal)
       
       
       
       ## TENEMOS CAPEX 
       
       a1=(a/(1-(riesgototal/100)-(tasa_capex/100)-(imprevistos_1/100)))*(1+(ipc/100))

       totales+=a1
       
       
       
       #b1=(b/(1-(riesgototal[0]/100)-(tasa_opex1t[0]/100)-  (imprevistos_1[0]/100)))*(1+(ipc[0]/100))
       #c1=(c/(1-(riesgototal[0]/100)-(tasa_otroopex[0]/100)-(imprevistos_1[0]/100)))*(1+(ipc[0]/100))
       #d1=(d/(1-(riesgototal[0]/100)-(tasa_personal[0]/100)-(imprevistos_1[0]/100)))*(1+(ipc[0]/100))
      # unitario=((1+nacionalizacion/100)*(1+iva/100))*((mesesfact[0]+mesesnofact)/mesesfact[0])
      # unit=unitario*costo
      # cuota = npf.pmt(tasa_financiacion/100, mesesfact[0], unit*-1*cantidad , 0,1)
      # cuota_mensual_capex=round(cuota,3)
           #unitario= ((1+nacionalizacion/100)*(1+iva/100))*((mesesfact[0]+mesesnofact)/mesesfact[0])
           #print(unitario)
           
       #ARRANCAMOS CON OPEX ONE TIME 
       
       cursor3=conexion1.cursor()
       cursor3.execute("select * from opex1t where CRM = " + CRM[-1])
       mesesfact=mfact
       for i in cursor3:

           
           
           veces_ejecutado=i[2]
           cantidad=i[3]
           nacio=i[4]
           costo=i[5]
           iva=i[6]
           unitario= costo*(1+nacio/100)*(1+iva/100)
           
           cuota_mensual_opex1t=npf.pmt(tasa_financiacion_general/100,mesesfact/veces_ejecutado,-1*unitario*cantidad,0,1)

           sumacostoopex+=cuota_mensual_opex1t
    
       b=sumacostoopex    
       b1=(b/(1-(riesgototal/100)-(tasa_opex1t/100)-  (imprevistos_1/100)))*(1+(ipc/100))
       totales+=b1
       ##########33
       
       
       ###ARRANCAMOS CON OTRO OPEX 
       
       cursor4=conexion1.cursor()
       cursor4.execute("select * from opex where CRM = " + CRM[-1])
              
       for i in cursor4:
           
           

           costo=i[4]
           iva=i[5]
           meses_ejecutado=i[2]
           cantidad=i[3]
           
           
           unit=costo*(1+iva/100)
           
           cuota_mensual_otropex=npf.pmt(tasa_financiacion_general/100,mesesfact/meses_ejecutado,-1*cantidad*unit,0,1)


           sumacostootroopex+=cuota_mensual_otropex
       c=sumacostootroopex
        
       c1=(c/(1-(riesgototal/100)-(tasa_otroopex/100)-(imprevistos_1/100)))*(1+(ipc/100))
       totales+=c1
       
       #############
       
       cursor5=conexion1.cursor()
       cursor5.execute("select * from personal where CRM = " + CRM[-1])
       print("#### VAMOS ACA #####")
       print(cursor5)
       
       conexion2=mysql.connector.connect(host="localhost", 
                                         user="root", 
                                         passwd="", 
                                         database="cotizador_servicios_gestionados")
       
       cursor6=conexion2.cursor()
       cursor6.execute("select * from perfiles")
       print(cursor6)

       for i in cursor5:
           print("N#### OK ####")
           
           


           perfil=i[2]
           meses_ejecutado=i[4]
           cantidad=i[5]
           ubicacion=i[6]
           mesesno=i[3]
           print(perfil)
           
           

           for g in cursor6:
               print(g)
               if perfil==g[1]:
                   costo=g[2]
           
           En1=651900
           En2=296150
           En3=647500
           En4=291750
           En5=225800
           En6=581550
           En7=392630
           En8=196315
           En9=130877
           En10=80550
           if ubicacion=="En Sonda Pc":
               ubi=En1
           elif ubicacion=="En Cliente Pc":
               ubi=En2
           elif ubicacion=="SONDA Portatil":
               ubi=En3
           elif ubicacion=="Cliente Portatil":
               ubi=En4
           elif ubicacion=="En cliente sin equipo ":
               ubi=En5
           elif ubicacion=="En Sonda sin equipo":
               ubi=En6
           elif ubicacion=="Zona Franca RU1":
               ubi=En7
           elif ubicacion=="Zona Franca RU2":
               ubi=En8
           elif ubicacion=="Zona Franca RU3":
               ubi=En9
           elif ubicacion=="Field Services EUS":
               ubi=En10
           P=(costo)+ubi
           
           cuota=P*cantidad*(meses_ejecutado+mesesno)/mesesfact
           cuota_total_personal_=npf.pmt(tasa_financiacion_general/100,mesesfact/(meses_ejecutado+mesesno),-1*P*cantidad,0,1)
           sumacostopersonal+=cuota_total_personal_

       d=sumacostopersonal
       d1=(d/(1-(riesgototal/100)-(tasa_personal/100)-(imprevistos_1/100)))*(1+(ipc/100)) 
       totales+=d1
       
       
       ## ARRANCAMOS PERSONAL 
       
       
       
       ###########
       TOTAL=totales
       print(" en costos Mensuales iria ", TOTAL)
       TOTALAÑO=TOTAL*mesesfact

       conexion1.close()
       conexion2.close()
       ### ACTUALIZO LOS DATOS 
       
       
       conexion1=mysql.connector.connect(host="localhost", 
                                         user="root", 
                                         passwd="", 
                                         database="cotizador_servicios_gestionados")
       
       #busco el nit del cliente
       cursor1=conexion1.cursor()
       sql="UPDATE cotizacion SET  Precio_Mensual=%s, Precio_Total=%s WHERE CRM = %s;"

       TOTAL=float(TOTAL)
       TOTALT=TOTAL*mesesfact
       datos=(TOTAL,TOTALT,CRM[-1])
       cursor1.execute(sql, datos)
       conexion1.commit()
       conexion1.close()
       ############
       
       
    
class Admin(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 
    def __init__(self,parent=None):
        super(Admin, self).__init__(parent)
        loadUi('archivos_interfaz/admin.ui', self)
        self.boton_4.clicked.connect(self.Variables1)
        self.boton_3.clicked.connect(self.usuarios)
        self.boton_5.clicked.connect(self.contactos)
        self.boton_6.clicked.connect(self.comerciales)
        self.boton.clicked.connect(self.reportes)
        self.boton_7.clicked.connect(self.salarios)
    def Variables1(self):
         

         self.hide()
         otraventana=Variables(self)
         otraventana.show()
        
    
    def Variables(self):
         self.hide()
         otraventana=Variables(self)
         otraventana.show()
    def usuarios(self):
        os.startfile(archivo_usuarios)
    def reportes(self):
        os.startfile(archivo_reportes)
    def contactos(self):
        os.startfile(archivo_contactos)
    def comerciales(self):
        os.startfile(archivo_comerciales)
    def salarios(self):
        os.startfile(archivo_salarios)         
class infocliente(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 
    def __init__(self,parent=None):
        super(infocliente, self).__init__(parent)
        loadUi('archivos_interfaz/infocliente.ui', self)
        self.boton_regresar.clicked.connect(self.Variables)#boton abre personal
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        cursor1=conexion1.cursor()
        cursor1.execute("select Nombre_Cliente from clientes")
        
        for i in cursor1:
            self.comboBox_2.addItem(i[0])
        cursor1.execute("select CRM from cotizacion")
        
        for a in cursor1:
            b=str(a[0])
            self.comboBox_3.addItem(b)

        
        
        conexion1.close()          
        
    def Variables(self):
         
         otraventana=Variables(self)
         CRMID=self.comboBox_3.currentText()
         CRM.append(CRMID)
         CLIENTE=self.comboBox_2.currentText()
         cliente.append(CLIENTE)
         versiont=version[-1]
         conexion1=mysql.connector.connect(host="localhost", 
                                           user="root", 
                                           passwd="", 
                                           database="cotizador_servicios_gestionados")
         df = pd.read_sql_query("SELECT * from cotizacion", conexion1)
         
         for i in range(len(df)):
             a=str(df.iloc[i]["CRM"])
             if (CRMID==a):
                 otraventana.label_11.setText(str(df.iloc[i]["Margen_Personal"]))
                 otraventana.label_12.setText(str(df.iloc[i]["Precio_Mensual"]))
                 otraventana.label_13.setText(str(df.iloc[i]["Precio_Total"]))
         
         self.hide()
        
         otraventana.label_5.setText(CLIENTE)
         otraventana.label_10.setText(CRMID)
         otraventana.label_15.setText(versiont) 
         ##http://pythonlcpa.blogspot.com/p/blog-page_1.html
         
         #voy a traer personal: 
         conexion1=mysql.connector.connect(host="localhost", 
                                           user="root", 
                                           passwd="", 
                                           database="cotizador_servicios_gestionados")
        
         cursor1=conexion1.cursor()
         sql=("SELECT rol FROM personal WHERE CRM= %s")
         CRM2=(int(CRM[-1]),)
         cursor1.execute(sql,(CRM2[0],))
         
         columnas=["QT","                                                                                                          item                                                                                                                  ","    %    ", "    Valor Mensual   ", "  Valor Total   ","  Componente "]
         
         otraventana.tableWidget.setRowCount(55)
         otraventana.tableWidget.setColumnCount(6)
         otraventana.tableWidget.setHorizontalHeaderLabels(columnas)
         otraventana.tableWidget.setSortingEnabled(True) 
         count=0
         dates=[]
         # PERSONAL

         for i in cursor1:

             count +=1
             dates.append(i[0])
             for g in range(len(dates)):
                 otraventana.tableWidget.setItem(g,1, QTableWidgetItem(dates[g]))
                 otraventana.tableWidget.setItem(g,5, QTableWidgetItem("Personal"))
         
          # traigo el capex  
         cursor2=conexion1.cursor()
         sql=("SELECT Id_Producto FROM capex WHERE CRM= %s")
         CRM2=(int(CRM[-1]),)
         cursor2.execute(sql,(CRM2[0],))
         capex=[]
         count2=count-1
         for u in cursor2:
             count2+=1
             capex.append(str(u[0]))
             for g in range(len(capex)):
                 otraventana.tableWidget.setItem(count2,1, QTableWidgetItem(capex[g]))
                 otraventana.tableWidget.setItem(count2,5, QTableWidgetItem("CAPEX"))
             
        # traigo el one time
         cursor3=conexion1.cursor()
         sql=("SELECT Id_Producto FROM opex1t WHERE CRM= %s")
         CRM2=(int(CRM[-1]),)
         cursor3.execute(sql,(CRM2[0],))
         one=[]
         count3=count2-1
         for u in cursor3:

             count3+=1
             one.append(str(u[0]))
             for g in range(len(one)):
                 otraventana.tableWidget.setItem(count3,1, QTableWidgetItem(one[g]))
                 otraventana.tableWidget.setItem(count3,5, QTableWidgetItem("OPEX 1T"))
        
        
        ### ME TRAIGO EL OPEX
        
         cursor4=conexion1.cursor()
         sql=("SELECT Id_Producto FROM opex WHERE CRM= %s")
         CRM2=(int(CRM[-1]),)
         cursor4.execute(sql,(CRM2[0],))
         opex=[]
         count4=count3-1
         for u in cursor4:
             count4+=1
             opex.append(str(u[0]))
             for g in range(len(opex)):
                 otraventana.tableWidget.setItem(count4,1, QTableWidgetItem(opex[g]))
                 otraventana.tableWidget.setItem(count4,5, QTableWidgetItem("OPEX"))
        
            
        
        
        
        
        
         #Layout
         otraventana.tableWidget.resizeRowsToContents()
         otraventana.tableWidget.resizeColumnsToContents()
         otraventana.show()
         
         
         
         
         conexion1.close()


class Parametros(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 


 
    def __init__(self,parent=None):
        super(Parametros, self).__init__(parent)
        loadUi('archivos_interfaz/Parametros.ui', self)
        self.boton_regresar.clicked.connect(self.Variables)#boton abre la pagina de atras variables
        self.boton.clicked.connect(self.anadir)#s
    
    def Variables(self):
         

         self.hide()

         otraventana=Variables(self)

         f=str(CRM[-1])
         otraventana.label_5.setText(cliente[-1])
         print(type(f))
         otraventana.label_10.setText(f)
         otraventana.label_15.setText(version[-1])
         otraventana.show()
         otraventana.show()
    

    def anadir(self):
        riesgo=self.p20.value()
        margencapex=self.p14.value()
        margen1t=self.p13.value()
        trm=self.p19.value()
        ipc=self.p15.value()
        meses=self.p21.value()
        margenotro=self.p12.value()
        margenp=self.p10.value()
        tasa_gnral=self.gg.value()
        trm_serv=self.p24.value()
        impuestos=self.p15_2.value()
        dias_pago=self.p11.value()
        diaspago.append(dias_pago)
        imprevistos=impuestos+((tasa_gnral + (dias_pago - 30))/30)
        # vamos actualizar los datos 
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        
        #busco el nit del cliente
        cursor1=conexion1.cursor()
        sql="UPDATE cotizacion SET Dias_Pago = %s, Tasa_Financiacion_General=%s, Margen_Personal=%s, Margen_Opex1t=%s, Margen_Opex=%s,Margen_Capex=%s, Meses_Facturables=%s,TRM=%s, TRM_Servicios=%s,  Riesgo_Proyecto=%s, Imprevistos=%s, IPC=%s WHERE CRM = %s;"
        datos=(dias_pago,tasa_gnral,margenp,margen1t,margenotro,margencapex,meses,trm,trm_serv,riesgo,imprevistos,ipc,CRM[-1])
        cursor1.execute(sql, datos)
        conexion1.commit()
        conexion1.close()
        QMessageBox.about(self, ' ', 'Parametros han sido actualizados con éxito ')

      
class agregar(QtWidgets.QMainWindow, Ui_MainWindow): # aca entran los 4 elementos 

    def __init__(self,parent=None):
        super(agregar, self).__init__(parent)
        loadUi('archivos_interfaz/agregar.ui', self)
        self.boton_regresar.clicked.connect(self.Variables)#boton abre personal
        self.boton_otroopex.clicked.connect(self.Otroopex)#boton abre personal
        self.boton_opex1t.clicked.connect(self.opex1t)#boton abre personal
        self.boton_capex.clicked.connect(self.Capex)#boton abre personal
        self.boton_personal.clicked.connect(self.Personal)#boton abre personal
        self.boton_regresar_2.clicked.connect(self.crearpro)
        self.boton_regresar_3.clicked.connect(self.crearfabricante)
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        cursor1=conexion1.cursor()
        cursor1.execute("select Nombre_Producto from productos_y_servicios")
        
        for i in cursor1:
            self.comboBox_2.addItem(i[0])        
        conexion1.close()
        self.comboBox.setEditable(True)
    def eliminar(self):
        pass
         
    def Variables(self):

         self.hide()
         otraventana=Variables(self)
         f=str(CRM[-1])
         otraventana.label_5.setText(cliente[-1])
         print(type(f))
         otraventana.label_10.setText(f)
         otraventana.label_15.setText(version[-1])
         otraventana.show()
    def crearpro(self):

         self.hide()
         otraventana=Crearpro(self)
         otraventana.show()
    def crearfabricante(self):

         self.hide()
         otraventana=Crearfabricante(self)
         otraventana.show()
    def Personal(self):
         a=self.comboBox.currentText()
         componente.append(a)
         self.hide()
         status=self.comboBox.currentText()
         componente_status.append(status)
         otraventana=Personal(self)
         otraventana.show()
         
    def Otroopex(self):
         a=self.comboBox.currentText()
         componente.append(a)
         self.hide()
         status=self.comboBox.currentText()
         otraventana=Otroopex(self)
         otraventana.show()
    def opex1t(self):
         a=self.comboBox.currentText()
         componente.append(a)
         self.hide()
         otraventana=opex1t(self)
         otraventana.show()
    def Capex(self):
         a=self.comboBox.currentText()
         componente.append(a)
         self.hide()
         status=self.comboBox.currentText()
         otraventana=Capex(self)
         otraventana.show()
    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show()


        
class Tipooferta(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 
    def __init__(self,parent=None):
        super(Tipooferta, self).__init__(parent)
        loadUi('archivos_interfaz/tipooferta.ui', self)
        self.boton_regresar.clicked.connect(self.Variables)#boton regresa
        self.boton_regresar_2.clicked.connect(self.abrir_adicion)#boton regresa
        self.boton_regresar_3.clicked.connect(self.abrir_nuevo)#boton regresa
        
    
    def Variables(self):
         self.hide()
         otraventana=Variables(self)
         otraventana.show()
    def abrir_adicion(self):
        os.startfile(archivo_adicion)
    def abrir_nuevo(self):
        os.startfile(archivo_nuevo)
class Modificar(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 



 
    def __init__(self,parent=None):
        super(Modificar, self).__init__(parent)
        loadUi('archivos_interfaz/modificar.ui', self)
        self.pushButton.clicked.connect(self.Variables)
        self.comboBox.addItems(list(reg1))
        self.pushButton_2.clicked.connect(self.abrir)
        
        
    def Variables(self):
         

         self.hide()
         otraventana=Variables(self)
         otraventana.show()
         
         
    def abrir(self):
        
        self.demo = DFEditor()
        self.demo.show()
        self.close()



        otraventana.show() 
        
        
class Crearopor(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(Crearopor, self).__init__(parent)
        loadUi('archivos_interfaz/crearopor.ui', self)
        self.pushButton_2.clicked.connect(self.Variables)
        self.pushButton_3.clicked.connect(self.Cliente)
        self.pushButton_4.clicked.connect(self.Preventa)
        self.pushButton.clicked.connect(self.crear)#creacion
        
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        cursor1=conexion1.cursor()
        cursor1.execute("select Nombre_Cliente from clientes")
        
        for i in cursor1:
            print(i)
            self.comboBox.addItem(i[0])
            
        cursor1.execute("select Nombre from preventas")
        
        for i in cursor1:
            self.comboBox_5.addItem(i[0])
        
        conexion1.close()
    
    def crear(self):
        # sacar los datos 
        a=self.comboBox.currentText()
        cliente.append(str(a))
        b=self.comboBox_3.currentText()
        c=self.comboBox_5.currentText()
        d=self.comboBox_2.currentText()
        e=self.textEdit_5.toPlainText()
        f=self.comboBox_4.currentText()
        g=int(e)
        CRM.append(g)
        #a la bd
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        
        #busco el nit del cliente
        cursor1=conexion1.cursor()
        cursor1.execute("select NIT_Cliente, Nombre_Cliente from clientes")
        
        for i in cursor1:
            print(i)
            if (i[1]==a):
                nit=i[0]
        print(nit)
        fecha=datetime.now()
        print(fecha)
        print(g)
        cursor1=conexion1.cursor()
        sql="insert into cotizacion(CRM, Version, NIT_Cliente,Tipo_Cotizacion,Tipo_Vertical,fecha) values (%s,%s,%s,%s,%s,%s)"
        datos=(g,1,nit,d,f,fecha)
        cursor1.execute(sql, datos)
        conexion1.commit()
        conexion1.close()
       
        ###
        
        QMessageBox.about(self, ' ', 'Su Oportunidad ha sido creada con éxito ')
    def Variables(self):

         self.hide()
         otraventana=Variables(self)

         f=str(CRM[-1])
         otraventana.label_5.setText(cliente[-1])
         print(type(f))
         otraventana.label_10.setText(f)
         otraventana.label_15.setText(version[-1])
         otraventana.show()
    def Cliente(self):

         self.hide()
         otraventana=Crearcliente(self)
         otraventana.show()
    def Preventa(self):

         self.hide()
         otraventana=Crearpreventa(self)
         otraventana.show()
    def Crear(self):

         self.hide()
         otraventana=Variables(self)
         otraventana.show()
    
class Crearcliente(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(Crearcliente, self).__init__(parent)
        loadUi('archivos_interfaz/crearcliente.ui', self)
        self.pushButton_3.clicked.connect(self.Cliente)
        self.pushButton_4.clicked.connect(self.Variables)
    def Cliente(self):
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        a=self.textEdit_5.toPlainText()# nombre
        b=self.textEdit_6.toPlainText()# nit
        c=self.textEdit_7.toPlainText()# ciudad
        e=self.textEdit_8.toPlainText()#telefono
        cursor1=conexion1.cursor()
        sql="insert into clientes(NIT_Cliente, Nombre_Cliente, Ciudad, Telefono ) values (%s,%s,%s,%s)"
        datos=(b,a,c,e)
        cursor1.execute(sql, datos)
        conexion1.commit()
        conexion1.close()
        QMessageBox.about(self, ' ', 'Cliente creado con éxito ')

        self.hide()
        otraventana=Variables(self)
        otraventana.show()
    def Variables(self):

         self.hide()
         otraventana=Crearopor(self)
         otraventana.show()
    
class Crearpreventa(QtWidgets.QMainWindow, Ui_MainWindow):
    

    def __init__(self,parent=None):
        super(Crearpreventa, self).__init__(parent)
        loadUi('archivos_interfaz/crearpreventa.ui', self)
        self.pushButton_3.clicked.connect(self.Preventa)
        self.pushButton_4.clicked.connect(self.Variables)
    def Preventa(self):
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        a=self.textEdit_5.toPlainText()# nombre
        b=self.textEdit_6.toPlainText()# nit
        c=self.textEdit_7.toPlainText()# ciudad
        d=self.textEdit_8.toPlainText()# ciudad
        e=self.textEdit_9.toPlainText()#telefono
        cursor1=conexion1.cursor()
        sql="insert into preventas(Nombre, Cargo, Vertical, Ciudad, Telefono_Preventa ) values (%s,%s,%s,%s,%s)"
        datos=(a,b,c,d,e)
        cursor1.execute(sql, datos)
        conexion1.commit()
        conexion1.close()
        QMessageBox.about(self, ' ', 'Preventa creado con éxito ')
    def Variables(self):

         self.hide()
         otraventana=Crearopor(self)
         otraventana.show()
class Crearpro(QtWidgets.QMainWindow, Ui_MainWindow):
    

    def __init__(self,parent=None):
        super(Crearpro, self).__init__(parent)
        loadUi('archivos_interfaz/crearproducto.ui', self)
        self.boton_anadir.clicked.connect(self.Crear)
        self.boton_regresar.clicked.connect(self.agregar)
    def Crear(self):
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        a=self.c1_4.toPlainText()# nombre
        b=self.c1.toPlainText()# nit
        c=self.comboBox.currentText()# ciudad
        d=self.c1_2.toPlainText()# ciudad
        e=self.c1_3.toPlainText()# ciudad
        cursor1=conexion1.cursor()
        sql="insert into productos_y_servicios(Id_Producto, Nombre_Producto, Tipo, Numero_de_Parte, Id_Fabricante ) values (%s,%s,%s,%s,%s)"
        datos=(a,b,c,d,e)
        cursor1.execute(sql, datos)
        conexion1.commit()
        conexion1.close()
        QMessageBox.about(self, ' ', 'Producto creado con éxito ')
    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show() 
        
class Crearfabricante(QtWidgets.QMainWindow, Ui_MainWindow):
    

    def __init__(self,parent=None):
        super(Crearfabricante, self).__init__(parent)
        loadUi('archivos_interfaz/crearfabricante.ui', self)
        self.pushButton.clicked.connect(self.Crear)
        self.pushButton_2.clicked.connect(self.agregar)
    def Crear(self):
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        a=self.textEdit_8.toPlainText()# nombre
        b=self.textEdit_2.toPlainText()# nit
        c=self.textEdit_3.toPlainText()# ciudad
        d=self.textEdit_4.toPlainText()# ciudad
        e=self.textEdit_5.toPlainText()
        cursor1=conexion1.cursor()
        sql="insert into fabricantes(id_Fabricante, Nombre, Persona_Contacto, Correo, Telefono ) values (%s,%s,%s,%s,%s)"
        datos=(a,b,c,d,e)
        cursor1.execute(sql, datos)
        conexion1.commit()
        conexion1.close()
        QMessageBox.about(self, ' ', 'Fabricante creado con éxito ')
    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show() 
class Personal(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase del personal
 
    def __init__(self,parent=None):
        super(Personal, self).__init__(parent)
        loadUi('archivos_interfaz/Personal.ui', self)
        self.boton_regresar.clicked.connect(self.agregar)#boton abre agregar
        self.boton_regresar1.clicked.connect(self.anadir)#boton abre agregar
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        cursor1=conexion1.cursor()
        cursor1.execute("select Tipo_Empleado from perfiles")
        
        for i in cursor1:
            self.c3.addItem(i[0])        
        conexion1.close()
    
    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show() 
    def anadir(self):
        rol=self.c1.toPlainText()
        perfil=self.c3.currentText()
        meses_ejecutados=self.c2.value()
        cantidad=self.c4.value()
        recargos=self.c5.value()
        ubicacion=self.c6.currentText()
        mesesno=self.c22.value()
        ver=version[-1]
        CRMw=CRM[-1]
        comp=componente[-1]
        costo=1000
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        
        
        cursor1=conexion1.cursor()
        sql="insert into personal(CRM, Rol,Id_Perfil, Meses_no_Facturables, Meses_Requeridos, Cantidad, ubicacion_recurso, Costo,Id_Componente,Version) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        datos=(CRMw,rol,perfil,mesesno,meses_ejecutados,cantidad,ubicacion,costo,comp,ver)
        cursor1.execute(sql, datos)
        conexion1.commit()
        
        
        conexion1.close()
        QMessageBox.about(self, ' ', 'Producto creado con éxito ')
class opex1t(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de Opex 1t 
 
    def __init__(self,parent=None):
        super(opex1t, self).__init__(parent)
        loadUi('archivos_interfaz/opex1t.ui', self)
        self.boton_regresar.clicked.connect(self.agregar)#boton abre personal
        self.anadi.clicked.connect(self.anadir)
        self.boton_regresar_2.clicked.connect(self.crearpro)
        self.c3.setEditable(True)
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        cursor1=conexion1.cursor()
        cursor2=conexion1.cursor()
        cursor1.execute("select Nombre_Producto from productos_y_servicios")
        
        for i in cursor1:
            self.c3.addItem(i[0])        
        cursor2.execute("select Nombre from fabricantes")
        
        for i in cursor2:
            self.comboBox_3.addItem(i[0]) 
        
        conexion1.close()
    def crearpro(self):

         self.hide()
         otraventana=Crearpro(self)
         otraventana.show()
         
    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show()
    def anadir(self):
    
        item=self.c3.currentText()
        item=str(item)
        fabricante=self.comboBox_3.currentText()
        veces_ejecutado=self.v.value()
        cantidad=self.c.value()
        nacio=self.n.value()
        costo=self.c1.value()
        iva=self.i.value()
        seguro=self.comboBox_2.currentText()
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        
        
        cursor1=conexion1.cursor()
        sql="insert into opex1t(CRM,Id_Producto,Veces_Requerido,Cantidad,Nacionalizacion,Costo_Unitario,IVA,Id_Componente,Version) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)  "
        datos=(CRM[-1],item,veces_ejecutado,cantidad,nacio,costo,iva,componente[-1],version[-1])
        cursor1.execute(sql, datos)
        conexion1.commit()
        
        
        conexion1.close()
        QMessageBox.about(self, ' ', 'Producto creado con éxito ')
class Otroopex(QtWidgets.QMainWindow, Ui_MainWindow): # esta es la clase de otro opex
 
    def __init__(self,parent=None):
        super(Otroopex, self).__init__(parent)
        loadUi('archivos_interfaz/Otroopex.ui', self)
        self.boton_regresar.clicked.connect(self.agregar)#boton abre personal
        self.boton_anadir.clicked.connect(self.anadir)
        self.boton_regresar_2.clicked.connect(self.crearpro)
        self.comboBox.setEditable(True)
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        cursor1=conexion1.cursor()
        cursor2=conexion1.cursor()
        cursor1.execute("select Nombre_Producto from productos_y_servicios")
        
        for i in cursor1:
            self.comboBox.addItem(i[0])
        
        cursor2.execute("select Nombre from fabricantes")
        
        for i in cursor2:
            self.comboBox_3.addItem(i[0]) 
            
        conexion1.close()
    
    def crearpro(self):

         self.hide()
         otraventana=Crearpro(self)
         otraventana.show()
    
    
    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show()
    def anadir(self):
    
        item=self.comboBox.currentText()
        item=str(item)
        meses_ejecutado=self.spinBox.value()
        cantidad=self.c.value()
        costo=self.c1.value()
        iva=self.i.value()
        
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        
        
        cursor1=conexion1.cursor()
        sql="insert into opex(CRM,Id_Producto,Meses_Requeridos,Cantidad,Costo_Unitario,IVA,Id_Componente,Version) values (%s,%s,%s,%s,%s,%s,%s,%s)  "
        datos=(CRM[-1],item,meses_ejecutado,cantidad,costo,iva,componente[-1],version[-1])
        cursor1.execute(sql, datos)
        conexion1.commit()
        
        
        conexion1.close()
        QMessageBox.about(self, ' ', 'Producto creado con éxito ')
        

class Capex(QtWidgets.QMainWindow, Ui_MainWindow):# esta es la clase de Opex 1t 
         
    def __init__(self,parent=None):
        super(Capex, self).__init__(parent)
        loadUi('archivos_interfaz/Capex.ui', self)
        self.boton_regresar.clicked.connect(self.agregar)#boton abre personal
        self.boton_anadir.clicked.connect(self.anadir)#boton añade
        self.boton_regresar_2.clicked.connect(self.crearpro)
        self.comboBox.setEditable(True)
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        cursor1=conexion1.cursor()
        cursor2=conexion1.cursor()
        cursor1.execute("select Nombre_Producto from productos_y_servicios")
        
        for i in cursor1:
            self.comboBox.addItem(i[0])  
        cursor2=conexion1.cursor()
        cursor2.execute("select Nombre from fabricantes")
        
        for i in cursor2:
            self.comboBox_3.addItem(i[0]) 
        conexion1.close()
        
    def crearpro(self):

         self.hide()
         otraventana=Crearpro(self)
         otraventana.show()
         
         
    def agregar(self):
        self.hide()
        otraventana=agregar(self)
        otraventana.show()
    def anadir(self):
        

        # aca empiezo a darle con los precios 
        item=self.comboBox.currentText()
        item=str(item)
        mesesnofact=self.c2.value()
        nacionalizacion=self.c3.value()
        plataforma=self.c4.value()
        iva=self.c5.value()
        tasa_financiacion=self.c6.value()
        cantidad=self.c7.value()
        costo=self.c8.value()
        seguro1=self.c10.isChecked()
        dolar=self.comboBox_2.currentText()        
        conexion1=mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="", 
                                          database="cotizador_servicios_gestionados")
        
        
        cursor1=conexion1.cursor()
        sql="insert into capex(CRM,Id_Producto,Meses_no_Facturables,Nacionalizacion,IVA,Tasa_Mensual_Financiacion,Cantidad,Costo,Id_Componente,Version,seguro,Moneda) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)  "
        datos=(CRM[-1],item,mesesnofact,nacionalizacion,iva,tasa_financiacion,cantidad,costo,componente[-1],version[-1],seguro1,dolar)
        cursor1.execute(sql, datos)
        conexion1.commit()
        
        
        conexion1.close()
        QMessageBox.about(self, ' ', 'Producto agregado con éxito ')
        
    def Variables(self):

         self.hide()
         otraventana=Crearopor(self)
         otraventana.show()
if __name__ == "__main__": # abre la pantalla principal

        app =  QtWidgets.QApplication(sys.argv)
        window = Ventana()
        window.show()
        sys.exit(app.exec_())



    
