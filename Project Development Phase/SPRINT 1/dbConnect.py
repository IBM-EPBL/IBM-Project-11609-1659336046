import ibm_db


def connection():
    try:
        conn = ibm_db.connect(
            "DATABASE=bludb;HOSTNAME=824dfd4d-99de-440d-9991-629c01b3832d.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30119;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=wgm09612;PWD=h0i0L1VmjpNBDhoK", '', '')
        print(conn)
    except:
        print("connection successful...")
