

t = io.read("*n")

for i =t, 0, -1
do
    chunks = {}
    for substring in s:gmatch("%S+") 
    do
        table.insert(chunks, substring)
    end
    x = chunks[0]
    n = chunks[1]
    each_case = x/10
    ans = each_case*n
    print(ans)
end
