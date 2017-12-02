import psycopg2

def main(args=[]):
    
    conn = psycopg2.connect("host=127.0.0.1, database=helloif_usuario, user=root, password=ifpbinfo, port=3306")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tb_usuario")
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print("ID: %i"%(usuario[0]))
        print("Login: %s" %(usuario[2]))
        print("Senha: %s" %(usuario[1]))
        print("Nome: %s" %(usuario[4]))
        print("Data de nascimento: %s" %(usuario[5]))
        print("Gênero: %s" %(usuario[6]))
        print("Profissão: %s" %(usuario[7]))
        print("Logado: %s" %(usuario[3]))
        print("")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
