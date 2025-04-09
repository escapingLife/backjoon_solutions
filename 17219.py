import sys

user_input = sys.stdin.read().strip().splitlines()
N, M = map(int, user_input[0].split())

#site_name -> pw
site_identification = {}

for i in range(1, N + 1):
    site_name, pw = user_input[i].split()
    site_identification[site_name] = pw

for site_name in user_input[N + 1 :]:
    print(site_identification[site_name])