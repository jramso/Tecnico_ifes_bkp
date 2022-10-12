def listsum(listaA):
	if len(listaA)==1:
		return listaA[0]
	else:
		return listaA[0] + listsum(listaA[1:])