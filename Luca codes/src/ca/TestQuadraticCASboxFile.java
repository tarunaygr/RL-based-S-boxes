package ca;

/**
 * Test the construction from a set of rules described in a file
 * 
 * @author Luca Mariot
 */

import boolfun.*;
import java.io.*;
import java.util.Scanner;
import java.math.BigInteger;

public class TestQuadraticCASboxFile {
    
    public static void main(String[] args) {
        
        if(args.length != 5) {
            
            System.err.println("\nUsage: java ca.TestCASboxFile rulefile diameter minlength maxlength periodic");
            System.err.println("\nwhere:\n");
            System.err.println("- rulefile is the name of the file containing the rules to be tested");
            System.err.println("- diameter is the number of variables of the CA local rule");
            System.err.println("- minlength is the minimum number of input cells in the CA to test");
            System.err.println("- maxlength is the maximum number of input cells in the CA to test");
            System.err.println("- periodic is a boolean flag specifying whether the CA has periodic "
                    + "boundary conditions (true) or no boundary conditions (false)");
            System.err.println("\nNOTICE: the local rule is always applied with offset 0. Hence, each cell"
                    + " looks at itself and the diameter-1 cells to its right to compute the local rule");
            System.err.println("\nExample: java ca.TestQuadraticCASbox rulefile.txt 3 3 5 false");
            System.err.println("\nThe above command will loop over all rules contained in rulefile.txt of 3 variables (i.e., elementary "
                    + "local rules) and for each of them will generate the 3x1, 4x2 and 5x3 Sboxes corresponding "
                    + "to the no boundary CA with 3, 4, and 5 input cells.\n");
            System.exit(1);
            
        }
        
        //Read command-line parameters
        File filename = new File(args[0]);
        int nvar = Integer.parseInt(args[1]);
        int mincells = Integer.parseInt(args[2]);
        int maxcells = Integer.parseInt(args[3]);
        boolean periodic = Boolean.parseBoolean(args[4]);
        
        //Derived parameters: truth table length
        int tlength = (int)Math.pow(2, nvar);
        
        //Print initial info
        System.out.println("File name: "+args[0]);
        System.out.println("Local rule diameter: "+nvar);
        System.out.println("Range of CA lengths: "+mincells+" - "+maxcells);
        System.out.println("Periodic boundary conditions: "+periodic+ "\n");
        
        //Initialize array of quadratic bounds
        System.out.println("Quadratic bound values:");
        int[] bounds = new int[maxcells-mincells+1];
        for(int i=0; i<bounds.length; i++) {
            int r = 0;
            if((nvar+i+1)%2 == 0) {
                r = (nvar+i+1)/2;
            } else {
                r = (nvar+i+2)/2;
            }
            
            int sprad = (int)Math.pow(2, r);
            int nlbound = BoolTransf.calcNL(sprad, nvar+i);
            bounds[i] = nlbound;
            System.out.println("n = "+(nvar+i)+" r = "+r+" quadratic bound: "+bounds[i]);
        }
        
        System.out.println("");
        
        try {
            
            Scanner sc = new Scanner(filename);
            
            while(sc.hasNext()) {
                
                String text = sc.next();
                BigInteger funcnum = new BigInteger(text);
                
                //Instatiate the boolean function of the local rule
                BooleanFunction boolfun = new BooleanFunction(funcnum,nvar);
                boolean[] ruletable = boolfun.getTtable();
                String binrule = BinTools.bool2Bin(ruletable);
                boolean[][] sbox = null;   //Initialize the CA S-box

                //Compute the ANF and nonlinearity of the rule
                System.out.print("Rule "+funcnum+" - ANF: ");
                CheckProp.computeANF(boolfun);
                CheckProp.computeNlin(boolfun);
                CheckProp.printANF(boolfun);
                System.out.println(" Nonlinearity: "+boolfun.getNlin());

                //For each length between mincells and maxcells, compute the
                //corresponding S-box.
                boolean meetbound = true;
                int l=mincells;
                while(l<=maxcells && meetbound==true) {

                    //There are two cases: one for periodic boundary
                    //CA and the other for no boundary CA, depending on the flag periodic
                    if(periodic) { 

                        //Periodic boundary condition case

                        //Instantiate the CA
                        OneDimCellAut ca = new OneDimCellAut(l, ruletable, nvar);

                        //Build the S-box corresponding to the CA
                        sbox = CASbox.buildSboxPeriodicCA(ca);

                    }

                    else {

                        //No boundary conditions case

                        //Instantiate the CA
                        
                        OneDimCellAut ca = new OneDimCellAut(l, ruletable, nvar);

                        //Build the corresponding S-box and print it
                        sbox = CASbox.buildSboxCANoBound(ca);


                    }

                    //Print the S-box in decimal form
                    /*for(int k=0; k<sbox.length; k++) {

                        int value = BinTools.bin2Dec(sbox[k]);  //Each output vector is converted to int
                        System.out.print(value+" ");

                    }*/

                    //Compute the cryptographic properties of the S-box and print them
                    //System.out.println("\nBalanced: "+SboxTools.computeUnbalancedness(l, sbox));
                    //System.out.print("Nonlinearity: "+SboxTools.calcNlinSbox(sbox, l));
                    //System.out.println(" ; Delta-uniformity: "+SboxTools.computeDeltaUniformity(sbox, l));

                    //Compute all nontrivial component functions of the S-box, along
                    //with their nonlinearity, and print them
                    //System.out.println("\nComponent Functions:\n");
                    int m = sbox[0].length;
                    int ncomp = (int)Math.pow(2, m);
                    

                    /*for(int k = 1; k<ncomp; k++) {

                        boolean[] curcomp = BinTools.dec2BinMod(k, m);

                        //Compute the component function selected by curcomp and
                        //determine its nonlinearity
                        boolean[] compfunc = SboxTools.calcComponent(l, sbox, curcomp);
                        BooleanFunction bfcomp = new BooleanFunction(compfunc, l);
                        CheckProp.computeNlin(bfcomp);
                        boolean isBent = CheckProp.checkBent(bfcomp.getWhcoeffs(), bfcomp.getSprad());
                        boolean isPlat = CheckProp.checkPlateaued(bfcomp.getWhcoeffs(), bfcomp.getSprad());

                        System.out.print("Component "+BinTools.bool2Bin(curcomp)+" -- Wolfram Code "+
                                bfcomp.getDeccode()+": BENT: "+isBent+" -- PLAT: "
                                +isPlat+" -- NL:"+bfcomp.getNlin());
                        System.out.println("");

                    }*/
                    
                    //Check only the component with all 1s
                    boolean[] curcomp = BinTools.dec2BinMod(ncomp-1, m);
                    boolean[] compfunc = SboxTools.calcComponent(l, sbox, curcomp);
                    BooleanFunction bfcomp = new BooleanFunction(compfunc, l);
                    CheckProp.computeNlin(bfcomp);
                    boolean isBent = CheckProp.checkBent(bfcomp.getWhcoeffs(), bfcomp.getSprad());
                    boolean isPlat = CheckProp.checkPlateaued(bfcomp.getWhcoeffs(), bfcomp.getSprad());
                    boolean isBal = false;
                    if(bfcomp.getNlin() == bounds[l-mincells]) {
                        if(bfcomp.getWhcoeffs()[0]==0)
                            isBal=true;

                        if(periodic) {
                            System.out.print("Size "+l+" X "+l+": ");
                        } else {
                            System.out.print("Size "+l+" X "+(l-nvar+1)+": ");
                        }
                        System.out.print(" BAL: "+isBal+" BENT: "+isBent+" -- PLAT: "
                                    +isPlat+" -- NL: "+bfcomp.getNlin());
                            System.out.println("");

                        //System.out.println("\n********");
                        l++;
                    } else {
                        meetbound = false;
                    }
                
            
                }
                
            }
        
            
        } catch(IOException ioe) {
            System.err.println("I/O Error");
            System.exit(3);
        }
        
    }
    
}
