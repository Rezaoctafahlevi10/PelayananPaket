class PriorityQueue(object):
	def __init__(self):
		self.queue = [] #buat menmapung data 


	def isEmpty(self): #buat menghapus semua data nya
		return len(self.queue) == 0 

	def insert(self, data): #buat nenambahkan data nya
		self.queue.append(data)

	def delete(self): #menghapus data nya
		try:
			min_val = 0
			for i in range(len(self.queue)): #buat mencari nilai terkecil dalam piority quue buat tahu yang mana lebih diprioritaskan
				if  self.queue  [i] < self.queue[min_val]: #1,2,3,0,3 < [min val] ==> jadi min val indeks ke 0 ini sama dengan 1
					min_val = i  # 1 < 1 (tidak memenuhi diskio kembali ke for lop)
			item = self.queue[min_val] 
			del self.queue[min_val] #buat penghapusan data dgn value terkecil
			return item
		except IndexError:
			print()
			exit()