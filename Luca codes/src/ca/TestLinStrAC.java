package ca;

import java.math.BigInteger;

import boolfun.BinTools;
import boolfun.BoolTransf;
import boolfun.BooleanFunction;
import boolfun.CheckProp;
import boolfun.CombTools;
import boolfun.SboxTools;

/**                                                                             
 * Checks the number of linear structures of the all ones component functions   
 * of the functions obtained applying the construction                          
 *                                                                                                                                        
 */ 
public class TestLinStrAC {

	public static void main(String args[]) {                                    
        
        if(args.length != 3) {                                                  
            System.err.println("\nUsage:");                                     
            System.err.println("java boolfun.TestLinearStructures boolfun nvar maxCells");
            System.exit(1);                                                     
        }                                                                       
                                                                                
        //parse arguments                                                       
        BigInteger rulenum = new BigInteger(args[0]);                                
        int nvar = Integer.parseInt(args[1]);                                                               
        int maxCells = Integer.parseInt(args[2]);
        //boolean periodic = Boolean.parseBoolean(args[3]);
        
        //output
        int lenRow = (maxCells - nvar) + 2;                                 
        String[] output = new String[lenRow];                                   
                                                                
        int tlength = (int) Math.pow(2, nvar);
        int nrules = (int) Math.pow(2, tlength);
        boolean[] ttable = BinTools.dec2Bin(rulenum, tlength);
        BooleanFunction boolfun = new BooleanFunction(ttable, nvar);
        boolean[] ruletable = boolfun.getTtable();
        String binrule = BinTools.bool2Bin(ruletable);
        
        CheckProp.computeANF(boolfun);
        CheckProp.computeNlin(boolfun);
                                           
        boolean[][] sbox = null;
        
        output[0] = args[0];  
        int outInd = 1;
        
        //loop on different AC dimensions                                       
        for(int i = nvar; i <= maxCells; i++) {                                        
            
        	OneDimCellAut ca = new OneDimCellAut(i, ruletable, nvar);
        	sbox = CASbox.buildSboxCANoBound(ca);
        	
        	//all ones component function
        	int m = sbox[0].length;
        	int ncomp = (int) Math.pow(2, m) - 1;
        	boolean[] curcomp = BinTools.dec2BinMod(ncomp, m);
        	boolean[] compfunc = SboxTools.calcComponent(i, sbox, curcomp);
        	
        	BooleanFunction compfuncBF = new BooleanFunction(compfunc, i);
        	
        	// FWT attributes
        	int[] whcoeffs = new int[compfuncBF.getNinputs()];
        	int[] poltable = compfuncBF.getPoltable();
        	System.arraycopy(poltable, 0, whcoeffs, 0, whcoeffs.length);
        	int sprad = BoolTransf.calcFWT(whcoeffs, 0, whcoeffs.length);
        	compfuncBF.setWhcoeffs(whcoeffs);
        	compfuncBF.setSprad(sprad);
        	
        	// autocorrelation function
        	int[] accoeffs = new int[compfuncBF.getNinputs()];
        	System.arraycopy(whcoeffs, 0, accoeffs, 0, accoeffs.length);
        	int acmax = BoolTransf.calcAC(accoeffs, true);
        	
            int ls = -1;
            for(int j = 0; j < accoeffs.length; j++) {
            	if(Math.abs(accoeffs[j]) == Math.pow(2, i)) {
            		ls++;
            	}
            }
            output[outInd] = Integer.toString(ls);
            outInd += 1;
        }                                                                       
                                                                                
        for(int i = 0; i < lenRow; i++) {                                       
            System.out.print(output[i] + " ");                                                                                 
        }
        System.out.println();
    }
}
