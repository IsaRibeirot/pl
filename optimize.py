import gurobipy as gp
from gurobipy import GRB
import csv, sys, re

try:
    # Define vars
    vars = {}
    try:
        maximize = True if sys.argv[1] == "max" else False
    except:
        maximize = False

    # Create a new model
    m = gp.Model("cervejaria")
    
    # Create variables and objective function
    with open('data/distancias.csv', 'r') as csvfile:
        lines = list(csv.reader(csvfile, delimiter=','))

        # Add variables
        for i in range(1,len(lines)):
            for j in range(1,len(lines[i])):
                vars["x" + str(i) + str(j)] = m.addVar(vtype=GRB.INTEGER, name="x" + str(i) + str(j))
                #print("x" + str(i) + str(j))

        # Define objective 
        obj = gp.LinExpr()
        for i,row in enumerate(lines):
            if i == 0: continue
            for j,col in enumerate(row):
                if j == 0: continue
                obj += vars["x" + str(i) + str(j)] * int(col)

        print(obj)
        m.setObjective(obj, GRB.MAXIMIZE if maximize else GRB.MINIMIZE)

    # Add constraints
    with open('data/restricoes.txt', 'r') as f:
        for n,line in enumerate(f):
            exp = gp.LinExpr()
            line = line.strip().split(' ')

            last = line[-1]
            line = line[:-1]

            comp = line[-1]
            line = line[:-1]

            for i in line:
                if i == "+": continue
                j = i.split('*')
                if len(j) == 1:
                    exp += vars[j[0]]
                else:
                    exp += int(j[0]) * vars[j[1]]

            if (comp == "<="):
                m.addConstr(exp <= int(last))
            elif (comp == ">="):
                m.addConstr(exp >= int(last))
            elif (comp == ">"):
                m.addConstr(exp > int(last))
            elif (comp == "<"):
                m.addConstr(exp < int(last))
            elif (comp == "!="):
                m.addConstr(exp != int(last))
            elif (comp == "=="):
                m.addConstr(exp == int(last))
            else:
                print("Invalid constraint")

    # Optimize model
    m.optimize()

    for v in m.getVars():
        print("%s %g" % (v.varName, v.x))
        
    print("Obj: %g" % m.objVal)

except gp.GurobiError as e:
    print("Error code" + str(e.errno) + ": " + str(e))
except AttributeError:
    print("Encountered an attribute error")
