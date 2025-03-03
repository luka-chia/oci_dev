import oracledb
import time

def conn_db(username, password):
    print("username="+username)
    print("password="+password)
    connection = oracledb.connect(
        user=username, password=password, host="213.35.108.92", 
        port=1521, service_name="DB1220_PDB1.lukasingaporepu.lukasingaporevc.oraclevcn.com")
    print(connection.db_name)
    print(connection.dsn)

def ras_connect():
    v_user = "ras_common"
    v_password = "OracleCanton10__"

    v_dns = "(DESCRIPTION=(RETRY_DELAY=1)(ADDRESS=(PROTOCOL=tcp)(HOST=213.35.108.92)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=DB1220_PDB1.lukasingaporepu.lukasingaporevc.oraclevcn.com)))"

    try:
        connection = oracledb.connect(user=v_user, password=v_password, dsn=v_dns)
        cursor = connection.cursor()

        print("Successfully connected to Oracle Database")
        v_sessionid = cursor.var(oracledb.DB_TYPE_RAW)

        # Create RAS Session
        external_user = False
        if external_user:
            cursor.callproc("SYS.DBMS_XS_SESSIONS.CREATE_SESSION",["boss_team_ras", v_sessionid, True, False])
        else:
            cursor.callproc("SYS.DBMS_XS_SESSIONS.CREATE_SESSION", ["north_sales_team_ras", v_sessionid])

        # Print RAS session id
        # print(v_sessionid.getvalue())

        # Create dynamic role
        #a = connection.gettype("XS$NAME_LIST").newobject()
        #a.append("dept50")
        #enabled_dynamic_roles = a

        # Attach RAS Session with dynamic role to DB session
        if external_user:
            pass
            #cursor.callproc("SYS.DBMS_XS_SESSIONS.ATTACH_SESSION", [v_sessionid, enabled_dynamic_roles])
        else:
            cursor.callproc("SYS.DBMS_XS_SESSIONS.ATTACH_SESSION", [v_sessionid])
            
        # The query
        v_select = "select text,region,metadata from text_embeddings"    

        time.sleep(1)
        cursor.execute(v_select)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        time.sleep(1)

    except Exception as e:
        print(str(e))

    finally:
        cursor.callproc("SYS.DBMS_XS_SESSIONS.DETACH_SESSION", [])
        cursor.callproc("SYS.DBMS_XS_SESSIONS.DESTROY_SESSION", [v_sessionid, True])  

if __name__ == '__main__':
    #conn_db("ras_common","OracleCanton10__")
    ras_connect()