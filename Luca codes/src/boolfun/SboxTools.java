package boolfun;

/**
 * Class containing methods to compute the cryptographic properties of S-boxes
 * 
 * @author Luca Mariot (luca.mariot@gmail.com)
 */

public class SboxTools {
    
    /**
     * Compute the component function of a S-box
     * 
     * @param nvar  number of variables of the component function
     * @param sbox  boolean matrix specifying the S-box
     * @param v     boolean vector specifying the component
     * @return      the truth table of the component function selected by v 
     */
    public static boolean[] calcComponent(int nvar, boolean[][] sbox, boolean[] v) {
        
        int complength = (int)Math.pow(2, nvar);
        boolean[] compfunc = new boolean[complength];
        
        //Build the truth table of the component function as the scalar product
        //of the s-box and the vector v
        for(int i = 0; i<complength; i++) {
            
            boolean[] sboxout = sbox[i];
            compfunc[i] = BinTools.scalarProduct(v, sboxout);
            
        }
        
        return compfunc;
        
    }
    
    /**
     * Compute the nonlinearity of a S-box as the minimum nonlinearity of its
     * component functions.
     * 
     * @param sbox      boolean matrix specifying the S-box
     * @param ncells    number of input cells in the S-box 
     * @return          an int number denoting the nonlinearity of the S-box
     */
    public static int calcNlinSbox(boolean[][] sbox, int ncells) {
        
        int minnlin = 0;
        int m = sbox[0].length;
        int ncomp = (int)Math.pow(2, m);
        
        for(int i=1; i<ncomp; i++) {
            
            boolean[] curcomp = BinTools.dec2BinMod(i, m);
            
            //Compute the component function selected by curcomp and
            //determine its nonlinearity
            boolean[] compfunc = calcComponent(ncells, sbox, curcomp);
            BooleanFunction bfcomp = new BooleanFunction(compfunc, ncells);
            CheckProp.computeNlin(bfcomp);
            
            //Update the minimum nonlinearity
            if(i==1) {
                minnlin = bfcomp.getNlin();
            } else {
                
                if (bfcomp.getNlin() < minnlin) {
                    minnlin = bfcomp.getNlin();
                }
            
            }
            
        }
        
        return minnlin;
        
    }
    
    /**
     * Compute the nonlinearity of the 1* component of a CA S-box
     * 
     * @param sbox      a boolean matrix representing an S-box
     * @param ncells    number of input cells in the S-box
     * @return          an int number denoting the nonlinearity of the all-1s
     *                  component of a S-box
     */
    public static int calcNlinSboxAllOnes(boolean[][] sbox, int ncells) {
        
        int m = sbox[0].length;
        int ncomp = (int)Math.pow(2, m);
        boolean[] curcomp = BinTools.dec2BinMod(ncomp-1, m);
            
        //Compute the component function selected by curcomp and
        //determine its nonlinearity
        boolean[] compfunc = calcComponent(ncells, sbox, curcomp);
        BooleanFunction bfcomp = new BooleanFunction(compfunc, ncells);
        CheckProp.computeNlin(bfcomp);

        /*System.out.print("Rule "+rule+" Component "+BinTools.bool2Bin(curcomp)+" -- Comp Rule "+
                bfcomp.getDeccode()+": BENT: "+isBent+" -- PLAT: "+isPlat+" -- NL:"+bfcomp.getNlin());
        System.out.println("");*/
        
        return bfcomp.getNlin();
        
    }
    
    /**
     * Compute the delta-uniformity of a S-box
     * 
     * @param sbox      a boolean matrix representing an S-box
     * @param ncells    number of input cells in the S-box
     * @return          an int number denoting the delta-uniformity of the S-box
     * 
     */
    public static int computeDeltaUniformity(boolean[][] sbox, int ncells) {
        
        //Initialize delta-uniformity and delta distribution table
        int deltaun = 0;
        int[][] ddt = new int[sbox.length][sbox.length];
        
        //First step: build the delta distribution table
        for(int a=0; a<sbox.length; a++) {
            
            boolean[] abin = BinTools.dec2BinMod(a, ncells);
            
            for(int b=0; b<sbox.length; b++) {
                
                boolean[] bbin = BinTools.dec2BinMod(b, ncells);
                
                for(int x=0; x<sbox.length; x++) {
                    
                    boolean[] fx = sbox[x];
                    boolean[] xbin = BinTools.dec2BinMod(x, ncells);
                    boolean[] xxora = BinTools.xorBits(xbin, abin);
                    int ixxora = BinTools.bin2Dec(xxora);
                    boolean[] fxxora = sbox[ixxora];
                    boolean[] result = BinTools.xorBits(fx, fxxora);
                    int iresult = BinTools.bin2Dec(result);
                    
                    if(iresult == b) {
                        ddt[a][b]++;
                    }
                    
                }
                
            }
            
        }
        
        //Second step: compute delta-uniformity as the maximum of the ddt table
        //over all nonzero input differences
        for(int a=1; a<ddt.length; a++) {
            
            for(int b=0; b<ddt.length; b++) {
                
                if (ddt[a][b] > deltaun) {
                    
                    deltaun = ddt[a][b];
                    
                }
                
            }
            
        }
        
        
        return deltaun;
        
    }
    
    /**
     * Determine whether a S-box is balanced or not. Basically, this amounts to
     * verifying if all its non-trivial component functions are balanced.
     * 
     * @param nvar  number of input variables of the S-box
     * @param sbox  a boolean matrix representing a S-box
     * @return      true if sbox is balanced, false otherwise
     */
    public static boolean computeUnbalancedness(int nvar, boolean[][] sbox) {

        boolean toRet = true;               //boolean variable to return
        int m = sbox[0].length;             //number of output variables of the S-box
        int ncomp = (int)Math.pow(2, m);    //number of component functions    
        
        int i=1;
        while((toRet==true) && i<ncomp) {
            
            boolean[] curcomp = BinTools.dec2BinMod(i, m);
            
            //Compute the component function selected by curcomp and determine if it is balanced or not
            boolean[] compfunc = calcComponent(nvar, sbox, curcomp);
            if(!BinTools.isBalanced(compfunc)) {
                toRet = false;
            }
            
            i++;
            
        }
        
        return toRet;
        
    }
    
}
