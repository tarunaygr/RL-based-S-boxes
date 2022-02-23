package boolfun;

/**
 * Computes and prints the properties (attributes) of a BooleanFunction object.
 * 
 * @author Luca Mariot
 * @version 1.0
 * 
 */

public class CheckProp {
    
    /**
     * Computes all cryptographic properties of a boolean function, excluding the
     * statistical tests. The following attributes are supposed to be already
     * set: deccode, ttable, poltable, nvar, ninputs. Since all the transforms
     * methods modify the vectors inplace, it is necessary to make copies of
     * them before invoking those methods. The properties related to the ANF
     * and the algebraic degree are computed only if a flag is set.
     * 
     * @param boolfun a BooleanFunction instance representing the function.
     * @param indices matrix containing the indices of the vector of a given
     *        Hamming weight.
     */
    public static void computeAllCryptoProp(BooleanFunction boolfun,
            int[][] indices) {
        
        //Compute FMT-related attributes (ANF and algebraic degree)
        boolean[] anfcoeffs = new boolean[boolfun.getNinputs()];
        boolean[] ttable = boolfun.getTtable();
        System.arraycopy(ttable, 0, anfcoeffs, 0, anfcoeffs.length);
        int algdeg = BoolTransf.calcFMT(anfcoeffs, 0, anfcoeffs.length);
        boolfun.setAnfcoeffs(anfcoeffs);
        boolfun.setAlgdeg(algdeg);
        
        //Compute FWT-related attributes
        int[] whcoeffs = new int[boolfun.getNinputs()];
        int[] poltable = boolfun.getPoltable();
        System.arraycopy(poltable, 0, whcoeffs, 0, whcoeffs.length);
        int sprad = BoolTransf.calcFWT(whcoeffs, 0, whcoeffs.length);
        int nlin = BoolTransf.calcNL(sprad, boolfun.getNvar());
        int[] cid = new int[boolfun.getNvar()];
        int[] reqcid = BoolTransf.calcDevs(whcoeffs, indices);
        System.arraycopy(reqcid, 0, cid, 0, reqcid.length);
        
        if(whcoeffs[0] == 0) {
            boolfun.setIsBalanced(true);
        } else {
            boolfun.setIsBalanced(false);
        }
        boolfun.setWhcoeffs(whcoeffs);
        boolfun.setSprad(sprad);
        boolfun.setNlin(nlin);
        boolfun.setCid(cid);
        
        //Compute AC-related attributes
        int[] accoeffs = new int[boolfun.getNinputs()];
        System.arraycopy(whcoeffs, 0, accoeffs, 0, accoeffs.length);
        int acmax = BoolTransf.calcAC(accoeffs, true);
        int ssi = BoolTransf.calcSSI(accoeffs);
        int[] pcd = new int[boolfun.getNvar()];
        int[] reqpcd = BoolTransf.calcDevs(accoeffs, indices);
        System.arraycopy(reqpcd, 0, pcd, 0, reqpcd.length);
        int nzls = BoolTransf.countNZLinStruct(accoeffs);
        
        boolfun.setAccoeffs(accoeffs);
        boolfun.setAcmax(acmax);
        boolfun.setSsi(ssi);
        boolfun.setNlinstruct(nzls);
        boolfun.setPcd(pcd);
        
        //Compute chaos-related attributes
        boolean[] iperm = BoolTransf.checkPerm(accoeffs, boolfun.getNvar());
        boolfun.setIperm(iperm);
        
    }
    
    public static void computeANF(BooleanFunction boolfun) {
        
        //Compute FMT-related attributes (ANF and algebraic degree)
        boolean[] anfcoeffs = new boolean[boolfun.getNinputs()];
        boolean[] ttable = boolfun.getTtable();
        System.arraycopy(ttable, 0, anfcoeffs, 0, anfcoeffs.length);
        int algdeg = BoolTransf.calcFMT(anfcoeffs, 0, anfcoeffs.length);
        boolfun.setAnfcoeffs(anfcoeffs);
        boolfun.setAlgdeg(algdeg);
        
    }
    
    /**
     * Computes only the Walsh spectrum, balancedness, spectral radius and
     * nonlinearity of a boolean function -- useful when Hill Climbing is
     * performed together with a Genetic Algorithm.
     * 
     * @param boolfun   a BooleanFunction object representing a boolean function.
     */
    public static void computeWHProp(BooleanFunction boolfun, int[][] indices) {
        
        //Compute FWT-related attributes
        int[] whcoeffs = new int[boolfun.getNinputs()];
        int[] poltable = boolfun.getPoltable();
        System.arraycopy(poltable, 0, whcoeffs, 0, whcoeffs.length);
        int sprad = BoolTransf.calcFWT(whcoeffs, 0, whcoeffs.length);
        int nlin = BoolTransf.calcNL(sprad, boolfun.getNvar());
        
        if(whcoeffs[0] == 0) {
            boolfun.setIsBalanced(true);
        } else {
            boolfun.setIsBalanced(false);
        }
        boolfun.setWhcoeffs(whcoeffs);
        boolfun.setSprad(sprad);
        boolfun.setNlin(nlin);
        
        int[] cid = new int[boolfun.getNvar()];
        int[] reqcid = BoolTransf.calcDevs(whcoeffs, indices);
        System.arraycopy(reqcid, 0, cid, 0, reqcid.length);
        boolfun.setCid(cid);
        
    }
    
    public static void computeNlin(BooleanFunction boolfun) {
        
        //Compute FWT-related attributes
        int[] whcoeffs = new int[boolfun.getNinputs()];
        int[] poltable = boolfun.getPoltable();
        System.arraycopy(poltable, 0, whcoeffs, 0, whcoeffs.length);
        int sprad = BoolTransf.calcFWT(whcoeffs, 0, whcoeffs.length);
        int nlin = BoolTransf.calcNL(sprad, boolfun.getNvar());
        
        if(whcoeffs[0] == 0) {
            boolfun.setIsBalanced(true);
        } else {
            boolfun.setIsBalanced(false);
        }
        boolfun.setWhcoeffs(whcoeffs);
        boolfun.setSprad(sprad);
        boolfun.setNlin(nlin);
        
    }
    
    /**
     * Computes the cyptographic properties of a boolean function, excluding
     * the Walsh spectrum, balancedness and nonlinearity.
     * 
     * @param boolfun   a BooleanFunction object representing a boolean function.
     * @param indices   indices matrix containing the indices of the vector of a given
     *                  Hamming weight.
     */
    public static void computeRemProp(BooleanFunction boolfun, 
            int[][] indices) {
        
        //Compute CI deviations
        int[] whcoeffs = boolfun.getWhcoeffs();
        int[] cid = new int[boolfun.getNvar()];
        int[] reqcid = BoolTransf.calcDevs(whcoeffs, indices);
        System.arraycopy(reqcid, 0, cid, 0, reqcid.length);
        boolfun.setCid(cid);
        
        //Compute FMT-related attributes (ANF and algebraic degree)
        boolean[] anfcoeffs = new boolean[boolfun.getNinputs()];
        boolean[] ttable = boolfun.getTtable();
        System.arraycopy(ttable, 0, anfcoeffs, 0, anfcoeffs.length);
        int algdeg = BoolTransf.calcFMT(anfcoeffs, 0, anfcoeffs.length);
        boolfun.setAnfcoeffs(anfcoeffs);
        boolfun.setAlgdeg(algdeg);
        
        //Compute AC-related attributes
        int[] accoeffs = new int[boolfun.getNinputs()];
        System.arraycopy(whcoeffs, 0, accoeffs, 0, accoeffs.length);
        int acmax = BoolTransf.calcAC(accoeffs, true);
        int[] pcd = new int[boolfun.getNvar()];
        int[] reqpcd = BoolTransf.calcDevs(accoeffs, indices);
        System.arraycopy(reqpcd, 0, pcd, 0, reqpcd.length);
        int nzls = BoolTransf.countNZLinStruct(accoeffs);
        
        boolfun.setAccoeffs(accoeffs);
        boolfun.setAcmax(acmax);
        boolfun.setNlinstruct(nzls);
        boolfun.setPcd(pcd);
        
        //Compute chaos-related attributes
        boolean[] iperm = BoolTransf.checkPerm(accoeffs, boolfun.getNvar());
        boolfun.setIperm(iperm);
        
    }
    
    /**
     * Computes the cyptographic properties of a boolean function, excluding
     * the Walsh spectrum, balancedness and nonlinearity.
     * 
     * @param boolfun   a BooleanFunction object representing a boolean function.
     */
    public static void computeIPerm(BooleanFunction boolfun) {
        
        //Compute CI deviations
        int[] whcoeffs = boolfun.getWhcoeffs();
        
        //Compute AC-related attributes
        int[] accoeffs = new int[boolfun.getNinputs()];
        System.arraycopy(whcoeffs, 0, accoeffs, 0, accoeffs.length);
        int acmax = BoolTransf.calcAC(accoeffs, true);
        int nzls = BoolTransf.countNZLinStruct(accoeffs);
        
        boolfun.setAccoeffs(accoeffs);
        boolfun.setAcmax(acmax);
        
        //Compute chaos-related attributes
        boolean[] iperm = BoolTransf.checkPerm(accoeffs, boolfun.getNvar());
        boolfun.setIperm(iperm);
        
    }
    
    public static void printFuncNum(BooleanFunction boolfun) {
        
        int nvar = boolfun.getNvar();
        System.out.println("\nFunction "+boolfun.getDeccode());
        System.out.println("\nNumber of variables: "+nvar);
        
    }
    
    /**
     * Prints the truth table, Walsh spectrum and autocorrelation function
     * of a boolean function.
     * 
     * @param boolfun a BooleanFunction object representing a boolean function.
     */
    public static void printFuncTables(BooleanFunction boolfun) {
        
        //Print truth table
        int nvar = boolfun.getNvar();
        System.out.println("\nTruth table:");
        boolean[] ttable = boolfun.getTtable();
        for(int i=0; i<ttable.length; i++) {
            
            System.out.println("f("+
                    BinTools.bool2Bin(BinTools.dec2BinMod(i, nvar))+") = "+
                    BinTools.singleBool2Bin(ttable[i]));
            
        }
        
        //Print Walsh spectrum.
        System.out.println("\nWalsh spectrum:");
        int[] whcoeffs = boolfun.getWhcoeffs();
        for(int i=0; i<whcoeffs.length; i++) {
            
            System.out.println("F("+
                    BinTools.bool2Bin(BinTools.dec2BinMod(i, nvar))+") = "+
                    whcoeffs[i]);
        
        }
        
        //Print autocorrelation function.
        System.out.println("\nAutocorrelation function:");
        int[] accoeffs = boolfun.getAccoeffs();
        for(int i=0; i<accoeffs.length; i++) {
            
            System.out.println("r("+
                    BinTools.bool2Bin(BinTools.dec2BinMod(i, nvar))+") = "+
                    accoeffs[i]);
        
        }
        
    }
    
    /**
     * Prints the algebraic normal form (ANF) of a boolean function.
     * 
     * @param boolfun a BooleanFunction object representing a boolean function.
     */
    public static void printANF(BooleanFunction boolfun) {
        
        int nvar = boolfun.getNvar();
        boolean[] anfcoeffs = boolfun.getAnfcoeffs();
        
        //Find the last nonzero coefficient in the ANF
        int last = 0;
        int k = anfcoeffs.length-1;
        
        while((last == 0) && (k>=0)) {
            
            if(anfcoeffs[k])
                last = k;
            
            k--;
            
        }
        
        //Print the ANF
        //System.out.println("\nAlgebraic Normal Form:");
        System.out.print("f(");
        for(int i=0; i<nvar; i++) {
            System.out.print("x"+(i+1));
            if(i<nvar-1) {
                System.out.print(",");
            }
        }
        System.out.print(") = ");
        
        if(anfcoeffs[0]) {
            System.out.print("1 + ");
        }
        
        for(int i=1; i<=last; i++) {
            
            if(anfcoeffs[i]) {
                
                //Print the i-th variation of variables
                boolean[] input = BinTools.dec2BinMod(i,nvar);
                
                for(int j=0; j<nvar; j++) {
                    
                    if(input[j]) {
                        
                        System.out.print("x"+(j+1));
                        
                    }
                    
                }
                
                if(i<last) {
                    System.out.print(" + ");
                }
                
                
            }
            
        }
        
        //System.out.println("");
        
    }
    
    /**
     * Prints the algebraic normal form (ANF) of a boolean function in LaTeX.
     * 
     * @param boolfun a BooleanFunction object representing a boolean function.
     */
    public static String printANFLatex(BooleanFunction boolfun) {
        
        String toRet = "";
        int nvar = boolfun.getNvar();
        boolean[] anfcoeffs = boolfun.getAnfcoeffs();
        
        //Find the last nonzero coefficient in the ANF
        int last = 0;
        int k = anfcoeffs.length-1;
        
        while((last == 0) && (k>=0)) {
            
            if(anfcoeffs[k])
                last = k;
            
            k--;
            
        }
        
        //Print the ANF
        //System.out.println("\nAlgebraic Normal Form:");
        toRet +="$f(";
        for(int i=0; i<nvar; i++) {
            toRet +="x_"+(i+1);
            if(i<nvar-1) {
                toRet +=",";
            }
        }
        toRet +=") = ";
        
        if(anfcoeffs[0]) {
            toRet +="1 \\oplus ";
        }
        
        for(int i=1; i<=last; i++) {
            
            if(anfcoeffs[i]) {
                
                //Print the i-th variation of variables
                boolean[] input = BinTools.dec2BinMod(i,nvar);
                
                for(int j=0; j<nvar; j++) {
                    
                    if(input[j]) {
                        
                        toRet +="x_"+(j+1);
                        
                    }
                    
                }
                
                if(i<last) {
                    toRet +=" \\oplus ";
                }
                
                
            }
            
        }
        
        toRet +="$";
        
        return toRet;
        
    }
    
    /**
     * Prints the polynomial associated to the linear terms of a boolean function.
     * 
     * @param boolfun a BooleanFunction object representing a boolean function.
     */
    public static String printPolynomial(BooleanFunction boolfun) {
        
        String poly = "";
        int nvar = boolfun.getNvar();
        boolean[] anfcoeffs = boolfun.getAnfcoeffs();
        
        //Find the last nonzero coefficient in the ANF
        int last = 0;
        int k = anfcoeffs.length-1;
        
        while((last == 0) && (k>=0)) {
            
            if((anfcoeffs[k]) && (BinTools.hwt(BinTools.dec2BinMod(k, nvar)) == 1))     //only care for linear terms of weight 1
                last = k;
            
            k--;
            
        }
        
        //Print the Polynomial
        //System.out.println("\nAlgebraic Normal Form:");
        poly += "P(X) = ";
        int p=-1;
        
        for(int i=1; i<=last; i++) {
            
            if((BinTools.hwt(BinTools.dec2BinMod(i, nvar)) == 1)) {
                
                p++;
                if(anfcoeffs[i]) {
                    
                    //Print the i-th variation of variables
                    if(p==0) {
                        poly += "1";
                    } else {
                        poly += "X^"+p;
                    }
                    
                    if(i<last) {
                        poly +=" + ";
                    }   
                    
                }
                
                
            }
            
        }
        
        return poly;
        
    }
    
    /**
     * Given two Boolean functions, return true if they have all nonlinear
     * terms in their ANFs in common.
     * 
     * @param boolfun1
     * @param boolfun2
     * @return 
     */
    public static boolean checkNonlinearTerms(BooleanFunction boolfun1, BooleanFunction boolfun2) {
        
        boolean[] anf1 = boolfun1.getAnfcoeffs();
        boolean[] anf2 = boolfun2.getAnfcoeffs();
        int nvar = boolfun1.getNvar();
        
        for(int i=2; i<anf1.length; i++) {
            
            if((BinTools.hwt(BinTools.dec2BinMod(i, nvar)) != 1)) {
                
                if(anf1[i] != anf2[i]) {
                    
                    return false;
                    
                }
                
            }
            
        }
        
        return true;
        
    }
    
    /**
     * Prints the cryptographic properties of a boolean function.
     * 
     * @param boolfun a BooleanFunction object representing a boolean function.
     * @param indprop an index representing the maximum order of the CI and PC
     *                properties to be printed.
     */
    public static void printCryptoProp(BooleanFunction boolfun, int indprop) {
        
        System.out.println("\n\nCryptographic Properties");
        boolean isbal = boolfun.isIsBalanced();
        System.out.print("\nBalanced = "+isbal+"; ");
        int algdeg = boolfun.getAlgdeg();
        System.out.println("Algebraic degree =  "+algdeg);
        int sprad = boolfun.getSprad();
        int nlin = boolfun.getNlin();
        System.out.println("\nSpectral radius = "+ sprad+"; Nonlinearity = "+nlin);
        System.out.println("\nCorrelation Immunity:");
        for(int i=0; i<indprop; i++) {
            System.out.println("CI("+(i+1)+") = "+boolfun.getCid()[i]);
        }
        int acmax = boolfun.getAcmax();
        int ssi = boolfun.getSsi();
        int nzls = boolfun.getNlinstruct();
        System.out.println("\nMaximum autocorrelation value: "+acmax+
                ";\nSum of squares indicator: "+ssi+";\nNumber of nonzero linear"
                + " structures: "+nzls);
        System.out.println("\nPropagation Criterion:");
        for(int i=0; i<indprop; i++) {
            System.out.println("PC("+(i+1)+") = "+boolfun.getPcd()[i]);
        }
        System.out.println("\nPermutivity:");
        for(int i=0; i<indprop; i++) {
            System.out.println((i+1)+"-permutive: "+boolfun.getIperm()[i]);
        }
        System.out.println("");   
        
    }
    
    
    //The following methods generalize the formers for populations of functions.
    public static void computeAllCryptoPropPop(BooleanFunction[] bfpop,
            int[][] indices) {
        
        for(int i=0; i<bfpop.length; i++) {
            
            computeAllCryptoProp(bfpop[i], indices);
            
        }
        
    }
    
    public static void computeWHPropPop(BooleanFunction[] bfpop,
            int[][] indices) {
        
        for(int i=0; i<bfpop.length; i++) {
            
            computeWHProp(bfpop[i], indices);
            
        }
        
    }
    
    public static void computeRemPropPop(BooleanFunction[] bfpop,
            int[][] indices) {
        
        for(int i=0; i<bfpop.length; i++) {
            
            computeRemProp(bfpop[i], indices);
            
        }
        
    }
    
    /**
     * Prints essential information of a population of boolean function.
     * 
     * @param bfpop
     * @param indices 
     */
    public static void printPop(BooleanFunction[] bfpop, int indprop) {
        
        for(int i=0; i<bfpop.length; i++) {
            
            System.out.println("Individual "+(i+1)+":");
            printFuncNum(bfpop[i]);
            printCryptoProp(bfpop[i], indprop);
            
        }
        
    }  
    
    //Creates the set of indices to check crypto properties.
    public static int[][] createIndices(int len) {
        
        int[][] indices = new int[len][];
        for(int i=0; i<len; i++) {
            
            indices[i] = CombTools.genBinCombs(len-i-1, i+1);
            
        }
        
        return indices;
        
    }
    
    /**
     * Check if a boolean function is plateaued. This means that its Walsh
     * spectrum is composed of only three values: {-sprad, 0, +sprad}, where
     * sprad is the spectral radius (maximum absolute vlue of the Walsh transform)
     * 
     * @param spec      int array specifying the Walsh spectrum of a boolean function
     * @param sprad     spectral radius of the function
     * @return          true if spec contains only 0, -sprad and +sprad as values,
     *                  false otherwise
     */
    public static boolean checkPlateaued(int[] spec, int sprad) {
        
        int i = 0;
        
        while((i<spec.length) && ((spec[i]==0)||(spec[i]==sprad)||(spec[i]==-sprad))) {
            
            i++;
            
        }
        
        if(i==spec.length) {
            
            return true;
            
        } else {
            
            return false;
            
        }
        
    }
    
    /**
     * Check if a boolean function is bent. This means that its Walsh
     * spectrum is composed of only two values: {-sprad, +sprad}, where
     * sprad is the spectral radius (maximum absolute vlue of the Walsh transform).
     * 
     * NOTICE: Bent -> Plateaued, but the converse does not hold
     * 
     * @param spec      int array specifying the Walsh spectrum of a boolean function
     * @param sprad     spectral radius of the function
     * @return          true if spec contains only -sprad and +sprad as values,
     *                  false otherwise
     */
    public static boolean checkBent(int[] spec, int sprad) {
        
        int i = 0;
        
        while((i<spec.length) && ((spec[i]==sprad)||(spec[i]==-sprad))) {
            
            i++;
            
        }
        
        if(i==spec.length) {
            
            return true;
            
        } else {
            
            return false;
            
        }
        
    }

}
