package ca;

import boolfun.BinTools;

/**
 * Implementation of a 1-dimensional cellular automata. The offset is always
 * assumed to be 0. Hence, given a local rule of diameter d, each cell looks at
 * itself and d-1 cells to its right to apply it. 
 * 
 * @author Luca Mariot (luca.mariot@gmail.com)
 */

public class OneDimCellAut {
    
    private boolean[] cells;        //cells array
    private boolean[] rule;         //local rule (the truth table of a Boolean function represented in LSBF order).
    private int nbr;                //CA neighborhood (=diameter, number of variables of local rule)

    /**
     * Computes the transition function of a single cell of the CA, given in
     * input its neighborhood. The functions is computed simply as a look-up
     * table, so the neighborhood of the cell is converted in decimal notation,
     * and the boolean value in the truth table of the rule at the position
     * specified by the neighborhood is returned as the output value.
     * 
     * @param nbrhood   a boolean array specifying the neighborhood of the cell
     * @return          the value of the local rule corresponding to nbrhood
     */
    private boolean delta(boolean[] nbrhood) {
        
        int index = boolfun.BinTools.bin2Dec(nbrhood);
        boolean value = false;

        value = rule[index];
         
        return value;

    }
    
    /**
     * Class constructor parameters: number of cells, local rule represented as
     * the boolean array representing its truth table and diameter (nbr) of the
     * local rule.
     * 
     * @param nCells    the number of the cells of the CA
     * @param rule      the local rule of the CA
     * @param nbr       the diameter (neighborhood size) of the CA
     */
    public OneDimCellAut(int nCells, boolean[] rule, int nbr) {
        
        cells = new boolean[nCells];
        this.rule = rule;
        this.nbr = nbr;

    }
    
    /**
     * Evolves the CA from its current configuration to the next one, with
     * periodic boundary conditions
     */
    public void nextConfigPeriodic() {

        boolean[] nextConf = new boolean[cells.length];
        int n = cells.length;

        for(int i=0; i<n; i++) {

            //Build the neighborhood of the i-th cell
            boolean[] nbrhood = new boolean[nbr];
            for(int j=0; j<nbr; j++) {

                nbrhood[j] = cells[(i+n+j)%n];

            }

            //Update the state of the i-th cell. The neighborhood has to
            //be reversed, since the representation of the truth table is
            //in Least Significant Bit First order.
            nextConf[i] = delta(boolfun.BinTools.reverse(nbrhood));
            
        }

        //Reassign the cellular array
        cells=nextConf;

    }
    
    /**
     * Evolves the CA from its current configuration to the next one, with
     * no boundary conditions. Hence, the output configuration will be smaller.
     * 
     */
    public void nextConfigNoBound() {

        boolean[] nextConf = new boolean[cells.length-nbr+1]; //the next configuration is composed of n-d+1 cells (where n: cells.length and d: nbr)
        int n = cells.length;
        
        //Check whether there are at least nbr cells to apply the local rule
        if(n >= nbr) {
            
            for(int i=0; i<nextConf.length; i++) {

                //Apply local rule to the cell in position i
                //1: Build the neighborhood of cell i
                boolean[] nbrhood = new boolean[nbr];
                for(int j=0; j<nbr; j++) {

                    nbrhood[j] = cells[i+j];

                }

                //2: Update the state of the i-th cell. The neighborhood has to
                //be reversed, since the representation of the truth table is
                //in Least Significant Bit First order.
                nextConf[i] = delta(boolfun.BinTools.reverse(nbrhood));
                
            }
            
        }
        //Reassign the cellular array
        cells=nextConf;

    }

    //Getters and setters methods
    
    public boolean[] getCells() {
        return cells;
    }

    public void setCells(boolean[] cells) {
        this.cells = cells;
    }

    public boolean[] getRule() {
        return rule;
    }

    public void setRule(boolean[] rule) {
        this.rule = rule;
    }

    public int getNbr() {
        return nbr;
    }

    public void setNbr(int nbr) {
        this.nbr = nbr;
    }
    
    
}
