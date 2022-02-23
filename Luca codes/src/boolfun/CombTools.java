package boolfun;

/**
 * Utilities to generate combinations of objects (particularly bitstrings with
 * a specified Hamming weight) and compute their cardinalities. The bitstrings
 * are sorted in LSBF (Least Significant Bit First) order, unless otherwise
 * specified.
 * 
 * @author  Luca Mariot
 * @version 1.0
 */
import java.math.BigInteger;
import java.io.*;

public class CombTools {
    
    /**
     * Computes the factorial of an integer number.
     * 
     * @param num   an integer number
     * @return fact the factorial of num
     */
    public static int factorial(int num) {
        
        int fact = 1;
        
        if((num==0) || (num==1)) {            
            return fact;   
        }
        
        for(int i=2; i<=num; i++) {
            fact *= i;
        }
        
        return fact;
        
    }
    
    /**
     * Computes the binomial coefficient (n,k).
     * 
     * @param n         the size of the set from which combinations are drawn.
     * @param k         the size of the combinations.
     * @return bCoeff   the binomial coefficient (n,k)
     */
    public static int binCoeff(int n, int k) {
        
        long numerator = 1;
        
        for(int i=n-k+1; i<=n; i++) {
            numerator *= i;
        }
        
        long denominator = factorial(k);
        int bCoeff = (int)(numerator/denominator);
        
        return bCoeff;
        
    }
    
    /**
     * Generates all the (s+t)-bit strings with Hamming weight t, in decimal
     * notation. The algorithm is described in Knuth, "The Art of Computer
     * Programming, pre-Fascicle 3A" (Algorithm L, p. 4).
     * 
     * @param s         number of 0s in the bitstrings
     * @param t         number of 1s in the bitstrings
     * @return combset  array of integers representing the bitstrings of length
     *                  (s+t) and Hamming weight t
     */
    public static int[] genBinCombs(int s, int t) {

        int size = binCoeff(s+t, t);
        int[] combset = new int[size];
        
        int index = 0; //index for the set combs.
        
        //Initialisation
        int[] comb = new int[t+2]; //the two additional cells are sentinels.
        for(int j=0; j<t; j++) {
            comb[j] = j;
        }
        comb[t] = s+t;
        comb[t+1] = 0;
        
        int j = 0;
        
        while(j<t) {
            
            boolean[] conf = new boolean[s+t];
            
            for(int k=0; k<t; k++) {
                conf[comb[k]] = true;
            }
            
            //Convert the combination in decimal notation and
            //copy it in the final set.
            int deccomb = BinTools.bin2Dec(conf);
            combset[index] = deccomb;
            index++;            
            
            j=0;
            while((comb[j]+1)==comb[j+1]) {
                comb[j] = j;
                j++;
            }
            
            if(j<t) {
                comb[j]++;
            }
            
        }
        
        return combset;
      
    }
    
    /**
     * Generates all the (s+t)-bit strings with Hamming weight t, in binary
     * notation. The algorithm is described in Knuth, "The Art of Computer
     * Programming, pre-Fascicle 3A" (Algorithm L, p. 4).
     * 
     * @param s         number of 0s in the bitstrings
     * @param t         number of 1s in the bitstrings
     * @return combset  array of integers representing the bitstrings of length
     *                  (s+t) and Hamming weight t
     */
    public static boolean[][] genBinCombsBin(int s, int t) {

        int size = binCoeff(s+t, t);
        boolean[][] combset = new boolean[size][];
        
        int index = 0; //index for the set combs.
        
        //Initialisation
        int[] comb = new int[t+2]; //the two additional cells are sentinels.
        for(int j=0; j<t; j++) {
            comb[j] = j;
        }
        comb[t] = s+t;
        comb[t+1] = 0;
        
        int j = 0;
        
        while(j<t) {
            
            boolean[] conf = new boolean[s+t];
            
            for(int k=0; k<t; k++) {
                conf[comb[k]] = true;
            }
            
            //Copy the combination in the final set.
            //int deccomb = BinTools.bin2Dec(conf);
            combset[index] = conf;
            index++;            
            
            j=0;
            while((comb[j]+1)==comb[j+1]) {
                comb[j] = j;
                j++;
            }
            
            if(j<t) {
                comb[j]++;
            }
            
        }
        
        return combset;
      
    }
    
    /**
     * Generates all ind-permutive functions of nvar variables.
     * 
     * @param nvar number of variables of the functions
     * @param ind  index of the variable which satisfies permutivity.
     */
    public static void GenerateIpermFunc(int nvar, int ind) {
        
        int ngraph = (int)Math.pow(2,nvar-1);
        int nfunc = (int)Math.pow(2, ngraph);
        int funclength = (int)Math.pow(2,nvar);
        
        for(int i=nfunc-1; i>=0; i--) {
            
            boolean[] conf = BinTools.dec2BinMod(i, ngraph);
            boolean[] func = new boolean[funclength];
            
            for(int j=0; j<conf.length; j++) {
                
                boolean[] input1 = BinTools.dec2BinMod(j, nvar);
                boolean[] input2 = new boolean[nvar];
                System.arraycopy(input1, 0, input2, 0, input1.length);
                input2[ind] = !input2[ind];
                int j2 = BinTools.bin2Dec(input2);
                func[j] = conf[j];
                func[j2] = !conf[j];
                
            }
            
            System.out.println(BinTools.bin2Dec(func));
            
        }
        
    }   
    
}
