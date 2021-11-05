from my_or_tools import SolVal, ObjVal, newSolver


def ex1(N,a):
    s = newSolver ("Racao para gado")
    n_nutri = len(N)-1
    n_alim = len(N[0])
    
    Custo_alim = n_nutri
    
    alim = [s.NumVar(0,a,"")for i in range (n_alim)]
    
    P = s.NumVar(0.6*a,1.0*a,"")
    
    G = s.NumVar(0.0*a,0.6*a,"")
    
    F = s.NumVar(0.6*a,1.0*a,"")
    
    
    
    s.Add(s.Sum([alim[i] for i in range (n_alim)])==1)
    s.Add(s.Sum([0.01*a*N[0][j]*alim[j] for j in range(n_alim)])==P)
    s.Add(s.Sum([0.01*a*N[1][j]*alim[j] for j in range(n_alim)])==G)
    s.Add(s.Sum([0.01*a*N[2][j]*alim[j] for j in range(n_alim)])==F)
    
    custo = s.Sum([N[Custo_alim][i]*alim[i]for i in range(n_alim)])
    s.Minimize (custo)
    rc = s.Solve()
    return rc, ObjVal(s), SolVal(alim), SolVal(P), SolVal(G), SolVal(F)

def main():
    import sys
    import tableutils

    n=4
    m=4
    
    if len(sys.argv)<=1:
        print('Usage is main [table|run]')
        return
    a=1
    N = [[60,80,55,40],
        [50,70,40,100],
        [90,30,60,80],
        [200,150,100,75]]
    if sys.argv[1]=="table":
        N[n-4].inset(0,"% Proteina")
        N[n-3].inset(0,"% Gordura")
        N[n-2].inset(0,"% Fibra")
        N[n-1].inset(0, "Custo")
        N.insert(0,["Insumo","Aveia","Milho","Alfafa","Amendoim"])
        tableutils.printmat(N)
        
    elif sys.argv[1]=="run":
        rc,Value,alim,P,G,F = ex1(N,a)
        custo = round(Value,2)
        amendoim = [round(alim[3],3)]
        alfafa = [round(alim[2],3)]
        milho = [round(alim[1], 3)]   
        aveia = [round(alim[0],3)]
        print("Custo = "+ str(custo))
        print("Aveia = "+ str(aveia))
        print("Milho = "+ str(milho))
        print("Alfafa = "+ str(alfafa))
        print("Amendoim = "+ str(amendoim))
        
        


        
                
main()