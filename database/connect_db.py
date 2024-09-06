import oracledb

def conn_db(username, password):
    print("username="+username)
    print("password="+password)
    connection = oracledb.connect(
        user=username, password=password, host="140.245.127.31", 
        port=1521, service_name="db0821_pdb1.lukasingaporepu.lukasingaporevc.oraclevcn.com")
    print(connection.db_name)
    print(connection.dsn)
    return connection.dsn

if __name__ == '__main__':
    conn_db()