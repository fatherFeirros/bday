import sys, time, random, requests, os, math

class Tomasz:
    
    def __init__(self):
        
        url = "https://raw.githubusercontent.com/fatherFeirros/bday/main/tomasz.json"
        
        self.age = 30
        self.occupation = "Software Engineer"
        self.location = "Tychy"
        self.hobby = "Saxophone"
        self.has_wonderful_wife = True
        self.can_achive_anything_he_wants = True
        self.secret_message = dict(requests.get(url).json())
        
    def __enter__(self):
        
        return self
    
    def __exit__(self,exc_type, exc_value, traceback):
        
        time.sleep(5)
    
    def typing(self,m,m_s=100,t='fast',k=10):
        if t == 'slow':
            for i in m:
                sys.stdout.write(chr(i) if type(i) == int else i)
                sys.stdout.flush()
                time.sleep(random.random() * random.uniform(1,10) / m_s)
            print("")

        else:
            a = math.ceil(len(m)/k)
            
            for i in range(k):
                for j in m[i*a:(i+1)*a]:
                     sys.stdout.write(chr(j) if type(j) == int else j)
                time.sleep(0.5)
            print("")
            
    def progressbar(self,it, prefix="", size=60, out=sys.stdout):
    
        count = len(it)
        def show(j):
        
            x = int(size*j/count)
            print("{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count), 
                    end='\r', file=out, flush=True)
                    
        show(0)
        
        for i, item in enumerate(it):
        
            yield item
            show(i+1)
            
        print("\n", flush=True, file=out)
                
    def hacker_time(self,toolbar_width=61):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        for i in range(3):
            
            self.typing(self.secret_message['words']['other'][i],m_s=1000,t='slow')
            
            for j in self.progressbar(range(100), "Progress: ", 40):
                if random.uniform(1,100) < 3:
                    time.sleep(random.random())
                time.sleep(0.07*random.random())
            
        print("Success!")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    
    try:
        
        with Tomasz() as ma_urodziny:
        
            ma_urodziny.hacker_time()
            ma_urodziny.typing(ma_urodziny.secret_message['words']['start'],100,'slow')
            ma_urodziny.typing(ma_urodziny.secret_message['cake'])
            ma_urodziny.typing(ma_urodziny.secret_message['words']['end'],100,'slow')
    
    except Exception as e:
        
        backup_msg = [78,111,32,99,111,115,32,110,105,101,32,112,121,107,108,
                      111,32,58,80,32,90,100,114,111,119,105,97,32,105,32,112,
                      105,101,110,105,101,100,122,121,32,109,111,114,100,101,
                      99,122,107,111,33,33,33]
        
        print(e)
        
        for i in backup_msg:
            sys.stdout.write(chr(i) if type(i) == int else i)
