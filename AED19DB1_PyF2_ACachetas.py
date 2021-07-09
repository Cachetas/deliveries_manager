# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 13:24:11 2019

@author: António Cachetas - nº 30002421
Professor: Laércio Curnivel Júnior
Universidade Autonoma de Lisboa

Last update on Mon May 27 04:53:45 2019

"""

import os
import pickle

#-----------------FUNÇÃO PARA MANTER OS MENUS NA MESMA POSIÇÃO-----------------

class clear:
 def __call__(self):
     
     if os.name==('ce','nt','dos'): os.system('cls')
     elif os.name=='posix': os.system('clear')
     else: print('\n'*100)
 def __neg__(self): self()
 def __repr__(self):
     self();return ''

clear=clear() #Clear() é chamado após cada escolha de opção nos menus

#----------------------Criação da classe Viatura-------------------------------
class Viatura: 
    def __init__(self, matricula, capacidade): #Atributos defenidos na Classe Viatura
        self.matricula=matricula #Atributo
        self.capacidade=capacidade #Atributo
  

#----------------------Criação da Subclasse Camiao-----------------------------
class Camiao (Viatura): #Criação da Classe Camião (tem atributos da Classe Viatura)
    def __init__(self, matricula, capacidade): #Atributos defenidos na Classe Camiao
        super().__init__(matricula, capacidade) #Atributos Herdados da Classe Viatura
        
#-----MÉTODO __STR__ PARA QUE SEJA POSSÍVEL CONSULTAR DADOS EM TIPO STRING-----         
    def __str__(self):  
        info_camiao = '_ _ _ _ _ _ _ _ _ _ _ _ _\n'\
                      ' -----------------------'\
            +         '\n  Informação do Camião:        \n' \
            +         '  Matrícula: ' + self.matricula + '; \n' \
            +         '  Capacidade: ' + str(self.capacidade) + 'cm3;'
        return info_camiao
    
    
    
#--------------------FUNÇÃO PARA INSERIR DADOS EM CAMIAO----------------------- 
def inserirCamiao():
        cicloCamiao = True
        while cicloCamiao:
            try:
                capacidade = int(input("Insira a capacidade (cm3): "))
            
                if capacidade < 1200000:
                    print("\nCapacidade introduzida fora dos limites esperados para o camião" \
                              "\nA capacidade do camião deve ser superior a 1200000cm3." \
                              "\nDeverá adicionar esta viatura noutro tipo.")
                    cicloCamiao = False
                    return
                else:
                    matricula = str(input("Insira a matrícula: "))
                    camiao = Camiao(matricula, capacidade)
                    FCamiao.enqueue(camiao)
                    cicloCamiao = False
                    
                return camiao
                listaCamiao.append(camiao)
            except ValueError:
                print ("\nIntroduza números apenas, por favor!")
            
#-------------------FUNÇÃO PARA MODIFICAR DADOS EM CAMIAO----------------------             
def modificarCamiao():
    opcaoModificarCamiao = input("Introduza a matrícula do camião para modificar-> ")
    verificarModificarCamiao = False
    for camiao in listaCamiao:
        if camiao.matricula == opcaoModificarCamiao:
            verificarModificarCamiao = True
            
            erro = True
            while erro:
                try:
                    novaCapacidade = int(input("Introduza a capacidade para atualizar na viatura (cm3): "))
                    if novaCapacidade > 1200000:
                        camiao.matricula = opcaoModificarCamiao
                        camiao.capacidade = novaCapacidade
                        erro = False
                    else:
                        print("Capacidade introduzida fora dos limites esperados para o camião" \
                        "\nA capacidade do camião deve ser superior a 1200000cm3.")
                        
                except ValueError:
                    print("\nIntroduza números apenas, por favor.")
                    
    if verificarModificarCamiao == False:
        print("A matrícula ", opcaoModificarCamiao, " não está na lista dos camiões.")

    return camiao

def consultaCamiao():
    for camiao in listaCamiao:
        if camiao is not None:
            print(camiao)
                                    

#------------------FUNÇÃO PARA CONSULTAR QUEUE CAMIÃO--------------------------

def verQueueCamiao ():
  for i in range (FCamiao.size()):
    verQueue = FCamiao.dequeue()
    if verQueue is not None:
      print(verQueue)
      FCamiao.enqueue(verQueue)

#----------------------Criação da Subclasse Automovel-------------------------------
      
class Automovel (Viatura): #Criação da Classe Automovel (tem atributos da Classe Viatura)
    def __init__(self, matricula, capacidade): #Atributos defenidos na Classe Automóvel
        super().__init__(matricula, capacidade) #Atributos Herdados da Classe Viatura
        
        
#-----MÉTODO __STR__ PARA QUE SEJA POSSÍVEL CONSULTAR DADOS EM TIPO STRING----- 
    def __str__(self): 
        info_automovel = '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n'\
                         ' ---------------------------'\
            +            '\n  Informação do Automóvel: \n' \
            +            '  Matrícula: ' + self.matricula + '; \n' \
            +            '  Capacidade: ' + str(self.capacidade) + 'cm3;'
        return info_automovel

    
#-------------------FUNÇÃO PARA INSERIR DADOS EM AUTOMOVEL---------------------     
def inserirAutomovel():
    
    cicloAutomovel = True
    while cicloAutomovel:
        try:
            capacidade = int(input("Insira a capacidade (cm3): "))
            
            if capacidade < 80000 or capacidade > 1200000:
                print("\nCapacidade introduzida está fora dos limites esperados para o automóvel." \
                      "\nA capacidade do automóvel deve ser entre 80000cm3 e 1200000cm3." \
                      "\nDeverá adicionar esta viatura noutro tipo.")
                cicloAutomovel = False
                return
            else:
                matricula = str(input("Insira a matrícula: "))
                automovel = Automovel(matricula, capacidade)
                FAutomovel.enqueue(automovel)
                cicloAutomovel = False
                
                return automovel
            
        except ValueError:
            
            print ("\nIntroduza números apenas, por favor!")
            
            

#------------------FUNÇÃO PARA MODIFICAR DADOS EM AUTOMOVEL-------------------- 
def modificarAutomovel():
    opcaoModificarAutomovel = input("Introduza a matrícula do automóvel para modificar-> ")
    verificarModificarAutomovel = False
    for automovel in listaAutomovel:
        if automovel.matricula == opcaoModificarAutomovel:
            verificarModificarAutomovel = True
            
            erro = True
            while erro:
                try:
                    novaCapacidade = int(input("Introduza a capacidade para atualizar na viatura (cm3): "))
                    if novaCapacidade > 80000 and novaCapacidade < 1200000:
                        automovel.matricula = opcaoModificarAutomovel
                        automovel.capacidade = novaCapacidade
                        erro = False
                    else:
                        print("Capacidade introduzida fora dos limites esperados para o automóvel" \
                        "\nA capacidade do automóvel deve estar entre 80000cm3 e 1200000cm3.")
                        
                except ValueError:
                    print("\nIntroduza números apenas, por favor.")
                    
    if verificarModificarAutomovel == False:
        print("A matrícula ", opcaoModificarAutomovel, " não está na lista dos automóveis.")

    return automovel

def consultaAutomovel():
    for automovel in listaAutomovel:
        if automovel is not None:
            print(automovel)


#------------------FUNÇÃO PARA CONSULTAR QUEUE AUTOMÓVEL-----------------------

def verQueueAutomovel ():
  for automovel in range (FAutomovel.size()):
    verQueue = FAutomovel.dequeue()
    if verQueue is not None:
      print(verQueue)
      FAutomovel.enqueue(verQueue)


#----------------------Criação da Subclasse Mota-------------------------------
class Mota (Viatura): #Criação da Classe Mota (tem atributos da Classe Viatura)
    def __init__(self, matricula, capacidade): #Atributos defenidos na Classe Mota
        super().__init__(matricula, capacidade) #Atributos Herdados da Classe Viatura

#-----MÉTODO __STR__ PARA QUE SEJA POSSÍVEL CONSULTAR DADOS EM TIPO STRING-----
    def __str__(self):
        info_mota = '_ _ _ _ _ _ _ _ _ _ _ _ _\n'\
                    ' -----------------------'\
            +       '\n  Informação da Mota: \n' \
            +       '  Matrícula: ' + self.matricula + '; \n' \
            +       '  Capacidade: ' + str(self.capacidade) + 'cm3;'
        return info_mota

    
#---------------------FUNÇÃO PARA INSERIR DADOS EM MOTA------------------------ 
def inserirMota():
    cicloMota = True
    while cicloMota:
        
        try:
            
            capacidade = int(input("Insira a capacidade (cm3): "))
            
            if capacidade >= 80000:
                print("\nCapacidade introduzida fora dos limites esperados para a mota" \
                      "\nA capacidade da mota deve ser inferior a 80000cm3." \
                      "\nDeverá adicionar esta viatura noutro tipo.")
                cicloMota = False
                return
            else:
                matricula = str(input("Insira a matrícula: "))
                mota = Mota(matricula, capacidade)
                FMota.enqueue(mota)
                cicloMota = False
                
                return mota
        except ValueError: 
            print ("\nIntroduza números apenas, por favor!")


#--------------------FUNÇÃO PARA MODIFICAR DADOS EM MOTA----------------------- 
def modificarMota():
    opcaoModificarMota = input("Introduza a matrícula da mota para modificar-> ")
    verificarModificarMota = False
    for mota in listaMota:
        if mota.matricula == opcaoModificarMota:
            verificarModificarMota = True
            
            erro = True
            while erro:
                try:
                    novaCapacidade = int(input("Introduza a capacidade para atualizar na viatura (cm3): "))
                    if novaCapacidade < 80000:
                        mota.matricula = opcaoModificarMota
                        mota.capacidade = novaCapacidade
                        erro = False
                    else:
                        print("Capacidade introduzida está fora dos limites esperados para a mota." \
                        "\nA capacidade da mota deve ser inferior a 80000cm3.")
                        
                except ValueError:
                    print("\nIntroduza números apenas, por favor.")
                    
    if verificarModificarMota == False:
        print("A matrícula ", opcaoModificarMota, " não está na lista das Motas.")

    return mota


def consultaMota():
    for mota in listaMota:
        if mota is not None:
            print(mota)


#--------------------FUNÇÃO PARA CONSULTAR QUEUE MOTA--------------------------

def verQueueMota ():
  for mota in range (FMota.size()):
    verQueue = FMota.dequeue()
    if verQueue is not None:
      print(verQueue)
      FMota.enqueue(verQueue)
      

#----------------------Criação da Classe Condutor------------------------------
class Condutor: #Criação da Classe Condutor
    def __init__(self, nome, email, numero, telefone, carta): #Atributos defenidos na Classe Condutor
        
        self.nome=nome #Atributo
        self.email=email #Atributo
        self.numero=numero #Atributo
        self.telefone=telefone #Atributo
        self.carta=carta #Atributo
        
#-----MÉTODO __STR__ PARA QUE SEJA POSSÍVEL CONSULTAR DADOS EM TIPO STRING----- 
    def __str__(self):
        info_condutor = '_ _ _ _ _ _ _ _ _ _ _ _ _ _\n'\
                        ' -------------------------'\
            +           '\n  Informação do Condutor: \n' \
            +           '  Nome: ' + self.nome + '; \n' \
            +           '  Número: ' + str(self.numero) + '; \n' \
            +           '  Telefone: ' + str(self.telefone) + '; \n'\
            +           '  E-mail: ' + self.email + '; \n'\
            +           '  Carta: Tipo ' + str(self.carta) + ';'
        return info_condutor

#-------------------FUNÇÃO PARA INSERIR DADOS EM CONDUTOR----------------------     
def inserirCondutor():
    nome = str(input("Insira a nome: "))
    email = str(input("Insira o e-mail: "))
    
    cicloInserirCondutor = True
    while cicloInserirCondutor:
        erro = True
        while erro:
            try:
                contador = 1
                for condutor in listaCondutor:
                    contador = contador + 1
                numero = contador
                erro = False
            except ValueError:
                print("\nIntroduza números apenas, por favor.")
                
        erro = True
        while erro:
            try:
                telefone = int(input("Insira o telefone-> "))
                erro = False
            except ValueError:
                print("\nIntroduza números apenas, por favor.")
        erro = True
        while erro:
            try:
                
                carta = int(input("Insira o número correspondente ao tipo de carta deste condutor: \n(1 Camião)\n" \
                          "(2 Automóvel) \n" \
                          "(3 Mota) \n-> "))
                
                if carta == 1 or carta == 2 or carta == 3:
                    erro = False
                   
                else:
                    print("Introduza o número 1, 2 ou 3 apenas, por favor.")
                    erro = True
                
                                                        
            except ValueError:
                print("\nIntroduza números apenas, por favor.")
                
        condutor = Condutor(nome, email, numero, telefone, carta)


#-CONDIÇÕES IF PARA DISTRIBUIÇÃO DE CONDUTORES PELAS QUEUES PELO TIPO DE CARTA

        if condutor.carta == 1:
          FCondCamiao.enqueue(condutor)
        if condutor.carta == 2:
          FCondAutomovel.enqueue(condutor)
        if condutor.carta == 3:
          FCondMota.enqueue(condutor)
        
        return condutor
                 

#------------------FUNÇÃO PARA MODIFICAR DADOS EM CONDUTOR--------------------- 
def modificarCondutor():
    erro = True
    cicloModificarCondutor = True
    while cicloModificarCondutor:
        try:
            opcaoModificarCondutor = int(input("Insira o número do condutor para modificar os dados-> "))
            erro = False
        
            
            verificarModificarCondutor = False
            for condutor in listaCondutor:
                if condutor.numero == opcaoModificarCondutor:
                    verificarModificarCondutor = True
                    
#-----------APÓS "PESQUISA" DO NÚMERO DO CONDUTOR IRÁ AFIXAR NO ECRÃ-----------
#--------A INFORMAÇÃO ATUAL DO CONDUTOR PARA FACILITAR A SUA ALTERAÇÃO---------
                    nome = condutor.nome
                    print("Nome do condutor->", nome, ";")
                    numero = condutor.numero
                    print("Número do condutor->", numero, ";")
                    telefone = condutor.telefone
                    print("Número de telefone atual->", telefone, ";")
                    email = condutor.email
                    print("E-mail atual-> ", email, ";")
                    carta = condutor.carta
                    ncarta = carta
                    
                    print("Tipo de carta atual-> Tipo", carta)
                    
                    
                    
                    cicloModificarCondutor = True
                    while cicloModificarCondutor:
                        erro = True
                        while erro:
                            try:
                                condutor.telefone = int(input("Insira o novo telefone-> "))
                                erro = False
                            except ValueError:
                                print("\nIntroduza números apenas, por favor.")
                                
                        condutor.email = str(input("Insira o novo email-> "))
                        erro = True
                        while erro:
                            try:
                                condutor.carta = int(input("Insira 1,2 ou 3 para o tipo de carta para atualizar-> "))
                                
                                carta = condutor.carta
                                
                
                                if carta == 1 or carta == 2 or carta == 3:
                                    erro = False
                                   
                                else:
                                    print("Introduza o número 1, 2 ou 3 apenas, por favor.")
                                    erro = True
                                
                                                                        
                            except ValueError:
                                print("\nIntroduza números apenas, por favor.")
                        condutor = Condutor(nome, email, numero, telefone, carta)               

#--------ALTERAR QUEUE DE CONDUTORES CASO SEJA MUDADO O TIPO DE CARTA----------
                        
                        #Condição para alteração de Camião para Automóvel
                        if carta != 1:
                            if carta == 2 and ncarta == 1:
                                for condutor in range (FCondCamiao.size()):
                                    alterarQueue = FCondCamiao.dequeue()
                                    if alterarQueue is not None and alterarQueue.carta == 2:
                                      FCondAutomovel.enqueue(alterarQueue)
                                    else:
                                        FCondCamiao.enqueue(alterarQueue)
                                        
                            #Condição para alteração de Camiao para Mota            
                            if carta == 3 and ncarta == 1:
                                for condutor in range (FCondCamiao.size()):
                                    alterarQueue = FCondCamiao.dequeue()
                                    if alterarQueue is not None and alterarQueue.carta == 3:
                                      FCondMota.enqueue(alterarQueue)
                                    else:
                                        FCondCamiao.enqueue(alterarQueue)
                                        
                                        
                                        
                        #Condição para alteração de Automóvel para Camiao                
                        if carta != 2:           
                            if carta == 1 and ncarta == 2:
                                for condutor in range (FCondAutomovel.size()):
                                    alterarQueue = FCondAutomovel.dequeue()
                                    if alterarQueue is not None and alterarQueue.carta == 1:
                                      FCondCamiao.enqueue(alterarQueue)
                                    else:
                                        FCondAutomovel.enqueue(alterarQueue)
                                        
                            #Condição para alteração de Automóvel para Mota           
                            if carta == 3 and ncarta == 2:
                                for condutor in range (FCondAutomovel.size()):
                                    alterarQueue = FCondAutomovel.dequeue()
                                    if alterarQueue is not None and alterarQueue.carta == 3:
                                      FCondMota.enqueue(alterarQueue)
                                    else:
                                        FCondAutomovel.enqueue(alterarQueue)
                                        
                                        
                        #Condição para alteração de Mota para Camião                
                        if carta != 3:
                            if carta == 1 and ncarta == 3:
                                for condutor in range (FCondMota.size()):
                                    alterarQueue = FCondMota.dequeue()
                                    if alterarQueue is not None and alterarQueue.carta == 1:
                                      FCondCamiao.enqueue(alterarQueue)
                                    else:
                                        FCondMota.enqueue(alterarQueue)
                                        
                                        
                            #Condição para alteração de Mota para Automóvel            
                            if carta == 2 and ncarta == 3:
                                for condutor in range (FCondMota.size()):
                                    alterarQueue = FCondMota.dequeue()
                                    if alterarQueue is not None and alterarQueue.carta == 2:
                                      FCondAutomovel.enqueue(alterarQueue)
                                    else:
                                        FCondMota.enqueue(alterarQueue)
                                
                            
                            
                        cicloModificarCondutor = False
                
            if verificarModificarCondutor == False:
                    print("O número ", opcaoModificarCondutor, " não está na lista dos condutores.")
            
                
            return condutor
                 
        except ValueError:
            print("Introduza números apenas, por favor.")
            
def consultaCondutor():
    for condutor in listaCondutor:
        if condutor is not None:
            print(condutor)

#------FUNÇÕES PARA VER QUEUES DE CONDUTORES (DE CAMIÃO, AUTOMÓVEL E MOTA)-----
            
def verQueueCondutorCamiao():
  for condutor in range (FCondCamiao.size()):
    verQueue = FCondCamiao.dequeue()
    if verQueue is not None:
      print(verQueue)
      FCondCamiao.enqueue(verQueue)

def verQueueCondutorAutomovel():
  for condutor in range (FCondAutomovel.size()):
    verQueue = FCondAutomovel.dequeue()
    if verQueue is not None:
      print(verQueue)
      FCondAutomovel.enqueue(verQueue)

def verQueueCondutorMota():
  for condutor in range (FCondMota.size()):
    verQueue = FCondMota.dequeue()
    if verQueue is not None:
      print(verQueue)
      FCondMota.enqueue(verQueue)
      
      
#-------------------------------Criação BST-----------------------------------

class CliTree:  
    def __init__(self, data):  
        self.data = data  
        self.left = None
        self.right = None

def pesquisarTree(root, key): 
    while root != None: 
        if key > root.data:  
            root = root.right 
        elif key < root.data: 
            root = root.left  
        else: 
            return True  
    return False

def inserirTree(Node, data): 
      
    if Node == None: 
        return CliTree(data)  
  
    if data < Node.data:  
        Node.left = inserirTree(Node.left, data)  
    elif data > Node.data:  
        Node.right = inserirTree(Node.right, data) 
    return Node 
  
  
def ordenarTree(root): 
    if root: 
        ordenarTree(root.left) 
        print(root.data)
        ordenarTree(root.right)


#----------------------Criação da Classe Cliente-------------------------------
class Cliente: #Criação da Classe Cliente
    def __init__(self, nome, email, morada, numero, telefone): #Atributos defenidos na Classe Cliente
        
        self.nome=nome #Atributo
        self.email=email #Atributo
        self.morada=morada #Atributo
        self.numero=numero #Atributo
        self.telefone=telefone #Atributo
        
    
#-----MÉTODO __STR__ PARA QUE SEJA POSSÍVEL CONSULTAR DADOS EM TIPO STRING-----
    def __str__(self):
        info_cliente = '_ _ _ _ _ _ _ _ _ _ _ _ _ _\n'\
                       ' -------------------------'\
            +          '\n  Informação do Cliente: \n' \
            +          '  Nome: ' + str(self.nome) + '; \n' \
            +          '  Número: ' + str(self.numero) + '; \n' \
            +          '  Morada: ' + self.morada + '; \n' \
            +          '  Telefone: ' + str(self.telefone) + '; \n' \
            +          '  E-mail: ' + self.email + '; \n'
        return info_cliente        

#--------------------FUNÇÃO PARA INSERIR DADOS EM CLIENTE---------------------- 
def inserirCliente():
    
    nome = str(input("Insira a nome: "))
    email = str(input("Insira o e-mail: "))
    morada = str(input("Insira a morada: "))
    cicloInserirCliente = True
    while cicloInserirCliente:
        erro = True
        while erro:
            try:
                contador = 1
                for cliente in listaCliente:
                    contador = contador + 1
                numero = contador
                erro = False
            except ValueError:
                print("\nIntroduza números apenas, por favor.")
                
        erro = True
        while erro:
            try:
                telefone = int(input("Insira o telefone: "))
                erro = False
            except ValueError:
                print("\nIntroduza números apenas, por favor.")
                
        cliente = Cliente(nome, email, morada, numero, telefone)
        return cliente

#-------------------FUNÇÃO PARA MODIFICAR DADOS EM CLIENTE--------------------- 
def modificarCliente():
    erro = True
    while cicloModificar:
        try:
            opcaoModificarCliente = int(input("Insira o número de cliente para modificar os dados-> "))
            erro = False
        
            
            verificarModificarCliente = False
            for cliente in listaCliente:
                if cliente.numero == opcaoModificarCliente:
                    verificarModificarCliente = True
                    
                    nome = cliente.nome
                    print("Nome do cliente->", nome, ";")
                    numero = cliente.numero
                    print("Número do cliente->", numero, ";")
                    morada = cliente.morada
                    print("Morada atual->", morada, ";")
                    telefone = cliente.telefone
                    print("Número de telefone atual->", telefone, ";")
                    email = cliente.email
                    print("E-mail atual->", email, ";")
                    
                    
                    cicloModificarCliente = True
                    while cicloModificarCliente:
                        erro = True
                        while erro:
                            try:
                                cliente.telefone = int(input("Insira o novo telefone-> "))
                                erro = False
                            except ValueError:
                                print("\nIntroduza números apenas, por favor.")
                        
                        cliente.morada = str(input("Insira a nova morada-> "))                                
                        cliente.email = str(input("Insira o novo email-> "))
                        cliente = Cliente(nome, email, morada, numero, telefone)
                        cicloModificarCliente = False
                
            if verificarModificarCliente == False:
                    print("O número ", opcaoModificarCliente, " não está na lista dos clientes.")
                
                
            return cliente
                 
        except ValueError:
            print("Introduza números apenas, por favor.")

            
#------------------------Função para consultar lista de clientes-----------------           
def consultaCliente():
    for cliente in listaCliente:
        if cliente is not None:
            print(cliente)


#----------------------Criação da Classe Entrega-------------------------------
class Entrega: #Criação da Classe Entrega
    def __init__(self, identificador, ponto_recolha, ponto_entrega, mercadoria_descricao, mercadoria_volume): #Atributos defenidos na Classe Entrega
        self.identificador=identificador #Atributo
        self.ponto_recolha=ponto_recolha #Atributo
        self.ponto_entrega=ponto_entrega #Atributo
        self.mercadoria_descricao=mercadoria_descricao #Atributo
        self.mercadoria_volume=mercadoria_volume #Atributo
    

#-----MÉTODO __STR__ PARA QUE SEJA POSSÍVEL CONSULTAR DADOS EM TIPO STRING-----
    def __str__(self):
        info_entrega = '_ _ _ _ _ _ _ _ _ _ _ _ _ _\n'\
                       ' -------------------------'\
            +          '\n  Informação da Entrega: \n' \
            +          '  Identificador: ' + str(self.identificador) + '; \n' \
            +          '  Ponto de recolha: ' + self.ponto_recolha + '; \n' \
            +          '  Ponto de entrega: ' + self.ponto_entrega + '; \n' \
            +          '  Descriçao da Mercadoria: ' + self.mercadoria_descricao + '; \n' \
            +          '  Volume da mercadoria: ' + str(self.mercadoria_volume) + 'cm3; \n'
        return info_entrega
    

#--------------------FUNÇÃO PARA INSERIR DADOS EM ENTREGA----------------------      
def inserirEntrega():
    
    erro = True
    while erro:
        try:
            contador = 1
            for entrega in listaEntrega:
                contador = contador + 1
            identificador = contador
            erro = False
        except ValueError:
            print("\nIntroduza números apenas, por favor.")
            
    ponto_recolha = str(input("Insira o ponto de recolha: "))
    ponto_entrega = str(input("Insira o ponto de entrega: "))
    mercadoria_descricao = str(input("Insira a descrição da mercadoria: "))
    
    erro = True
    while erro:
        try:
            mercadoria_volume = int(input("Insira o volume da mercadoria: "))
            erro = False
        except ValueError:
            print("\nIntroduza números apenas, por favor.")
            
    entrega = Entrega(identificador, ponto_recolha, ponto_entrega, mercadoria_descricao, mercadoria_volume)


#CONDIÇÕES PARA ATRIBUIÇÃO DAS ENTREGAS NAS QUEUES BASEADO NO VOLUME DA MERCADORIA    
    if mercadoria_volume <= 80000:
        FEntregaMota.enqueue(entrega)
        
    if mercadoria_volume > 80000 and mercadoria_volume <= 1200000:
        FEntregaAutomovel.enqueue(entrega)
    
    if mercadoria_volume > 1200000:
        FEntregaCamiao.enqueue(entrega)
    
    return entrega


#-------------------FUNÇÃO PARA MODIFICAR DADOS EM ENTREGA---------------------
def modificarEntrega():
    while cicloModificar:
        try:
            opcaoModificarEntrega = int(input("Insira o número identificador da  entrega para modificar-> "))
            verificarModificarEntrega = False
            for entrega in listaEntrega:
                if entrega.identificador == opcaoModificarEntrega:
                    verificarModificarEntrega = True
                    
                    identificador = entrega.identificador
                    print("Identificador da entrega-> {};".format(identificador))
                    ponto_recolha = entrega.ponto_recolha
                    print("Ponto de recolha da mercadoria-> {};" .format(ponto_recolha))
                    ponto_entrega = entrega.ponto_entrega
                    print("Ponto de entrega da mercadoria->{};" .format(ponto_entrega))
                    mercadoria_descricao = entrega.mercadoria_descricao
                    print("Descrição da mercadoria-> {};".format(mercadoria_descricao))
                    mercadoria_volume = entrega.mercadoria_volume
                    print("Volume da Mercadoria-> {}cm3;" .format(mercadoria_volume))
                    
                    
                    cicloModificarEntrega = True
                    while cicloModificarEntrega:
                        entrega.ponto_recolha = str(input("Insira o novo ponto de recolha-> "))                                
                        entrega.ponto_entrega = str(input("Insira o novo ponto de entrega-> "))
                        entrega.mercadoria_descricao = str(input("Insira a nova descrição da mercadoria-> "))
                        try:
                            erro = True
                            while erro:
                                entrega.mercadoria_volume = int(input("Insira o novo volume da mercadoria-> "))
                                volume = entrega.mercadoria_volume
                                erro = False
                        except ValueError:
                            print("Insira apenas números, por favor.")
                        entrega = Entrega(identificador, ponto_recolha, ponto_entrega, mercadoria_descricao, mercadoria_volume)
                        cicloModificarEntrega = False
                        
 
#-----ALTERAR QUEUE DE ENTREGAS CASO SEJA ALTERADO O VOLUME DA MERCADORIA------ 
                        
                        #Condição para alterar Entrega de Camião para Automóvel
                        if volume <= 1200000 and volume > 80000:
                            for entrega in range (FEntregaCamiao.size()):
                                alterarQueue = FEntregaCamiao.dequeue()
                                if alterarQueue is not None and alterarQueue.mercadoria_volume <= 1200000 and alterarQueue.mercadoria_volume >80000:
                                  FEntregaAutomovel.enqueue(alterarQueue)
                                else:
                                    FEntregaCamiao.enqueue(alterarQueue)
                                        
                        #Condição para alterar Entrega de Camião para Mota                
                        if volume <= 80000:
                            
                            for entrega in range (FEntregaCamiao.size()):
                                
                                alterarQueue = FEntregaCamiao.dequeue()
                                if alterarQueue is not None and alterarQueue.mercadoria_volume <= 80000:
                                    FEntregaMota.enqueue(alterarQueue)
                                else:
                                    FEntregaCamiao.enqueue(alterarQueue)
                       
                        
                        #Condição para alterar Entrega de Automóvel para Camião
                        if volume > 1200000:
                            for entrega in range (FEntregaAutomovel.size()):
                                alterarQueue = FEntregaAutomovel.dequeue()
                                if alterarQueue is not None and alterarQueue.mercadoria_volume > 1200000:
                                  FEntregaCamiao.enqueue(alterarQueue)
                                else:
                                    FEntregaAutomovel.enqueue(alterarQueue)
                                        
                        #Condição para alterar Entrega de Automóvel para Mota                
                        if volume <= 80000:
                            
                            for entrega in range (FEntregaAutomovel.size()):
                                
                                alterarQueue = FEntregaAutomovel.dequeue()
                                if alterarQueue is not None and alterarQueue.mercadoria_volume <= 80000:
                                    FEntregaMota.enqueue(alterarQueue)
                                else:
                                    FEntregaAutomovel.enqueue(alterarQueue)
                                    
                        #Condição para alterar Entrega de Mota para Automóvel            
                        if volume > 80000 and volume <= 1200000:
                            for entrega in range (FEntregaMota.size()):
                                alterarQueue = FEntregaMota.dequeue()
                                if alterarQueue is not None and alterarQueue.mercadoria_volume > 80000 and alterarQueue.mercadoria_volume <= 1200000:
                                  FEntregaAutomovel.enqueue(alterarQueue)
                                else:
                                    FEntregaMota.enqueue(alterarQueue)
                                        
                        #Condição para alterar Entrega de Mota para Camião                
                        if volume > 1200000:
                            
                            for entrega in range (FEntregaMota.size()):
                                
                                alterarQueue = FEntregaMota.dequeue()
                                if alterarQueue is not None and alterarQueue.mercadoria_volume > 1200000:
                                    FEntregaCamiao.enqueue(alterarQueue)
                                else:
                                    FEntregaMota.enqueue(alterarQueue)
                                        
                        
                
            if verificarModificarEntrega == False:
                    print("O número identificador", opcaoModificarEntrega, " não está na lista de entregas.")
                
                
            return entrega
        except ValueError:
            print("Introduza números apenas, por favor.")    


#---------------Função de consulta de dados da lista de entregas----------------            
def consultaEntrega():
    for entrega in listaEntrega:
        if entrega is not None:
            print(entrega)



#FUNÇÃO PARA CONSULTAR QUEUES DE ENTREGAS PENDENTES (DE CAMIÃO, AUTOMÓVEL e MOTA)

def verQueueEntregaCamiao ():
  for entrega in range (FEntregaCamiao.size()):
    verQueue = FEntregaCamiao.dequeue()
    if verQueue is not None:
      print(verQueue)
      FEntregaCamiao.enqueue(verQueue)
      
def verQueueEntregaAutomovel ():
  for entrega in range (FEntregaAutomovel.size()):
    verQueue = FEntregaAutomovel.dequeue()
    if verQueue is not None:
      print(verQueue)
      FEntregaAutomovel.enqueue(verQueue)
      
      
def verQueueEntregaMota ():
  for entrega in range (FEntregaMota.size()):
    verQueue = FEntregaMota.dequeue()
    if verQueue is not None:
      print(verQueue)
      FEntregaMota.enqueue(verQueue)


def exportarFicheiroTexto():
    
#---------------------Listar Conteudo do diretorio atual-----------------------                    
    ficheirosExistentes = os.listdir('./')
    print('Ficheiros do diretório atual:\n')
    contador = 0
    for file in ficheirosExistentes:
        print(file)
        contador = contador + 1
    if contador == 0:
        print('Diretório vazio.')
        print('Não existem ficheiros neste diretório.')
#---------------------Escolher nome do Ficheiro Binário------------------------                      
    nomeFicheiro = str(input('Introduza o nome do ficheiro para gravar: '))
    extensaoFicheiro = (".txt")
    ficheiroTexto = str(nomeFicheiro) + str(extensaoFicheiro)
    
#---------------------Verificar se Ficheiro Binário existe---------------------  
    contadorFicheiros = 0
    for file in ficheirosExistentes:
        if ficheiroTexto == file:
            
            print("O ficheiro ({}) já existe." .format(ficheiroTexto))
            contadorFicheiros = contadorFicheiros + 1
    
    
            if contadorFicheiros != 0:
                print("\nPretende substutuir o ficheiro?" .format(ficheiroTexto))
                print("ATENÇÃO! O conteúdo do ficheiro ({}) não poderá ser recuperado." .format(ficheiroTexto))
                opcao = str(input("\nIntroduza sim ou não? [s/n] -> "))
            
            
    if contadorFicheiros == 0 or opcao == ('s') or opcao == ('S') or opcao == ('sim') or opcao == ('Sim') or opcao == ('SIm') or opcao == ('SIM') or opcao == ('sIM') or opcao == ('siM') or opcao == ('si') or opcao == ('Si') or opcao == ('SI') or opcao == ('y') or opcao == ('Y') or opcao == ('yes') or opcao == ('YES'):


        file = open(ficheiroTexto,'w')
        file.write('\n\n* * * * * * * * * * * *\n')
        file.write('* Entregas de Camião  *\n')    
        file.write('* * * * * * * * * * * *\n')
        contadorEntregas = 0
        for entrega in range (FEntregaCamiao.size()):
            verQueue = FEntregaCamiao.dequeue()
            
            if verQueue is not None:
                file.write('\n  Informação da Entrega\n')
                file.write(str(verQueue))
                file.write('\n')
                contadorEntregas = contadorEntregas + 1
            FEntregaCamiao.enqueue(verQueue)
            
                    
        file.write('\n\n* * * * * * * * * * * * *\n')
        file.write('* Entregas de Automovel *\n')    
        file.write('* * * * * * * * * * * * *\n')
        for entrega in range (FEntregaAutomovel.size()):
            verQueue = FEntregaAutomovel.dequeue()
            
            if verQueue is not None:
                file.write('\n  Informação da Entrega\n')
                file.write(str(verQueue))
                file.write('\n')
                contadorEntregas = contadorEntregas + 1
            FEntregaAutomovel.enqueue(verQueue)
                
            
        file.write('\n\n* * * * * * * * * * *\n')
        file.write('* Entregas de Mota  *\n')    
        file.write('* * * * * * * * * * *\n')        
        for entrega in range (FEntregaMota.size()):
            verQueue = FEntregaMota.dequeue()
            file.write('\n  Informação da Entrega\n')
            if verQueue is not None:
                file.write(str(verQueue))
                file.write('\n')
                contadorEntregas = contadorEntregas + 1
            FEntregaMota.enqueue(verQueue)
        print("Ficheiro ({}) criado com sucesso." .format(ficheiroTexto))
        print("Tem {} entregas pendentes" .format(contadorEntregas))
        file.close()
    else:
        print('\nOperação cancelada, os dados não foram exportados.')

def verFicheiroTexto():
    
    ficheirosExistentes = os.listdir('./')
    print('Ficheiros do diretório atual:\n')
    contador = 0
    for file in ficheirosExistentes:
        print(file)
        contador = contador + 1
    if contador == 0:
        print('Diretório vazio.')
        print('Não existem ficheiros neste diretório.')
    
    nome = str(input("Introduza o nome do ficheiro para abrir: "))
    extensao = (".txt")
    nomeFicheiro = (str(nome)) + (str(extensao))
   
    #for file in ficheirosExistentes:
    try:
        ficheiro = open(nomeFicheiro, "r")
        print(ficheiro.read()) 
        print('Ficheiro ({}) aberto com sucesso.' .format(str(nomeFicheiro)))
        
                    
    except FileNotFoundError:
        print('\nO ficheiro ({}) não existe.' .format(str(nomeFicheiro)))
        print('Utilize a opção (Exportar ficheiro de texto), por favor.')

#-----------------------------CRIAÇÃO DA QUEUE---------------------------------    
class Queue():
        
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def enqueue(self, item):
        self.items.insert(0,item)
            
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return  len(self.items)


def criarFicheiro():
    ficheiro = ("EstafetaListas")
    file = open(ficheiro, "w+")
    file.close()

#--------------------------------MÉTODO MAIN-----------------------------------

if __name__=="__main__":

#-------------DECLARAÇÃO DAS LISTAS VAZIAS PARA RECEBER DADOS------------------      
    listaCamiao = []
    listaAutomovel = []
    listaMota = []
    listaCondutor = []
    listaCliente = []
    listaEntrega = []
    
#-------------------DECLARAÇÃO DAS QUEUES DE VIATURAS--------------------------
    FCamiao = Queue()
    FAutomovel = Queue()
    FMota = Queue()
    
#------------------DECLARAÇÃO DAS QUEUES DE CONDUTORES-------------------------
    FCondCamiao = Queue()
    FCondAutomovel = Queue()
    FCondMota = Queue()
    
    
#------------------DECLARAÇÃO DAS QUEUES DE ENTREAGAs--------------------------
    FEntregaCamiao = Queue()
    FEntregaAutomovel = Queue()
    FEntregaMota = Queue()
    
#----------------------------MENU INCIAL---------------------------------------

    clear()
    
    cicloMenu = True
    while cicloMenu:
        print ("\n\nGESTÃO DE FROTA - ESTAFETA")
        print("   _ _ _ _ _ _ _ _ _ _ _ _ _ ")
        print("  |                         |")
        print("  |       MENU              |")
        print("  |                         |") 
        print("  |  1 -> Ficheiros         |")
        print("  |  2 -> Inserir dados     |")
        print("  |  3 -> Modificar dados   |")
        print("  |  4 -> Consultar dados   |")
        print("  |  5 -> Gestão            |")
        print("  |  0 -> Sair do Programa  |")
        print("  |_ _ _ _ _ _ _ _ _ _ _ _ _|")
        
        opcaoMenu = int(input("\nIntroduza um número -> "))
        clear()
        
        if opcaoMenu == 1:
            cicloAbrirGravar = True
            while cicloAbrirGravar:
                print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
                print("  |                                     |")
                print("  |       FICHEIROS                     |")
                print("  |                                     |")
                print("  |  1 -> Novo ficheiro                 |")
                print("  |  2 -> Abrir ficheiro                |")
                print("  |  3 -> Gravar ficheiro               |")
                print("  |  0 -> Voltar ao menu anterior       |")
                print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                
                opcaoAbrirGravar = int(input("\nIntroduza um número -> "))
                clear()
        
        
#---------------------------Novo Ficheiro Binário------------------------------
                if opcaoAbrirGravar == 1:

#---------------------Listar Conteudo do diretorio atual----------------------- 
                    
                    ficheirosExistentes = os.listdir('./')
                    print('Ficheiros do diretório atual:\n')
                    contador = 0
                    for file in ficheirosExistentes:
                        print(file)
                        contador = contador + 1
                    if contador == 0:
                        print('Diretório vazio.')
                        print('Não existem ficheiros neste diretório.')
                        

                    nomeFicheiro = str(input('Introduza o nome do novo ficheiro: '))
                    extensaoFicheiro = ".bin"
                    ficheiro = str(nomeFicheiro) + str(extensaoFicheiro)
                    
                    contadorFicheiros = 0
                    for file in ficheirosExistentes:
                        
                        if ficheiro == file:
                            
                            print("O nome ({}) já existe, escolha outro nome ou utilize a opção (Gravar ficheiro) por favor." .format(ficheiro))
                            contadorFicheiros = contadorFicheiros + 1
                    
                        
                    if contadorFicheiros == 0:
                        
                        extensaoFicheiro = ".bin"
                        ficheiro = str(nomeFicheiro) + str(extensaoFicheiro)
                        
                        file = open(ficheiro, "w+")
                        print("O novo ficheiro foi criado com sucesso como nome ({}) " .format(ficheiro))
                        file.close()
                    
                
#---------------------------Abrir Ficheiro Binário------------------------------
#----------Criação das mesmas listas para carregar o ficheiro binário-----------
                if opcaoAbrirGravar == 2:
                    
                    listaCamiao = []
                    listaAutomovel = []
                    listaMota = []
                    listaCondutor = []
                    listaCliente = []
                    listaEntrega = []
                   
                    
                    
#---------------------Listar Conteudo do diretorio atual----------------------- 
                    ficheirosExistentes = os.listdir('./')
                    print('Ficheiros do diretório atual:\n')
                    contador = 0
                    for file in ficheirosExistentes:
                        print(file)
                        contador = contador + 1
                    if contador == 0:
                        print('Diretório vazio.')
                        print('Não existem ficheiros neste diretório.')

#---------------------Escolher nome do Ficheiro Binário------------------------                    
                    nomeFicheiro = str(input('Introduza o nome do ficheiro para abrir: '))
                    extensaoFicheiro = ".bin"
                    ficheiro = str(nomeFicheiro) + str(extensaoFicheiro)
                    
                    
                    try:
                        with open(ficheiro, "rb") as f:
                            
#-------------Leitura dos primeiros registos/objetos no ficheiro---------------
#------------Estes registos são apenas variáveis com um número-----------------
#------------este número corresponde a quantos objetos das litas foram 
#------------guardados quando se grava o ficheiro, desta forma é possível fazer 
#------------um ciclo for com o Range do seu valor para cada lista guardada----
                            contadorCamiao = (pickle.load(f))
                            contadorAutomovel = (pickle.load(f))
                            contadorMota = (pickle.load(f))
                            contadorCondutor = (pickle.load(f))
                            contadorCliente = (pickle.load(f))
                            contadorEntrega = (pickle.load(f))

#------------Um ciclo For com o Range do contador de cada lista, neste ciclo---
#------------para cada registo obtido, é feito o .append à lista a que pertence
#------------é também colocado na sua queue em seguida, para que a estrutura---
#------------se mantenha. Está presente também um contador de objtos para------
#------------informação do utilizador do total do numero de registos no ficheiro
                            contadorRegistos = 0
                            for camiao in range(contadorCamiao):
                                lista = (pickle.load(f))
                                listaCamiao.append(lista)
                                FCamiao.enqueue(lista)
                                contadorRegistos = contadorRegistos + 1 
                                
                            for automovel in range(contadorAutomovel):
                                lista = (pickle.load(f))
                                listaAutomovel.append(lista)
                                FAutomovel.enqueue(lista)
                                contadorRegistos = contadorRegistos + 1 
                            
                            for mota in range(contadorMota):
                                lista = (pickle.load(f))
                                listaMota.append(lista)
                                FMota.enqueue(lista)
                                contadorRegistos = contadorRegistos + 1 
                                
                            for condutor in range(contadorCondutor):
                                lista = (pickle.load(f))
                                listaCondutor.append(lista)
                                if lista.carta == 1:
                                  FCondCamiao.enqueue(lista)
                                if lista.carta == 2:
                                  FCondAutomovel.enqueue(lista)
                                if lista.carta == 3:
                                  FCondMota.enqueue(lista)
                                contadorRegistos = contadorRegistos + 1 
                                
                                
                            for cliente in range(contadorCliente):
                                lista = (pickle.load(f))
                                listaCliente.append(lista)
                                contadorRegistos = contadorRegistos + 1 
                                
                                
                            for entrega in range(contadorEntrega):
                                lista = (pickle.load(f))
                                listaEntrega.append(lista)
                                if lista.mercadoria_volume <= 80000:
                                    FEntregaMota.enqueue(lista)
                                    
                                if lista.mercadoria_volume > 80000 and lista.mercadoria_volume <= 1200000:
                                    FEntregaAutomovel.enqueue(lista)
                                
                                if lista.mercadoria_volume > 1200000:
                                    FEntregaCamiao.enqueue(lista)
                                contadorRegistos = contadorRegistos + 1 
                            
                            print("O ficheiro ({}) foi aberto com sucesso." .format(ficheiro))
                            print("Foram criados {} registos no programa." .format(contadorRegistos))
                           
                                    
                            f.close()
                    except FileNotFoundError:
                        print("O ficheiro ({}) não existe. \nUtilize a opção (Novo ficheiro) ou (Gravar ficheiro) por favor." .format(ficheiro))
                    except EOFError: 
                        print("O ficheiro ({}) está vazio \nInsira dados e utilize a opção (Gravar ficheiro) por favor." .format(ficheiro))


#---------------------------Gravar Ficheiro Binário----------------------------
                if opcaoAbrirGravar == 3:
                    
#---------------------Listar Conteudo do diretorio atual-----------------------                    
                    ficheirosExistentes = os.listdir('./')
                    print('Ficheiros do diretório atual:\n')
                    contador = 0
                    for file in ficheirosExistentes:
                        print(file)
                        contador = contador + 1
                    if contador == 0:
                        print('Diretório vazio.')
                        print('Não existem ficheiros neste diretório.')
                        
#---------------------Escolher nome do Ficheiro Binário------------------------                      
                    nomeFicheiro = str(input('Introduza o nome do ficheiro para gravar: '))
                    extensaoFicheiro = ".bin"
                    ficheiro = str(nomeFicheiro) + str(extensaoFicheiro)
                    
#---------------------Verificar se Ficheiro Binário existe---------------------  
                    contadorFicheiros = 0
                    for file in ficheirosExistentes:
                        if ficheiro == file:
                            
                            print("O ficheiro ({}) já existe." .format(ficheiro))
                            contadorFicheiros = contadorFicheiros + 1
                            
#-------------------Caso o nome do ficheiro estja presente do diretório onde---
#-------------------o programa está guardado, procede à confirmação se pretende
#-------------------substituir o ficheiro--------------------------------------
                    if contadorFicheiros != 0:
                        print("Pretende substutuir o ficheiro?" .format(ficheiro))
                        print("ATENÇÃO! O conteúdo do ficheiro ({}) não poderá ser recuperado." .format(ficheiro))
                        opcao = str(input("Introduza sim ou não? [s/n] -> "))
                    
#-------------------Caso o ficheiro nao exista no diretorio, irá proceder à sua
#-------------------criação normal e gravar o respetivo conteudo---------------
                    if contadorFicheiros == 0 or opcao == ('s') or opcao == ('S') or opcao == ('sim') or opcao == ('Sim') or opcao == ('SIm') or opcao == ('SIM') or opcao == ('sIM') or opcao == ('siM') or opcao == ('si') or opcao == ('Si') or opcao == ('SI') or opcao == ('y') or opcao == ('Y') or opcao == ('yes') or opcao == ('YES'):
                        with open(ficheiro, 'wb') as f:
                            
#-------------------Criação de váriáveis para contar o número de objetos-------
#-------------------que irão ser guardados no ficheiro-------------------------
                            contadorCamiao = int(0)
                            contadorAutomovel = int(0)
                            contadorMota = int(0)
                            contadorCondutor = int(0)
                            contadorCliente = int(0)
                            contadorEntrega = int(0)
                            
                            
#-------------------Ciclos FOR para precorrer cada lista e por cada objeto-----
#-------------------incrementa a variável contador, no final do ciclo FOR guarda
#-------------------a variável no ficheiro com o seu valor, esta variável irá--
#-------------------servir para determinar o valor do Range do ciclo FOR no----
#-------------------momento de abertura do ficheiro novamente------------------
                            for camiao in listaCamiao:
                                contadorCamiao = int(contadorCamiao) + int(1)
                            pickle.dump(int(contadorCamiao), f)
                            
                            for automovel in listaAutomovel:
                                contadorAutomovel = int(contadorAutomovel) + int(1)
                            pickle.dump(int(contadorAutomovel), f)
                            
                            for mota in listaMota:
                                contadorMota = int(contadorMota) + int(1)
                            pickle.dump(int(contadorMota), f)
                                
                            for condutor in listaCondutor:
                                contadorCondutor = int(contadorCondutor) + int(1)
                            pickle.dump(int(contadorCondutor), f)
                            
                            for cliente in listaCliente:
                                contadorCliente = int(contadorCliente) + int(1)    
                            pickle.dump(int(contadorCliente), f)
                            
                            for entrega in listaEntrega:
                                contadorEntrega = int(contadorEntrega) + int(1)
                            pickle.dump(int(contadorEntrega), f)    
                            
#---------------------------Serializar listas guardando os objetos no ficherio--   
                            contadorRegistos = 0 
                            for camiao in listaCamiao:
                                pickle.dump(camiao, f)
                                contadorRegistos = contadorRegistos + 1 
                            
                            for automovel in listaAutomovel:
                                pickle.dump(automovel, f)
                                contadorRegistos = contadorRegistos + 1 
                                
                            for mota in listaMota:
                                pickle.dump(mota, f)
                                contadorRegistos = contadorRegistos + 1 
                                
                            for condutor in listaCondutor:
                                pickle.dump(condutor, f)
                                contadorRegistos = contadorRegistos + 1 
                                
                            for cliente in listaCliente:
                                pickle.dump(cliente, f)
                                contadorRegistos = contadorRegistos + 1 
                                
                            for entrega in listaEntrega:
                                pickle.dump(entrega, f)
                                contadorRegistos = contadorRegistos + 1 
                            
                            print("{} Registos guardados no ficheiro ({}) com sucesso." .format(contadorRegistos, ficheiro))
                            
                            f.close()
                    else:
                        print("O ficheiro ({}) não foi alterado" .format(ficheiro))
            
                if opcaoAbrirGravar == 0:
                    cicloAbrirGravar = False

        if opcaoMenu == 2:
#------------------------SUB-MENU INSERIR DADOS--------------------------------            
            cicloInserir = True
            while cicloInserir:
                print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
                print("  |                                 |")
                print("  |        INSERIR DADOS            |")
                print("  |                                 |")
                print("  |   1 -> Inserir Viatura          |")
                print("  |   2 -> Inserir Condutor         |")
                print("  |   3 -> Inserir Cliente          |")
                print("  |   4 -> Inserir Entrega          |")
                print("  |   0 -> Voltar ao menu anterior  |")
                print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                
                opcaoInserir = int(input("\nIntroduza um número -> "))
                clear()
#-----------------------SUB-MENU INSERIR VIATURA-------------------------------  
                if opcaoInserir == 1:
                    cicloInserirViatura = True
                    while cicloInserirViatura:
                        print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                        print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
                        print("  |                                 |")
                        print("  |        INSERIR VIATURA          |")
                        print("  |                                 |")                    
                        print("  |   1 -> Inserir Camião           |")
                        print("  |   2 -> Inserir Automóvel        |")
                        print("  |   3 -> Inserir Mota             |")
                        print("  |   0 -> Voltar ao menu anterior  |")
                        print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                        
                        opcaoInserirViatura = int(input("\nIntroduza um número -> "))
                        clear()
#-------PARA CADA OPÇÃO CHAMA FUNÇÃO PARA INSERIR DADOS CORRESPONDENTE---------                  
                        if opcaoInserirViatura == 1:
                            listaCamiao.append(inserirCamiao())
                        
                        elif opcaoInserirViatura == 2:
                            listaAutomovel.append(inserirAutomovel())
                        
                        elif opcaoInserirViatura == 3:
                            listaMota.append(inserirMota())
#----------------------OPÇÃO ZERO VOLTAR AO MENU ANTERIOR----------------------
                        elif opcaoInserirViatura == 0:
                            cicloInserirViatura = False
                        
                        
#-------PARA CADA OPÇÃO CHAMA FUNÇÃO PARA INSERIR DADOS CORRESPONDENTE---------
#---------------ACRESCENTA OS DADOS NA LISTA CORRESPONDENTE--------------------
#-----------------------OPÇÕES DO MENU INSERIR DADOS---------------------------
                            
                if opcaoInserir == 2:
                    listaCondutor.append(inserirCondutor())
                
                if opcaoInserir == 3:
                    listaCliente.append(inserirCliente())
                
                if opcaoInserir == 4:
                    listaEntrega.append(inserirEntrega())
#----------------------OPÇÃO ZERO VOLTAR AO MENU ANTERIOR----------------------                    
                if opcaoInserir == 0:
                    cicloInserir = False

        elif opcaoMenu == 3:
            cicloModificar = True
            while cicloModificar:
                print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
                print("  |                               |")
                print("  |       MODIFICAR DADOS         |")
                print("  |                               |")
                print("  |  1 -> Modificar Viaturas      |")
                print("  |  2 -> Modificar Condutores    |")
                print("  |  3 -> Modificar Clientes      |")
                print("  |  4 -> Modificar Entregas      |")
                print("  |  0 -> Voltar ao menu anterior |")
                print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                
                opcaoModificar = int(input("Introduza um número -> "))
                clear()
                
                if opcaoModificar == 1:
                    cicloModificarViatura = True
                    while cicloModificarViatura:
                        print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                        print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                        print("  |                               |")
                        print("  |       MODIFICAR VIATURAS      |")
                        print("  |                               |")
                        print("  |  1 -> Modificar Camiões       |")
                        print("  |  2 -> Modificar Automóveis    |")
                        print("  |  3 -> Modificar Motas         |")
                        print("  |  0 -> Voltar ao menu anterior |")
                        print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                        
                        opcaoModificarViaturas = int(input("Introduza um número -> "))
                        clear()
                        
                        if opcaoModificarViaturas == 1:
                            modificarCamiao()
                          
                        elif opcaoModificarViaturas == 2:
                            modificarAutomovel()
                        
                        elif opcaoModificarViaturas == 3:
                            modificarMota()
                        
                        elif opcaoModificarViaturas == 0:
                            cicloModificarViatura = False
                        
                elif opcaoModificar == 2:
                    modificarCondutor()
                
                
                elif opcaoModificar == 3:
                    modificarCliente()
                    
                
                elif opcaoModificar == 4:
                    modificarEntrega()
                    
                elif opcaoModificar == 0:
                    cicloModificar = False
            
                    
        elif opcaoMenu == 4:
            
            cicloConsulta = True
            while cicloConsulta:
                print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
                print("  |                               |")
                print("  |       CONSULTAR DADOS         |")
                print("  |                               |")
                print("  |  1 -> Consultar Viaturas      |")
                print("  |  2 -> Consultar Condutores    |")
                print("  |  3 -> Consultar Clientes      |")
                print("  |  4 -> Consultar Entregas      |")
                print("  |  0 -> Voltar ao menu anterior |")
                print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                
                opcaoConsulta = int(input("Introduza um número -> "))
                clear()
                
                if opcaoConsulta == 1:
                    cicloConsultarViatura = True
                    while cicloConsultarViatura:
                        print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                        print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                        print("  |                               |")
                        print("  |       CONSULTAR VIATURAS      |")
                        print("  |                               |")
                        print("  |  1 -> Consultar Camiões       |")
                        print("  |  2 -> Consultar Automóveis    |")
                        print("  |  3 -> Consultar Motas         |")
                        print("  |  0 -> Voltar ao menu anterior |")
                        print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                        
                        opcaoConsultaViaturas = int(input("Introduza um número -> "))
                        clear()
                        if opcaoConsultaViaturas == 1:
                           consultaCamiao()
                    
                        elif opcaoConsultaViaturas == 2:
                            consultaAutomovel()
                        
                        elif opcaoConsultaViaturas == 3:
                            consultaMota()
                        
                        elif opcaoConsultaViaturas == 0:
                            cicloConsultarViatura = False
                    
                elif opcaoConsulta == 2:
                    consultaCondutor()
                
                elif opcaoConsulta == 3:

                    cicloConsultaCliente = True
                    while cicloConsultaCliente:
                        print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                        print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
                        print("  |                               |")
                        print("  |       CONSULTAR CLIENTES      |")
                        print("  |                               |")
                        print("  |  1 -> Oredenado por número    |")
                        print("  |  2 -> Ordenado por nome       |")
                        print("  |  3 -> Pesquisar nome          |")
                        print("  |  0 -> Voltar ao menu anterior |")
                        print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                        
                        opcaoConsultaCliente = int(input("Introduza um número -> "))
                        clear()

                        if opcaoConsultaCliente == 1:
                            consultaCliente()
                    
                        if opcaoConsultaCliente == 2:
                            
                            inserirArvore = [str(cliente) for cliente in listaCliente]
                            root = None
                            for cliente in inserirArvore:
                                root = inserirTree(root, cliente)

                            ordenarTree(root)

                        if opcaoConsultaCliente == 3:
                            
                            inserirArvore = [str(cliente.nome) for cliente in listaCliente]
                            root = None
                            for cliente in inserirArvore:
                                root = inserirTree(root, cliente)
                            
                            pesquisaCliente = (str(input("Introduza o nome de cliente para pesquisar: ")))
                            
                            if pesquisarTree(root, pesquisaCliente):
                                print("O nome ({}) foi encontrado na lista de clientes." .format(pesquisaCliente))
                                
                                #pesquisaListaCliente = [str(cliente) for cliente in listaCliente]
                                contador = 0
                                for cliente in listaCliente:
                                    
                                    if cliente.nome == pesquisaCliente:
                                        contador = contador + 1
                                        print(cliente)
                                        
                                print("Foram encontrados {} clientes na lista." .format(contador))
                                                                
                            else:
                                print("O nome ({}) não foi encontrado na lista de clientes." .format(pesquisaCliente))
                                
                        if opcaoConsultaCliente == 0:
                            cicloConsultaCliente = False

                                        
                elif opcaoConsulta == 4:
                    consultaEntrega()
                    
                elif opcaoConsulta == 0:
                    cicloConsulta = False
                
        elif opcaoMenu == 5:
            cicloGestao = True
            while cicloGestao:
                print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                print("  |                               |")
                print("  |       Gestão DE VIATURAS      |")
                print("  |                               |")
                print("  |  1 -> Gerir Viaturas          |")
                print("  |  2 -> Gerir Condutores        |")
                print("  |  3 -> Gerir Entregas          |")
                print("  |  0 -> Voltar ao menu anterior |")
                print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                
                opcaoGestao = int(input("Introduza um número -> "))
                clear()
                
                if opcaoGestao == 1:
                    cicloGerirViaturas = True
                    while cicloGerirViaturas:
                        print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                        print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
                        print("  |                                     |")
                        print("  |       VIATURAS DISPONÍVEIS          |")
                        print("  |                                     |")
                        print("  |  1 -> Ver Camiões disponíveis       |")
                        print("  |  2 -> Ver Automóveis disponíveis    |")
                        print("  |  3 -> Ver Motas disponíveis         |")
                        print("  |  0 -> Voltar ao menu anterior       |")
                        print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                        
                        opcaoGerirViaturas = int(input("Introduza um número -> "))
                        clear()
                        
                        if opcaoGerirViaturas == 1:
                            verQueueCamiao()
                            
                        if opcaoGerirViaturas == 2:
                            verQueueAutomovel()
                        
                        if opcaoGerirViaturas == 3:
                            verQueueMota()

                        if opcaoGerirViaturas == 0:
                            cicloGerirViaturas = False

                if opcaoGestao == 2:
                    cicloGerirCondutores = True
                    while cicloGerirCondutores:
                        print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                        print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
                        print("  |                                     |")
                        print("  |       GERIR CONDUTORES              |")
                        print("  |                                     |")
                        print("  |  1 -> Ver Condutores disponíveis    |")
                        print("  |  0 -> Voltar ao menu anterior       |")
                        print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                        
                        opcaoGerirCondutores = int(input("Introduza um número -> "))
                        clear()
                        
                        if opcaoGerirCondutores == 1:
                            cicloVerCondutores = True
                            while cicloVerCondutores:
                                print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                                print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
                                print("  |                                     |")
                                print("  |       CONDUTORES DISPONÍVEIS        |")
                                print("  |                                     |")
                                print("  |  1 -> Ver Condutores de Camião      |")
                                print("  |  2 -> Ver Condutores de Autmóvel    |")
                                print("  |  3 -> Ver Condutores de Mota        |")
                                print("  |  0 -> Voltar ao menu anterior       |")
                                print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                                
                                opcaoVerCondutores = int(input("Introduza um número-> "))
                                clear()
                                
                                if opcaoVerCondutores == 1:
                                    verQueueCondutorCamiao()
                                
                                if opcaoVerCondutores == 2:
                                    verQueueCondutorAutomovel()
                                
                                
                                if opcaoVerCondutores == 3:
                                    verQueueCondutorMota()
                                
                                if opcaoVerCondutores == 0:
                                    cicloVerCondutores = False
                            
                        if opcaoGerirCondutores == 0:
                            cicloGerirCondutores = False
                        
                if opcaoGestao == 3:
                    cicloGerirEntregas = True
                    while cicloGerirEntregas:
                        print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                        print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
                        print("  |                                     |")
                        print("  |       GERIR ENTREGAS                |")
                        print("  |                                     |")
                        print("  |  1 -> Ver Entrgas Pendentes         |")
                        print("  |  0 -> Voltar ao menu anterior       |")
                        print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                        
                        opcaoGerirEntregas = int(input("Introduza um número -> "))
                        clear()
                        
                        if opcaoGerirEntregas == 1:
                            cicloVerEntregas = True
                            while cicloVerEntregas:
                                print ("\n\nGESTÃO DE FROTA - ESTAFETA")
                                print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
                                print("  |                                     |")
                                print("  |       ENTREGAS PENDENTES            |")
                                print("  |                                     |")
                                print("  |  1 -> Ver Entregas Camião           |")
                                print("  |  2 -> Ver Entregas Automóvel        |")
                                print("  |  3 -> Ver Entregas Mota             |")
                                print("  |  4 -> Exportar ficheiro de texto    |")
                                print("  |  5 -> Consultar ficheiro de texto   |")
                                print("  |  0 -> Voltar ao menu anterior       |")
                                print("  |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                                
                                opcaoVerEntregas = int(input("Introduza um número -> "))
                                clear()
                                                        
                                if opcaoVerEntregas == 1:
                                    verQueueEntregaCamiao()
                                
                                if opcaoVerEntregas == 2:
                                    verQueueEntregaAutomovel()
                                
                                if opcaoVerEntregas == 3:
                                    verQueueEntregaMota()
                                
                                if opcaoVerEntregas == 4:
                                    exportarFicheiroTexto()
                                    
                                if opcaoVerEntregas == 5:
                                    verFicheiroTexto()
                                
                                if opcaoVerEntregas == 0:
                                    cicloVerEntregas = False

                        if opcaoGerirEntregas == 0:
                            cicloGerirEntregas = False

                if opcaoGestao == 0:
                    cicloGestao = False

        elif opcaoMenu == 0:
            cicloMenu = False
    

print("\n\nO programa terminou.\nObrigado! :) ")
