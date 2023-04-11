# pip install psycopg2-binary

import psycopg2 as db

class Config:
	def __init__(self):
		self.config = {
			'user': 'postgres',
			'password': 'mpe',
			'host': 'localhost',
			'port': '5432',
			'database': 'sistema_de_vendas'
		}

class Connection(Config):
	def __init__(self):
		Config.__init__(self) 
		try:
			self.conn = db.connect(**self.config)
			self.cur = self.conn.cursor()
		except Exception as e:
			print('Erro na conexão')
			exit(1)

	def __enter__(self):
		return self
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.commit()
		self.connection.close()

	@property
	def connection(self):
		return self.conn

	def fetchall(self):
		return self.cursor.fetchall()

	def execute(self, sql, params=None):
		self.cursor.execute(sql, params or ())
		self.connection.commit()

	def query(self, sql, params=None):
		self.cursor.execute(sql, params or ())
		return self.fetchall()



	@property
	def cursor(self):
		return self.cur

	def commit(self):
		self.connection.commit()
		
		
