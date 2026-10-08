n=int(input())
i=0
fn=0
while i<=n:
    fn=fn + ((-1)**(i+1))*i


    i=i+1

print(fn)