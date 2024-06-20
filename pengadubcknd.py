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

def get_pengaduan_by_user_id(user_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT id_pengaduan, judul, tgl_pengaduan, attachment, status FROM pengaduan WHERE id_user = %s"
        cursor.execute(query, (user_id,))
        pengaduan_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return pengaduan_list
    return []

def submit_pengaduan(user_id, date_reported, title, description, attachment, status, last_updated):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            if attachment:  # Jika ada attachment
                sql = """
                INSERT INTO pengaduan (id_user, tgl_pengaduan, judul, isi_pengaduan, attachment, status, last_updated)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                values = (user_id, date_reported, title, description, attachment, status, last_updated)
            else:  # Jika tidak ada attachment
                sql = """
                INSERT INTO pengaduan (id_user, tgl_pengaduan, judul, isi_pengaduan, status, last_updated)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                values = (user_id, date_reported, title, description, status, last_updated)
                
            cursor.execute(sql, values)
            connection.commit()
        except Exception as error:
            print(f"Failed to insert record into table: {error}")
        finally:
            cursor.close()
            connection.close()


def get_pengaduan_detail(id_pengaduan):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT judul, tgl_pengaduan, isi_pengaduan, attachment, status FROM pengaduan WHERE id_pengaduan = %s"
        cursor.execute(query, (id_pengaduan,))
        pengaduan_detail = cursor.fetchone()
        cursor.close()
        connection.close()
        return pengaduan_detail
    return None

def get_tanggapan_detail(id_pengaduan):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT t.tgl_tanggapan, t.id_user, t.isi_tanggapan, u.nama, t.attachment 
            FROM tanggapan t
            JOIN users u ON t.id_user = u.id
            WHERE t.id_pengaduan = %s
        """
        cursor.execute(query, (id_pengaduan,))
        pengaduan_detail = cursor.fetchone()
        cursor.close()
        connection.close()
        return pengaduan_detail
    return None

def delete_pengaduan_by_id(id_pengaduan):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Hapus pengaduan
            delete_query = "DELETE FROM pengaduan WHERE id_pengaduan = %s"
            cursor.execute(delete_query, (id_pengaduan,))
            connection.commit()
            cursor.close()
            connection.close()
            return True  # Berhasil menghapus
        except Exception as e:
            print(f"Error deleting pengaduan: {e}")
            connection.rollback()
        finally:
            if connection:
                connection.close()
    return False  # Gagal menghapus

def update_pengaduan(id_pengaduan, judul, isi_pengaduan, attachment, last_updated):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
            UPDATE pengaduan
            SET judul = %s, isi_pengaduan = %s, attachment = %s, last_updated = %s
            WHERE id_pengaduan = %s
        """
        cursor.execute(query, (judul, isi_pengaduan, attachment, last_updated, id_pengaduan))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    return False
