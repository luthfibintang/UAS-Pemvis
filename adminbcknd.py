from connection import create_connection

def get_user_name(user_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT nama FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        if user:
            return user['nama']
    return None

def get_pengaduan_unverified():
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT p.id_pengaduan, p.id_user, u.nik, p.judul, p.tgl_pengaduan, p.attachment 
            FROM pengaduan p
            JOIN users u ON p.id_user = u.id
            WHERE p.status = %s
        """
        cursor.execute(query, ("Belum Diverifikasi",))
        pengaduan_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return pengaduan_list
    return []

def get_pengaduan_verified():
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT p.id_pengaduan, p.id_user, u.nik, p.judul, p.tgl_pengaduan, p.attachment, p.status 
            FROM pengaduan p
            JOIN users u ON p.id_user = u.id
            WHERE p.status = %s OR p.status = %s
        """
        cursor.execute(query, ("Terverifikasi", "Sedang Diproses"))
        pengaduan_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return pengaduan_list
    return []

def get_pengaduan_selesai():
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT p.id_pengaduan, p.id_user, u.nik, p.judul, p.tgl_pengaduan, p.attachment, p.status 
            FROM pengaduan p
            JOIN users u ON p.id_user = u.id
            WHERE p.status = %s
        """
        cursor.execute(query, ("Selesai",))
        pengaduan_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return pengaduan_list
    return []

def verifikasi_pengaduan(id_pengaduan):
    connection = create_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        query = "UPDATE pengaduan SET status='Terverifikasi' WHERE id_pengaduan=%s"
        cursor.execute(query, (id_pengaduan,))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

def tolak_pengaduan(id_pengaduan):
    connection = create_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        query = "UPDATE pengaduan SET status='Ditolak' WHERE id_pengaduan=%s"
        cursor.execute(query, (id_pengaduan,))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def proses_pengaduan(id_pengaduan):
    connection = create_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        query = "UPDATE pengaduan SET status='Sedang Diproses' WHERE id_pengaduan=%s"
        cursor.execute(query, (id_pengaduan,))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

def get_pengaduan_detail(id_pengaduan):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        # query = "SELECT id_user, judul, tgl_pengaduan, isi_pengaduan, attachment FROM pengaduan WHERE id_pengaduan = %s"
        query = """
            SELECT p.id_pengaduan, p.id_user, u.nama, u.nik, p.judul, p.tgl_pengaduan, p.isi_pengaduan, p.attachment, p.status 
            FROM pengaduan p
            JOIN users u ON p.id_user = u.id
            WHERE p.id_pengaduan = %s
        """
        cursor.execute(query, (id_pengaduan,))
        pengaduan_detail = cursor.fetchone()
        cursor.close()
        connection.close()
        return pengaduan_detail
    return None

def submit_tanggapan(id_pengaduan, user_id, date_reported, description, attachment, last_updated):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            if attachment:  # Jika ada attachment
                sql = """
                INSERT INTO tanggapan (id_pengaduan, id_user, tgl_tanggapan, isi_tanggapan, attachment, last_updated)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                values = (id_pengaduan, user_id, date_reported, description, attachment, last_updated)
            else:  # Jika tidak ada attachment
                sql = """
                INSERT INTO tanggapan (id_pengaduan, id_user, tgl_tanggapan, isi_tanggapan, last_updated)
                VALUES (%s, %s, %s, %s, %s)
                """
                values = (id_pengaduan, user_id, date_reported, description, last_updated)
                
            cursor.execute(sql, values)
            connection.commit()
        except Exception as error:
            print(f"Failed to insert record into table: {error}")
        finally:
            cursor.close()
            connection.close()

def update_status_selesai(id_pengaduan):
    connection = create_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        query = "UPDATE pengaduan SET status='Selesai' WHERE id_pengaduan=%s"
        cursor.execute(query, (id_pengaduan,))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def get_all_user():
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT id, nik, nama, email, telp FROM users"
        cursor.execute(query)
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        if user:
            return user
    return None