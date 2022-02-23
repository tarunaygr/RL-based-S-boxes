package boolfun;

/**
 * Class which represents a generic boolean function, along with its
 * representations (truth table, ANF), cryptographic properties (balancedness,
 * algebraic degree, nonlinearity, resiliency, propagation criterion, number of
 * nonzero linear structures), chaos properties (permutivity) and performances
 * as a CA-based PRNG rule over the ENT tests. The parameters of the PRNG are
 * supposed to be standard:
 * 
 * 1) The CA is composed by 64 cells, with periodic boundary conditions.
 * 2) The ENT tests are run on a single sequence produced as follows: 
 *    2.1) The CA is initialized with an initial configuration containing
 *         only a 1 in the 32nd cell.
 *    2.2) The CA is evolved for 65536 iterations.
 *    2.3) The trace of the 32nd cell is taken as the pseudorandom sequence.
 * 
 * @author Luca Mariot
 * @version 1.0
 * 
 */

import java.math.BigInteger;

public class BooleanFunction {
    
    //Representation-related attributes.
    private BigInteger deccode;
    private int nvar;
    private int ninputs;
    private boolean[] ttable;
    private boolean[] anfcoeffs;
    private String anfexpr;
    
    //Transforms-related attributes.
    private int[] poltable;
    private int[] whcoeffs;
    private int sprad;
    private int nlin;
    private int[] accoeffs;
    private int acmax;
    private int ssi; //Sum of square indicator
    
    //Crypto-related attributes.
    private boolean isBalanced;
    private int algdeg;
    private int nlinstruct;
    private int[] cid;
    private int[] pcd;
    
    //Chaos-related attributes.
    private boolean[] iperm;
    
    
    // Constructors
    
    /** 
     * First constructor, decimal representation-based.
     * 
     * @param deccode   decimal representation code of the function.
     * @param nvar      number of variables of the function.
     */
    public BooleanFunction(BigInteger deccode, int nvar) {
        
        this.deccode = deccode;
        this.nvar = nvar;
        
        ninputs = (int)Math.pow(2,nvar);
        ttable = BinTools.dec2Bin(deccode, ninputs);
        poltable = BinTools.bin2Pol(ttable);
        
        whcoeffs = new int[ninputs];
        accoeffs = new int[ninputs];
        anfcoeffs = new boolean[ninputs];
        cid = new int[nvar];
        pcd = new int[nvar];
        iperm = new boolean[nvar];
        
    }
    
    /** 
     * Second constructor, truth table representation-based.
     * 
     * @param ttable    truth table of the function (LSBF order)
     * @param nvar      number of variables of the function.
     */
    public BooleanFunction(boolean[] ttable, int nvar) {
        
        this.ttable = ttable;
        this.nvar = nvar;
        
        ninputs = ttable.length;
        deccode = BinTools.bin2DecBig(ttable);
        poltable = BinTools.bin2Pol(ttable);
        
        whcoeffs = new int[ninputs];
        accoeffs = new int[ninputs];
        anfcoeffs = new boolean[ninputs];
        cid = new int[nvar];
        pcd = new int[nvar];
        iperm = new boolean[nvar];
        
    }
    
    //Getters.

    public int[] getAccoeffs() {
        return accoeffs;
    }

    public int getAcmax() {
        return acmax;
    }

    public int getAlgdeg() {
        return algdeg;
    }

    public boolean[] getAnfcoeffs() {
        return anfcoeffs;
    }

    public String getAnfexpr() {
        return anfexpr;
    }

    public BigInteger getDeccode() {
        return deccode;
    }

    public boolean[] getIperm() {
        return iperm;
    }

    public boolean isIsBalanced() {
        return isBalanced;
    }

    public int getNinputs() {
        return ninputs;
    }

    public int getNlinstruct() {
        return nlinstruct;
    }

    public int getNvar() {
        return nvar;
    }

    public int[] getPoltable() {
        return poltable;
    }

    public int getSprad() {
        return sprad;
    }

    public boolean[] getTtable() {
        return ttable;
    }

    public int[] getWhcoeffs() {
        return whcoeffs;
    }

    public int getNlin() {
        return nlin;
    }

    public int[] getCid() {
        return cid;
    }

    public int[] getPcd() {
        return pcd;
    }
    
    //Setters.

    public void setAccoeffs(int[] accoeffs) {
        this.accoeffs = accoeffs;
    }

    public void setAcmax(int acmax) {
        this.acmax = acmax;
    }

    public void setAlgdeg(int algdeg) {
        this.algdeg = algdeg;
    }

    public void setAnfcoeffs(boolean[] anfcoeffs) {
        this.anfcoeffs = anfcoeffs;
    }

    public void setAnfexpr(String anfexpr) {
        this.anfexpr = anfexpr;
    }

    public void setDeccode(BigInteger deccode) {
        this.deccode = deccode;
    }

    public void setIperm(boolean[] iperm) {
        this.iperm = iperm;
    }

    public void setIsBalanced(boolean isBalanced) {
        this.isBalanced = isBalanced;
    }

    public void setNinputs(int ninputs) {
        this.ninputs = ninputs;
    }

    public void setNlinstruct(int nlinstruct) {
        this.nlinstruct = nlinstruct;
    }

    public void setNvar(int nvar) {
        this.nvar = nvar;
    }

    public void setPoltable(int[] poltable) {
        this.poltable = poltable;
    }

    public void setSprad(int sprad) {
        this.sprad = sprad;
    }

    public void setTtable(boolean[] ttable) {
        this.ttable = ttable;
    }

    public void setWhcoeffs(int[] whcoeffs) {
        this.whcoeffs = whcoeffs;
    }

    public void setNlin(int nlin) {
        this.nlin = nlin;
    }

    public void setCid(int[] cid) {
        this.cid = cid;
    }

    public void setPcd(int[] pcd) {
        this.pcd = pcd;
    }

    public int getSsi() {
        return ssi;
    }

    public void setSsi(int ssi) {
        this.ssi = ssi;
    }
    
}
