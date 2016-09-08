from configobj import ConfigObj
from sets import Set
import argparse,codes3d,os

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="")
	parser.add_argument("-e","--eqtls_files",nargs='+',help="The list of eQTLs generated by find_eqtls.py")
	parser.add_argument("-f","--fdr_threshold",type=float,default=0.05,help="The FDR threshold to consider an eQTL statistically significant (default: 0.05).")
	parser.add_argument("-o","--output_dir",default="hiCquery_output",help="The directory in which to output results (\"hiCquery_output\" by default).")
	parser.add_argument("-p","--num_processes",type=int,default=1,help="Desired number of processes for multiprocessing (default: 1).")
	args = parser.parse_args()
	eqtls,num_sig = codes3d.parse_eqtls_files(args.eqtls_files,args.fdr_threshold)
	if not os.path.isdir(args.output_dir):
		os.makedirs(args.output_dir)
	
	pathways = codes3d.retrieve_pathways(eqtls,args.fdr_threshold,args.num_processes,args.output_dir)