/**
 * Global constants and type declarations.
 *
 * Commented out until used.
 */

//const GREEN = '#228F1D';
//const RED = '#A2000C';
//const ORANGE = '#FFA500';
export const LIGHT_GREY = '#F3F3F3';
export const MEDIUM_GREY = '#D0D0D0';
export const PTS_BLUE = '#60DEFD';
//const DARK_GREY = '#ADADAD';
//const BLACK = '#404040';

export const COLWIDTH = "25em";

export interface BranchNode {
  short_id: string,
  nodeid: string,
  status: string,
  parent_ids: Array<string>,
  child_branches: { [key: string]: BranchNode },
  child_leaves: { [key: string]: LeafNode },
  environment_state: string,
}

export interface LeafNode {
  short_id: string,
  nodeid: string,
  status: string,
  parent_ids: Array<string>,
  longrepr: string,
}
