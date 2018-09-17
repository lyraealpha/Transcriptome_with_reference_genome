# !/usr/bin/env python
# coding=UTF-8
import argparse,\
        re,\
        os,\
        subprocess,\
        datetime,\
        scipy,\
        numpy,\
        pandas


def Quality_control(fq_dir,qc_result_dir):
    print datetime.datetime.now()+ ' :'+ 'Qc_process start runing!'
    fq_file_name = []
    for paths,folders,files in os.walk(fq_dir):
        fq_file_name = fq_files
    for file in files:
        Qc_cmd = 'fastqc '+ fq_dir + '/' + file +' ' + '-o ' + qc_result_dir
    child=subprocess.Popen([Qc_cmd])
    child.wait()
    print datetime.datetime.now()+ ' :'+'Qc_process has been finished!'

# def Mapping():
#
# def Quantify():
#
# def Different_analysis():
#
# def enrichment():
#
# def Interaction():


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        description='This is a test RNA_seq pipeline')
    parser.add_argument('-fd',
                        type = str,
                        nargs = '?',
                        dest = fq_dir,
                        help = 'input dir with fastq files')
    parser.add_argument('-fd_out',
                        type = str,
                        nargs = '?',
                        dest = fq_out,
                        help = 'output dir for fastq Q_c results')
    args = parser.parse_args()
    if not args.fq_dir:
        parser.print_help()
        print '\033[1;33;40m input fq dir is missing, please try again \033[0m'
        exit()
    Quality_control(args.fq_dir,args.fq_out)




