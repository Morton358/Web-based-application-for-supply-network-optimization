import math
import mathModel
import prepareDataLINDO


lowerBoundsoBB = []
upperBoundsoBB = []
lowerBoundsoBB.extend(0 for i in range((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)))
upperBoundsoBB.extend(1000000 for i in range((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)))

print(lowerBoundsoBB, "\n", upperBoundsoBB)
flat_matrixOfDecisionVariables = [item for sublist in prepareDataLINDO.matrixOfDecisionVariables for item in sublist]
print('Flat matrix: ', flat_matrixOfDecisionVariables)
