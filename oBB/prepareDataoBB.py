import math
import mathModel


lowerBoundsoBB = []
upperBoundsoBB = []
lowerBoundsoBB.extend(0 for i in range((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)))
upperBoundsoBB.extend(math.inf for i in range((mathModel.I * mathModel.R) + (mathModel.R * mathModel.E)))


