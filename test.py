import gurobipy as gp
from gurobipy import GRB

try:
    # Create a new model
    m = gp.Model("cervejaria")
    
    # Create variables
    x11 = m.addVar(vtype=GRB.INTEGER, name="x11")
    x12 = m.addVar(vtype=GRB.INTEGER, name="x12")
    x13 = m.addVar(vtype=GRB.INTEGER, name="x13")
    x14 = m.addVar(vtype=GRB.INTEGER, name="x14")
    x15 = m.addVar(vtype=GRB.INTEGER, name="x15")

    x21 = m.addVar(vtype=GRB.INTEGER, name="x21")
    x22 = m.addVar(vtype=GRB.INTEGER, name="x22")
    x23 = m.addVar(vtype=GRB.INTEGER, name="x23")
    x24 = m.addVar(vtype=GRB.INTEGER, name="x24")
    x25 = m.addVar(vtype=GRB.INTEGER, name="x25")

    x31 = m.addVar(vtype=GRB.INTEGER, name="x31")
    x32 = m.addVar(vtype=GRB.INTEGER, name="x32")
    x33 = m.addVar(vtype=GRB.INTEGER, name="x33")
    x34 = m.addVar(vtype=GRB.INTEGER, name="x34")
    x35 = m.addVar(vtype=GRB.INTEGER, name="x35")

    x41 = m.addVar(vtype=GRB.INTEGER, name="x41")
    x42 = m.addVar(vtype=GRB.INTEGER, name="x42")
    x43 = m.addVar(vtype=GRB.INTEGER, name="x43")
    x44 = m.addVar(vtype=GRB.INTEGER, name="x44")
    x45 = m.addVar(vtype=GRB.INTEGER, name="x45")

    x51 = m.addVar(vtype=GRB.INTEGER, name="x51")
    x52 = m.addVar(vtype=GRB.INTEGER, name="x52")
    x53 = m.addVar(vtype=GRB.INTEGER, name="x53")
    x54 = m.addVar(vtype=GRB.INTEGER, name="x54")
    x55 = m.addVar(vtype=GRB.INTEGER, name="x55")

    x61 = m.addVar(vtype=GRB.INTEGER, name="x61")
    x62 = m.addVar(vtype=GRB.INTEGER, name="x62")
    x63 = m.addVar(vtype=GRB.INTEGER, name="x63")
    x64 = m.addVar(vtype=GRB.INTEGER, name="x64")
    x65 = m.addVar(vtype=GRB.INTEGER, name="x65")

    x71 = m.addVar(vtype=GRB.INTEGER, name="x71")
    x72 = m.addVar(vtype=GRB.INTEGER, name="x72")
    x73 = m.addVar(vtype=GRB.INTEGER, name="x73")
    x74 = m.addVar(vtype=GRB.INTEGER, name="x74")
    x75 = m.addVar(vtype=GRB.INTEGER, name="x75")

    x81 = m.addVar(vtype=GRB.INTEGER, name="x81")
    x82 = m.addVar(vtype=GRB.INTEGER, name="x82")
    x83 = m.addVar(vtype=GRB.INTEGER, name="x83")
    x84 = m.addVar(vtype=GRB.INTEGER, name="x84")
    x85 = m.addVar(vtype=GRB.INTEGER, name="x85")
    
    # Set objective
    m.setObjective(x11 + 5 * x12 + 500 * x13 + 200 * x14 + 700 * x15 + x21 + 5 * x22 + 500 * x23 + 200 * x24 + 700 * x25 + x31 + 5 * x32 + 500 * x33 + 200 * x34 + 700 * x35 + x41 + 5 * x42 + 500 * x43 + 200 * x44 + 700 * x45 + x51 + 5 * x52 + 500 * x53 + 200 * x54 + 700 * x55 + 1 * x61 + 5 * x62 + 500 * x63 + 200 * x64 + 700 * x65 + x71 + 5 * x72 + 500 * x73 + 200 * x74 + 700 * x75 + x81 + 5 * x82 + 500 * x83 + 200 * x84 + 700 * x85, GRB.MINIMIZE)
    
    # Add constraints (fontes):
    m.addConstr(x11 + x12 + x13 + x14 + x15 <= 1000, "Fonte1")
    m.addConstr(x21 + x22 + x23 + x24 + x25 <= 1000, "Fonte2")
    m.addConstr(x31 + x32 + x33 + x34 + x35 <= 1000, "Fonte3")
    m.addConstr(x41 + x42 + x43 + x44 + x45 <= 1000, "Fonte4")
    m.addConstr(x51 + x52 + x53 + x54 + x55 <= 500, "Fonte5")
    m.addConstr(x61 + x62 + x63 + x64 + x65 <= 500, "Fonte6")
    m.addConstr(x71 + x72 + x73 + x74 + x75 <= 500, "Fonte7")
    m.addConstr(x81 + x82 + x83 + x84 + x85 <= 500, "Fonte8")

    # Add constraints (destinos):
    m.addConstr(x11 + x21 + x31 + x41 + x51 + x61 + x71 + x81 == 1500, "c0")
    m.addConstr(x12 + x22 + x32 + x42 + x52 + x62 + x72 + x82 == 1500, "c1")
    m.addConstr(x13 + x23 + x33 + x43 + x53 + x63 + x73 + x83 == 1800, "c2")
    m.addConstr(x14 + x24 + x34 + x44 + x54 + x64 + x74 + x84 == 1080, "c3")
    m.addConstr(x15 + x25 + x35 + x45 + x55 + x65 + x75 + x85 == 120, "c4")

    # Relaxa o modelo
    # m.computeIIS()
    # m.feasRelaxS(0, True, False, True)

    # Optimize model
    m.optimize()

    for v in m.getVars():
        print("%s %g" % (v.varName, v.x))
        
    print("Obj: %g" % m.objVal)

except gp.GurobiError as e:
    print("Error code" + str(e.errno) + ": " + str(e))
except AttributeError:
    print("Encountered an attribute error")
