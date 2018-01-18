# -*- coding: utf-8 -*-
import prepareDataLINDO
from pyLindo import *
import time


#\\\\\\\\\\\\\\\\\\\\\\\\
# for measure time of compilation
#////////////////////////
start_time = time.time()

# \\\\\\\\\\\\\\
# model data
#//////////////

nCons = prepareDataLINDO.countOfConstraints # count of constrains
nVars = prepareDataLINDO.countOfDesitionVariables # count of decision variables
nDir = 1 # direction 1 - it`s minimisation of function fit
dObjConst = 0.0 # constant term in the objective function
adC = N.array(prepareDataLINDO.constantsOfFunctionFit, dtype=N.double) # coficients of variables in function fit
adB = N.array(prepareDataLINDO.allConstsOfConstraints, dtype=N.double) # constant on the right hand
# of constrain expressions
acConTypes = N.array(prepareDataLINDO.signsOfConstrainExpressions, dtype=N.character) # signs of the
# constrain expressions
nNZ = len(prepareDataLINDO.nonZeroCoeficients)  # the number of nonzero coefficients in the constraint matrix
anBegCol = N.array(prepareDataLINDO.columnStartIndices, dtype=N.int32) # column-start indices
pnLenCol = N.asarray(None) # if no blanks are been lefy in matrix = None
adA = N.array(prepareDataLINDO.nonZeroCoeficients, dtype=N.double) # nonzero coefficients
anRowX = N.array(prepareDataLINDO.rowIndices, dtype=N.int32) # row indices
pdLower = N.array(prepareDataLINDO.lowerBounds, dtype=N.double) # lower bounds for desition variables
pdUpper = N.array(prepareDataLINDO.upperBounds, dtype=N.double) # upper bounds for desition variables
pachVarType = N.array(prepareDataLINDO.pointersToCharacters,dtype=N.character) # A pointer to a character vector
# containing the type of each variable (‘C’, ‘B’, ‘I’, or ‘S’ for continuous, binary, general integer or semi-continuous, respectively.)

print("\nnCons", nCons, "\nnVars", nVars, "\nnDir", nDir, "\ndObjCons", dObjConst, "\nlen adC", len(adC), "\nadC",
      adC, "\nlen adB", len(adB),"\nadB", adB, "\nlen acConTypes", len(acConTypes), "\nacConTypes", acConTypes)
print("\nnNZ", nNZ, "\nlen anBegCol", len(anBegCol), "\nanBegCol", anBegCol, "\npnLenCol", pnLenCol, "\nlen adA",
      len(adA), "\nadA", adA, "\nlen anRowX", len(anRowX), "\nanRowX", anRowX, "\nlen pdLower", len(pdLower),
      "\npdLower", pdLower, "\nlen pdUpper", len(pdUpper), "\npdUpper", pdUpper)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#create LINDO environment and model objects
#//////////////////////////////////////////
LicenseKey = N.array('', dtype='S1024')
lindo.pyLSloadLicenseString('/home/morton/lindoapi/license/lndapi110.lic',
                            LicenseKey)
pnErrorCode = N.array([-1], dtype=N.int32) # A reference to an integer to return the error code
pEnv = lindo.pyLScreateEnv(pnErrorCode, LicenseKey)

pModel = lindo.pyLScreateModel(pEnv, pnErrorCode)

geterrormessage(pEnv, pnErrorCode[0])

#pszFname = "/home/morton/My_Files/Politechnika_Wroclawska/DYPLOM/Program/LINDO/input.mps"



#\\\\\\\\\\\\\\\\\\\\\\\\\
#load data into the model
#/////////////////////////
print("Loading LP data...")
errorcode = lindo.pyLSloadLPData(pModel, nCons, nVars, nDir, dObjConst, adC, adB, acConTypes, nNZ, anBegCol, pnLenCol,
                                 adA, anRowX, pdLower, pdUpper)
geterrormessage(pEnv, errorcode)

errorcode = lindo.pyLSloadVarType(pModel, pachVarType) # When use pachVarType (for example in MIP problem)

lindo.pyLSwriteMPSFile(pModel, "something.mps", 0)

#\\\\\\\\\\\\\\\
#solve the model
#///////////////
print("Solving the model...")
pnStatus = N.array([-1], dtype=N.int32)
#errorcode = lindo.pyLSoptimize(pModel, LSconst.LS_METHOD_FREE, pnStatus)
errorcode = lindo.pyLSsolveMIP(pModel,pnStatus)
geterrormessage(pEnv, errorcode)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#retrieve the objective value
#//////////////////////////////
dObj = N.array([-1.0], dtype=N.double)
#errorcode = lindo.pyLSgetInfo(pModel, LSconst.LS_DINFO_POBJ, dObj)
errorcode = lindo.pyLSgetInfo(pModel,LSconst.LS_DINFO_MIP_OBJ,dObj)
geterrormessage(pEnv, errorcode)
print("Objective is: %.5f" % dObj[0])
print("")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#retrieve the primal solution
#/////////////////////////////
padPrimal = N.empty((nVars), dtype=N.double)
#errorcode = lindo.pyLSgetPrimalSolution(pModel, padPrimal)
errorcode = lindo.pyLSgetMIPPrimalSolution(pModel,padPrimal)
geterrormessage(pEnv, errorcode)
print("Primal solution is: ")
for x in padPrimal:
    print("%.5f" % x)


#delete LINDO model pointer
errorcode = lindo.pyLSdeleteModel(pModel)
geterrormessage(pEnv, errorcode)

#delete LINDO environment pointer
errorcode = lindo.pyLSdeleteEnv(pEnv)
geterrormessage(pEnv, errorcode)

#show time of execution
print("--- %s seconds ---" % (time.time() - start_time))
