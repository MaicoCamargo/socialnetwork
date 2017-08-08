import metodos

perfis = [] #lista que tera todos os perfis dos usuarios
verificados = [] #amigos que ja foram verificados sao guardados aqui para evitar looping
metodos.criaUsuarioBot(perfis)#cria os usuario bot
MatrizAmizades= metodos.criaMatrizAmizades(len(perfis))#cria a matriz que representa as amizades de cada usuario
vi =[] #lista que guarada os caminhos ja verificados no metodo de caminhamento do grafo
listaTiposDeLigacao=[] #guarda os tipos de ligacoes para fazer o grupo de amigos depois
coordenadas = [] #sabe o usuario que farão parte do grupo
amigosDosAmigos = [] #sera a lista dos amigos dos meus amigos
metodos.criaAmizadesBot(MatrizAmizades)#cria as amizades bot

print("------------------BEM VINDO A REDE SOCIAL PYcamargGRAM --------------------------------")
print("-----------------------%%%%%%%%%%%%%%%%%%%%%%%%%%--------------------------------------")


while(True):
    print("                       0-Criar Usuario")
    print("                       1-Ver Usuarios")
    print("                       2-Criar Amizade")
    print("                       3-Ver Todas as Amizade - exibe a matriz")
    print("                       4-Apagar Usuario")
    print("                       5-Desfazer Amizade")
    print("                       6-Criar Grupo")
    print("                       7-Sugerir Amizades")
    print("                       8-Ver Perfil")
    print("                       9-Ver Amizades")
    print("                       10-SAIR")

    escolha = int(input("Quero Fazer O que Diz a Opção? "))
    # --------------------------------------------------------------------
    if(escolha==0):
        print("criar usuarios")
        perfis.append(metodos.criarPerfil(MatrizAmizades))
    # --------------------------------------------------------------------
    elif(escolha==1):
        print("ver usuarios")
        metodos.vizualizarPerfis(perfis)
    # --------------------------------------------------------------------
    elif(escolha==2):
        print("criar amizades")
        metodos.criaAmizades(MatrizAmizades,perfis)
    # --------------------------------------------------------------------
    elif (escolha==3):
        print("ver a tabela que representa as amizades")
        metodos.verAmizades(MatrizAmizades,perfis)
    # --------------------------------------------------------------------
    elif (escolha==4):
        print("apagar usuarios")
        print("Escolha o ID do Usuario que Deseja Apagar")
        metodos.verIDs(perfis)
        excluir=int(input("digite o do Usuario ID= "))
        metodos.apagarUsuario(perfis,MatrizAmizades,excluir)
    # --------------------------------------------------------------------
    elif (escolha==5):
        print("apagar amizade")
        metodos.verIDs(perfis)
        idUsuario = int(input("Digite ID do Usuario"))
        metodos.apagarAmizades(MatrizAmizades,idUsuario)
    #--------------------------------------------------------------------
    elif (escolha==6):#bugando*******************
        print("criar grupo de amigos")
        print("Escolha O Usuario,Verificarei se ele ele tem amigos e se seus amigos tem amigos e\nde acordo com interesses vou sugerir\n a criaçao de grupos de acorco com algum intesse em comum")
        metodos.verIDs(perfis)
        usuario=int(input("Usuario: "))
        for i in range(len(perfis)):#laco que cria uma lista que guardara os indices visitados pelo metodo a seguir, essa lista tem o tamanho da lista perfis pq esse é o total de nos do grafo
            vi.append(False)
        metodos.caminhamentoProfundidade(len(MatrizAmizades),int(usuario) ,vi,MatrizAmizades,amigosDosAmigos)
        print(amigosDosAmigos)
        metodos.sugerirGrupo(amigosDosAmigos,perfis,MatrizAmizades)
    #---------------------------------------------------------------------
    elif (escolha==7):
        print("sugerir novas amizades")

        for i in range(len(perfis)):
            vi.append(False)
        print("Escolha o Usuario Para Sugerir Amizades")
        metodos.verIDs(perfis)
        op= int(input("Digite o ID Do Usuario Desejado: "))
        #print("id:",op)
        metodos.caminhamentoProfundidade(len(MatrizAmizades),op ,vi,MatrizAmizades,amigosDosAmigos)
        metodos.sugerirAmigos(amigosDosAmigos,op,MatrizAmizades,perfis)
    #---------------------------------------------------------------------
    elif (escolha==8):
        print("escolha um Perfil para Visualizar")
        metodos.verIDs(perfis)
        indice = int(input("Digite o ID do Usuario Desejado:"))
        metodos.verPerfilDoUsuario(perfis,indice)
    # ---------------------------------------------------------------------
    elif(escolha==9):
        print("ver as amizades de um determinado usuario")
        metodos.verIDs(perfis)
        indic=int(input("Digite o ID do Usuario que deseja ver as Amizades"))
        metodos.verAmizadesUsuario(MatrizAmizades,perfis,indic)
    # ---------------------------------------------------------------------
    elif(escolha==10):
        print("sair")
        break
    #---------------------------------------------------------------------
    elif (escolha!=1 or escolha!=2 or escolha!=3 or escolha!=4 or escolha!=5 or escolha!=6 or escolha!=7 or escolha!=8 or escolha!=9 or escolha!=10):
        print("essa opcao nao consta no menu, tente uma opção valida")
