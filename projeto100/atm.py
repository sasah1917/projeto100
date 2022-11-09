def registar_cartao(dados):
    cadastro_cartao = input("\n\nCartao: ")
    if cadastro_cartao in dados:
        print("ERRO! Ja existe um cartao com esse nome")
        return
    cadastro_senha = input("\n\nSenha: ")
    print("cadastro realizado com sucesso!")
    dados[cadastro_cartao] = cadastro_senha

dados_login_e_senha = {}
answer = input("Voce é um novo usuario? Responda 'sim' ou 'nao': ")

if answer == "Sim" or answer == "sim":
    print("Vamos nos cadastrar!")
    registar_cartao(dados_login_e_senha)

usuario = input("Entre com o usuario: ")
senha = input("Informe sua senha: ")
if usuario in dados_login_e_senha:
    if dados_login_e_senha[usuario] == senha:
        print("login efetuado")
    else:
        print("Senha incorreta")
else:
    print('Nao existe senhum cadastro com esse nome de usuario')