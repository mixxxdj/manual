/**
 * Adjust Sphinx Search Scoring
 * This script overrides the default Sphinx scoring to de-prioritize hardware manuals
 * and control documentation.
 *
 * https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_search_scorer
 *
 * Priorities:
 * 0 chapters/
 * 1 chapters/appendix
 * 2 hardware manuals
 */
var Scorer = {
    score: result => {
        const [docName, title, anchor, descr, score, filename] = result;
        let adjustedScore = score;
        if (docName.includes('hardware/')) {
            adjustedScore -= 100;
        } else if (docName.includes('chapters/appendix/')) {
            adjustedScore += 50;
        } else { // docName.includes('chapters/')
            adjustedScore += 100;
        }
        return adjustedScore;
    },

    // Standard Sphinx weights
    // query matches the full name of an object
    objNameMatch: 11,
    // or matches in the last dotted part of the object name
    objPartialMatch: 6,
    // Additive scores depending on the priority of the object
    objPrio: {
      0: 15, // used to be importantResults
      1: 5, // used to be objectResults
      2: -5, // used to be unimportantResults
    },
    //  Used when the priority is not in the mapping.
    objPrioDefault: 0,

    // query found in title
    title: 15,
    partialTitle: 7,

    // query found in terms
    term: 5,
    partialTerm: 2,
};
