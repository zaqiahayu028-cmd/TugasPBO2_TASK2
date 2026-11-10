from domain.entities import Mahasiswa
from infrastructure.database import Database


class StudentRepository:
    def __init__(self, database: Database):
        self.database = database

    def get_all(self):
        connection = self.database.get_connection()
        if connection is None:
            return []

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM mahasiswa")
            rows = cursor.fetchall()

            return [
                Mahasiswa(
                    nim=row["nim"],
                    nama=row["nama"],
                    prodi=row["prodi"],
                    angkatan=row["angkatan"]
                )
                for row in rows
            ]
        except Exception as e:
            print(f"Error mengambil data: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

    def add(self, mahasiswa):
        connection = self.database.get_connection()
        if connection is None:
            return False

        try:
            cursor = connection.cursor()
            sql = """
                INSERT INTO mahasiswa (nim, nama, prodi, angkatan)
                VALUES (%s, %s, %s, %s)
            """
            values = (
                mahasiswa.nim,
                mahasiswa.nama,
                mahasiswa.prodi,
                mahasiswa.angkatan
            )
            cursor.execute(sql, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error menambah data: {e}")
            return False
        finally:
            cursor.close()
            connection.close()