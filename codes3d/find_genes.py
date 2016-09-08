from configobj import ConfigObj
import argparse,codes3d,os

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="")
	parser.add_argument("-i","--interactions_files",nargs='+',help="The file containing the interactions discovered for the queried SNPs, generated by find_interactions.py")
	parser.add_argument("-c","--config",default="docs/conf.py",help="The configuration file to be used in this instance (default: conf.py)")
	parser.add_argument("-o","--output_dir",default="hiCquery_output",help="The directory in which to output results (\"hiCquery_output\" by default).")
	args = parser.parse_args()
	config = ConfigObj(args.config)
	fragment_database_fp = config["FRAGMENT_DATABASE_FP"]
	gene_bed_fp = config["GENE_BED_FP"]
	if not os.path.isdir(args.output_dir):
		os.makedirs(args.output_dir)

	interactions = codes3d.parse_interactions_file(args.interactions_files)
	genes = codes3d.find_genes(interactions,fragment_database_fp,gene_bed_fp,args.output_dir)
	
