

temp = [73,74,75,71,69,72,76,73]
stack = [73]
rslt = [0, 0]

size stack 0 add 73 stack = [73]  rslt [0]
last item 73, 73 <76 then pop, stack size 0, add [76] rslt [0,0]
last item 76, 76 > 72, then stack size 1, add [72, 76] rslt [0,0,1]
last item 69, 69 < 72
