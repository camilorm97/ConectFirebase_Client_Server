import socket
import threading
import sys
import pickle


class Servidor():
	def __init__(self, host=socket.gethostname(), port=59989):
		self.clientes = []
		self.allUsers = []
		self.intento = 0
		self.sock = socket.socket()
		self.sock.bind((str(host), int(port)))
		self.sock.listen(20)
		self.sock.setblocking(False)

		aceptar = threading.Thread(target=self.aceptarC)
		procesar = threading.Thread(target=self.procesarC)

		aceptar.daemon = True
		aceptar.start()

		procesar.daemon = True
		procesar.start()

		while True:
			msg = input('SALIR = Q\n').upper()
			if msg == 'Q':
				print("**** TALOGOOO *****")
				self.sock.close()
				sys.exit()
			else:
				pass

	def broadcast(self, msg, cliente):
		for c in self.clientes:
			try:
				if c != cliente:
					c.send(msg)
			except:
				self.clientes.remove(c)

	def aceptarC(self):
		while True:
			try:
				conn, addr = self.sock.accept()
				print(f"\nConexion aceptada via {conn}\n")
				conn.setblocking(False)
				self.clientes.append(conn)
			except:
				pass

	def procesarC(self):
		print("Procesamiento de mensajes iniciado")
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						data = c.recv(128)
						if data:
							########################################
							############ EJERCICIO C ###############
							a = pickle.loads(data)
							print(a[0] + " -- " + a[1] + " -- " + a[2])
					except:
						pass


s = Servidor()
