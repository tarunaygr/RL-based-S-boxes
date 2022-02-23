package boolfun;

/**
 *
 * Utilities to convert and manipulate binary strings and numbers. The
 * conversion methods come in two versions, one using int and the other
 * using BigInteger (to convert bigger numbers). The order used in the
 * bitstrings is LSBF (Least Significant Bit First).
 * 
 * @author  Luca Mariot
 * @version 1.0
 */

import java.math.BigInteger;
import java.util.Vector;

public class BinTools {
    
    /**
     * 
     * Returns a binary string in polar form (0 -> 1, 1 -> -1)
     * 
     * @param   vect    a boolean array representing the binary string
     * @return  toRet   an int array representing the polar form of the string                  string
     */
    public static int[] bin2Pol(boolean[] vect) {

        int[] toRet = new int[vect.length];

        for(int i=0; i<vect.length; i++) {
            if(vect[i])
                toRet[i] = -1;
            else
                toRet[i] = 1;
        }

        return toRet;
    }
    
    /**
     * 
     * Returns a polar string in binary form (1 -> 0, -1 -> 1)
     * 
     * @param   vect    a boolean array representing the binary string
     * @return  toRet   an int array representing the polar form of the string                  string
     */
    public static boolean[] pol2Bin(int[] vect) {

        boolean[] toRet = new boolean[vect.length];

        for(int i=0; i<vect.length; i++) {
            if(vect[i]==1)
                toRet[i] = false;
            else
                toRet[i] = true;
        }

        return toRet;
    }   
    

    /**
     * Converts a binary string in a decimal number (BigInteger version).
     * 
     * @param   bNum a binary string (LSBF order)
     * @return  dNum the conversion of bNum as a decimal number
     */
    public static BigInteger bin2DecBig(boolean[] bNum) {
        
        BigInteger dNum = new BigInteger("0");
        
        for(int i=0; i<bNum.length; i++) {
            
             if(bNum[i]) {
                 BigInteger toAdd = new BigInteger("2");
                 toAdd = toAdd.pow(i);
                 dNum = dNum.add(toAdd);
             }
             
        }

        return dNum;
        
    }

    /**
     * Converts a binary string in a decimal number (int version).
     * 
     * @param   bNum a binary string (LSBF order)
     * @return  dNum the conversion of bNum as a decimal number
     */
    public static int bin2Dec(boolean[] bNum) {
        
        int dNum = 0;
        
        for(int i=0; i<bNum.length; i++) {
            
             if(bNum[i]) {
                 dNum += Math.pow(2, i);
             }
             
        }

        return dNum;

    }

    /**
     * Converts a decimal number in a binary string (BigInteger version).
     * 
     * @param   dNum    a decimal number
     * @param   length  the length of the binary string necessary to hold dNum
     * @return  bNum    the conversion of dNum as a binary string
     */
    public static boolean[] dec2Bin(BigInteger dNum, int length) {
        
        boolean[] bNum = new boolean[length];
        BigInteger temp = dNum;
        BigInteger two = new BigInteger("2");
        int i = 0;

        while(temp.compareTo(BigInteger.ZERO) != 0) {

            BigInteger mod = temp.remainder(two);
            temp = temp.divide(two);

            if(mod.compareTo(BigInteger.ONE) == 0) {
                bNum[i] = true;
            }

            i++;

        }

        return bNum;

    }

    /**
     * Converts a decimal number in a binary string (int version).
     * 
     * @param   dNum    a decimal number
     * @param   length  the length of the binary string necessary to hold dNum
     * @return  bNum    the conversion of dNum as a binary string
     */
    public static boolean[] dec2BinMod(int dNum, int length) {
        
        boolean[] bNum = new boolean[length];
        int temp = dNum;
        int i = 0;

        while(temp!=0) {

            int mod = temp%2;
            temp = temp/2;

            if(mod==1) {
                bNum[i] = true;
            }

            i++;
        }

        return bNum;

    }

    /**
     * Converts a binary string represented as a boolean array in a
     * corresponding string of 0s and 1s.
     * 
     * @param   boolstr the binary string represented as a boolean array
     * @return  binstr  the binary string represented as string of 0s and 1s.
     */
    public static String bool2Bin(boolean[] boolstr) {
            
        String binstr = "";

        for(int i=0; i<boolstr.length; i++) {
                
            if(boolstr[i])
                binstr += "1";
            else
                binstr += "0";
            
        }

        return binstr;
            
    }

    /**
     * Converts a single boolean value in a 0 (false) or 1 (true).
     * 
     * @param   bval a boolean value.  
     * @return  1 if bval=true, 0 otherwise
     */
    public static int singleBool2Bin(boolean bval) {
        
        if(bval)
            return 1;
        else
            return 0;
        
    }
   
   public static int[] bin2Int(boolean[] binstring) {
       
       int[] toRet = new int[binstring.length];
       
       for(int i=0; i<binstring.length; i++) {
           
           if(binstring[i]) {
               toRet[i] = 1;
           } else {
               toRet[i] = 0;
           }
           
       }
       
       return toRet;
       
   }

   /**
    * Compute the bitwise XOR between two boolean arrays of equal length.
    * 
    * @param seq1 a boolean array (first operand)
    * @param seq2 a boolean array (second operand)
    * @return xoredSeq the bitwise XOR of seq1 and seq2
    */
   public static boolean[] xorBits(boolean[] seq1, boolean[] seq2) {

       assert(seq1.length == seq2.length);
       boolean[] xoredSeq = new boolean[seq1.length];

       for(int i=0; i<seq1.length; i++) {
           xoredSeq[i] = seq1[i] ^ seq2[i];
       }

       return xoredSeq;
       
   }
   
   /**
    * Return a vector containing the positions where two boolean arrays differ.
    * 
    * @param table1 first boolean array
    * @param table2 second boolean array
    * @return a Vector of Integer containing the positions where table1 and 
    *         table 2 differ.
    */
   public static Vector<Integer> findDifPos(boolean[] table1,
           boolean[] table2) {
       
       Vector<Integer> difpos = new Vector<Integer>();
       
       for(int i=0; i<table1.length; i++) {
           
           if(table1[i] != table2[i]) {
                difpos.add(i);
           }
           
       }
       
       difpos.trimToSize();
       return difpos;
       
   }

   /**
    * Verifies whether a boolean array is balanced (that is, it contains an
    * equal number of true (1) and false (0).
    * 
    * @param   bVect a boolean array
    * @return  true if bVect is balanced, false if it is not.
    */
   public static boolean isBalanced(boolean[] bVect) {


        //If the length of the array is odd, then it will never be balanced
        if(bVect.length % 2 != 0) {
            return false;
        }

        //Otherwise, count the number of 1s in the array
        int ones = 0;

        for(int i=0; i<bVect.length; i++) {

            if(bVect[i]) {
                ones++;
            }

        }

        if(ones == bVect.length/2) {

            return true;

        } else {

            return false;

        }
    } 
    
    /**
     * Inverts the order of a boolean array.
     * 
     * 
     * @param   binStr  a boolean array
     * @return  rev     the reverse of binStr
     */
    public static boolean[] reverse(boolean[] binStr) {
            
        boolean[] rev = new boolean[binStr.length];

        for(int i=0; i<rev.length; i++) {

            rev[i] = binStr[binStr.length-1-i];

        }

        return rev;

    }
    
    /**
     * Computes the Hamming weight of a boolean vector.
     * 
     * @boolean[] binStr    The boolean vector whose Hamming weight has to be
     *                      computed.
     * @return              The Hamming weight of binStr.
     */
    public static int hwt(boolean[] binStr) {
        
        int weight = 0;
        
        for(int i=0; i<binStr.length; i++) {
            
            if(binStr[i])
                weight++;
            
        }
        
        return weight;
        
    }
    
    /** Compute the scalar product between two boolean vectors-
     * 
     * @param vect1 first boolean aray
     * @param vect2 second boolean array
     * @return the scalar product vect1.vect2, defined as: XOR_{i=1}^n (vect1[i] AND vect2[i])
     */
    public static boolean scalarProduct(boolean[] vect1, boolean[] vect2) {
        
        boolean prod = false;
        
        for(int i=0; i<vect2.length; i++) {
            
            prod ^= vect1[i] && vect2[i];
            
        }
        
        return prod;
        
    }
    
    /**
     * Compute the multiplication between a boolean square matrix and a boolean vector
     * 
     * @param matrix
     * @param vector
     * @return 
     */
    public static boolean[] matVectMult(boolean[][] matrix, boolean[] vector) {
        
        boolean[] result = new boolean[vector.length];
        
        for(int i=0; i<vector.length; i++) {
            
            result[i] = scalarProduct(matrix[i], vector);

        }
        
        return result;
        
    }
    
    public static boolean[] String2BoolStr(String binstr) {
        
        boolean[] toRet = new boolean[binstr.length()];
        
        for(int i=0; i<binstr.length(); i++) {
            
            if(binstr.charAt(i)=='1') {
                toRet[i] = true;
            } else {
                toRet[i] = false;
            }
        }
        
        return toRet;
        
    }

}
