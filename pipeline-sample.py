#!/usr/bin/env python
#encoding=utf8

import os, sys, argparse, textwrap
from ruffus import *
import logging
from michelia import path, run_cmd


parser = argparse.ArgumentParser(description='''
    pipeline illustrate
            ''')
parser.add_argument('-v', '--verbose', dest='verbose',
        action="count", default=3,
        help="Print more detailed messages for each additional verbose level. E.g. run_parallel_blast --verbose --verbose --verbose ... (or -vvv)")

parser.add_argument("-j", "--jobs", dest="jobs",
                    default=4,
                    metavar="jobs",
                    type=int,
                    help="Specifies the number of jobs (operations) to run in parallel.")

parser.add_argument("-p", "--flowchart", dest="flowchart",
                    metavar="FILE",
                    type=str,
                    help="Print flowchart of the pipeline to FILE. Flowchart format "
                       "depends on extension. Alternatives include ('.dot', '.jpg', "
                       "'*.svg', '*.png' etc). Formats other than '.dot' require "
                       "the dot program to be installed (http://www.graphviz.org/).")
parser.add_argument("-n", "--just_print", dest="just_print",
                    action="store_true", default=False,
                    help="Only print a trace (description) of the pipeline. "
                         " The level of detail is set by --verbose.")
parser.add_argument("-r", "--run",
                    action="store_true", default=False,
                    help="run pipeline")

args = parser.parse_args()

if len(sys.argv)==1:
    parser.parse_args(['-h'])


#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

#   Logger

logger = logging.getLogger("run_parallel_blast")
#
# We are interesting in all messages
#
if args.verbose:
    logger.setLevel(logging.DEBUG)
    stderrhandler = logging.StreamHandler(sys.stderr)
    stderrhandler.setFormatter(logging.Formatter("    %(message)s"))
    stderrhandler.setLevel(logging.DEBUG)
    logger.addHandler(stderrhandler)


#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
#   Pipeline tasks




#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
#   piplne exce

exce_tasks = [....]

if args.just_print and args.run:
    pipeline_printout(sys.stdout, exce_tasks, verbose=args.verbose)
elif args.flowchart:
    # use file extension for output format
    output_format = os.path.splitext(args.flowchart)[1][1:]
    pipeline_printout_graph (open(args.flowchart, "w"),
                             output_format,
                             exce_tasks,
                             no_key_legend = True)
    os.system('eog %s' % args.flowchart)
else:
    pipeline_run(exce_tasks,  multiprocess = args.jobs,
                        logger = logger, verbose=args.verbose)

