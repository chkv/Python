import argparse


parser=argparse.ArgumentParser()
parser.add_argument("--p",help="Physics Marks",choices=range(0,101),type=int,default=0)
parser.add_argument("--c",help="Chemistry Marks",type=int,choices=range(0,101),default=0)
parser.add_argument("--m",help="Maths Marks",type=int,choices=range(0,101),default=0)
args=parser.parse_args()

print(args.p)
print(args.c)
print(args.m)

print("Result:",(args.p+args.c+args.m)/3)