package boolfun;

/**
 * Utilities to compute various transforms (Walsh, Haar, Moebius) and check
 * cryptographic properties of boolean functions. Unless otherwise specified,
 * the boolean functions are represented in their polar form (0->1 and 1->-1)
 * with LSBF order (Least Significant Bit First).
 * 
 * @author Luca Mariot
 * @version 1.0
 */
public class BoolTransf {
    
    /**
     * Computes the Walsh Transform of a boolean function using the Fast Walsh
     * Transform (FWT) algorithm, which requires O(NlogN) operations (N=2^n is
     * the length of the truth table). The method directly computes the spectrum
     * in the original vector, and it must be called with the initial parameters
     * (vector, 0, vector.length). The reference for the algorithm is Carlet,
     * "Cryptography and Error-Correcting Codes", chapter 8 in Crama, Hammer,
     * "Boolean Models and Methods in Mathematics, Computer Science and
     * Engineering", p. 272.
     * 
     * @param vector an array of integers representing the boolean function.
     * @param start  the index of the truth table where to start computations.
     * @param length    the index of the truth table where to stop computations.
     */
    public static int calcFWT(int[] vector, int start, int length) {
        
        int half = length/2;
        
        //Main cycle: split vector in two parts (v0 e v1), 
        //update v0 as v0=v0+v1, and v1 as v1=v0-v1.
        for(int i=start; i<start+half; i++) {
            int temp = vector[i];
            vector[i] += vector[i+half];
            vector[i+half] = temp - vector[i+half];
        }
        
        //Recursive call on v0 and v1.
        if(half>1) {
            
            int val1 = calcFWT(vector,start,half);
            int val2 = calcFWT(vector,start+half,half);
            
            if(val1 > val2) {
                    //System.out.println(" val1 > val2 Degree of subfunction "+start+"-"+
                    //        (start+length-1)+": "+val1);
                    return val1;
            }
            else {
                //System.out.println("val1 <= val 2 Degree of subfunction "+(start)+"-"+
                //        (start+length-1)+": "+val2);
                return val2;
            }

        } else {
        
            //If we have reached half=1 (function in 2 variables),
            //return the highest coefficient in absolute value.
            if(Math.abs(vector[start]) > Math.abs(vector[start+half]))
                return Math.abs(vector[start]);
            else
                return Math.abs(vector[start+half]);           
            
        }
        
    }
    
    /**
     * Computes the inverse Walsh Transform using the Fast Walsh Transform (FWT)
     * algorithm, which requires O(nlogn) operations. Starting from the spectrum
     * of a boolean function, the method returns its truth table in polar form.
     * The method directly computes the truth table in the original vector, and
     * it must be called with the initial parameters (vector, 0, vector.length);
     * 
     * @param vector an array of integers representing the spectrum of a
     *               boolean function.
     * @param start  the index of the spectrum where the subvector begins.
     * @param length length of the subvector.
     * 
     */
    public static int calcInvFWT(int[] vector, int start, int length) {
        
        int half = length/2;
        
        //Main cycle: split vector in two parts (v0 e v1), 
        //update v0 as v0=v0+v1, and v1 as v1=v0-v1.
        for(int i=start; i<start+half; i++) {
            int temp = vector[i];
            vector[i] = (int)((vector[i] + vector[i+half]) / 2);
            vector[i+half] = (int)((temp - vector[i+half]) / 2);
        }
        
        //Recursive call on v0 and v1.
        if(half>1) {
            
            int val1 = calcInvFWT(vector,start,half);
            int val2 = calcInvFWT(vector,start+half,half);
            
            if(val1 > val2) {
                    //System.out.println(" val1 > val2 Degree of subfunction "+start+"-"+
                    //        (start+length-1)+": "+val1);
                    return val1;
            }
            else {
                //System.out.println("val1 <= val 2 Degree of subfunction "+(start)+"-"+
                //        (start+length-1)+": "+val2);
                return val2;
            }

        } else {
        
            //If we have reached half=1 (function in 2 variables),
            //return the highest coefficient in absolute value
            
            //If we are checking the null position, return the index in the
            //first position. This is because this method is used to calculate
            //the autocorrelation function, whose value ACmax must be computed
            //only on the nonnull vectors.
            if(start == 0) {
                return Math.abs(vector[1]);
            } else {
                
                if(Math.abs(vector[start]) > Math.abs(vector[start+half])) {
                    return Math.abs(vector[start]);
                }
                else {
                    return Math.abs(vector[start+half]);           
                }
                
            }
        }
        
    }

    
    /**
     * Computes the autocorrelation function of a boolean function, using the
     * FWT algorithm and the Wiener-Khintchine theorem. The computation flow is
     * the following: F=FWT(f) -> F^2 = F*F -> AC(f) = InvFWT(F^2). The method
     * directly computes the autocorrelation in the original vector.
     * 
     * @param vector    an array of integers representing the boolean function
     *                  or its walsh spectrum.
     * @param mode      a boolean flag specifying whether vector is the truth
     *                  table of the function (false) or the Walsh spectrum
     *                  (true), used to avoid unnecessary computations.
     */
    public static int calcAC(int[] vector, boolean mode) {
        
        //Compute the spectrum of the function, if vector
        //represents the truth table of the function.
        if(!mode) {
            
            calcFWT(vector, 0, vector.length);
            
        }        
        //Square the spectrum
        for(int i=0; i<vector.length; i++) {
            vector[i] *= vector[i];
        }
        
        //Compute the inverse WT of the squared spectrum
        int acmax = calcInvFWT(vector, 0, vector.length);
        return acmax;
        
    }
    
    /**
     * Compute the sum of squares indicator (i.e., sum of the squared
     * autocorrelation spectrum).
     * 
     * @param vector a vector of integer representing the autocorrelation 
     *               spectrum of a boolean function
     * @return the sum of squares indicator corresponding to the autocorrelation
     *         spectrum
     */
    public static int calcSSI(int[] vector) {
        
        int ssi = 0;
        
        for(int i=0; i<vector.length; i++) {
            
            ssi += (int)(Math.pow(vector[i],2));
            
        }
        
        return ssi;
        
    }
    
    /**
     * Find the highest coefficient (in absolute value) in a vector. The method
     * can be used to determine the spectral radius of a boolean function
     * (by giving in input the Walsh spectrum of the function, with parameter mode
     * set to false) or the maximum value of autocorrelation (by giving in input
     * the autocorrelation function, with mode set to true).
     * 
     * @param vector    an array of integers
     * @param mode      flag to specify the type of return (spectral radius: 
     *                  false, max autocorrelation: true)
     * @return maxcoeff the maximum coefficient in absolute value in vector
     */
    public static int findMaxCoeff(int[] vector, boolean mode) {
        
        int maxcoeff = 0;
        int ind = 0;
        
        //In the case of max autocorrelation, counting must start from 1,
        //since ^r(0)=2^n with balanced functions.
        if(mode) {
            ind = 1; 
        }
        
        for(int i=ind; i<vector.length; i++) {
            
            int absval = Math.abs(vector[i]);
            
            if(absval>maxcoeff) {
                maxcoeff = absval;
            }
            
        }
        
        return maxcoeff;
        
    }
    
    /**
     * Computes the nonlinearity of a boolean function, given in input its
     * spectral radius and the number of variables.
     * 
     * @param sprad   the spectral radius of the function.
     * @param nvar    the number of variables of the function.
     * @return nl     the nonlinearity of the function
     */
    public static int calcNL(int sprad, int nvar) {

        int nl = (int)(0.5*(Math.pow(2, nvar) - sprad));

        return nl;

    }
    
    /**
     * Finds the maximum absolute values of a vector in the positions with
     * specified Hamming weights. Useful to determine the correlation-immunity
     * of order m of a boolean function (by giving in input its Walsh spectrum)
     * or its propagation criterion PC(l) (by giving in input the 
     * autocorrelation function).
     * 
     * @param coeffs    an array of coefficients (it can be the Walsh spectrum
     *                  or the autocorrelation function of a boolean function).
     * @param indices   an array containing arrays of indices with a specified
     *                  Hamming weight (for example, indices[i] contains all
     *                  indices of Hamming weight i).
     * @return devs     an array containing the maximum absolute values in coeffs
     *                  at the positions specified by indices.
     */
    public static int[] calcDevs(int[] coeffs, int[][] indices) {
        
        int[] devs = new int[indices.length];
        
        //Cycle through Hamming weights from 1 to indices.length
        //(the vector indices *must* be initialised from weight 1, not 0!)
        for(int i=0; i<indices.length; i++) {
            
            //Cycle through inputs with Hamming weight i
            for(int j=0; j<indices[i].length; j++) {
                
                int absval = Math.abs(coeffs[indices[i][j]]);
                
                if(absval > devs[i]) {
                    devs[i] = absval;
                }
                
            }
            
            //Deviations of order i must take into account also deviations
            //of lower orders.
            for(int k=0; k<i; k++) {
                
                if(devs[k] > devs[i]) {
                    devs[i] = devs[k];
                }
                
            }
            
        }
        
        return devs;
        
    }
    
    /**
     * Computes the number of nonzero linear structures in a boolean function
     * given its autocorrelation function. An input a!=0 is a nonzero linear
     * structure if and only if |AC(a)|=2^n (where n is the number of variables
     * of the boolean function, so 2^n equals vector.length).
     * 
     * @param vector    the autocorrelation function of a boolean function
     * @return nzlstr   the number of nonzero linear structure of the function
     */
    public static int countNZLinStruct(int[] vector) {
        
        int nzlstr = 0;
        
        for(int i=1; i<vector.length; i++) {
            if((int)Math.abs(vector[i]) == vector.length) {
                nzlstr++;
            }
        }
        
        return nzlstr;
        
    }
    
    /**
     * Check whether a boolean function is permutive in any of its variables,
     * given its autocorrelation function. A boolean function is permutive in
     * the i-th variable if and only if A(0,1_i) = -2^n, where (0,1_i) indicates
     * the input vector having only a 1 in position i.
     * 
     * @param vector     the autocorrelation function of a boolean function
     * @param nvar       the number of variables of the function.
     * @return permvect  a boolean vector which specifies, for all i ranging
     *                   from 0 to vector.length, if the function is i-permutive.
     */
    public static boolean[] checkPerm(int[] vector, int nvar) {
        
        boolean[] permvect = new boolean[nvar];
        
        for(int i=0; i<permvect.length; i++) {
            
            //The input of Hamming weight 1 are those having as
            //decimal representation a power of 2.
            int index = (int)Math.pow(2,i);
            if(vector[index] == -vector.length) {
                permvect[i] = true;
            }
            
        }
        
        return permvect;
        
    }
    
    /**
     * Computes the Moebius Transform of a boolean function using the Fast
     * Moebius Transform (FMT) algorithm, which requires O(NlogN) operations
     * (N=2^n is the length of the truth table). The method directly computes
     * the spectrum in the original vector, and it must be called with the
     * initial parameters (vector, 0, vector.length). The reference for the
     * algorithm is Carlet, "Cryptography and Error-Correcting Codes", chapter 8
     * in Crama, Hammer, "Boolean Models and Methods in Mathematics, Computer
     * Science and Engineering", p. 263.
     * 
     * @param vector an array boolean representing the boolean function.
     * @param start  the index of the truth table where to start computations.
     * @param length the length of the subvector.
     */
    public static int calcFMT(boolean[] vector, int start, int length) {
        
        int half = length/2;
        
        //Main cycle: split vector in two parts (v0 e v1),
        //update v1 as v1=v0 XOR v1.
        for(int i=start; i<start+half; i++) {
            vector[i+half] = vector[i]^vector[i+half];
        }
        
        //Recursive call on v0 and v1.
        if(half>1) {
            
            int val1 = calcFMT(vector,start,half);
            int val2 = calcFMT(vector,start+half,half);
            
            if(val1 > val2) {
                    //System.out.println(" val1 > val2 Degree of subfunction "+start+"-"+
                    //        (start+length-1)+": "+val1);
                    return val1;
            }
            else {
                //System.out.println("val1 <= val 2 Degree of subfunction "+(start)+"-"+
                //        (start+length-1)+": "+val2);
                return val2;
            }

        } else {
        
            //If we have reached half=1 (function in 2 variables),
            //return the Hamming weight of the largest input having nonzero
            //coefficient in the current subvector.
            
                
            //If both coefficient are zero, then the degree of the subfunction
            //is zero.
            if((vector[start] == false) && (vector[start+half] == false)) {
                //System.out.println("Degree of subfunction "+start+"-"+
                //        (start+half)+": 0");
                return 0;
            } else {

                //Compute the length of the input vectors.
                int inplen = (int)(Math.log(vector.length)/Math.log(2));

                //If the coefficient of the higher vector is null,
                //then return the Hamming weight of the lower vector.
                if(vector[start+half] == false) {

                    boolean[] input = BinTools.dec2BinMod(start, inplen);
                    int subdeg = BinTools.hwt(input);
                    //System.out.println("Degree of subfunction "+start+"-"+
                    //    (start+half)+": "+subdeg);
                    return subdeg;

                } else {

                    //In all other cases, return the Hamming weight of the
                    //higher vector.
                    boolean[] input = BinTools.dec2BinMod(start+half, inplen);
                    int subdeg = BinTools.hwt(input);
                    //System.out.println("Degree of subfunction "+start+"-"+
                    //    (start+half)+": "+subdeg);
                    return subdeg;

                }
            }
            
        }
        
    }
    
    /**
     * Computes the algebraic degree of a boolean function, given its Moebius
     * Transform.
     * 
     * @param fmt       Boolean vector containing the Moebius Transform of the
     *                  function.
     * @param indices   Matrix containing the decimal positions of the input
     *                  vectors, sorted by Hamming weight.
     * @return          The algebraic degree of the boolean function.
     */
    public static int calcAlgDeg(boolean[] fmt, int[][] indices) {
        
        int algdeg = 0;
        int i = indices.length-1;
        
        //Check if there are coefficients != 0 in the ANF,
        //in decreasing order wrt Hamming weight.
        while((algdeg == 0) && (i >= 0)) {
            
            int j = 0; //index to loop over all inputs of Hamming weight i
            while((algdeg == 0 ) && (j<indices[i].length)) {
                
                if(fmt[indices[i][j]]) {
                    algdeg = i+1;
                }
                
                j++;
                
            }
            
            i--;
            
        }
        
        return algdeg;
        
    }
    
}
