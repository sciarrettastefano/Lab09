from database.DB_connect import DBConnect
from model.airoport import Airport
from model.edge import Edge


class DAO():

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """SELECT *
                    from airports"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(xMin, idMapAiroports):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """SELECT t1.id1 as id1, t1.id2 as id2, (t1.dTot+t2.dTot)/(t1.cnt+t2.cnt) as distanzaMedia
                    from (SELECT f1.ORIGIN_AIRPORT_ID as id1, f1.DESTINATION_AIRPORT_ID as id2, SUM(f1.DISTANCE) as dTot, COUNT(*) as cnt
                            from flights f1
                            group by id1, id2) as t1,
                         (SELECT f1.ORIGIN_AIRPORT_ID as id1, f1.DESTINATION_AIRPORT_ID as id2, SUM(f1.DISTANCE) as dTot, COUNT(*) as cnt
                            from flights f1
                            group by id1, id2) as t2
                    WHERE t1.id1 = t2.id2
                    and t1.id2 = t2.id1
                    group BY id1, id2
                    having distanzaMedia >= %s"""

        cursor.execute(query, (xMin, ))

        for row in cursor:
            result.append((idMapAiroports[row["id1"]], idMapAiroports[row["id2"]], row["distanzaMedia"]))

        cursor.close()
        conn.close()
        return result


