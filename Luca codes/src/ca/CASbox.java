package ca;

/**
 * Class containing methods to build the S-box defined by a CA.
 * 
 * @author Luca Mariot
 */

import boolfun.BinTools;

public class CASbox {
    
    /**
     * Build the Sbox corresponding to a CA with periodic boundary conditions
     * 
     * @param ca    a OneDimCellAut object
     * @return      a boolean matrix representing the S-box of the CA global rule
     *              applied with periodic boundary conditions.
     */
    public static boolean[][] buildSboxPeriodicCA(OneDimCellAut ca) {
       
       //Initialize the parameters related to the s-box
       int nvar = ca.getCells().length;                 //number of input/output variables
       int tlength = (int)Math.pow(2, nvar);            //length of the truth table of the S-box
       boolean[][] sbox = new boolean[tlength][nvar];   //boolean matrix representing the CA S-box
       
       //Main cycle: loop over all possible input vectors of the CA and compute
       //the global rule with periodic boundary conditions
       for(int i=0; i<tlength; i++) {
           
           //Initialize the CA to the configuration indexed by i
           boolean[] init = BinTools.dec2BinMod(i, nvar);
           ca.setCells(init);
           
           //Evolve the CA with periodic boundary conditions and copy the output configuration in the sbox
           ca.nextConfigPeriodic();
           System.arraycopy(ca.getCells(), 0, sbox[i], 0, sbox[i].length);
           
       }

       return sbox;
        
    }
    
    /**
     * Build the Sbox corresponding to a CA with no boundary conditions
     * 
     * @param ca    a OneDimCellAut object
     * @return      a boolean matrix representing the S-box of the CA global rule
     *              applied with periodic boundary conditions.
     */
    public static boolean[][] buildSboxCANoBound(OneDimCellAut ca) {
       
       //Initialize the parameters related to the S-box
       int nvar = ca.getCells().length;                     //number of input variables
       int outlength = nvar - ca.getNbr() + 1;              //number of output variables
       int tlength = (int)Math.pow(2, nvar);                //length of the Sbox truth table
       boolean[][] sbox = new boolean[tlength][outlength];  //boolean matrix representing the S-box
       
       //Main cycle: loop over all possible input vectors of the CA and compute
       //the global rule with periodic boundary conditions
       for(int i=0; i<tlength; i++) {
           
           //Initialize the CA to the configuration indexed by i
           boolean[] init = BinTools.dec2BinMod(i, nvar);
           ca.setCells(init);
           
           //Evolve the CA with no boundary conditions and copy the output to the sbox
           ca.nextConfigNoBound();
           System.arraycopy(ca.getCells(), 0, sbox[i], 0, sbox[i].length);
           
       }
       
       return sbox;
        
    }
    
}
