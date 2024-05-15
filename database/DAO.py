from database.DB_connect import DBConnect
from model import country
from model import border


class DAO():
    @staticmethod
    def getCountries():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """select CCode from country c"""

        cursor.execute(query)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(row[0])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getBorders(year):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """select state1no, state2no from contiguity c where c.`year` <= %s"""

        cursor.execute(query, (year,))
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append((row[0], row[1]))
        cursor.close()
        cnx.close()
        return result


    @staticmethod
    def getCountry(code):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select * from country c where c.CCode = %s"""

        cursor.execute(query, (code,))
        row = cursor.fetchone()

        result = country.Country(**row)
        cursor.close()
        cnx.close()
        return result






