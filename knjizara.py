import psycopg2
import pandas as pd

class Proizvodi:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="Bookstore",
            user="postgres",
            password="Sekiraumed12"
        )

    def ucitaj_proizvode(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT naziv, cena, stanje FROM proizvodi;")
        result = cursor.fetchall()
        cursor.close()
        # Pretvaranje rezultata u pandas DataFrame
        df = pd.DataFrame(result, columns=['naziv', 'cena', 'stanje'])
        return df


    def trazi_proizvod(self, search):
        cursor = self.conn.cursor()
        query = "SELECT * FROM proizvodi WHERE naziv LIKE '%{}%'".format(search)
        cursor.execute(query)

        results = cursor.fetchall()
        cursor.close()

       

        if len(results) == 0:
            return "Nema rezultata za pretragu"

        # Pretvaranje rezultata u pandas DataFrame
        df = pd.DataFrame(results, columns=['id', 'naziv', 'opis', 'stanje', 'cena'])
        # Filtriranje rezultata
        df['stanje'] = df['stanje'].apply(lambda x: 'Na stanju' if x > 0 else 'Nije na stanju')
        filtered_results = df[['naziv', 'stanje']]

        return filtered_results

class Administrator:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="Bookstore",
            user="postgres",
            password="Sekiraumed12"
        )

    def ucitaj_administratora(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM admin;")
        result = cursor.fetchall()
        cursor.close()
        # Pretvaranje rezultata upita u pandas DataFrame
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame.from_records(result, columns=columns)

        return df

    
proizvodi = Proizvodi()
df_proizvodi = proizvodi.ucitaj_proizvode()
#print(df_proizvodi)
administrator = Administrator()
df_administrator = administrator.ucitaj_administratora()
print(df_administrator)
