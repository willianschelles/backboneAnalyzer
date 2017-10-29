import os
import re

fileNames = ["www.pop-ac.rnp.br","www.pop-al.rnp.br","www.pop-am.rnp.br","www.pop-ap.rnp.br","www.pop-ba.rnp.br","www.pop-ce.rnp.br","www.pop-df.rnp.br","www.pop-es.rnp.br","www.pop-go.rnp.br","www.pop-ma.rnp.br","www.pop-mg.rnp.br","www.pop-ms.rnp.br","www.pop-mt.rnp.br","www.pop-pa.rnp.br","www.pop-pb.rnp.br","www.pop-pe.rnp.br","www.pop-pi.rnp.br","www.pop-pr.rnp.br","master.uerj.br","www.pop-rn.rnp.br","www.pop-ro.rnp.br","www.pop-rr.rnp.br","www.pop-rs.rnp.br","www.pop-sc.rnp.br","www.pop-se.rnp.br","www.pop-sp.rnp.br","www.pop-to.rnp.br"]
countStates = 0
for fileName in fileNames:
	print fileName
	f = open("./pops/" + fileName + ".txt", "r")

	if countStates == 2:
		state = "am"
		regex = state + "\S*rnp"
	elif countStates == 17:
		countStates += 1
		print "pi ar"
		continue
	elif countStates == 18:
		state = "rj"
		regex = state + "\S*bkb"
	else:
		#pega em state a sigla do estado
		res = fileName.split('-')
		aux = res[1]
		stateAux = aux.split('.')
		state = stateAux[0]
		regex = state + "\S*bkb"
	#print regex

	#print f

	f.readline()

	for line in f:
		match = re.search(regex, line, 0)
		if match:
			dateRegex = "[0-9]{2}:[0-9]{2}:[0-9]{2}"
			print dateRegex
			DateMatch = re.match(dateRegex, line, 0)
			print DateMatch
			#DateMatch >> stateFile.txt
			#print "we done"
		else:
			print "Posto ipiranga"
		# print (num.start(),	num.end())

	countStates += 1
	# print ("count: %d", countStates)