#!/usr/bin/python

#Sidharth Bambah
#UID: 904 787 435
import locale, sys, string
from optparse import OptionParser

class file_compare:
	def __init__(self, file1, file2):
		try:
			if file1 == "-":
				f1 = sys.stdin
				f2 = open(file2, 'r')
			elif file2 == "-":
				f2 = sys.stdin
				f1 == open(file1, 'r')
			elif file1 == "-" and file2 == "-":
				print("Both files cannot be from standard input")
				exit()
			else:
				f1 = open(file1, 'r')
				f2 = open(file2, 'r')
			self.lines1 = f1.read().split('\n')
			self.lines2 = f2.read().split('\n')
			del self.lines1[len(self.lines1)-1]
			del self.lines2[len(self.lines2)-1]
			self.list1 = []
			self.list2 = []
			self.list3 = []
			f1.close()
			f2.close()
		except IOError as e:
			errno = e.errno
			strerror = e.strerror
			parser.error("I/O error({0}): {1}".format(errno, strerror))
	def insert_newline(self, file):
		for j in range(len(file)):
			if file[j] == '':
				file[j] = '\n'
			if file[j].count(' ') >= 1 and file[j].isspace():
				file[j] = '\n' * file[j].count(' ')
	def check_sort(self, file, file_num):
		for i in range(len(file) - 1):
			if locale.strcoll(file[i],file[i+1]) > 0:
				print ("The given file is not sorted")
				exit()
		return True

	def sorted_comparison(self):
		if self.check_sort(self.lines1, 1) and self.check_sort(self.lines2, 2):
			self.insert_newline(self.lines1)
			self.insert_newline(self.lines2)
			i = j = 0
			while i < len(self.lines1) and j < len(self.lines2):
				if self.lines1[i] == self.lines2[j]:
					self.list3.append(self.lines1[i])
					self.list1.append('	')
					self.list2.append('	')
					self.lines1[i] = ''
					self.lines2[j] = ''
					i += 1
					j += 1
				elif self.lines1[i] > self.lines2[j]:
					self.list2.append(self.lines2[j])
					self.list1.append('	')
					self.list3.append("")
					self.lines2[j] = ''
					j += 1
				elif self.lines1[i] < self.lines2[j]:
					self.list1.append(self.lines1[i])
					self.list2.append("")
					self.list3.append("")
					self.lines1[i] = ''
					i += 1
			if i > j:
				z = j
				while z != i:
					self.lines2[z] = "	" + self.lines2[z]
					z += 1
				more_spaces = [""] * len(self.lines2)
				self.list2 += self.lines2
				self.list1 += more_spaces
				self.list3 += more_spaces
			elif i < j:
				more_spaces = [""] * len(self.lines1)
				self.list1 += self.lines1
				self.list2 += more_spaces
				self.list3 += more_spaces

	def unsorted_comparison(self):
		self.insert_newline(self.lines1)
		self.insert_newline(self.lines2)
		for g in range(len(self.lines1)):
			for k in range(len(self.lines2)):
				if self.lines1[g] == self.lines2[k]:
					self.list3.append(self.lines1[g])
					self.list1.append('	')
					self.list2.append('	')
					del self.lines2[k]
					diff = False
					break
				else:
					diff = True
			if diff == True:
				self.list1.append(self.lines1[g])
				self.list2.append("")
				self.list3.append("")
		more_spaces = ['	'] * len(self.lines2)
		more_null = [""] * len(self.lines2)
		self.list1 += more_spaces
		self.list3 += more_null
		self.list2 += self.lines2
	def output(self, op1, op2, op3):
		if op1 == True:
			self.list1 = [''] * len(self.list1)
		if op2 == True:
			self.list2 = [''] * len(self.list2)
		if op3 == True:
			self.list3 = [''] * len(self.list3)
		true_list = []
		for i in range(len(self.list1)):
			true_list.append(self.list1[i] + self.list2[i] + self.list3[i])
		for j in range(len(true_list)):
			for k in range(len(true_list[j])):
				if true_list[j][k] != " ":
					if true_list[j][k] == "\n":
						str = true_list[j]
						for i in range(len(str)):
							if str[i] == "\n":
								sys.stdout.write(" ")
							else:
								sys.stdout.write(str[i])
						print('')
						break
					else:
						print(true_list[j])
						break

def main():
	version_msg = "%prog 0.0.0.1"
	usage_msg = """%prog [OPTION]... FILE1 FILE2"""
	locale.setlocale(locale.LC_ALL, 'C')
	
	parser = OptionParser(version=version_msg, usage=usage_msg)
	parser.add_option("-1", action="store_true", dest="opt1", default=False,
						help="supress column 1 of output")
	parser.add_option("-2", action="store_true", dest="opt2", default=False,
						help="supress column 2 of output")
	parser.add_option("-3", action ="store_true", dest="opt3", default=False,
						help="supress column 3 of output")
	parser.add_option("-u", action="store_true", dest="optu", default=False,
						help="allow unsorted files as inputs")
	options, args = parser.parse_args(sys.argv[1:])

	if len(args) != 2:
		parser.error("incorrect number of operands")
	
	try:
		opt1 = bool(options.opt1)
		opt2 = bool(options.opt2)
		opt3 = bool(options.opt3)
		optu = bool(options.optu)
	except:
		parser.error("invalid option type: {0}".format(options.opt1))

	file_1 = args[0]
	file_2 = args[1]
	try:
		comm = file_compare(file_1, file_2)
		if optu:
			comm.unsorted_comparison()
		else:
			comm.sorted_comparison()
		comm.output(opt1, opt2, opt3)
	except IOError as e:
		errno = e.errno
		strerror = e.strerror
		parser.error("I/O error({0}): {1}".format(errno, strerror))

if __name__ == "__main__":
	main()