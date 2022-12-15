from tools.utils import cvt_cfgPathToDict, build_logger
from pprint import pformat

import torch 
import argparse


def parse_args():

    parser = argparse.ArgumentParser(description='Train a segmentor')
    parser.add_argument('config', help='train config file path')

    args = parser.parse_args()

    return args



def main():

    args = parse_args()

    # build config 
    cfg_path = args.config

    cfg = cvt_cfgPathToDict(cfg_path)

    logger, log_path = build_logger(cfg['WORK_DIR'])

    # Print paths
    logger.info('Log file is %s' % log_path)
    
    logger.info(pformat(cfg, width=100))

    # build dataset 


    

    
    



if __name__ == '__main__':
    main()

