#/bin/bash

popName[0]="www.pop-ac.rnp.br"
popName[1]="www.pop-al.rnp.br"
popName[2]="www.pop-am.rnp.br"
popName[3]="www.pop-ap.rnp.br"
popName[4]="www.pop-ba.rnp.br"
popName[5]="www.pop-ce.rnp.br"
popName[6]="www.pop-df.rnp.br"
popName[7]="www.pop-es.rnp.br"
popName[8]="www.pop-go.rnp.br"
popName[9]="www.pop-ma.rnp.br"
popName[10]="www.pop-mg.rnp.br"
popName[11]="www.pop-ms.rnp.br"
popName[12]="www.pop-mt.rnp.br"
popName[13]="www.pop-pa.rnp.br"
popName[14]="www.pop-pb.rnp.br"
popName[15]="www.pop-pe.rnp.br"
popName[16]="www.pop-pi.rnp.br"
popName[17]="www.pop-pr.rnp.br"
popName[18]="master.uerj.br"
popName[19]="www.pop-rn.rnp.br"
popName[20]="www.pop-ro.rnp.br"
popName[21]="www.pop-rr.rnp.br"
popName[22]="www.pop-rs.rnp.br"
popName[23]="www.pop-sc.rnp.br"
popName[24]="www.pop-se.rnp.br"
popName[25]="www.pop-sp.rnp.br"
popName[26]="www.pop-to.rnp.br"

while true
do
	for i in {0..26}
	do
		echo ""
		echo $i
		pop=${popName[$i]}
		pop_file="./pops/"${popName[$i]}".txt"

		echo $pop
		echo $pop_file

		date >> $pop_file
		sudo traceroute -T $pop >> $pop_file

		echo ""
	done

	sleep 600
done

exit 0
