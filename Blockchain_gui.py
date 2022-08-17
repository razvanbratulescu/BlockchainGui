import time
import hashlib
import tkinter as tk

class Block:
	def __init__(self , data , prev_hash , height , timestamp = None):
		self.prev_hash = prev_hash
		self.height = height
		self.data = data
		self.timestamp = timestamp or time.time()
		self.hash = self.calculate_hash()

	def calculate_hash(self):
		strr = "{}{}{}".format(self.prev_hash , self.height , self.data )
		return hashlib.sha256(strr.encode()).hexdigest()

class Blockchain:

	def __init__(self):
		self.chain = []
		self.curr_data = {}
		self.create_genesis()

	def create_genesis(self):
		self.curr_data = {"0" : "The first Block of the chain"}
		self.Create_Block("0")

	def Create_Block(self , prev_hash = None):
		blk = Block(  self.curr_data , prev_hash or self.get_last_block().hash , len(self.chain))
		self.chain.append(blk)
		self.curr_data = {}
		return blk

	def get_last_block(self):
		return self.chain[-1]

	def add_data(self):


		def add_more():
			idd = id_field.get()
			rec = rec_field.get()
			self.curr_data[idd] = rec #self.curr_data[int(idd)] = rec
			id_field.delete(0 , len(idd))
			rec_field.delete(0 , len(rec))
			tk.Label(win2 , text = "Record Added").grid()


		def add_block():
			self.Create_Block()
			tk.Label(win2 , text = "Block Added").grid()


		win2 = tk.Toplevel(win)
		win2.title("Add Data")
		win2.geometry("300x200")
		tk.Label(win2 , text = "You can add upto 5 Records perBlock..").grid(row = 0 , column = 0 , columnspan = 3)
		id_b = tk.Label(win2 , text = "Enter Name: ")
		id_b.grid(row = 1 , column = 0 , stick = tk.W)
		id_field = tk.Entry(win2)
		id_field.grid(row = 1 , column = 1 , stick = tk.W)

		rec_b = tk.Label(win2 , text = "Enter The Data: ")
		rec_b.grid(row = 2 , column = 0 , stick = tk.W)
		rec_field = tk.Entry(win2)
		rec_field.grid(row = 2 , column = 1 , stick = tk.W)
		
		add_b = tk.Button(win2 , text = "Add More" , command = add_more).grid(row = 3 , column = 1, pady = 10 , padx = 5 ,  sticky = tk.E , columnspan = 2)
		done_b = tk.Button(win2 , text = "Done" , command = add_block).grid(row = 3 , column = 1 , pady = 10 , padx = 5 , stick = tk.W ,  columnspan = 2)
		tk.Button(win2 , text = "GO BACK" , command = win2.destroy).grid(row = 4 , column = 1,)

		win2.mainloop()

		
	def disp_chain(self):
		win2 = tk.Toplevel(win)
		win2.title("Display All Data")
		win2.geometry("400x300")
		cnt = 0
		for x in self.chain:
			tk.Label(win2 , text = "Block "+str(cnt) + ": " + str(x.data)).pack()
			cnt+=1
		tk.Button(win2 , text = "GO BACK" , command = win2.destroy).pack()
		win2.mainloop()


	def see_records(self):

		def search():
			idd = int(id_field.get())
			disp_data = []
			for x in self.chain:
				if x.data.get(idd) is not None:
					disp_data.append(x.data.get(idd))
			
			if(len(disp_data) == 0):
				tk.Label(win2 , text = "The given id could not be found.").pack()
			else:
				tk.Label(win2 , text = "Here are the medical records of ID: " + str(idd)).pack()
				for x in disp_data:
					tk.Label(win2 , text = x).pack()

		win2 = tk.Toplevel(win)
		win2.title("See Records")
		win2.geometry("400x300")

		tk.Label(win2 , text = "Enter the Name").pack()
		id_field = tk.Entry(win2)
		id_field.pack()
		idd = tk.Button(win2 , text = "Search" , command = search  ).pack()
		tk.Button(win2 , text = "GO BACK" , command = win2.destroy).pack()
		win2.mainloop()

		
	def see_blocks(self):

		win2 = tk.Toplevel(win)
		win2.title("Block Details")
		win2.geometry("500x300")
		for x in reversed(self.chain):
			tk.Label(win2 , text = "Height: " + str(x.height)).pack()
			tk.Label(win2 , text = "Prev Hash: " + str(x.prev_hash)).pack()
			tk.Label(win2 , text = "Data in the Block: " + str(x.data)).pack()
			tk.Label(win2 , text = "Hash: " + str(x.hash)).pack()
			tk.Label(win2 , text = "Creation Time: " + str(x.timestamp)).pack()

		tk.Button(win2 , text = "GO BACK" , command = win2.destroy).pack()
		win2.mainloop()


bc = Blockchain()
win = tk.Tk()
win.title("SWAM")
win.geometry("400x300")

tk.Label(win , text = "Internet of Things").pack(pady = 5)
tk.Button(win , text = "Add Data" , command = bc.add_data).pack()
tk.Button(win , text = "Display All Data" , command = bc.disp_chain).pack(pady = 5)
tk.Button(win , text = "Display Specific Records" , command = bc.see_records).pack()
tk.Button(win , text = "To see the Chain" , command = bc.see_blocks).pack(pady = 5)
tk.Button(win , text = "Exit" , command = win.destroy).pack()

win.mainloop()

