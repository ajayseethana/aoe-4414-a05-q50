# script_name.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Ajay Seethana
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import math # math module
import sys # argv

# constants
R_E_KM = 6378.137
E_E    = 0.081819221456

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

def mag(v):
    sum = 0.0
    for ele in v:
        sum += ele ** 2
    return math.sqrt(sum)

def smul(s, v):
    return [s * ele for ele in v]

def add(v1, v1):
    v = []
    for i in range(0, len(v1)):
        v.append(v1[i] + v2[i])
    return v

def sub(v1, v2):
    v = []
    for i in range(0, len(v1)):
        v.append(v1[i] - v2[i])
    return v

def dot(v1, v2):
    dp = 0.0
    for i in range(0, len(v1)):
        dp += v1[i] * v2[i]
    return dp

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2
# parse script arguments
if len(sys.argv)==7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
else:
  print(\
   'Usage: '\
   'python3 arg1 arg2 ...'\
  )
  exit()
r_s = R_E_KM


d_l = [d_l_x, d_l_y, d_l_z]
c_l = [c_l_x, c_l_y, c_l_z]



a = d_l_x**2 + d_l_y**2 + (d_l_z**2)/(1-E_E**2)
b = 2 * (d_l_x * c_l_x + d_l_y * c_l_y + (d_l_z * c_l_z)/(1-E_E**2))
c = c_l_x**2 + c_l_y**2 + (c_l_z**2)/(1-E_E**2) - R_E_KM**2

discr = b*b-4.0*a*c

if discr >= 0.0:
    d = (-b - math.sqrt(discr))/(2.0 * a)
    if d < 0.0:
        d = (-b + math.sqrt(discr))/(2.0 * a)
    if d >= 0.0:
        l_d = add(smul(d, d_l), c_l)
        print(l_d[0]) # x-component of intersection point
        print(l_d[1]) # y-component of intersection point
        print(l_d[2]) # z-component of intersection point


