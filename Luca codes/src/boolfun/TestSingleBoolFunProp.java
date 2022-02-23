package boolfun;

/**
 * Tests various cryptographic properties of a boolean function passed as
 * command line argument and prints them.
 * 
 * @author Luca Mariot
 * @version 1.0
 */

import java.math.BigInteger;

public class TestSingleBoolFunProp {
    
    public static void main(String[] args) {
        
        //The arguments passed must be the function number (according to
        //Wolfram's convention) and the number of variables.
        if(args.length!= 2) {
            
            System.err.println("\nUsage: java boolfun.TestSingleBoolFunProp func_num nvar");
            System.err.println("\nwhere:");
            System.err.println("- func_num is the decimal encoding (Wolfram code) of the truth table of the boolean function");
            System.err.println("- nvar is the number of input variables of the boolean function");
            System.err.println("\nExample: java boolfun.TestSingleBoolFunProp 30 3");
            System.err.println("\nThe above command will print the cryptographic properties of the boolean function"
                    + "of 3 variables having Wolfram code 30 (i.e., Wolfram's rule 30)\n");
            
            System.exit(1);           
            
        }
        
        BigInteger funcnum = new BigInteger(args[0]);
        int nvar = Integer.parseInt(args[1]);
        
        //Creates the set of indices to check crypto properties.
        int[][] indices = new int[nvar][];
        for(int i=0; i<nvar; i++) {
            
            indices[i] = CombTools.genBinCombs(nvar-i-1, i+1);
            
        }
        
        //Instatiate the boolean function.
        BooleanFunction boolfun = new BooleanFunction(funcnum,nvar);
        
        //Compute the cryptographic properties.
        CheckProp.computeAllCryptoProp(boolfun, indices);
        
        //Print the tables and the properties of the function.
        CheckProp.printFuncNum(boolfun);
        CheckProp.printFuncTables(boolfun);
        System.out.println();
        CheckProp.printANF(boolfun);
        System.out.println();
        CheckProp.printPolynomial(boolfun);
        CheckProp.printCryptoProp(boolfun, nvar);
        
        System.out.println("");
        
    }
    
}
