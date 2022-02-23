/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ca;

import boolfun.BinTools;
import boolfun.BooleanFunction;
import boolfun.CheckProp;
import boolfun.SboxTools;
import java.math.BigInteger;

public class TestSingleCASbox {
    
    public static void main(String[] args) {
        
        if(args.length != 5) {
            
            System.err.println("\nUsage: java ca.TestGenerateSBoxAllCA diameter minlength maxlength periodic");
            System.err.println("\nwhere:\n");
            System.err.println("- diameter is the number of variables of the CA local rule");
            System.err.println("- rulenum is the Wolfram code of the local rule");
            System.err.println("- minlength is the minimum number of input cells in the CA to test");
            System.err.println("- maxlength is the maximum number of input cells in the CA to test");
            System.err.println("- periodic is a boolean flag specifying whether the CA has periodic "
                    + "boundary conditions (true) or no boundary conditions (false)");
            System.err.println("\nNOTICE: the local rule is always applied with offset 0. Hence, each cell"
                    + " looks at itself and the diameter-1 cells to its right to compute the local rule");
            System.err.println("\nExample: java ca.TestGenerateSBoxAllCA 3 3 5 false");
            System.err.println("\nThe above command will loop over all local rules of 3 variables (i.e., elementary "
                    + "local rules) and for each of them will generate the 3x1, 4x2 and 5x3 Sboxes corresponding "
                    + "to the no boundary CA with 3, 4, and 5 input cells.\n");
            System.exit(1);
            
        }
        
        //Read command-line parameters
        int nvar = Integer.parseInt(args[0]);
        BigInteger rulenum = new BigInteger(args[1]);
        int mincells = Integer.parseInt(args[2]);
        int maxcells = Integer.parseInt(args[3]);
        boolean periodic = Boolean.parseBoolean(args[4]);
        
        //Derived parameters: truth table length and number of local rules
        int tlength = (int)Math.pow(2, nvar);
        int nrules = (int)Math.pow(2,tlength);
            
        boolean[][] sbox = null;   //Initialize the CA S-box

        //Convert the decimal index (Wolfram code) in the truth table of the rule
        boolean[] ttable = BinTools.dec2Bin(rulenum, tlength);
        System.out.print("\n__________\n\nRule "+rulenum+" - Truth table: ");

        //Instatiate the boolean function of the local rule
        BooleanFunction boolfun = new BooleanFunction(ttable,nvar);
        boolean[] ruletable = boolfun.getTtable();
        String binrule = BinTools.bool2Bin(ruletable);

        //Compute the ANF and nonlinearity of the rule
        System.out.print(binrule+" - ANF: ");
        CheckProp.computeANF(boolfun);
        CheckProp.computeNlin(boolfun);
        CheckProp.printANF(boolfun);
        System.out.println(" Nonlinearity: "+boolfun.getNlin());

        //For each length between mincells and maxcells, compute the
        //corresponding S-box.
        for(int i=mincells; i<=maxcells; i++) {

            //There are two cases: one for periodic boundary
            //CA and the other for no boundary CA, depending on the flag periodic
            if(periodic) { 

                //Periodic boundary condition case

                //Instantiate the CA and print the size of the S-box
                System.out.print("\nSize "+i+" X "+i+": ");
                OneDimCellAut ca = new OneDimCellAut(i, ruletable, nvar);

                //Build the S-box corresponding to the CA
                sbox = CASbox.buildSboxPeriodicCA(ca);

            }

            else {

                //No boundary conditions case

                //Instantiate the CA
                System.out.print("\nSize "+i+" X "+(i-nvar+1)+": ");
                OneDimCellAut ca = new OneDimCellAut(i, ruletable, nvar);

                //Build the corresponding S-box and print it
                sbox = CASbox.buildSboxCANoBound(ca);


            }

            //Print the S-box in decimal form
            for(int j=0; j<sbox.length; j++) {

                int value = BinTools.bin2Dec(sbox[j]);  //Each output vector is converted to int
                System.out.print(value+" ");

            }

            //Compute the cryptographic properties of the S-box and print them
            System.out.println("\nBalanced: "+SboxTools.computeUnbalancedness(i, sbox));
            System.out.print("Nonlinearity: "+SboxTools.calcNlinSbox(sbox, i));
            //System.out.println(" ; Delta-uniformity: "+SboxTools.computeDeltaUniformity(sbox, i));

            //Compute all nontrivial component functions of the S-box, along
            //with their nonlinearity, and print them
            System.out.println("\nComponent Functions:\n");
            int m = sbox[0].length;
            int ncomp = (int)Math.pow(2, m);

            for(int k = 1; k<ncomp; k++) {

                boolean[] curcomp = BinTools.dec2BinMod(k, m);

                //Compute the component function selected by curcomp and
                //determine its nonlinearity
                boolean[] compfunc = SboxTools.calcComponent(i, sbox, curcomp);
                BooleanFunction bfcomp = new BooleanFunction(compfunc, i);
                CheckProp.computeNlin(bfcomp);
                boolean isBent = CheckProp.checkBent(bfcomp.getWhcoeffs(), bfcomp.getSprad());
                boolean isPlat = CheckProp.checkPlateaued(bfcomp.getWhcoeffs(), bfcomp.getSprad());

                System.out.print("Component "+k+": "+BinTools.bool2Bin(curcomp)+" -- Wolfram Code "+
                        bfcomp.getDeccode()+": BENT: "+isBent+" -- PLAT: "
                        +isPlat+" -- NL:"+bfcomp.getNlin());
                System.out.println("");

            }

            System.out.println("\n********");

        }
        
    }
    
}
