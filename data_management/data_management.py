import sqlite3

class DataMan:

    def store_vocabulary(
        self,
        word,
        reading,
        meaning,
        created_date
    ):

        try:

            connection = sqlite3.connect("base/jp_pb.db")

            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO Vocabulary
                (
                    Word,
                    Reading,
                    Meaning,
                    CreatedDate
                )
                VALUES
                (
                    ?, ?, ?, ?
                )
                """,
                (
                    word,
                    reading,
                    meaning,
                    created_date
                )
            )

            cursor.execute("SELECT * FROM Vocabulary")

            rows = cursor.fetchall()

            for row in rows:
                print(row)

            connection.commit()

            connection.close()

            return "OK"

        except Exception as e:
            print(e)
            return "NOT OK"