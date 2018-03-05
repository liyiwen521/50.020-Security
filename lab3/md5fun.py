import hashlib
import random
import time

def getFileContent(filename):
	file = open(filename, mode = 'r', encoding = 'utf-8', newline = '\n')
	lines = []
	for line in file:
		if line.strip():
			lines.append(line.strip())
	return lines

def genFile(filename, content):
	file = open(filename, mode = 'w', encoding = 'utf-8', newline = '\n')
	file.write(content)
	return

def printList(list):
	out = ''
	for i in list:
		out += i + '\n'
	return out

### BRUTE-FORCE AND DICTIONARY ATTACK ###
words5 = getFileContent('words5.txt')
hash5 = getFileContent('hash5.txt')

def getPasswords(words, hashes):
	passwords = []
	for i in range (len(words)):
		hashed = hashlib.md5(words[i].encode('utf-8')).hexdigest()
		if hashed in hashes:
			passwords.append(words[i])
	return passwords

def getPasswordsBrute(hashes):
	characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
	lenChar = len(characters)
	passwords = []
	for c0 in range (0, lenChar):
		for c1 in range (0, lenChar):
			for c2 in range (0, lenChar):
				for c3 in range (0, lenChar):
					for c4 in range (0, lenChar):
						word = characters[c0] + characters[c1] + characters[c2] + characters[c3] + characters[c4]
						m = hashlib.md5(word.encode('utf-8')).hexdigest()
						if m in hashes:
							passwords.append(word)
							# print('found : ', word)
							if len(passwords) == 15:
								return passwords
	return passwords



def Part3():
	startTime = time.perf_counter()
	passwords = getPasswordsBrute(hash5)
	endTime = time.perf_counter()
	print(passwords)
	print('Elapsed time = ', endTime - startTime)
	genFile('pass5.txt', printList(passwords))
	return

### SALTING ###
def getSalt():
	characters = 'abcdefghijklmnopqrstuvwxyz'
	salt = characters[int (random.random() * 100) % len(characters)]
	return salt

def Part5():
	passwords = getFileContent('pass5.txt')
	passwordsWithSalt = []
	
	outPass6 = ''
	outSalted6 = ''

	for pw in passwords:
		salt = getSalt()
		passwordsWithSalt.append((pw, salt))
		newPassword = pw + salt
		
		outPass6 += newPassword + '\n'
		outSalted6 += hashlib.md5(newPassword.encode('utf-8')).hexdigest() + '\n'

	genFile('pass6.txt', outPass6)
	genFile('salted6.txt', outSalted6)


def Part6():
	hashesContent = getFileContent('hashes.txt')
	hashes = []
	difficulty = -1
	for line in hashesContent:
		if 'Weak' in line or 'Moderate' in line or 'Strong' in line:
			hashes.append([])
			difficulty += 1
			hashes[difficulty] = []
		else:
			print(difficulty)
			hashes[difficulty].append(line.split()[1])
	genFile('hashes_weak.txt', printList(hashes[0]))
	genFile('hashes_moderate.txt', printList(hashes[1]))
	genFile('hashes_strong.txt', printList(hashes[2]))

	return

# Part3()
Part5()
# Part6()


