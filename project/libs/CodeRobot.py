
from ast import Return
from cryptography.fernet import Fernet


class CodeRobot:
    def __init__(self):
        self.atributos()

    def atributos(self):
        #----> Seto as variaveis que podem ser usadas em todos os metodos <-----#
        self.caminhokey = open('novachave.key', 'wb')
        self.key = Fernet.generate_key()
        self.fernet =   Fernet(self.key)
        self.arquivo_lido = open('resources/token/token.txt', "rb").read()
        self.arquivo_lido_encriptado = open('resources/token/token.txt', "rb").read()
        

    def escrever_arquivo_encryptado(self, filename, encripted):
        #-----> Metodo para escrever no arquivo O que foi encriptado do propio <-----#
        with open(filename, "wb") as file:
            file.write(encripted)
        return     encripted

    

    def criar_key(self,filekey):
        #-----> Metodo que cria o arquivo(se nescessario) e preenche com a key <-----#
        self.atributos()
        caminhokey = open(filekey, 'wb')
        caminhokey.write(self.key)
    
    def load_file(self, arquivo): 
        #-----> Metodo que Le e retorna o conteudo do arquivo desejado <-----#  
        return  open(arquivo, "rb").read()

    def load_key(self, filekey):
        #----->  Metodo que Lê e retorna a key do arquivo desejado <-----#
        return open(filekey, "rb").read()

    def load_encripted_file(self):
        #-----> metodo que le e retorna o conteudo encriptado <-----#
        return  open('resources/token/token.txt', "rb").read()

    def encrypt(self, filename,filekey):
        #-----> Metodo que faz o encript do arquivo desejado pela key que foi gerada e retorna o conteudo encriptado <-----#
        #       key = bytes                                                                                                #
        #       m = objeto fernet                                                                                          #
        #       conteudo = string do arquivo encriptado                                                                    #
        #------------------------------------------------------------------------------------------------------------------#
        #         PASSOS                                                                                                   #
        #-----> Carrego a key <--------------------------------------------------------------------------------------------#
        key = self.load_key(filekey)                    
        #-----> Crio um objeto da classe Fernet <-----#
        m = Fernet(key)
        #-----> Faço o encrip do objedo passando o arquivo que vou criptografar em bytes por isso temos a funçao load_file() <------#
        #   Se preferir use:                                                                                                        #
        #   arquivo = self.load_key('nome do arquivo')     notas da linha -> ou passe o nome_do_arquivo por prarametro              #
        #   conteudo = m.encrypt(arquivo)                                                                                           #
        #---------------------------------------------------------------------------------------------------------------------------#
        conteudo = m.encrypt(filename) 
        
        return  conteudo

    def decrypt(self, filename, conteudo, filekey):
        #-----> Metodo que faz o encript do arquivo desejado pela key que foi gerada e retorna o conteudo encriptado <-----#
        #       key = bytes                                                                                                #
        #       f = objeto fernet                                                                                          #
        #       conteudo = string do arquivo encriptado                                                                    #
        #------------------------------------------------------------------------------------------------------------------#
        #         PASSOS                                                                                                   #
        #-----> Carrego a key <--------------------------------------------------------------------------------------------#
        key = self.load_key(filekey)
        #-----> Crio um objeto da classe Fernet <-----#
        f = Fernet(key)
        #-----> Faço o deencrip do objedo passando o arquivo que vou criptografar em bytes por isso temos a funçao load_file() <------#
        decrypted_data = f.decrypt(conteudo)
        
        with open(filename, "wb") as file:
            file.write(decrypted_data)
        return      decrypted_data

# m = CodeRobot()
# m.criar_key("novachave.txt")
# arquivo_encripted = m.encrypt('token.txt')
# print (arquivo_encripted)
# print(m.decrypt('token.txt'))