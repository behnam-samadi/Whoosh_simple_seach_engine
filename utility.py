def precision_recall(results, ground_truth):
	if len(results) ==0:
	    return(0,0)
	number_of_hits = 0
	for result in results:
	    
	    if result in ground_truth:
	        number_of_hits +=1
	precision = float(number_of_hits) / len(results)
	recall =    float(number_of_hits) / len(ground_truth)
	return(precision,recall)
