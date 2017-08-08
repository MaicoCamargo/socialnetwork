def criaUsuarioBot(perfis):
    usuario = []
    nome = "Eder"
    idade = "19"
    email = "eder@hotmail"
    telefone = "1111"
    senha = "SENHAa"

    usuario.append(nome)
    usuario.append(telefone)
    usuario.append(email)
    usuario.append(idade)
    usuario.append(senha)

    perfis.append(usuario)
    usuario = []
    nome = "Elaine"
    idade = "17"
    email = "xx@gmail"
    telefone = "5555"
    senha = "senha"

    usuario.append(nome)
    usuario.append(telefone)
    usuario.append(email)
    usuario.append(idade)
    usuario.append(senha)

    perfis.append(usuario)
    usuario = []
    nome = "Eloi"
    idade = "21"
    email = "zzz@yahoo"
    telefone = "999"
    senha = "0001"

    usuario.append(nome)
    usuario.append(telefone)
    usuario.append(email)
    usuario.append(idade)
    usuario.append(senha)
    perfis.append(usuario)
    usuario = []
    nome = "Maico"
    idade = "34"
    email = "ss@gmail"
    telefone = "9906844"
    senha = "senah111"

    usuario.append(nome)
    usuario.append(telefone)
    usuario.append(email)
    usuario.append(idade)
    usuario.append(senha)
    perfis.append(usuario)
    usuario = []
    nome = "Antonio"
    idade = "43"
    email = "12@gmail"
    telefone = "5599033"
    senha = "33111"

    usuario.append(nome)
    usuario.append(telefone)
    usuario.append(email)
    usuario.append(idade)
    usuario.append(senha)
    perfis.append(usuario)
    usuario = []
    nome = "Joce"
    idade = "22"
    email = "joce@gmail"
    telefone = "99064"
    senha = "ahahSENHA"

    usuario.append(nome)
    usuario.append(telefone)
    usuario.append(email)
    usuario.append(idade)
    usuario.append(senha)
    perfis.append(usuario)


def criaAmizadesBot(amizades):

    amigo1 = 2
    amigo2 = 5
    amizades[amigo1][amigo2] = "Familia"
    amigo1 = 5
    amigo2 = 2
    amizades[amigo1][amigo2] = "Familia"

    amigo1 = 3
    amigo2 = 1
    amizades[amigo1][amigo2] = "Conhecido"

    amigo1 = 1
    amigo2 = 3
    amizades[amigo1][amigo2] = "Trabalho"

    amigo1 = 2
    amigo2 = 4
    amizades[amigo1][amigo2] = "Familia"
    amigo1 = 4
    amigo2 = 2
    amizades[amigo1][amigo2] = "Familia"

    amigo1 = 5
    amigo2 = 0
    amizades[amigo1][amigo2] ="Conhecido"

    amigo1 = 0
    amigo2 = 5
    amizades[amigo1][amigo2] = "Conhecido"

    amigo1 = 0
    amigo2 = 4
    amizades[amigo1][amigo2] = "Amigos"
    amigo1 = 4
    amigo2 = 0
    amizades[amigo1][amigo2] = "Amigos"

    amigo1 = 3
    amigo2 = 2
    amizades[amigo1][amigo2] = "Trabalho"

    amigo1 = 2
    amigo2 = 3
    amizades[amigo1][amigo2] = "Trabalho"

    amigo1 = 0
    amigo2 = 2
    amizades[amigo1][amigo2] = "Amigos"

    amigo1 = 2
    amigo2 = 0
    amizades[amigo1][amigo2] = "Amigos"

    amigo1 = 4
    amigo2 = 1
    amizades[amigo1][amigo2] = "Trabalho"

    amigo1 = 1
    amigo2 = 4
    amizades[amigo1][amigo2] = "Trabalho"


def criarPerfil(amizades):#cria os perfis
    usuario= []
    nome= input("nome:")
    idade = input("idade:")
    email = input("email:")
    telefone = input("celular:")
    senha = input("senha:")
    usuario.append(nome)
    usuario.append(telefone)
    usuario.append(email)
    usuario.append(idade)
    usuario.append(senha)
    linha = []
    for i in range(len(amizades)):
        linha.append("----")


    amizades.append(linha)
    for i in range(len(amizades)):
        amizades[i].append("----")

    return usuario


def vizualizarPerfis(perfis):

    for i in range(len(perfis)):

        print(perfis[i][0])
        print(perfis[i][1])
        print(perfis[i][2])
        print(perfis[i][3])
        print(perfis[i][4],"\n")

def criaMatrizAmizades(dimensao):#cria matriz com valores 'nulos'
    amizades =[]
    for i in range(dimensao):
        linha = []
        for o in range(dimensao):
            linha.append('----')

        amizades.append(linha)
    return amizades

def verIDs(perfis):
    for i in range(len(perfis)):
        print("ID= ",i,"|->",perfis[i][0])

def criaAmizades(amizades,perfis):
    print("implementando...")
    verIDs(perfis)
    amigo1=int(input("digite o ID do 1º amigo:"))
    amigo2=int(input("digite o ID do amigo que deseja Ser amigo:"))
    ("Escolha o tipo de Amizade Entre Eles")
    tipoDeAmizades = int(input("1=>Trabalho | 2=>Conhecido | 3=>Amigos | 4=>Familia\n=>"))

    #tipoDeAmizades= int(input("1=>Trabalho | 2=>Conhecido | 3=>Amigos | 4=>Familia\n=>"))
    if tipoDeAmizades==1:
        amizades[amigo1][amigo2] = "Trabalho"  # cria a amizade em um sentido
        amizades[amigo2][amigo1] = "Trabalho"  # cria a amizade no outro sentido

    elif tipoDeAmizades==2:
        amizades[amigo1][amigo2] = "Conhecido"  # cria a amizade em um sentido
        amizades[amigo2][amigo1] = "Conhecido"  # cria a amizade no outro sentido

    elif tipoDeAmizades==3:
        amizades[amigo1][amigo2] = "Amigos"  # cria a amizade em um sentido
        amizades[amigo2][amigo1] = "Amigos"  # cria a amizade no outro sentido

    elif tipoDeAmizades==4:
        amizades[amigo1][amigo2] = "Familia"  # cria a amizade em um sentido
        amizades[amigo2][amigo1] = "Familia"  # cria a amizade no outro sentido
    else:
        print("escolha invalida insira uma opção valida")

def verAmizades(amizades,perfis):
    for o in range(len(amizades)):

        print(o,"<",perfis[o][0],"    -->", amizades[o],"\n")

def apagarPerfil(perfis):
    verIDs(perfis)
    print("escolha o ID do Perfil para Apagar")
    idDeletar= int(input("ID -}"))
    del perfis[idDeletar]
    print("perfil Apagado com sucesso")

def verPerfilDoUsuario(perfil,indice):
    print("...perfil...")
    print("NOME: ",perfil[indice][0])
    print("TELEFONE: ",perfil[indice][1])
    print("EMAIL: ",perfil[indice][2])
    print("IDADE: ",perfil[indice][3])
    print("SENHA: ",perfil[indice][4])

def caminhamentoProfundidade(totalDeNos,atual,visitados,m,amigosDosAmigos):

    amigosDosAmigos.append(atual)
    visitados[atual] = True
    for i in range(totalDeNos):
        if m[int(atual)][int(i)] !="----" and not visitados[int(i)]:
            caminhamentoProfundidade(totalDeNos,i,visitados,m,amigosDosAmigos)


def sugerirGrupo(amigosDosAmigos,perfis,amizades):
   amg=[]
   conh=[]
   trab=[]
   fam=[]#lista que terao os indices dos amigos que podemos criar grupos com ess tipo de ligacao
   for c in range(len(amigosDosAmigos)):
       for i in range(len(amizades[amigosDosAmigos[0]])):#ver quantos amigos o usuario tem e depois sugerir grupos com seus amigos e amigo dos amigos
           if amizades[amigosDosAmigos[c]][i]!='----':
               if amizades[amigosDosAmigos[c]][i] =="Trabalho":
                   trab.append(i)#add o indice dos usuarios que pode-se criar esse tipo de grupo

               elif amizades[amigosDosAmigos[c]][i] == "Amigos":
                    amg.append(i)
                    #print("crie um grupo de 'Amigos', com ", perfis[i][0])
               elif amizades[amigosDosAmigos[c]][i] == "Familia":
                   fam.append(i)
                   #print("crie um grupo da 'Familia', com ", perfis[i][0])
               elif amizades[amigosDosAmigos[c]][i] == "Conhecido":
                   conh.append(i)
                   #print("crie um grupo de 'Conhecidos', com ", perfis[i][0])

   for i in range(len(trab)):
       print("crie um grupo do 'Trabalho', com ", perfis[trab[i]][0])

   for i in range(len(amg)):
       print("crie um grupo do 'Amigos', com ", perfis[amg[i]][0])

   for i in range(len(fam)):
       print("crie um grupo do 'Familia', com ", perfis[fam[i]][0])
   for i in range(len(conh)):
       print("crie um grupo do 'Conhecido', com ", perfis[conh[i]][0])


def sugerirAmigos(amigosDosAmigos,Sugerir,MatrizDeAmizades,perfis):#sugerir e o usuario que vai ser sugerido os amigos
    validador=0 #verifica se tem amigos para que apartir desse possam ser sugeridos amigos caso nao tenha informa o para que se crie uma amizade
    for i in range(len(MatrizDeAmizades)):
        if(MatrizDeAmizades[i][Sugerir]!='----'):
            validador+=1


    if(validador!=0):

        del amigosDosAmigos[0]
        for i in range(len(MatrizDeAmizades[Sugerir])):
            if(MatrizDeAmizades[Sugerir][i] != "----"):
                amigosDosAmigos.remove(i)

        if len(amigosDosAmigos)==0:
            print("voce è amigos de todos os amigos dos seus amigos")
        else:
            print("Seus amigos Sao amigos de")
            for i in range(len(amigosDosAmigos)):
                print(perfis[i][0])

            print("e voce não,sugiro a amizade deles para ver para aumentar a sua rede de amigos")
    else:
        print("voce ainda nao é amigo de ninguem crie uma amizade com alguem para poder sugerir mais amigos pra voce")


def apagarUsuario(perfis,amizades,id):
    del perfis[id] #apagar da lista de perfil
    verIDs(perfis)
    del amizades[id]
    for i in range(len(amizades)):
        del amizades[i][id]

def apagarAmizades(amizades,id):

    indiceDosAmigos =[]
    for i in range(len(amizades)):#acha os indices dos amigos do usuario
        if(amizades[id][i]!='----'):
            indiceDosAmigos.append(i)

    for i in range(len(indiceDosAmigos)):#apaga as amizades do usuario um
        amizades[id][indiceDosAmigos[i]] = '----'

    for ii in range(len(indiceDosAmigos)):
        amizades[indiceDosAmigos[ii]][id]='----'# apaga o registro que os meus amigos tinham falando que eram meu amigo

def verAmizadesUsuario(amizades,perfis,id):
    for c in range(len(amizades[id])):
        if amizades[id][c] != '----':

            if amizades[id][c] == "Trabalho":
                print("   AMIZADE TIPO: Trabalho\n")

                print("NOME",perfis[c][0])
                print("EMAIL", perfis[c][2])
                print("TELEFONE", perfis[c][1])
                print("__--------------------------__")
            elif amizades[id][c] == "Familia":
                print("   AMIZADE TIPO: Familia\n")

                print("NOME", perfis[c][0])
                print("EMAIL", perfis[c][2])
                print("TELEFONE", perfis[c][1])
                print("IDADE", perfis[c][3])
                print("SENHA", perfis[c][4])
                print("__--------------------------__")
            elif amizades[id][c] == "Conhecido":
                print("   AMIZADE TIPO: Conhecido\n")

                print("NOME", perfis[c][0])
                print("EMAIL", perfis[c][2])
                print("__--------------------------__")
            else :
                print("   AMIZADE TIPO: Amigos\n")

                print("NOME", perfis[c][0])
                print("EMAIL", perfis[c][2])
                print("TELEFONE", perfis[c][1])
                print("IDADE", perfis[c][3])
                print("__--------------------------__")

